# robotech-rally

Welcome to the RobotechRally GitHub repository. If you're here you may have participated in our Take Your Child to Work Day activity where we programmed little vehicles to drive around a small course. Thanks for checking us out!

In this repository you'll find the working code that we used to program the vehicles, and in the README.md file we'll provide links to the various parts and how you could achieve this at home.

## Parts Needed
- [2WD Smart Robot Car Chasis Kit](https://a.co/d/00dGG6WV)
- [Raspberry Pi Pico W](https://www.raspberrypi.com/products/raspberry-pi-pico/)
- [Kitronic Motor Driver Board](https://kitronik.co.uk/products/5331-kitronik-compact-motor-driver-board-for-raspberry-pi-pico) (this board can be ordered from domestic resellers as well, just do some searched on the web)
- [Soldering Equipment](https://www.tomshardware.com/best-picks/best-soldering-irons)
- AA batteries

## Online Tutorials / Reference
Much of this activity was inspired and assembled from other activities found on the internet. There are a ton of possibilities, as well as other activities out there on the web, so feel free to explore and modify as you like. The following links are just some of the ones we used:
- https://www.tomshardware.com/how-to/raspberry-pi-pico-robot
- https://microcontrollerslab.com/getting-started-raspberry-pi-pico-thonny-ide/
https://electrocredible.com/raspberry-pi-pico-tutorial-for-beginners/


# Software & Programming

To program your microcontroller (Raspberry Pi Pico) you'll want to download the [Thonny App](https://thonny.org/) to your computer. [Thonny](https://thonny.org/) is a "Python IDE for beginners" which will allow you to edit the Python code used for this activity and upload directly to your device.

## General steps
1. Assemble your car kit (refer to the online tutorials / reference for more details)
    - soldering should be minimal, only need to connect the on/off switch wires and the wires connecting the motors. Everything else should be scew terminals on the motor controller board
    - you may have to get creative if you want to mount your Raspberry Pi and motor controller to the chassis, we used motherboard standoff screwsm but you could also just run a zip tie around them to lightly secure them
1. Download the contents of this repository
1. Open Thonny
1. In the bottom right of the Thonny window select "Configure Interpreter", choose "MicroPython (Raspberry Pi Pico)"
1. Open the "Files" pane from the "View" menu and find the repository code you just downloaded
1. Modify the code in the "conncetWifi.py" file to use your wifi netwrok name, and uncomment the password line, adding your wifi password in the quotes
1. Plug the USB cord into your computer and the Pico
1. In Thonny, hit the red "Stop" button in the top bar (this should attempt to connect Thonny to your Pico) - if you see an extra (empty) "Files" pane in the left column then you've succeeded
1. Select the files you want to load to the Pico board in the Thonny Files pane, right-click them and select "Upload to /"
1. Once the files are uplaoded to the board you can unploug the USB, 
1. Power on the car
1. Access your wireless router to try to find the IP address of your newly programmed car
1. Type the IP address of the car into your browser window - hope it works!
1. Now that you have it working, you can control the care from the browser, or click "Start Race" to run the preprogrammed sciprt that lives in "RACE.py"

IMPORTANT NOTE: You NEVER want to have the battery pack power turned on for the car while the USB is connected to your computer. This could damage the Rasperry Pico, or worse yet it could damage your computer. 

## Updating the code on your Pico
Updating the code on the Pico can sometimes require you to reset the Pico then upload code fresh again. In some cases you can upload new code directly over the old code, but this wasn't working for us, so we reset each time.

We used the "nuke file" option to reset our pi's to stock firmaware. It's apparently impossible to brick these devices, so don't stress about messing anything up, it'll be fine. Once you have the two files you need and you've done this once or twice you'll see its easy.

Check out these instructions to reset your device: https://electrocredible.com/how-to-reset-raspberry-pi-pico-w/#Method_3_Factory_Reset_Raspberry_Pi_Pico_Pico_W

After you wipe the Pico using the nuke file from the article above you'll need the new firmware to flash back on it: https://micropython.org/download/RPI_PICO_W/

