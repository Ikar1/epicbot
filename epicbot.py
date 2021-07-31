######### RANDOMLY GENERATED FUNNYNESS #########

import random, tweepy   #First install with <pip3 install tweepy>. If it doesn't work, try to install pip3 via package manager and try again.

# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_KEY", "ACCESS_SECRET")

# Create API object
api = tweepy.API(auth)

# Funnyness pool
#Fill the lists with whatever you want idc
names=["imposter","sussy baka","deez nuts","egirl"]
adjectives=["sus","black","baka","poggers","epic","unepic"]
body=["When the @n is @a","When the @n @n is @a","Me petting my @n ( he is very @a )","Somebody once told me the @a @n is gonna roll me"]
#@a and @n is where an adjective or name is supposed to go. pretty intuitive huh

# Funnyness oven
def build():
    raw=body[random.randint(0,len(body)-1)].split()
    treated=[]
    built=""
    for i in range(len(raw)):                   #magik
        if raw[i] == "@n":
            treated.append(pickName())
        elif raw[i] == "@a":
            treated.append(pickAdj())
        else:
            treated.append(raw[i])
    for i in range(len(treated)):
        built+=treated[i]+" "
    return built

def pickName():
    return (names[random.randint(0,len(names)-1)])

def pickAdj():
    return (adjectives[random.randint(0,len(adjectives)-1)])


api.update_status(build())  #Upload the funnyness






















"""

              .,-:;//;:=,
          . :H@@@MM@M#H/.,+%;,
       ,/X+ +M@@M@MM%=,-%HMMM@X/,
     -+@MM; $M@@MH+-,;XMMMM@MMMM@+-
    ;@M@@M- XM@X;. -+XXXXXHHH@M@M#@/.
  ,%MM@@MH ,@%=             .---=-=:=,.
  =@#@@@MX.,                -%HX$$%%%:;
 =-./@M@M$                   .;@MMMM@MM:
 X@/ -$MM/                    . +MM@@@M$
,@M@H: :@:                    . =X#@@@@-
,@@@MMX, .                    /H- ;@M@M=
.H@@@@M@+,                    %MM+..%#$.
 /MMMM@MMH/.                  XM@MH; =;
  /%+%$XHH@$=              , .H@@@@MX,      THANK YOU FOR PARTICIPATING
   .=--------.           -%H.,@@@@@MX,      IN THIS ENRICHMENT ACTIVITY!
   .%MM@@@HHHXX$$$%+- .:$MMX =M@@MM%.
     =XMMM@MM@MM#H;,-+HMM@M+ /MMMX=
       =%@M@M#@$-.=$@MM@@@M; %M%=
         ,:+$+-,/H#MMMMMMM@= =,
               =++%%%%+/:-.
"""
