import json
from functools import partial

import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("topic/mts_iot")


def on_message(df, client, userdata, message):
    try:
        js = json.loads(message.payload.decode("utf-8"))
        for k, v in js["data"].items():
            js[k] = v
        del js["data"]

        print(js)
        df.loc[len(df)] = js

    except:
        pass


def init_subscriber_client(df):
    client = mqtt.Client("MTS IoT testing : client")
    client.connect("mqtt.eclipse.org", 1883)

    client.on_connect = on_connect
    client.on_message = partial(on_message, df)

    return client
