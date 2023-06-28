import paho.mqtt.client as mqtt
import random
import time

# Parámetros de conexión MQTT
broker = "127.0.0.1"  # Dirección IP del servidor MQTT
port = 1883  # Puerto del servidor MQTT
usuario = "usuario_p"
contrasena = "prueba"
topicT = "casa/sensorTemp/1"  # Tópico para publicar las muestras de temperatura
topicP = "casa/sensorPresion/1"
topicH = "casa/sensorHum/1"


# Función para generar una muestra aleatoria de temperatura
def generar_muestra_temperatura():
    temperatura = random.uniform(15, 30)  # Generar temperatura aleatoria entre 20 y 30 grados Celsius
    return round(temperatura,2)

def generar_muestra_presion():
    presion = random.uniform(800, 1100)  # Generar temperatura aleatoria entre 20 y 30 grados Celsius
    return round(presion,2)

def generar_muestra_humedad():
    humedad = random.uniform(0, 100)  # Generar temperatura aleatoria entre 20 y 30 grados Celsius
    return round(humedad,2)


# Función de conexión al broker MQTT
def on_connect(client, userdata, flags, rc):
    print("Conectado al broker MQTT: " + broker)
    
# Crear cliente MQTT y configurar las funciones de conexión
client = mqtt.Client()
client.on_connect = on_connect

# Conectar al broker MQTT
client.username_pw_set(username=usuario,password=contrasena)
client.connect(broker, port, 60)

# Ciclo principal
while True:
    try:
        # Generar una muestra de temperatura aleatoria
        temperatura = generar_muestra_temperatura()
        presion = generar_muestra_presion()
        humedad = generar_muestra_humedad()

        # Publicar la muestra de temperatura en el tópico
        client.publish(topicT, temperatura)
        print("Muestra de temperatura publicada: " + str(temperatura))
        client.publish(topicP, presion)
        print("Muestra de presion publicada: " + str(presion))
        client.publish(topicH, humedad)
        print("Muestra de humedad publicada: " + str(humedad))

        # Esperar un tiempo antes de generar la siguiente muestra
        time.sleep(1)

    except KeyboardInterrupt:
        # En caso de interrupción por teclado, desconectar del broker MQTT
        client.disconnect()
        break
