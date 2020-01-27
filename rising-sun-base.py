'''
Created on 31 Oct 2019

@author: Tamalk
'''
import subprocess
from textwrap import wrap
import os
os.system("title THE RISING SUN PROJECT")
def ns(cat):
    while cat!=("Y") and cat!=("N") and cat!= ("y") and cat!=("n"):
        print(chr(7)); cat=input("Please type only [Y] or [N], according to your choice: ")
    return (cat)
def cho(dog):
    while dog!=("E") and dog!=("D") and dog!=("e") and dog!=("d"):
        print(chr(7)); dog=input("Please type only [E] or [D], according to your choice: ")
    return(dog)

dic_ris={'A':'F3','B':'E3','C':'G3','D':'D3','E':'H3','F':'C3','G':'I3','H':'B3','I':'JA','J':'A3','K':'A+','L':'C+','M':'E+','N':'G+','O':'I+','P':'J+','Q':'H+','R':'F+','S':'D+','T':'B+','U':'GA','V':'FA','W':'IA','X':'HA','Y':'EA','Z':'DA','.':'BA',',':'AA',':':'CA',' ':'J3','0':'EK','1':'FK','2':'AK','3':'GK','4':'BK','5':'HK','6':'CK','7':'IK','8':'DK','9':'JK','!':'F2','?':'G2','¿':'E2','¡':'D2','a':'F3','b':'E3','c':'G3','d':'D3','e':'H3','f':'C3','g':'I3','h':'B3','i':'JA','j':'A3','k':'A+','l':'C+','m':'E+','n':'G+','o':'I+','p':'J+','q':'H+','r':'F+','s':'D+','t':'B+','u':'GA','v':'FA','w':'IA','x':'HA','y':'EA','z':'DA'}
dic_trad={'F3':'A','E3':'B','G3':'C','D3':'D','H3':'E','C3':'F','I3':'G','B3':'H','JA':'I','A3':'J','A+':'K','C+':'L','E+':'M','G+':'N','I+':'O','J+':'P','H+':'Q','F+':'R','D+':'S','B+':'T','GA':'U','FA':'V','IA':'W','HA':'X','EA':'Y','DA':'Z','BA':'.','AA':',','CA':':','J3':' ','EK':'0','FK':'1','AK':'2','CK':'3','BK':'4','HK':'5','CK':'6','IK':'7','DK':'8','JK':'9','F2':'!','G2':'?','E2':'¿','D2':'¡'}

while True:
    print("-- Rising Sun --")
    print("Please choose one option: [E] - Encode. [D] - Decode.")
    chok = cho(input("> "))
    if chok == "E" or chok == "e":
        usinput = input("Please enter some text to encode: ")
        risen = []
        for i in usinput:
            if i in dic_ris:
                risen.append(dic_ris[i])
            else:
                print("There is no translation for character ",i," so it has been ignored.")
    
        risen_complete = ("").join(risen)
        print("")
        print("Final translation: ", risen_complete)
        print("")
        print("")
                
        
    elif chok == "D" or chok == "d":
        usinput2 = input("Please enter some text to decode: ")
        realinput  = wrap(usinput2, 2)
        trans = []
        for i in realinput:
            if i in dic_trad:
                trans.append(dic_trad[i])
            else:
                print("There is no translation for character ",i," so it has been ignored.")
    
        trans_complete = ("").join(trans)
        print("")
        print("Final translation: ", trans_complete)
        print("")
        print("")
                
        
    anoda = ns(input("Restart?"))
    if anoda == "N" or anoda == "n":
        break
    subprocess.call(["cmd.exe", "/C", "cls"])
