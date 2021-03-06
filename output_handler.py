from counterAct_actions import *
import time
import json
import re
from pulsar_consumer import *

attributes = ['sIP','cIP']

class Output_handler:

    def __init__(self,CounterACT_IP, CounterACT_User , CounterACT_Password, flow_input):
        self.CounterACT = CounterACT_IP
        self.CounterACT_User = CounterACT_User
        self. CounterACT_Password = CounterACT_Password
        self.flow_input = flow_input


    def get_output(self, internal_ip):
        counterAct = CounterACT_actions(self.CounterACT,self.CounterACT_User,self.CounterACT_Password)
        counterAct.copy_file_to_appliance('/publisher_test.py','/tmp')
        counterAct.run_command(f"""tail -f /usr/local/forescout/log/plugin/flowsuploader/flowsuploader.log | stdbuf -o0 grep {internal_ip} | stdbuf -o0 grep 'PulsarUploader.publish' > /usr/local/forescout/log/plugin/flowsuploader/automation &""")
        counterAct.run_command(f"""/opt/rh/rh-python36/root/usr/bin/python -u /tmp/publisher_test.py {self.flow_input}""")
        time.sleep( 15 )
        output = counterAct.run_command("cat /usr/local/forescout/log/plugin/flowsuploader/automation")
        print(output)
        output = str(output).replace('protocol','prot')
        output_string = re.findall(r'{".*}',output)
        print("output string: ")
        print(output_string)
        counterAct.run_command("""kill -9 `pidof tail`""")
        # counterAct.run_command("rm -rf /usr/local/forescout/log/plugin/flowsuploader/automation")
        return output_string


    def get_pulsar_output(self, pulsarIP, pulsarTopic):
        counterAct = CounterACT_actions(self.CounterACT,self.CounterACT_User,self.CounterACT_Password)
        counterAct.copy_file_to_appliance('/publisher_test.py','/tmp')
        pulsar_consumer = Pulsar_consumer(pulsarIP,pulsarTopic)
        consumer = pulsar_consumer.start_consumer()
        counterAct.run_command(f"""/opt/rh/rh-python36/root/usr/bin/python -u /tmp/publisher_test.py {self.flow_input}""")
        pulsar_output = pulsar_consumer.get_pulsar_output(consumer)
        print(pulsar_output)
        output_string = pulsar_output.decode("utf-8")
        output_string = output_string.replace("protocol","prot")
        output_json = json.loads(output_string)
        payload = output_json["payload"]
        return payload







    def get_payload_list(self,output_string):
        for i in output_string:
            session_flow = json.loads(i)
            print(session_flow)
            payload = session_flow["payload"]
        return payload








    # def output_to_list_of_payloads(output):
    #     payloads = re.findall(r'{"protocol.*?}',output)
    #     list_of_payloads=[]
    #     for i in output:
    #         payload = json.loads(i)
    #         list_of_payloads.append(payload)
    #     print(list_of_payloads)
    #     return list_of_payloads




