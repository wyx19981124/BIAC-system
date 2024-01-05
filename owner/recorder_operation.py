import json
from web3 import Web3
import os
import time
import token_verification

artifact = 'recorder_sol_recorder'
fn_abi = os.sep.join(['contract','{0}.abi'.format(artifact)])
fn_bin = os.sep.join(['contract','{0}.bin'.format(artifact)])
fn_addr = os.sep.join(['contract','{0}.addr'.format(artifact)])

def call_test_data(sub_id,obj_id,access_type):#测试数据
  t = int(time.time())
  w3 = Web3(Web3.HTTPProvider('http://163.221.216.107:8545', request_kwargs={'timeout': 120}))
  accounts = w3.eth.accounts
  with open(fn_abi, 'r') as f:
    abi = json.load(f)
  with open(fn_bin, 'r') as f:
    bin = f.read()
  with open(fn_addr,'r') as f:
    addr = f.read()
  w3.geth.personal.unlock_account(accounts[0], 'lsm12345678')
  factory = w3.eth.contract(abi=abi,address=Web3.to_checksum_address(addr))
  factory.functions.submit_record(sub_id, obj_id, access_type, t).transact({'from': accounts[0]})
  w3.geth.miner.set_etherbase(accounts[0])
  w3.geth.miner.start(8)
  time.sleep(5)
  w3.geth.miner.stop()
  print(factory.functions.get_record().call())

def press_recorder(sub_id):
  call_test_data(sub_id,'0x8e6415dc8cc0bd40a553b60bb8cacc9a59475aadaa120d16bc4a417c30c259b5','Trigger press')

def up_recorder(sub_id):
  call_test_data(sub_id, '0x8e6415dc8cc0bd40a553b60bb8cacc9a59475aadaa120d16bc4a417c30c259b5', 'Trigger up')

def down_recorder(sub_id):
  call_test_data(sub_id, '0x8e6415dc8cc0bd40a553b60bb8cacc9a59475aadaa120d16bc4a417c30c259b5', 'Trigger down')

def humid_read_recorder(sub_id):
  call_test_data(sub_id, '0xb7fec4a0295a38a48f16f58845fafab2411c332c8b39cc20573249f984928dbf', 'Read humidifier')

def humid_turnon_recorder(sub_id):
  call_test_data(sub_id, '0xb7fec4a0295a38a48f16f58845fafab2411c332c8b39cc20573249f984928dbf', 'Turn on')

def humid_turnoff_recorder(sub_id):
  call_test_data(sub_id, '0xb7fec4a0295a38a48f16f58845fafab2411c332c8b39cc20573249f984928dbf', 'Turn off')

def humid_setmode_recorder(sub_id,mode):
  if mode == "auto":
    call_test_data(sub_id, '0xb7fec4a0295a38a48f16f58845fafab2411c332c8b39cc20573249f984928dbf', 'Set auto mode')
  else:
    call_test_data(sub_id, '0xb7fec4a0295a38a48f16f58845fafab2411c332c8b39cc20573249f984928dbf', f'Set atomization efficiency to {mode}')

if __name__=="__main__":
  t = int(time.time())
  call_test_data('a','b','access',t)