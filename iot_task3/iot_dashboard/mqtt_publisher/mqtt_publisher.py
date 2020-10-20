import time
import json
from numpy.random import random_sample
import paho.mqtt.client as mqtt


"""
Some methods for testing mqtt_subscriber.py
"""


def init_publisher_client():
    client = mqtt.Client("MTS IoT testing : publisher")
    client.connect("mqtt.eclipse.org", 1883)

    return client


def main():
    client = init_publisher_client()

    while True:
        sample_json = {
          "data": {
            "co": random_sample(),
            "humidity": random_sample(),
            "light": random_sample() > 0.5,
            "lpg": random_sample(),
            "motion": random_sample() > 0.5,
            "smoke": random_sample(),
            "temp": random_sample()
          },
          "device_id": "6e:81:c9:d4:9e:58",
          "ts": time.time()
        }
        client.publish("MTS_IOT_TESTING", json.dumps(sample_json))
        print("Just published sample JSON to topic MTS_IOT_TESTING")
        time.sleep(2)


if __name__ == '__main__':
    main()
