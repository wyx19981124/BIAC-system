import json
import datetime
import os
from web3 import Web3
import time

p_time1 = time.time()
w3 = Web3(Web3.HTTPProvider('http://163.221.216.107:8545', request_kwargs={'timeout': 120}))
accounts = w3.eth.accounts
print(accounts[0])
artifact = 'publication_sol_publish'
fn_abi = os.sep.join(['contract','{0}.abi'.format(artifact)])
fn_bin = os.sep.join(['contract','{0}.bin'.format(artifact)])
fn_addr = os.sep.join(['contract','{0}.addr'.format(artifact)])
with open(fn_abi, 'r') as f:
    abi = json.load(f)
with open(fn_bin, 'r') as f:
    bin = f.read()
print(abi)
print(bin)
w3.geth.personal.unlock_account(accounts[0],'lsm12345678')
factory = w3.eth.contract(abi=abi, bytecode=bin)
tx_hash = factory.constructor().transact({'from': accounts[0]})
w3.geth.miner.set_etherbase(accounts[0])
w3.geth.miner.start(8)
time.sleep(1)
w3.geth.miner.stop()
receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(receipt)
p_time2 = time.time()
print("recorder contract time:"+str(p_time2-p_time1))
# with open(fn_addr, 'w') as f:
#     f.write(receipt.contractAddress)

