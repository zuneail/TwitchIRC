
import socket, string
import time, traceback, sched
from time import sleep
from datetime import datetime, timedelta
import random
import os, sys
import time, thread, threading

print ("ran succesfully")
# Variables needed to connect to Twitch IRC
HOST = "irc.twitch.tv"
NICK = ""#bots name
PORT = 6667
PASS = ""#private 
readbuffer = ""
MODT = False
dice = ["1", "2", "3", "4", "5", "6"]

 # Passing credentials to join IRC 
s = socket.socket()
s.connect((HOST, PORT))
s.send("PASS " + PASS + "\r\n")
s.send("NICK " + NICK + "\r\n")
s.send("JOIN #channelname \r\n")

# Sending a message
def Send_message(message):
    s.send("PRIVMSG #channelname :" + message + "\r\n")

Send_message("/me has re-joined ")

def hello_world():
    threading.Timer(120.0, hello_world).start() #called every min to keep session active, sometimes twitch dosent send a PING and expects a PONG
    s.send("PING\r\n")

hello_world()

while True:
    readbuffer = readbuffer + s.recv(1024)
    temp = string.split(readbuffer, "\n")
    readbuffer = temp.pop()
        
   
    for line in temp:
        #Twitch sends PING to check if youre active, if you are it sends PONG or else it closes the session.
        if (line[0] == "PING"):
            s.send("PONG\r" % line[1])
            
            
        else:
         
        
            #Splits the given string 
            parts = string.split(line, ":")
 
            if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
                try:
                    #Sets the message variable to the message  
                    message = parts[2][:len(parts[2]) - 1]
                except:
                    message = ""     
                #Sets the username variable to the username
                usernamesplit = string.split(parts[1], "!")
                username = usernamesplit[0]
                
                #MODT = Message of the day
                if MODT:
                    print username + ": " + message
                   

                    #Commands example

                    if ("!dice") in message:
                            dicec = str(random.choice(dice))
                            Send_message("/me You rolled a " + dicec + " " + username) 

                for l in parts:
                    if "End of /NAMES list" in l:
                        MODT = True

 

                 

                 

                    
                 
