import json
import os
ori_token = {}


def create(ID, Right, Time):#create ori_token
    ori_token["ID"] = ID
    ori_token["Access right"] = Right
    ori_token["Expired time"] = Time

if __name__=="__main__":
    ID = "0xadb3d11372340aa9b42d754fba66822f7c6b53d0e26efda7a7488ed563efffb5"
    create(ID,["write","read"], 2000000000)#test data
    print(ori_token)
    with open(os.sep.join(["ori_token","{0}.json"]).format(ID), "w") as file:
        json.dump(ori_token, file)
    file.close()