import json
from web3 import Web3
import os
import time
import token_verification

artifact = 'publication_sol_publish'
fn_abi = os.sep.join(['contract','{0}.abi'.format(artifact)])
fn_bin = os.sep.join(['contract','{0}.bin'.format(artifact)])
fn_addr = os.sep.join(['contract','{0}.addr'.format(artifact)])

def call_test_data():#测试数据
  w3 = Web3(Web3.HTTPProvider('http://163.221.216.107:8545', request_kwargs={'timeout': 120}))
  accounts = w3.eth.accounts
  w3.geth.personal.unlock_account(accounts[0], 'lsm12345678')
  w3.geth.miner.set_etherbase(accounts[0])
  w3.geth.miner.start(8)
  time.sleep(10)
  w3.geth.miner.stop()
  with open(fn_abi, 'r') as f:
    abi = json.load(f)
  with open(fn_bin, 'r') as f:
    bin = f.read()
  with open(fn_addr,'r') as f:
    addr = f.read()
  factory = w3.eth.contract(abi=abi,address=Web3.to_checksum_address(addr))
  return factory.functions.get_proof().call()

def type_conversion_ar(input):
  output = input.split(" ")
  return output[0:-1]

def reduct_token(input):
  inter_list = []
  inter_list.append(input[3])
  inter_list.append(input[4])
  inter_list.append(input[5])
  inter_list.append(input[6])
  inter_list.append(input[7])
  output_dic = {}
  output_dic['ID'] = input[0]
  output_dic['Access right'] = type_conversion_ar(input[1])
  output_dic['Expired time'] = input[2]
  output_dic['Zero-knowledge proof'] = inter_list
  return [output_dic,input[0]]

def token_reduction(ID,r):
  list = call_test_data()
  status = False
  for i in range(len(list)):
    if list[i][0] == ID and list[i][7] == r:
      zkp_token =  reduct_token(list[i])[0]
      with open(os.sep.join(['zkp_token','zkp_token-{0}.json'.format(reduct_token(list[i])[1])]),"w") as file:
        json.dump(zkp_token, file)
      status = True
  return status


if __name__=="__main__":
  list = call_test_data()
  print(list)
#   zkp_token = reduct_token(list[0])[0]
#   with open(r'C:\py\zkp-access-control\owner\zkp_token\zkp_token-{0}.json'.format(reduct_token(list[0])[1]), "w") as file:
#     json.dump(zkp_token, file)