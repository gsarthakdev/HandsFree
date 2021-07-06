import bluetooth, subprocess

#Look for all Bluetooth devices
#the computer knows about.
print("Searching for devices...")
print("\n")
#Create an array with all the MAC
#addresses of the detected devices
nearby_devices = bluetooth.discover_devices()
#Run through all the devices found and list their name
num = 0
print("Select your device by entering its coresponding number...")
for i in nearby_devices:
	num+=1
	print(num, ": ", bluetooth.lookup_name(i))

#Allow the user to select their Arduino
#bluetooth module. They must have paired
#it before hand.
selection = int(input("> ")) - 1
print("You have selected", bluetooth.lookup_name(nearby_devices[selection]))
bd_addr = nearby_devices[selection]

port = 1

passkey = "1111" # passkey of the device you want to connect

# kill any "bluetooth-agent" process that is already running
subprocess.call("kill -9 `pidof bluetooth-agent`",shell=True)

# Start a new "bluetooth-agent" process where XXXX is the passkey
status = subprocess.call("bluetooth-agent " + passkey + " &",shell=True)

# Now, connect in the same way as always with PyBlueZ
try:
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.connect((bd_addr,port))
except bluetooth.btcommon.BluetoothError as err:
    # Error handler
    pass

s.recv(1024) # Buffer size
s.send("Hello World!")