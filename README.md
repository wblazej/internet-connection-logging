# Internet connection logging
This project has been created because of annoying Internet connection breaks. This simple Python code will log every connection break, so you will know when your Internet operator is idling and lazy.

## Docker install
You need to have docker installed on your operating system.
```
git clone https://github.com/wblazej/internet-connection-logging
cd internet-connection-logging
sudo docker build -t icl .
sudo docker run -t -d icl
```
### Get logs
To get logs, type command `sudo docker ps` and copy `CONTAINER ID` of `IMAGE` icl. Then type command `sudo docker logs <container_id>` and you will get logs.

### Stop app
To get logs, type command `sudo docker ps` and copy `CONTAINER ID` of `IMAGE` icl. Then type command `sudo docker stop <container_id>` and wait some seconds to app stopped.

## Other install
You need `python3.*` installed on your operating system.
```
git clone https://github.com/wblazej/internet-connection-logging
cd internet-connection-logging
sudo python internet-connection-logging.py
```
If you are using Linux or Max, remember that you have to run this file as root.
### Detached running on Linux/Mac
```
chmod +x internet-connection-logging.py
nohup python ./internet-connection-logging.py > logs.log &
```
### Stop detached process
To stop detached python file running, type command:
```
pgrep python -a | grep internet-connection-logging.py
```
and copy process id (PID). Then type command `kill -9 <pid>`

## Config
To edit app configuration, open file `config.py` in any editor.<br/><br/>
`ICMP_DESTINATION_HOST` - a server that your computer will ping with icmp protocol to check if you still have internet connection. It's preferred to be big company server like Google because this server needs to work all the time.<br/><br/>
`ICMP_TIMEOUT` - a ping response timeout. It's preferred to be as low as possible, because if you have ping like 500 ms that means your internet connection is really bad and we can count it as no internet connection.<br/><br/>
`PINGS_BREAK_ONLINE` - break in seconds between pings when internet connection status is online.<br/><br/>
`PINGS_BREAK_OFFLINE`- break in seconds between pings when internet connection status of offline.<br/><br/>
