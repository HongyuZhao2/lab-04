import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    client.subscribe("hongyuz/ping")
    client.message_callback_add("hongyuz/ping", on_message_from_ping)

def on_message_from_ping(client, userdata, message):
    print("Custom Callback - Ping: " + message.payload.decode())
    count = int(message.payload.decode()) + 1
    time.sleep(1)
    client.publish("hongyuz/pong", f"{count}")

if __name__ == "__main__":

    client = mqtt.Client()
    # connect to RPI
    client.connect(host = "172.20.10.12", port = 1883, keepalive = 60)
    
    client.on_message = on_message_from_ping
    client.on_connect = on_connect
        
    client.loop_forever()




