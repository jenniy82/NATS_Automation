from input_handler import *
from output_handler import *
from compare_input_output import *

attributes = ["sIP","cIP","sPrt","prot"]
attributes_for_hash = ["sIP","cIP"]


# input that will be sent to NATS
input_to_Nats = '{"properties":{"sourceIp":"10.160.178.30","sourceNodeID":"2687540205173066847","sourceName":"FLOW"},"sessions":[{"prot":6,"sIP":"10.160.178.36","cIP":"10.160.112.1","sPrt":22,"cPrt":62198,"time":0,"bid":true,"exporterIp":"127.0.0.1","dirConf":"HIGH"},{"prot":17,"sIP":"10.160.178.20","cIP":"10.160.112.1","sPrt":31364,"cPrt":62397,"time":1584292383,"bid":false,"exporterIp":"127.0.0.1","dirConf":"LOW"}]}'

# we need internel ip for grepping the log file
internal_ip_in_flow = '10.160.178.36'


# input handler class
input_handler = Input_handler(input_to_Nats)

# return sessions(flows) list from input
sessions_list = input_handler.get_sessions_list_from_input()
print( "session list from input: ", sessions_list)

# output handler class
output_handler = Output_handler('10.160.178.30','root','aristo1', (f"""'{input_to_Nats}'"""))

# publish the input to NATS by copying and running the script on appliance -> look at the output in the log -> convert the output in the log to json format with regex
output_string = output_handler.get_output(internal_ip_in_flow)

# get the payload list(flows) from the json output
output_payload_list = output_handler.get_payload_list(output_string)
print("output payload list: ",output_payload_list)

# compare input output class
compare_input_output = Compare_input_output(sessions_list,output_payload_list,attributes,attributes_for_hash)

# The flows in input and output are not in the same order, for comparison we need to find the relevant flow by identifier, in this case the flow identifier will be hash of number of flow values the keys of these values can be configurable.
input_hash_map = compare_input_output.create_hash_map_for_flows(sessions_list)
print ("input hash map: ",input_hash_map)

output_hash_map = compare_input_output.create_hash_map_for_flows(output_payload_list)
print ("output hash map: ",output_hash_map)

compare_input_output.compare_input_output(input_hash_map,output_hash_map)
