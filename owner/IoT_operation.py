import paramiko
import time
import json
import time
import hashlib
import hmac
import base64
import uuid
import requests

def press_operation():
    time.sleep(10)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('163.221.216.111', port=22, username='pi', password='lsm12345678')
    stdin, stdout, stderr = ssh.exec_command('sudo python python-host/switchbot.py c7:38:32:30:4b:09 Bot Press')
    print(stdout.read().decode())
    ssh.close()

def up_operation():
    time.sleep(10)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('163.221.216.111', port=22, username='pi', password='lsm12345678')
    stdin, stdout, stderr = ssh.exec_command('sudo python python-host/switchbot.py c7:38:32:30:4b:09 Bot Up')
    print(stdout.read().decode())
    ssh.close()

def down_operation():
    time.sleep(10)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('163.221.216.111', port=22, username='pi', password='lsm12345678')
    stdin, stdout, stderr = ssh.exec_command('sudo python python-host/switchbot.py c7:38:32:30:4b:09 Bot Down')
    print(stdout.read().decode())
    ssh.close()

def humid_read_operation():
    apiHeader = {}
    API_HOST = 'https://api.switch-bot.com'
    token = '7558cd266a2d138974e3a18ccc90a10dea15337f6915f73c700121dd42bd2326972f427b055fc22e438e373a143626f0'  # copy and paste from the SwitchBot app V6.14 or later
    secret = 'd4727cd8f3b13a6c5a004fcfa7979f6b'  # copy and paste from the SwitchBot app V6.14 or later
    nonce = uuid.uuid4()
    t = int(round(time.time() * 1000))
    string_to_sign = '{}{}{}'.format(token, t, nonce)
    string_to_sign = bytes(string_to_sign, 'utf-8')
    secret = bytes(secret, 'utf-8')
    sign = base64.b64encode(hmac.new(secret, msg=string_to_sign, digestmod=hashlib.sha256).digest())
    apiHeader['Authorization'] = token
    apiHeader['Content-Type'] = 'application/json'
    apiHeader['charset'] = 'utf8'
    apiHeader['t'] = str(t)
    apiHeader['sign'] = str(sign, 'utf-8')
    apiHeader['nonce'] = str(nonce)
    device_id = '0CDC7EE69F12'
    status_url = f"{API_HOST}/v1.1/devices/{device_id}/status"
    response = requests.get(status_url, headers=apiHeader).text
    return response

def humid_turnon_operation():
    apiHeader = {}
    API_HOST = 'https://api.switch-bot.com'
    token = '7558cd266a2d138974e3a18ccc90a10dea15337f6915f73c700121dd42bd2326972f427b055fc22e438e373a143626f0'  # copy and paste from the SwitchBot app V6.14 or later
    secret = 'd4727cd8f3b13a6c5a004fcfa7979f6b'  # copy and paste from the SwitchBot app V6.14 or later
    nonce = uuid.uuid4()
    t = int(round(time.time() * 1000))
    string_to_sign = '{}{}{}'.format(token, t, nonce)
    string_to_sign = bytes(string_to_sign, 'utf-8')
    secret = bytes(secret, 'utf-8')
    sign = base64.b64encode(hmac.new(secret, msg=string_to_sign, digestmod=hashlib.sha256).digest())
    apiHeader['Authorization'] = token
    apiHeader['Content-Type'] = 'application/json'
    apiHeader['charset'] = 'utf8'
    apiHeader['t'] = str(t)
    apiHeader['sign'] = str(sign, 'utf-8')
    apiHeader['nonce'] = str(nonce)
    device_id = '0CDC7EE69F12'
    open_url = f"{API_HOST}/v1.1/devices/{device_id}/commands"
    data = {
        "command": "turnOn",
        "parameter": "default",
        "commandType": "command"
    }
    request = requests.post(open_url, data=json.dumps(data), headers=apiHeader).text
    print(request)

def humid_turnoff_operation():
    apiHeader = {}
    API_HOST = 'https://api.switch-bot.com'
    token = '7558cd266a2d138974e3a18ccc90a10dea15337f6915f73c700121dd42bd2326972f427b055fc22e438e373a143626f0'  # copy and paste from the SwitchBot app V6.14 or later
    secret = 'd4727cd8f3b13a6c5a004fcfa7979f6b'  # copy and paste from the SwitchBot app V6.14 or later
    nonce = uuid.uuid4()
    t = int(round(time.time() * 1000))
    string_to_sign = '{}{}{}'.format(token, t, nonce)
    string_to_sign = bytes(string_to_sign, 'utf-8')
    secret = bytes(secret, 'utf-8')
    sign = base64.b64encode(hmac.new(secret, msg=string_to_sign, digestmod=hashlib.sha256).digest())
    apiHeader['Authorization'] = token
    apiHeader['Content-Type'] = 'application/json'
    apiHeader['charset'] = 'utf8'
    apiHeader['t'] = str(t)
    apiHeader['sign'] = str(sign, 'utf-8')
    apiHeader['nonce'] = str(nonce)
    device_id = '0CDC7EE69F12'
    open_url = f"{API_HOST}/v1.1/devices/{device_id}/commands"
    data = {
        "command": "turnOff",
        "parameter": "default",
        "commandType": "command"
    }
    request = requests.post(open_url, data=json.dumps(data), headers=apiHeader).text
    print(request)

def humid_mode_operation(mode):
    apiHeader = {}
    API_HOST = 'https://api.switch-bot.com'
    token = '7558cd266a2d138974e3a18ccc90a10dea15337f6915f73c700121dd42bd2326972f427b055fc22e438e373a143626f0'  # copy and paste from the SwitchBot app V6.14 or later
    secret = 'd4727cd8f3b13a6c5a004fcfa7979f6b'  # copy and paste from the SwitchBot app V6.14 or later
    nonce = uuid.uuid4()
    t = int(round(time.time() * 1000))
    string_to_sign = '{}{}{}'.format(token, t, nonce)
    string_to_sign = bytes(string_to_sign, 'utf-8')
    secret = bytes(secret, 'utf-8')
    sign = base64.b64encode(hmac.new(secret, msg=string_to_sign, digestmod=hashlib.sha256).digest())
    apiHeader['Authorization'] = token
    apiHeader['Content-Type'] = 'application/json'
    apiHeader['charset'] = 'utf8'
    apiHeader['t'] = str(t)
    apiHeader['sign'] = str(sign, 'utf-8')
    apiHeader['nonce'] = str(nonce)
    device_id = '0CDC7EE69F12'
    open_url = f"{API_HOST}/v1.1/devices/{device_id}/commands"
    data = {
        "command": "setMode",
        "parameter": mode,
        "commandType": "command"
    }
    request = requests.post(open_url, data=json.dumps(data), headers=apiHeader).text
    print(request)

humid_turnoff_operation()