import json
import datetime
import os
from web3 import Web3
import time
import sha3

# def contract_deploy():
#     w3 = Web3(Web3.HTTPProvider('http://localhost:7545', request_kwargs={'timeout': 120}))
#     accounts = w3.eth.accounts
#     artifact = 'verifier_1_sol_Groth16Verifier'
#     fn_abi = os.sep.join(['contract', '{0}.abi'.format(artifact)])
#     fn_bin = os.sep.join(['contract', '{0}.bin'.format(artifact)])
#     fn_addr = os.sep.join(['contract', '{0}.addr'.format(artifact)])
#     with open(fn_abi, 'r') as f:
#         abi = json.load(f)
#     with open(fn_bin, 'r') as f:
#         bin = f.read()
#     print(abi)
#     print(bin)
#     factory = w3.eth.contract(abi=abi, bytecode=bin)
#     tx_hash = factory.constructor().transact({'from': accounts[0]})
#     receipt = w3.eth.waitForTransactionReceipt(tx_hash)
#     with open(fn_addr, 'w') as f:
#         f.write(receipt.contractAddress)
#     artifact = 'verifier_2_sol_Groth16Verifier'
#     fn_abi = os.sep.join(['contract', '{0}.abi'.format(artifact)])
#     fn_bin = os.sep.join(['contract', '{0}.bin'.format(artifact)])
#     fn_addr = os.sep.join(['contract', '{0}.addr'.format(artifact)])
#     with open(fn_abi, 'r') as f:
#         abi = json.load(f)
#     with open(fn_bin, 'r') as f:
#         bin = f.read()
#     print(abi)
#     print(bin)
#     factory = w3.eth.contract(abi=abi, bytecode=bin)
#     tx_hash = factory.constructor().transact({'from': accounts[0]})
#     receipt = w3.eth.waitForTransactionReceipt(tx_hash)
#     with open(fn_addr, 'w') as f:
#         f.write(receipt.contractAddress)

def contract_invoke(token,num):#测试数据
  artifact = 'verifier_{0}_sol_Groth16Verifier'.format(num)
  fn_abi = os.sep.join(['contract', '{0}.abi'.format(artifact)])
  fn_bin = os.sep.join(['contract', '{0}.bin'.format(artifact)])
  fn_addr = os.sep.join(['contract', '{0}.addr'.format(artifact)])
  w3 = Web3(Web3.HTTPProvider('http://163.221.216.107:8545', request_kwargs={'timeout': 120}))
  accounts = w3.eth.accounts
  with open(fn_abi, 'r') as f:
    abi = json.load(f)
  with open(fn_bin, 'r') as f:
    bin = f.read()
  with open(fn_addr,'r') as f:
    addr = f.read()
  factory = w3.eth.contract(abi=abi,address=Web3.to_checksum_address(addr))
  output = factory.functions.verifyProof(token['Zero-knowledge proof'][0],token['Zero-knowledge proof'][1],token['Zero-knowledge proof'][2],token['Zero-knowledge proof'][3]).call()
  return output

def type_conversion(input):
  output = []
  for i in input:
      output.append(int(i,16))
  return output

def type_conversion1(input):
  output = []
  for x in input:
    inter = []
    for i in x:
      inter.append(int(i,16))
    output.append(inter)
  return output

def keccak_enc(input):
    k = sha3.keccak_256()
    k.update(str.encode(input))
    return k.hexdigest()

def open_token(ID):
    with open(os.sep.join(['zkp_token','zkp_token-{0}.json'.format(ID)]),"r") as f:
        zkp_token = json.load(f)
        return zkp_token

def bin_hex(input):
    output = ""
    if "0b0000" in input:
        output = "0"
    output = output + hex(int(input, 2)).replace("0x","")
    return output

def output_conversion(input):
    list = input[-2]
    inter = ""
    output =""
    for i in list:
        if i == 1:
            inter = inter + "1"
        else:
            inter = inter + "0"
    # inter = inter[::-1]
    for x in range(len(inter)):
        if x%8 == 0:
            k = "0b"+inter[x:x+8][::-1]
            output = output + bin_hex(k)
        else:
            pass
    return output

def verify_time(token):
    dtime = datetime.datetime.now()
    now_time = int(time.mktime(dtime.timetuple()))
    exp_time = token['Expired time']
    if exp_time > now_time:
        return True
    else:
        return False

def verify_token(token):
    with open(os.sep.join(['ori_token','{0}.json'.format(token['ID'])]),"r") as f:
        ori_token = json.load(f)
    test_token = token.copy()
    del test_token['Zero-knowledge proof']
    if test_token == ori_token:
        return True
    else:
        return False

def verify_public_output(token):
    with open(os.sep.join(["access_list",'access_list.json']), 'r') as f:
        access_list = json.load(f)["item"]
    map_num = 0
    for item in access_list:
        if item['ID'] == token['ID']:
            map_num = item['Mapping number']
    secret = str(map_num)+token['Zero-knowledge proof'][-1]
    sec_kec_value = keccak_enc(secret)
    out_kec_value = output_conversion(token['Zero-knowledge proof'])
    if sec_kec_value == out_kec_value:
        return True
    else:
        return False

def verify_zkp(token):
    return (contract_invoke(token,"1") and contract_invoke(token,"2"))

def token_verification(ID):
    token = open_token(ID)
    print("Expired time verification:", verify_time(token))
    print("Token tampering verification:", verify_token(token))
    print("Public output verification:", verify_public_output(token))
    print("zkp verification:", verify_zkp(token))
    print("Result:", end=' ')
    if (verify_time(token) and verify_token(token)
            and verify_public_output(token) == True and verify_zkp(token) == True):
        return True
    else:
        return False

if __name__=="__main__":
    ID = "0x73b49fe9b2415f7043a9fabd65f4f4ea3962b31d51617906e5ba75ced62a3fb9"  # test ID
    token = open_token(ID)
    print(token)
    print("Expired time verification:",verify_time(token))
    print("Token tampering verification:",verify_token(token))
    print("Public output verification:",verify_public_output(token))
    print("zkp verification:",verify_zkp(token))
    if (verify_time(token) and verify_token(token)
            and verify_public_output(token) == True and verify_zkp(token) == True):
        print(True)
    else:
        print(False)

