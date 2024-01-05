import json
import os
access_list = {}

def create():#create access control list
    access_list["item"] = []

def add(ID,Right,Number):#add new subject
    access_list["item"].append({"ID":ID, "Access right":Right, "Mapping number": Number})

if __name__=="__main__":
    create()
    add("0xcaee213728819eb38a45674405bd894c1a0849a06e6a31e98119908773aafcb4",["write","read"],52244)#test data
    add("0xadb3d11372340aa9b42d754fba66822f7c6b53d0e26efda7a7488ed563efffb5", ["exe", "read"], 12345)  # test data
    print(access_list)
    with open(os.sep.join(["access_list",'access_list.json']), "w") as file:
        json.dump(access_list, file)
    file.close()


