# import paho.mqtt.client as mqtt

# Definir configuração MQTT, tópico, etc.
# MQTT_BROKER = "broker.emqx.io"
# MQTT_PORT = 1883
# MQTT_TOPIC = "garra/controle"

def conectar_mqtt():
    """
    Função para conectar ao broker MQTT.
    """
    # client = mqtt.Client()
    # client.connect(MQTT_BROKER, MQTT_PORT, 60)
    # return client
    pass

def enviar_dados_mqtt(posicao_garra):
    """
    Função que envia os dados da posição da garra via MQTT.
    """
    # client = conectar_mqtt()
    # payload = f"{posicao_garra[0]},{posicao_garra[1]},{posicao_garra[2]},{posicao_garra[3]}"
    # client.publish(MQTT_TOPIC, payload)
    pass
