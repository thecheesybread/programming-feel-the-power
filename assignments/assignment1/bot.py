#!/usr/bin/python
# -*- coding: koi8-r -*-
# $Id: bot.py,v 1.2 2006/10/06 12:30:42 normanr Exp $
import sys
import xmpp
from chat_bot import respond, gmail_username, gmail_password
commands={}
i18n={'ru':{},'en':{}}
########################### user handlers start ##################################
i18n['en']['HELP']="This is example jabber bot.\nAvailable commands: %s"
def helpHandler(user,command,args,mess):
    lst=commands.keys()
    lst.sort()
    return "HELP",', '.join(lst)

i18n['en']['EMPTY']="%s"
i18n['en']['HOOK1']='Responce 1: %s'
def hook1Handler(user,command,args,mess):
    return "HOOK1",'You requested: %s'%args

i18n['en']['HOOK2']='Responce 2: %s'
def hook2Handler(user,command,args,mess):
    return "HOOK2","hook2 called with %s"%(`(user,command,args,mess)`)

i18n['en']['HOOK3']='Responce 3: static string'
def hook3Handler(user,command,args,mess):
    return "HOOK3"*int(args)
########################### user handlers stop ###################################
############################ bot logic start #####################################
i18n['en']["UNKNOWN COMMAND"]='Unknown command "%s". Try "help"'
i18n['en']["UNKNOWN USER"]="I do not know you. Register first."


def messageCB(conn,mess):
    text=mess.getBody()
    conn.send(xmpp.Message(mess.getFrom(),respond(text)))


for i in globals().keys():
    if i[-7:]=='Handler' and i[:-7].lower()==i[:-7]: commands[i[:-7]]=globals()[i]

############################# bot logic stop #####################################

def StepOn(conn):
    try:
        conn.Process(1)
    except KeyboardInterrupt: return 0
    return 1

def GoOn(conn):
    while StepOn(conn): pass

if True:
    jid=xmpp.JID(gmail_username)
    user,server,password=jid.getNode(),jid.getDomain(),gmail_password

    conn=xmpp.Client(server)#,debug=[])
    conres=conn.connect()
    if not conres:
        print "Unable to connect to server %s!"%server
        sys.exit(1)
    if conres<>'tls':
        print "Warning: unable to estabilish secure connection - TLS failed!"
    authres=conn.auth(user,password)
    if not authres:
        print "Unable to authorize on %s - check login/password."%server
        sys.exit(1)
    if authres<>'sasl':
        print "Warning: unable to perform SASL auth os %s. Old authentication method used!"%server
    conn.RegisterHandler('message',messageCB)
    conn.sendInitPresence()
    print "Bot started."
    GoOn(conn)
