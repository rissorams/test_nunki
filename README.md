# API TEST NUNKI

## ORDER 

Practical Part

[https://fakejson.com/](https://fakejson.com/) is a tool that allows you to mock api's.

We want to use this tool without being identified by the service. Your task is to create a code that makes a https call to a mocked API (created by you) without being able to be identified by fakejson in any way. You can use the programming language of your choice. If your solution has limits, please explain them and how you would proceed to resolve them.

You should add a readme explaining how to launch it and package everything in a git repo.

## GET STARTED 

You have, in the root project :
-   launch the terminal and type :
    -   `pip install -r ./requirements.txt` _install dependencies_
    -   `python3 ./api.py` _launch the program_

## PROXIES SOLUTION 

Proxies is a great solution, because we can change the ip adress from the requests and make believe the servers that we are a different person. 

For this we would like to use different proxies to try and get the apis informations from different ip adress and then dont get caught by fakejson. 

So we used [https://free-proxy-list.net/](https://free-proxy-list.net/) to get different proxies. 

Naturally we used only proxies using HTTPS protocole and select the ones usable on the website. Then I would like to requests our website from the ip adress of the proxies. 
Then were gonna use selenium (a WebDriver library of Python) to connect with the website.
That is preferable to use a Ubuntu virtual machine to make it more effective.

## MY TESTS

First of all, I tried to use User-Agent with different Header from multiple navigator to fake requests but that didnt made me unable to identify.

So I figured that make a VPN was a great solution but I cant really make it that easely so I managed to Scrape the website with Python with other Proxies and multiple time to vanish from FakeJSON.