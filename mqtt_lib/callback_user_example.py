from wrapped_mqtt import MqttCustom
from mqtt_callback_mechanism import CallbackMechanism


@CallbackMechanism.wrap_on_connect
def on_connect(client):
    client.subscribe("test/callback/now")
    client.subscribe("test/test/test")
    print("***********connected********")


@CallbackMechanism.wrap_on_disconnect
def on_disconnect(client):
    print("disconnected")


@CallbackMechanism.wrap_on_message
def on_message(topic, payload):
    print("topic --> ", topic)
    print("payload --> ", payload)
    print("do anything")


@CallbackMechanism.make_callback("baby", "topic.split('/')[1] == 'callback'")
def callback_trigger(topic, payload):
    print("callback has been triggered")


class AnyClass:
    def __init__(self):
        self.param = 1
        CallbackMechanism.register_callback(
            clientId="baby",
            condition="topic.split('/')[2] == 'test'",
            callbackFunc=self.callback_on_test_topic)

    def callback_on_test_topic(self, topic, payload):
        print("this is callback from object ", topic, payload)
        print(mqttObj.client.connectionStatus)


mqttObj = MqttCustom(on_connect,
                     on_message,
                     on_disconnect,
                     credentials={"mqttclientid": "baby"})
print(mqttObj.client.connectionStatus)

anyClassObject = AnyClass()
