import sys

sys.path.append('./')

from flask import Flask, render_template, request

from iot_dashboard.mqtt_subscriber.mqtt_subscriber import init_subscriber_client
from iot_dashboard.plot.create_plot import create_plot
from iot_dashboard.plot.init_dataframe import init_dataframe

app = Flask(__name__)


df = init_dataframe()


@app.route("/")
def index():
    param_to_plot = "temp"
    plot_js = create_plot(df, param_to_plot)

    return render_template("index.html", plot=plot_js)


@app.route("/plot", methods=["GET", "POST"])
def change_column():
    param_to_plot = request.args["selected"]
    plot_js = create_plot(df, param_to_plot)

    return plot_js


def main():
    # running MQTT subscriber
    client = init_subscriber_client(df)
    client.subscribe("MTS_IOT_TESTING")
    client.loop_start()

    # running Flask
    app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
