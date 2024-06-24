# set the wifi network, and maybe a password if needed
ssid = 'dd-wrt'
# password = ''

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip
    
def open_socket(ip):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def webpage():
    #Template HTML
    with open('controls.html', 'r') as f:
        html = f.read()
    return str(html)

def serve(connection):
    #Start web server
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        if request == '/forward?':
            forward()
        elif request =='/left?':
            left()
        elif request =='/stop?':
            stop()
        elif request =='/right?':
            right()
        elif request =='/reverse?':
            reverse()
        elif request =='/race?':
            race()
        html = webpage()
        client.send(html)
        client.close()

# connect to the wifi, open a socket, serve the webpage
try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()