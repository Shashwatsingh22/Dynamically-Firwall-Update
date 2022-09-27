#Importing the Modules
import os
from dotenv import load_dotenv
import requests as req
import yaml
from yaml.loader import SafeLoader


#Loading the .env file
load_dotenv()

def getIP():
    apiURL = os.getenv('API_URL')
    data = req.get(url=apiURL)
    data = data.json()
    return data;

def isNewIP(newIP):
    fileLocation=os.getenv('LOCATION_VAR_FILE')
    data=""
    with open(fileLocation,'r') as f:
        data = yaml.load(f, Loader=SafeLoader)
        
    if(data['ipToAllow']==newIP):
        return False
    
    else:
        ipToDeny = data['ipToAllow']
        data['ipToAllow']=newIP
        data['ipToDeny']=ipToDeny
        with open(fileLocation, 'w') as f:
            yaml.dump(data, f, sort_keys=False, default_flow_style=False)
        return True;    

def main():
    data = getIP()
    if(data['status']):
        #Fetch the IP first
        newIP = data["ip"]
        
        #First we will update the variable file if there is any update in file
        #Here We Execute the Ansible Playbook
        if(isNewIP(newIP)):
            os.system('ansible-playbook /home/ubuntu/setup.yml')
        
            print("Task Completed")        
        

if __name__ == "__main__":
    main()