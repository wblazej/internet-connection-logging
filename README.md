# Internet connection logging
This project has been created because of annoying Internet connection breaks. This simple Python code will log every connection break, so you will know when your Internet operator is idling and lazy.

## Running on Docker container
```
git clone https://github.com/wblazej/internet-connection-logging
cd internet-connection-logging
sudo docker build -t icl .
sudo docker run -t -d --name icl icl
```

## Config
The config file is called `config.py`

`ICMP_DESTINATION_HOST` - a server that is going to be pinged with icmp protocol to check if you still have internet connection

`ICMP_TIMEOUT` - a ping response timeout

`PINGS_BREAK_ONLINE` - break in seconds between pings when internet connection status is online

`PINGS_BREAK_OFFLINE`- break in seconds between pings when internet connection status of offline
