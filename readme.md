# Hue Lights Script - Python
### What it is
It's a simple (and primitive) script to control your hue lights around your home. 
The script is as described earlier, "primitive", as I'm still early in my studies around python, but wanted to experiment with current knowledge.

Basic Functions include;
1. Toggling the light selected on/ off. 
2. Changing the colour of a light based on pre-sets configured in the script.
### What's to come
Below are the features I'll be looking to implement in the future;
1. Custom colour presets created by user. 
2. Easier switching of colour's pre-defined.
3. Targeting defined groups of lights, instead of single entities. 
4. Bug smashing and an easier to navigate/ use menu system.

### How to set up:
1. Locate your Hue bridge IP address.
   1. If you know this already, please ignore this step.
   2. If you do now know the IP, you can use Hue's broker server which will give this to you
      1. https://discovery.meethue.com/
2. Using the IP you now have for the bridge, in your browser, head to: https://bridge-IP-address/debug/clip.html replacing the "bridge IP address with your own IP."
3. Create a new user/ key to use with your bridge.
   1. in the URL textbox, set it to /api
   2. In the message body, insert the following, changing the details of the app name and username to whatever you choose.
      1. {"devicetype":"my_hue_app#iphone peter"}
   3. Click the POST button at the top of the menu
      1. You may be required to press the button on the hue bridge to sync.
      2. Once done, you'll be provided with an API key. Copy this.
4. Create a secrets.py file in the same dir as the lights.py file, create the below variables;
   1. key
      1. Input your API key obtained earlier, into this variable.
         1. Example: key = "xx123xxx123xxx"
   2. ip
      1. Input your Hue bridge IP address.
         1. Example: ip = "192.168.1.100"

### Notes:
If the lights.py script doesn't open, or immediately closes, you may be required to pip install "requests" and any other libraries.

