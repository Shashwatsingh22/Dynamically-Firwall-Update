## GET-IP API
This API going to help our script to check about the IP of server-x.

**Setup**

    $ npm ci
    $ npm run dev (Devlopment Env)
    $ npm start

Its better to configure the System file for this API, I have provided the system file in repo download it and put it at;

    $ sudo mv ./getIP-api.service /etc/systemd/system/
    $ sudo systemctl daemon-reload
    $ sduo systemctl start getIP-api.service

**Routes**
1.  /  (GET) --> OutPut -> Status About Server

![1.1](https://raw.githubusercontent.com/Shashwatsingh22/Dynamically-Firwall-Update/api/demo/1.2.PNG)

2. /getUpdatedIP --> OutPut -> Server IP as Response

![1.2](https://raw.githubusercontent.com/Shashwatsingh22/Dynamically-Firwall-Update/api/demo/home.PNG)
