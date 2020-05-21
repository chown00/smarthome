import socketio
from gpiozero import LED
import json

from config import ipAddress

socket = socketio.Client()

led1 = LED(17)
led2 = LED(27)
led3 = LED(22)
led1.off()
led2.off()
led3.off()

@socket.on('broadcastLEDState')
def handle_message(broadcastLEDState):
    ''' 
    Handle message containing the next led state from the
    server.
    '''
    next_state = json.loads(broadcastLEDState)

    if next_state['state'] == 1:
        eval("led" + str(next_state['ledNumber'])).on()
    elif next_state['state'] == 0:
        eval("led" + str(next_state['ledNumber'])).off()
    else:
        eval("led" + str(next_state['ledNumber'])).off()

if __name__ == '__main__':
    socket.connect(ipAddress)
    socket.wait()