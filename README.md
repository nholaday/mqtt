To run:
1. create a virtualenv
```
virtualenv -p 3.7 venv
. venv/bin/activate
```

2. install paho-mqtt (python mqtt client package)
```
pip install paho-mqtt
```

3. Run sub_client.py in one tab and pub_client.py in another tab
```
python3 sub_client.py
# (create new tab, activate venv)
python3 pub_client.py
```

Uses a public mqtt broker on the internet. `test.mosquitto.org`

These files can be run on the same machine or any separate machine on the internet


