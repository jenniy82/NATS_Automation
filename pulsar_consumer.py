import pulsar
import time
import json

class Pulsar_consumer:

    def __init__(self,pulsarIP,topic):
        self.pulsarIP = pulsarIP
        self.topic = topic
        self.client = pulsar.Client(self.pulsarIP)


    def start_consumer(self):
        # client = pulsar.Client('pulsar://10.160.178.100:6650')
        consumer = self.client.subscribe(self.topic, 'Jenia3')
        print("this is consumer")
        print(consumer)
        return consumer


    def get_pulsar_output(self,consumer):
        while True:

            msg = consumer.receive()

            try:
                print("Received message '{}' id='{}'".format(msg.data(), msg.message_id()))
                flow_message = msg.data()
                print(str(flow_message))
                # Acknowledge successful processing of the message
                consumer.acknowledge(msg)
                print("acknowledged")
                return flow_message
            except:
                # Message failed to be processed
                consumer.negative_acknowledge(msg)
            self.client.close()





# pulsar_consumer = Pulsar_consumer('pulsar://10.160.178.100:6650', 'internal/flowsUploader/flows')
# consumer = pulsar_consumer.start_consumer()
# #
# output = pulsar_consumer.get_pulsar_output(consumer)
# # print(output.decode("utf-8"))
# output_json = json.loads(output.decode("utf-8"))
# # print(output_json["payload"])