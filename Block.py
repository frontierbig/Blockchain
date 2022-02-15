import hashlib
import json
import os
BLOCKCHAIN_DIR = 'Data/'
class Block:

    def __init__(self,index, previous_block_hash, transaction):
        self.index=index
        self.previous_block_hash = previous_block_hash
        self.transaction = transaction
        self.data ={
            "index": index,
            "previous_block_hash": previous_block_hash,
            "data": transaction,
        }
        self.DataBlock = f"{index}{previous_block_hash}{transaction}"
        self.hash_block = hashlib.sha256(self.DataBlock.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.generate_genesis_block()

    def generate_genesis_block(self):
        self.chain.append(Block(0,"0", ['Genesis Block']))


    def create_block_from_transaction(self,transaction_list):
        index = len(self.chain)
        previous_block_hash = self.last_block.hash_block
        self.chain.append(Block(index,previous_block_hash, transaction_list))
    @property
    def last_block(self):
        return self.chain[-1]

###Setup Blockchain
myblockchain = Blockchain()
data1={
            "tram1": "Fannatic",
            "tram2": "T1",
            "Time": "16.00",
            "Date":"2022-01-27",
}
myblockchain.create_block_from_transaction(data1)
data2={
            "tram1": "Team Spirit",
            "tram2": "Virtus.pro",
            "Time": "16.00",
            "Date":"2022-01-28",
}
myblockchain.create_block_from_transaction(data2)
data3={
            "tram1": "PSG.LGD",
            "tram2": "Evil Geniuses",
            "Time": "9.00",
            "Date":"2022-01-28",
}
myblockchain.create_block_from_transaction(data3)
data4={
            "tram1": "Beastcoast",
            "tram2": "Evil Geniuses",
            "Time": "9.00",
            "Date":"2022-01-28",
}
myblockchain.create_block_from_transaction(data4)
data5={
            "tram1": "PSG.LGD",
            "tram2": "Evil Geniuses",
            "Time": "9.00",
            "Date":"2022-01-29",
}
myblockchain.create_block_from_transaction(data5)
data6={
            "tram1": "PSG.LGD",
            "tram2": "Fnatic",
            "Time": "9.00",
            "Date":"2022-01-29",
}
myblockchain.create_block_from_transaction(data6)
data7={
            "tram1": "Vici Gaming",
            "tram2": "Evil Geniuses",
            "Time": "9.00",
            "Date":"2022-01-29",
}
myblockchain.create_block_from_transaction(data7)
data8={
            "tram1": "PSG.LGD",
            "tram2": "Alliance",
            "Time": "9.00",
            "Date":"2022-01-30",

}
myblockchain.create_block_from_transaction(data8)
data9={
            "tram1": "SG esports",
            "tram2": "Evil Geniuses",
            "Time": "9.00",
            "Date":"2022-01-12",

}
myblockchain.create_block_from_transaction(data9)
data10={
            "tram1": "PSG.LGD",
            "tram2": "Elephant",
            "Time": "9.00",
            "Date":"2022-01-30",

}
myblockchain.create_block_from_transaction(data10)
data11={
            "tram1": "Quincy Crew",
            "tram2": "Invictus Gaming",
            "Time": "1.00",
            "Date":"2022-01-123",

}
myblockchain.create_block_from_transaction(data11)
data12={
            "tram1": "Quincy Crew",
            "tram2": "Invictus Gaming",
            "Time": "9.00",
            "Date":"2022-01-30",

}
myblockchain.create_block_from_transaction(data12)



####Funtion program

def printBlock (a):
    print(f"Block {myblockchain.chain[a].index}")
    print(f"Previous Hash: {myblockchain.chain[a].previous_block_hash}")
    print(f"Data : {myblockchain.chain[a].transaction}")
    print(f"Hash : {myblockchain.chain[a].hash_block}\n")


def printAllBlock():
    print("============================================================================")
    for i in range(len(myblockchain.chain)):
        printBlock(i)

# printAllBlock()

def delfile():
    for i in os.listdir(BLOCKCHAIN_DIR):
        os.remove(BLOCKCHAIN_DIR + i)
def write_block_database():
    delfile()
    for i in range(len(myblockchain.chain)):
        index =  myblockchain.chain[i].index
        previous_block_hash = myblockchain.chain[i].previous_block_hash
        transaction=myblockchain.chain[i].transaction
        hash_block=myblockchain.chain[i].hash_block
        data = {
            'Block_index':index,
            "previous_block_hash":previous_block_hash,
            "transaction":transaction,
            "hash_block":hash_block,
        }
        current_block = BLOCKCHAIN_DIR + str(len(os.listdir(BLOCKCHAIN_DIR)))
        with open(current_block, 'w') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            f.write('\n')
            f.close()
###เช็คในไฟลของตัวมันเองในเครื่องเช็คในเครื่อง
def check_integrity():
    files = sorted(os.listdir(BLOCKCHAIN_DIR), key=lambda x: int(x))
    results = []
    for file in files[0:]:
        with open(BLOCKCHAIN_DIR + file) as f:
            block = json.load(f)
        index = block.get('Block_index')
        previous_block_hash=block.get('previous_block_hash')
        transaction = block.get('transaction')
        DataBlock = f"{index}{previous_block_hash}{transaction}"
        new_hash_block = hashlib.sha256(DataBlock.encode()).hexdigest()
        file_hash_block = block.get('hash_block')
        if new_hash_block == file_hash_block:
            response = 'OK'
        else:
            response = 'Was Changed'
        print(f'Block {index}: {response}')
        results.append({'block': index, 'result': response})
    return results
###
def check_integrityblock():
    files = sorted(os.listdir(BLOCKCHAIN_DIR), key=lambda x: int(x))
    results = []
    for file in files:
        with open(BLOCKCHAIN_DIR + file) as f:
            block = json.load(f)
        index = block.get('Block_index')
        previous_block_hash = block.get('previous_block_hash')
        transaction = block.get('transaction')
        DataBlock = f"{index}{previous_block_hash}{transaction}"
        Data_hash_block = hashlib.sha256(DataBlock.encode()).hexdigest()

        if Data_hash_block == myblockchain.chain[index].hash_block:
            # print(block.get("transaction"))
            response = 'OK'
        else:
            response = 'Was Changed'


        # if new_hash_block == file_hash_block:
        #     response = 'OK'
        # else:
        #     response = 'Was Changed'
        print(f'Block {index}: {response}')
        results.append({'block': index, 'result': response})
    return results


write_block_database()
def addblock():
    Data ={}
    Team1 = input("Enter Team1 :")
    Team2 = input("Enter Team2 :")
    Time = input("Enter Time :")
    Date = input("Enter Date :")
    Data['Team1'] = Team1
    Data['Team2'] = Team2
    Data['Time']=Time
    Data['Date']=Date
    myblockchain.create_block_from_transaction(Data)

def option():
    print("==== OPTION ===")
    print("1:Printblockchain")
    print("2:PrintblockchainInDex")
    print("3:AddBlockchain")
    print("4:Detect")
    print("5:Exit")


A=0
#write_block_database()
while(A==0):
    option()
    op=input("Enter option :")
    lenchian=len(myblockchain.chain)
    if(op == "1"):
        printAllBlock()
    elif(op=="2"):
        index=int(input("Enter blockchain index :"))
        if (index>lenchian):
            print(f"invalid index try again, Blockchain has {lenchian} block")
            continue
        print("============================================================================")
        printBlock(index)
    elif(op=="3"):
        addblock()
    elif(op=="4"):
        check_integrityblock()
    elif(op=="5"):
        break
    else:
        print("invalid input , try again ")