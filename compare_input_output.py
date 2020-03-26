import re
import json

# attributes = ["sIP","cIP","sPrt"]
# attributes_for_hash = ["sIP","cIP"]



class Compare_input_output:


    def __init__(self, session_list, payload_list, attributes_to_comapre, attributes_for_hash_compare):
        self.session_list = session_list
        self.payload_list = payload_list
        self.attributes_to_compare = attributes_to_comapre
        self.attributes_for_hash_compare = attributes_for_hash_compare
#
 # input_to_Nats = """{"properties":{"sourceIp":"10.160.178.30","sourceNodeID":"2687540205173066847","sourceName":"FLOW"},"sessions":[{"prot":6,"sIP":"10.160.178.36","cIP":"10.160.112.1","sPrt":22,"cPrt":62198,"time":0,"bid":true,"exporterIp":"127.0.0.1","dirConf":"HIGH"},{"prot":17,"sIP":"10.160.178.20","cIP":"10.160.112.1","sPrt":31364,"cPrt":62397,"time":1584292383,"bid":false,"exporterIp":"127.0.0.1","dirConf":"LOW"}]}"""
# output_from_log = """flowsuploader:10584:1584909771.637202:Sun Mar 22 22:42:51 2020: 330|212|52|log(3)|PulsarUploader.publish:74| >> uploading message[{"applianceId":"2687540205173066847","type":"session","pluginVersion":"1.0.0","pluginVersionBuildNumber":"40","timestamp":1584909771636,"payload":[{"protocol":17,"count":1,"isIoT":true,"sPrt":31364,"startTime":1584909767000,"cIP":"10.160.112.1","sIP":"10.160.178.20","endTime":1584909767000,"type":"INBOUND"},{"protocol":6,"count":1,"isIoT":true,"sPrt":22,"startTime":1584909767000,"cIP":"10.160.112.1","sIP":"10.160.178.36","endTime":1584909767000,"type":"INBOUND"}],"compressionType":"none","flowsCount":2}] to topic[aaa/flowsUploader] < |pool-6-thread-1-615776473|cloud-client\n"""
#
# # output = re.findall(r'{"protocol.*?}',output_from_log)
# output_string = re.findall(r'{".*}',output_from_log)
# list_of_attributes = []
#
#
# def get_payload_list(output):
#     for i in output:
#         session_flow = json.loads(i)
#         print(session_flow)
#         payload = session_flow["payload"]
#     return payload
# print("start get payload")
# print(get_payload_list(output_string))
# print("end get payload")


# def get_sessions_list_from_input(input_string):
#     input_json = json.loads(input_string)
#     sessions_list = input_json["sessions"]
#     return sessions_list
#
# print("start get sessions list from input")
# print(get_sessions_list_from_input(input_to_Nats))
#
# print("end get sessions list from input")
#


    def get_hash_for_flow(self, flow, list_of_attributes_for_hash):
        string_for_hash = ""
        for i in list_of_attributes_for_hash:
            attribute_value = flow[i]
            string_for_hash = string_for_hash + attribute_value
        hash_for_flow = hash(string_for_hash)
        return hash_for_flow


    def create_hash_map_for_flows(self, list_of_flows):
        flows_hash_map = {}
        for i in list_of_flows:
            flow_map = {self.get_hash_for_flow(i,self.attributes_for_hash_compare):i}
            flows_hash_map.update(flow_map)
        return flows_hash_map

    def compare_input_output(self, input_hash_map,output_hash_map):
        result = "success"
        for key in input_hash_map:
            if key in output_hash_map:
                print("flow exists in output")
                input_flow = input_hash_map[key]
                output_flow = output_hash_map[key]
                for i in self.attributes_to_compare:
                    if input_flow[i] == output_flow[i]:
                        print (i," is equal for input and output: ", input_flow[i])
                    else:
                        print(i," is not equal for input and output: ", input_flow[i]," != ",output_flow)
                        break
            else:
                print("key doesn't exist in output hash map")
                result = "Failure"
                break
        print("great success!!!")
        return result





# print(compare_input_output(create_hash_map_for_flows(get_sessions_list_from_input(input_to_Nats)),create_hash_map_for_flows(get_payload_list(output_string))))
#
#
#
#
#
# print("input hash map")
# inputHash = create_hash_map_for_flows(get_sessions_list_from_input(input_to_Nats))
# for i in inputHash:
#     print("key: ")
#     print(i)
#
#
#
#
# print("out put hash map")
# print(create_hash_map_for_flows(get_payload_list(output_string)))












