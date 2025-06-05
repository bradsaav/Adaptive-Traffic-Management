

import os
import time
import firebase_admin; 
from firebase_admin import credentials, firestore;
import json
def pub(t, direct):
    if direct == 0:
        pubNorth(t)
    elif direct == 1:
        pubSouth(t)
    elif direct == 2:
        pubWest(t)
    else:
        pubEast(t)
def pubNorth(t):
    if t:
        os.system('python3 -c "import firebase_admin; from firebase_admin import credentials, firestore; cred=credentials.Certificate(\'Firestore.json\'); firebase_admin.initialize_app(cred); db=firestore.client(); db.collection(\'traffic_data\').document(\'north\').update({\'light_state\': 1})"')
    else:
        os.system('python3 -c "import firebase_admin; from firebase_admin import credentials, firestore; cred=credentials.Certificate(\'Firestore.json\'); firebase_admin.initialize_app(cred); db=firestore.client(); db.collection(\'traffic_data\').document(\'north\').update({\'light_state\': 0})"')
def pubSouth(t):
    if t:
        os.system('python3 -c "import firebase_admin; from firebase_admin import credentials, firestore; cred=credentials.Certificate(\'Firestore.json\'); firebase_admin.initialize_app(cred); db=firestore.client(); db.collection(\'traffic_data\').document(\'south\').update({\'light_state\': 1})"')
    else:
        os.system('python3 -c "import firebase_admin; from firebase_admin import credentials, firestore; cred=credentials.Certificate(\'Firestore.json\'); firebase_admin.initialize_app(cred); db=firestore.client(); db.collection(\'traffic_data\').document(\'south\').update({\'light_state\': 0})"')
def pubWest(t):
    if t:
        os.system('python3 -c "import firebase_admin; from firebase_admin import credentials, firestore; cred=credentials.Certificate(\'Firestore.json\'); firebase_admin.initialize_app(cred); db=firestore.client(); db.collection(\'traffic_data\').document(\'west\').update({\'light_state\': 1})"')
    else:
        os.system('python3 -c "import firebase_admin; from firebase_admin import credentials, firestore; cred=credentials.Certificate(\'Firestore.json\'); firebase_admin.initialize_app(cred); db=firestore.client(); db.collection(\'traffic_data\').document(\'west\').update({\'light_state\': 0})"')
def pubEast(t):
    if t:
        os.system('python3 -c "import firebase_admin; from firebase_admin import credentials, firestore; cred=credentials.Certificate(\'Firestore.json\'); firebase_admin.initialize_app(cred); db=firestore.client(); db.collection(\'traffic_data\').document(\'east\').update({\'light_state\': 1})"')
    else:
        os.system('python3 -c "import firebase_admin; from firebase_admin import credentials, firestore; cred=credentials.Certificate(\'Firestore.json\'); firebase_admin.initialize_app(cred); db=firestore.client(); db.collection(\'traffic_data\').document(\'east\').update({\'light_state\': 0})"')


#def read():
# return os.system('python3 -c "south_data = db.collection(\'traffic_data\').document(\'south\').get().to_dict(); south_queue, south_light = #south_data[\'vehicle_queue\'], south_data[\'light_state\']')

def main():
#Presets
    carClass = 3
    currentLight = [0,0,0,0] #0 - red, 1 - yellow, 2 - green
    incomingDensity = [0,0,0,0]
    laneDensity = [0,0,0,0]
    starvation = [1,1,1,1]
    priority = [0.0,0.0,0.0,0.0]

#PULL FROM CLOUD HERE TO RECIEVE INCOMING LANE DENSITY
#test = read()
    while True:
        laneDensity[0] = int(input())
        laneDensity[1] = int(input())
        laneDensity[2] = int(input())
        laneDensity[3] = int(input())


#compute which lane goes first
        totalVehicles = 0
        for i in laneDensity:
            totalVehicles += i
        if totalVehicles != 0:
            for i in range(len(priority)):
                calcPrio = (laneDensity[i]*starvation[i] + 0.5*incomingDensity[i])/totalVehicles
                priority[i] = float(calcPrio)

        #Start cycling lights
        for i in range(4):
            cPrio = priority.index(max(priority))
            currentLight[cPrio] == 2
            pub(1, cPrio)
            time.sleep(10)
            pub(0, cPrio)
            currentLight[cPrio] == 0
            priority[cPrio] = 0
            time.sleep(1)
            starvation[cPrio] == 4-i

        #reset vars
        laneDensity[0] = 0
        incomingDensity = [0,0,0,0]

if __name__ == '__main__':
    main()

