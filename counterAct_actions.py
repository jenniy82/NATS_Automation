import sys, paramiko
import time
import os
from scp import SCPClient


from paramiko import SSHClient


class CounterACT_actions:
    def __init__(self, CounterACT_IP, CoutnerACT_username,CounterACT_password):
        self.CounterACT_IP = CounterACT_IP
        self.CoutnerACT_username = CoutnerACT_username
        self.CounterACT_password = CounterACT_password

    def run_command(self,command_to_run):
        try:
            client = paramiko.SSHClient()
            paramiko.client.AutoAddPolicy()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(self.CounterACT_IP, 22, self.CoutnerACT_username, self.CounterACT_password)
            stdin, stdout, stderr = client.exec_command(command_to_run)
            return stdout.read()+stderr.read()
        finally:
            client.close()

    def copy_file_to_appliance(self,local_file_path, appliance_path):
        cwd = os.getcwd()
        ssh = SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.CounterACT_IP, 22, self.CoutnerACT_username, self.CounterACT_password)
        #scp = SCPClient(ssh.get_transport(), sanitize=lambda x: x, progress=progress)
        scp = SCPClient(ssh.get_transport(), sanitize=lambda x: x)
        scp.put(cwd + local_file_path, appliance_path)




    def run_SQL_command(self, command_to_run):
        try:
            client = paramiko.SSHClient()
            paramiko.client.AutoAddPolicy()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(self.CounterACT_IP, port=22, username=self.CoutnerACT_username,
                           password=self.CounterACT_password)
            stdin, stdout, stderr = client.exec_command(command_to_run)
            return stdout.read()

        finally:
            client.close()