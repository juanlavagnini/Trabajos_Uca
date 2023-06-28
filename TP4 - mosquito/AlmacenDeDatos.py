# Conectando a MQTT-Mosquitto
import paho.mqtt.client as mqtt
from sqlalchemy import *

engine = create_engine('sqlite:///MQTT_BD.db', echo=True)
connection = engine.connect()
meta = MetaData()

tabla = Table(
    'lecturas_sensores', meta,
    Column('id', Integer, primary_key=True),
    Column('id_sensor', Integer),
    Column('tipo', String),
    Column('valor', Float),
)
meta.create_all(engine)


# INGRESO
# Parametros para la conexión
servidormqtt = "127.0.0.1"
usuario = "usuario"
contrasena = "prueba"
topicolee = "#"

# Funciones de conexión y mensaje
# Al recibir CONNACK desde el servidor
def on_connect(client, userdata, flags, rc):
    print("Conexión/código de resultado: "+str(rc))
    # Inicio o renovación de subscripción
    client.subscribe(topicolee,2)

# el tópico tiene una publicación
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    unmensaje = msg.topic+" "+str(msg.payload)
    
    _id = msg.topic.split("/")[2]
    _tipo = msg.topic.split("/")[1]
    _valor = float(str(msg.payload).split("'")[1])
    print(_valor)
    
    ins = insert(tabla).values(
            id_sensor=_id,
            tipo = _tipo,
            valor = _valor
        )
    try:
        result = connection.execute(ins)
        connection.commit()
        print("Inserción exitosa")
    except Exception as e:
        print("Error durante la inserción:", str(e))
        connection.rollback()
    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username=usuario,password=contrasena)
client.connect(servidormqtt, 1883, 60)
try:
    client.loop_forever()
except KeyboardInterrupt:

    s = tabla.select()
    rp = connection.execute(s)
    results = rp.fetchall()
    print("")
    print("Resultados")
    print("{:<10} {:<10} {:<10} {:<10}".format("sensor","Temp","Presion","Hum"))
    cont=0
    for result in results:
        if cont == 3:
            print("{:<10} {:<10} {:<10} {:<10}".format(result[1],temp,pr,hum))
            cont =0
        if cont == 0:
            temp = result[3]
        if cont == 1:
            pr = result[3]
        if cont == 2:
            hum = result[3]
        cont+=1
       