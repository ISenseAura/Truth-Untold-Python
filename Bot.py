import websocket
import requests
import json
import config
import sys
import time
import commands

class Bot:
    def __init__(self):
        self.usr = config.userdetails
        self.ranks = config.ranks
        self.comchar = config.comchar
        self.devs = config.devs
        self.commands = commands
        self.ws = websocket.create_connection('wss://'+config.server+'/showdown/websocket')
        self.contime = time.time()
        msg = self.ws.recv()
        msg = msg.split('\n')[1]
        self.formats = []
        for m in msg.split('|'):
            if m[1:4] == 'Gen':
                self.formats.append(m.split(',')[0])
        msg = self.ws.recv()
        r = requests.post('https://play.pokemonshowdown.com/action.php',data = {'act':'login','name':self.usr['nickname'],'pass':self.usr['password'],'challstr':msg[10:]})
        self.ws.send('|/trn '+self.usr['nickname']+',0,'+json.loads(r.__dict__['_content'][1:])['assertion'])
        self.ws.send('|/avatar '+self.usr['avatar'])
        for room in config.rooms:
            self.ws.send('|/j '+room)
    
    def recv(self):
        return self.ws.recv()
    
    def send(self,text):
        self.ws.send(text)
        
    def dc(self):
        self.ws.close()
