
import Bot
import tools
from structures import Rooms
from structures import Users

import json



bot = Bot.Bot()

rdict = {}

i = 1
while bot.ws.connected:
    i+=1
    resp = bot.recv()
    room = ''
    r_l = resp.split('\n')
    if len(r_l)!= 1:
        room = r_l[0][1:]
        opts = r_l[1].split('|')
        
    else:
        opts = r_l[-1].split('|')
        
    if len(opts) == 1:
        continue
    elif opts[1]=='updateuser':
        continue
    elif opts[1]=='init':
        Rooms.add(resp)
    elif opts[1]=='J':
        bot.send('|/pm glycosshadow,/cmd userdetails ' + opts[2])
        
    elif opts[1]=='L':
        bot.send('|/pm glycosshadow,/cmd userdetails ' + opts[2])
       
        Rooms.get(room).updateul(r_l[1])
    elif opts[1]=='N':
        bot.send('|/pm glycosshadow,/cmd userdetails ' + opts[2])
        Rooms.get(room).updateul(r_l[1])
    elif opts[1]=='c:':
        bot.send('|/pm glycosshadow,/cmd userdetails ' + opts[3])
        if opts[4][0] in bot.comchar:
            com = opts[4][1:].split(' ')[0]
            arg = ' '.join(opts[4][1:].split(' ')[1:])
            user = Users.get(tools.toID(opts[3]))
            if(user is None):
                data = {'userid':tools.toID(opts[3]),'name': opts[3],"status":"null","avatar":"null","rooms":"null","autoconfirmed":"null","group":"none"}
                user = Users.add(data)
            
            room = Rooms.get(tools.toID(room))
            bot.commands.com(bot, room, arg, user, com)

    elif opts[1]=='queryresponse':

        print opts[3]
        Users.add(json.loads(opts[3]))

    elif opts[1]=='users':
        print opts
       # if (splitMessage[0] === '0') return;
	#let users = splitMessage[0].split(",");
	#for x in range(len(users)):
        #    print opts
		       
    elif opts[1]=='pm':
        bot.send('|/pm glycosshadow,/cmd userdetails ' + opts[2])         
        if opts[4][0] in bot.comchar:
            com = opts[4][1:].split(' ')[0]
            arg = ' '.join(opts[4][1:].split(' ')[1:])
            room = Users.get(tools.toID(opts[2]))
            user = Users.get(tools.toID(opts[2]))
            
            if(user is None):
                data = {'userid':tools.toID(opts[3]),'name': opts[3],"status":"null","avatar":"null","rooms":"null","autoconfirmed":"null","group":"none"}
                user = Users.add(data)
            
            if(room is None):
                room = user
            bot.commands.com(bot, room , arg, user, com, True)
