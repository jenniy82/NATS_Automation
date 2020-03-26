import json



class Input_handler:
    def __init__(self,input):
        self.input = input


    def get_sessions_list_from_input(self):
        input_json = json.loads(self.input)
        sessions_list = input_json["sessions"]
        return sessions_list

