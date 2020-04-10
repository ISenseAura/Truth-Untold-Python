from tools import toID
from structures import Rooms
import time, os
import commands

def js(bot, room, text, user, pm):
    room.say(eval(text))

def dc(bot, room, text, user, pm):
    bot.dc()

def c(bot, room, text, user, pm):
   
    if text[0] == '[' and ']' in text:
            e = text.index(']')
            room = Rooms.get(text[1:e])
            text = text[e+1:].strip()
        
    room.say(text)

def restart(bot, room, text, user, pm):
    room.say('Restarting...')
    bot.dc()
    os.system('python main.py')

def contime(bot, room, text, user, pm):
    pmtext = ''
    if pm:
        pmtext = '/pm '+user+','
    daytext = ''; hourtext = ''; minutetext = ''; secondtext = ''
    td = time.time() - bot.contime
    days = int(td/(24*60*60));  td-=days*24*60*60
    hours = int(td/(60*60)); td-=hours*60*60
    minutes = int(td/(60)); td-=minutes*60
    seconds = round(td, 2)
    if days!=0:
        daytext = str(days)+' days'
    if hours!=0:
        hourtext = str(hours)+' hours'
    if minutes!=0:
        minutetext = str(minutes)+' minutes'
    if seconds != 0:
        secondtext = str(seconds)+' seconds'
        room.say('The bot has been connected for: '+(daytext+' '+hourtext+' '+minutetext+' '+secondtext).strip()+'.')
    #bot.send(room, pmtext+'The bot has been connected for: '+(daytext+' '+hourtext+' '+minutetext+' '+secondtext).strip()+'.')

def repo(bot, room, text, user, pm):
    room.say("https://gitlab.com/XpRienzo/Pokemon-Showdown-Python-Bot")

def hotpatch(bot, room, text, user, pm):
    
    #to be extended to include config, current implementation just a dummy.
    bot.commands = reload(commands)
    room.say('The commands have been hotpatched!')

fdict = {'dc':dc, 'custom':c,'js':js, 'c':c, 'contime':contime, 'uptime':contime, 'kill':dc, 'restart':restart, 'hotpatch':hotpatch, 'reload':hotpatch, 'git':repo, 'repo':repo}

devcoms = ['dc', 'custom', 'c', 'kill', 'restart', 'reload','js']

infocoms = [ 'contime', 'git', 'repo']

ranks = {'uptime':' ', 'contime':'+', 'git':'+', 'repo':'+', 'hotpatch':' '}

def com(bot, room, text, user, command, pm=False):
    if toID(user.id) == toID(bot.usr['nickname']):
        return
    if command in devcoms and toID(user.id) in bot.devs:
        fdict[command](bot, room, text, user, pm)
        return
    if command in infocoms:
        prio = bot.ranks.index(ranks[command])
        if prio > bot.ranks.index(user[0]):
            fdict[command](bot, room, text, user, True)
        else:
            fdict[command](bot, room, text, user, pm)
