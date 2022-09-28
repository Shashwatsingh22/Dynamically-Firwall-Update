# Dynamically Firewall Update
## Modules 
1.  [API](https://github.com/Shashwatsingh22/Dynamically-Firwall-Update/tree/api)
2.  [Python Script](https://github.com/Shashwatsingh22/Dynamically-Firwall-Update/tree/python-script)
3.  [Ansible Role](https://github.com/Shashwatsingh22/Dynamically-Firwall-Update/tree/ansible-role)
4.  [Jenkinsfile](https://github.com/Shashwatsingh22/Dynamically-Firwall-Update/tree/trigger)

## Demo🎬
[![Demo](https://img.youtube.com/vi/bu2nBt45H6A/0.jpg)](https://www.youtube.com/watch?v=bu2nBt45H6A)

## *Problem Statement*

A company has a **server(S)** running on **Linux hosted** somewhere which is publicly accessible. You need to restrict its access to only 2 whitelisted IP addresses: **210.212.85.155 and X** on ports **22, 443, 80**.

**X** is the IP address of this **company's headquarters**.

The company's headquarters does not have a **static IP** and **keeps on changing**, which requires staff to manually grant the access to the **new IP address.**

## **Approach**

 - For fetching the IP  created an **API** which will **hosted at Server-X** (On GET request to this route /getUpdatedIP) (Create API by [NodeJS](https://github.com/Shashwatsingh22/Dynamically-Firwall-Update/tree/api))

 -  Created an [**Python Script**](https://github.com/Shashwatsingh22/Dynamically-Firwall-Update/tree/python-script) which making the **GET request** and find the **IP** after that it will **check with exitsing one** where it is **mainting IP data** in an [**variable file** (**of ansible**)](https://github.com/Shashwatsingh22/Dynamically-Firwall-Update/blob/ansible-role/changeUbuntuFirwall/vars/main.yml), 
	- If that **last IP not matches** **with current IP** then it will update the **variable file** of the **ansible** where deny-var now become the previous IP and allow-var become the current IP.
	  - Now, Finally **it will trigger** the **[ansible-playbook](https://github.com/Shashwatsingh22/Dynamically-Firwall-Update/blob/ansible-role/setup.yml)**.
	- Else it will exit with message (IP not change).
- For **Configuring Firewall** Created an [**Ansible Role**](https://github.com/Shashwatsingh22/Dynamically-Firwall-Update/tree/ansible-role).
		  - First **Deny the traffic** from the **last IP** (**Getting last IP  by the Help of Variable File**) on **respected Port number's**.
		  - Then **allow the traffic** for **new IP** on respected Port number's.
- **Python Script** can be **triggered by two ways** :-

    - By [**Scheduled CronJob** **(Dynamically)**](https://github.com/Shashwatsingh22/Dynamically-Firwall-Update/tree/python-script) according to the configured time  Or I can also able to setup in the Jenkins (i.e [Build Trigger](https://github.com/Shashwatsingh22/Dynamically-Firwall-Update/tree/python-script#readme) 
    - By Run Job[**Jenkins** **(Manually)**](https://github.com/Shashwatsingh22/Dynamically-Firwall-Update/tree/trigger)
				
**Complete Architecture Structure**

![ArchIMP1.1](https://raw.githubusercontent.com/Shashwatsingh22/Dynamically-Firwall-Update/main/archIMG/1.1.PNG)

**Working**

![ArchIMG1.2](https://raw.githubusercontent.com/Shashwatsingh22/Dynamically-Firwall-Update/main/archIMG/1.2.PNG)
