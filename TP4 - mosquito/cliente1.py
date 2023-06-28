# Conectando a MQTT-Mosquitto
import paho.mqtt.client as mqtt

# INGRESO
# Parametros para la conexión
servidormqtt = "127.0.0.1"
usuario = "usuario"
contrasena = "prueba"
topicolee = "casa/+/1"

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

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username=usuario,password=contrasena)
client.connect(servidormqtt, 1883, 60)
client.loop_forever()
