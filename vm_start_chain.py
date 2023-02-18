import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    client.subscribe("hongyuz/pong")
    client.message_callback_add("hongyuz/pong", on_message_from_pong)

def on_message_from_pong(client, userdata, message):
    print("Custom Callback - Pong: " + message.payload.decode())
    count = int(message.payload.decode()) + 1
    time.sleep(1)
    client.publish("hongyuz/ping", f"{count}")

if __name__ == "__main__":

    count = 1
    client = mqtt.Client()
    
    # connect to RPI
    client.connect(host = "172.20.10.12", port = 1883, keepalive = 60)

    client.on_message = on_message_from_pong
    client.on_connect = on_connect

    # publish initial number
    client.publish("hongyuz/ping", f"{count}")

    client.loop_forever()




