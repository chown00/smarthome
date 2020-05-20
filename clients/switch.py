import socketio
from gpiozero import LED
from config import ipAddress

socket = socketio.Client()

led = LED(17)
led.off()

@socket.on('broadcastLEDState')
def handle_message(broadcastLEDState):
    ''' 
    Handle message containing the next led state from the
    server.
    '''
    if broadcastLEDState == 1:
        led.on()
    elif broadcastLEDState == 0:
        led.off()
    else:
        led.off()

if __name__ == '__main__':
    socket.connect(ipAddress)
    socket.wait()