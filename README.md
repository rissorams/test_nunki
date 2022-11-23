# API test

## Consigne 


## Get started 

You have, in the root project :
-   launch the terminal and type :
    -   `pip install -r ./requirements.txt` _install dependencies_
    -   `python3 ./api.py` _launch the program_

## PROXIES SOLUTION 

Proxies is a great solution, because we can change the ip adress from the requests and make believe the servers that we are a different person. 

For this we would like to use different proxies to try and get the apis informations from different ip adress and then dont get caught by fakejson. 

So we used [https://free-proxy-list.net/](https://free-proxy-list.net/ "https://free-proxy-list.net/%22) to get different proxies. 

Naturally we used only proxies using HTTPS protocole and select the ones usable on the website. Then I would like to requests our website from the ip adress of the proxies. 
Then were gonna use selenium (a WebDriver library of Python) to connect with the website.
That is preferable to use a Ubuntu virtual machine to make it more effective.