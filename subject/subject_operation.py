import json
import os
import time
import json
import os
import time
import time
from web3 import Web3
import json
import time

artifact = 'publication_sol_publish'
fn_abi = os.sep.join(['contract','{0}.abi'.format(artifact)])
fn_addr = os.sep.join(['contract','{0}.addr'.format(artifact)])

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

def type_conversion2(input):
    output = ""
    for i in input:
        output += i
        output += " "
    return output

def call_test_data(ID,AR,et,_pA,_pB,_pC,_pubSignals,r):#测试数据
  w3 = Web3(Web3.HTTPProvider('http://163.221.216.105:8545', request_kwargs={'timeout': 120}))
  accounts = w3.eth.accounts
  print(accounts)
  with open(fn_abi, 'r') as f:
    abi = json.load(f)
  with open(fn_addr,'r') as f:
    addr = f.read()
  w3.geth.personal.unlock_account(accounts[0],'lsm12345678')
  factory = w3.eth.contract(abi=abi, address=Web3.to_checksum_address(addr))
  factory.functions.submit_proof(ID,AR,et,_pA,_pB,_pC,_pubSignals,r).transact({'from': accounts[0]})
  print(factory.functions.get_proof().call())


def raw_ascii(input):
    return ord(input)

def ascii_8str(input):
    inter = str(bin(input))
    inter = inter[2:]
    if len(inter) < 8:
        for i in range(8 - len(inter)):
            inter = "0" + inter
    return inter

def reverse(input):
    inter = input[::-1]
    return inter

def raw_1byte_out(input):
    i = raw_ascii(input)
    j = ascii_8str(i)
    k = reverse(j)
    return k

def zkp_conversion(input,ram_value):
    inter = "[" + input + "]"
    inter_list = eval(inter)
    inter_list.append(ram_value)
    list = inter_list
    return list

def transform(zkp,ori_token):#use ori_token to make zkp_token
    zkp_token = ori_token.copy()
    zkp_token["Zero-knowledge proof"] = zkp
    return zkp_token

if __name__=="__main__":
    output_dic = {}
    inter_list = []
    zkp_token = {}
    ori_token = {}
    ID = "0xcaee213728819eb38a45674405bd894c1a0849a06e6a31e98119908773aafcb4"  # test ID
    c = input()
    ram_value = c[-3:]
    for item in c:
        inter = raw_1byte_out(item)
        for bit in inter:
            inter_list.append(int(bit))
    output_dic["in"] =  inter_list
    print(output_dic)
    with open(os.sep.join(['zkp_kit',"input.json"]), "w") as file:
        json.dump(output_dic, file)
    print(os.getcwd())
    os.chdir(os.getcwd())
    pos = 'zkp_kit'+os.sep
    print(os.popen(r"node {0}generate_witness.js {0}keccak256.wasm {0}input.json {0}witness.wtns".format(pos)).read())
    print(os.popen(r"snarkjs groth16 prove {0}multiplier2_0001.zkey {0}witness.wtns {0}proof.json {0}public.json".format(pos)).read())
    zkp = os.popen(r"snarkjs zkey export soliditycalldata {0}public.json {0}proof.json".format(pos)).read()
    zkp_list = zkp_conversion(zkp,ram_value)
    with open(r'{0}.json'.format(ID), 'r') as f:
        ori_token = json.load(f)
    zkp_token = transform(zkp_list,ori_token)
    print(zkp_token)
    with open(r'zkp_token-{0}.json'.format(ID), "w") as file:
        json.dump(zkp_token, file)
    zkp_token_struct = []
    zkp_token_struct.append(zkp_token['ID'])
    zkp_token_struct.append(type_conversion2(zkp_token['Access right']))
    zkp_token_struct.append(zkp_token['Expired time'])
    zkp_token_struct.append(type_conversion(zkp_token['Zero-knowledge proof'][0]))
    zkp_token_struct.append(type_conversion1(zkp_token['Zero-knowledge proof'][1]))
    zkp_token_struct.append(type_conversion(zkp_token['Zero-knowledge proof'][2]))
    zkp_token_struct.append(type_conversion(zkp_token['Zero-knowledge proof'][3]))
    zkp_token_struct.append(zkp_token['Zero-knowledge proof'][4])
    print(zkp_token_struct)
    call_test_data(zkp_token_struct[0], zkp_token_struct[1], zkp_token_struct[2], zkp_token_struct[3],
                   zkp_token_struct[4], zkp_token_struct[5], zkp_token_struct[6], zkp_token_struct[7])






