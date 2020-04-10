from tools import toID
import Bot
import config
from collections import deque
bot = Bot.Bot()
class Room:
    
    def __init__(self, initstring):
        initlist = initstring.split('\n')
        self.id = toID(initlist[0])
        self.type = initlist[1].split('|')[2]
        self.title = initlist[2].split('|')[2]
        self.userlist = set(initlist[3].split('|')[2].split(',')[1:])
        #self.log = deque(initlist[5:])
        
    """
    def updatelog(self, message):
        self.log.append(message)
        if(len(self.log)>250):
            self.log.popleft()"""
    def updateul(self, opts):
        opts = opts.split('|')
        if opts[1] == 'J':
            self.userlist.add(opts[2])
        elif opts[1] == 'L':
            for u in self.userlist:
                if opts[2] == toID(u):
                    self.userlist.discard(u)
                    break
        elif opts[1] == 'N':
            for u in self.userlist:
                if opts[3] == toID(u):
                    self.userlist.discard(u)
                    break
            self.userlist.add(opts[2])


    def say(self, text) :
                bot.send(self.id + '|'+ str(text))
                


class Rooms:
    
    def __init__(self):
      self.rooms = {}
      self.room = Room


    def get(self,roomid):
        if(self.rooms.__contains__(roomid)):
         return self.rooms[roomid]

    def add(self,info):
        room = self.get(toID(info.split('\n')[0]))
       
        if(not room):
            room = Room(info)
            self.rooms[toID(info.split('\n')[0])] = room
            print self.rooms


class User:
    def __init__(self,info):
        
        
        self.id = info['userid']
        print self
        self.name = info['name']
        self.avatar = info['avatar']
        self.status = info['status']
        self.group = info['group']
        self.autoconfirmed =  info['autoconfirmed']
        self.rooms = info['rooms']

        
        
    def isDev(self):                                                
            if(self.id in config.devs): return true
            return false

    def say(self,text):
        bot.send('|/pm ' + self.id + ',' + str(text))

        

class Users:
    def __init__(self):
        self.users = {}
        self.user = User

    def add(self,info):
       if(info['userid'] not in self.users):
            user = User(info)
            self.users[user.id] = user
            return user

    def addTemp(self,info):
       if(toID(info) not in self.users):
            user = User(info)
            self.users[user.id] = user
            print user

    def get(self,userid):
        if(userid not in self.users): return None
        return self.users[userid]
    
    
        
Users = Users()
Rooms = Rooms()

        









    
