import paho.mqtt.client as mqtt

# Configuração MQTT
MQTT_BROKER = "192.168.144.239"  # Substitua pelo IP do broker Mosquitto
MQTT_PORT = 1883
MQTT_TOPIC = "garra/controle"  # Tópico onde os dados da garra serão enviados

# Criar uma instância global do cliente MQTT para manter a conexão
client = None

# Função para conectar ao broker MQTT (somente uma vez)
def conectar_mqtt():
    global client
    if client is None:
        client = mqtt.Client()
        
        try:
            client.connect(MQTT_BROKER, MQTT_PORT, 60)
            print(f"Conectado ao broker MQTT {MQTT_BROKER} na porta {MQTT_PORT}")
        except Exception as e:
            print(f"Erro ao conectar ao broker: {e}")
            return False
    
    return True

# Função para enviar dados via MQTT
def enviar_dados_mqtt(posicao_garra):
    """
    Função que envia os dados da posição da garra via MQTT.
    
    :param posicao_garra: Lista contendo [X, Y, Z, Estado da Mão]
    """
    if not conectar_mqtt():
        print("Não foi possível estabelecer a conexão MQTT.")
        return

    # Formatar a mensagem com os dados da garra
    payload = f"Posição alvo da garra: X={posicao_garra[0]:.2f}, Y={posicao_garra[1]:.2f}, Z={posicao_garra[2]:.2f}, Mão aberta: {posicao_garra[3]}"

    # Publicar no tópico MQTT
    result = client.publish(MQTT_TOPIC, payload)
    
    if result.rc == mqtt.MQTT_ERR_SUCCESS:
        print(f"Mensagem enviada: {payload}")
    else:
        print(f"Falha ao enviar mensagem. Código de retorno: {result.rc}")
