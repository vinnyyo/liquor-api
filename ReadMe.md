## Liquor API

```
pip install --user -r requirements.txt

python -m uvicorn routes:app
```

then open http://127.0.0.1:8000/docs#/

## Running On Raspberry Pi

Once you get the github repo cloned to your pi, all you need to do is cd into the repo folder, and type "make deps" to install the packages, then update the ip address of the shot.html file to the raspberry pi ip address, then type "make run" to run the api. Then if you open up the ip of the pi with port 8000 in the browser of any computer on your wifi (like http://10.0.0.197:8000/), then you can control the dispenser from the webpage that pops up. You can even turn that url into a qr code and other people can scan it and control it as well (https://webqr.com/create.html). 