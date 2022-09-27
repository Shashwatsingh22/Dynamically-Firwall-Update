## Python Script Configuration
It will make the request to API and get IP then trigger the Ansible-Playbook if the IP is updated.

**Requirements**
- python-dotenv
- requests
- pyyaml

**Env File**

- Give the API_URL
- File Loacation for var file of Ansible.

**Run the Script**

    python3 main.py

**Cron Configuration** 

![cron1.1](https://raw.githubusercontent.com/Shashwatsingh22/Dynamically-Firwall-Update/python-script/ConfigIMG/cron1.PNG)
![cron1.2](https://raw.githubusercontent.com/Shashwatsingh22/Dynamically-Firwall-Update/python-script/ConfigIMG/cron2.PNG)

**Jenkins Configuration**
For Configuration [Read My Blog](https://towardsaws.com/installation-of-jenkins-on-rhel8-8f7bd5c87d40) (Either on Ubuntu or CentOS)
