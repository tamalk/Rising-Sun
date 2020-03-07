'''
Created on 31 Oct 2019
Layer 2 addition: 16 Feb 2020
@author: Tamalk
'''
import subprocess
from textwrap import wrap
from datetime import datetime as date
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
def control(d): #enigmar la segunda capa. Obtiene el día que es y lo convierte en una codificación.
    dayswitch = {
        0: "A",
        1: "B",
        2: "C",
        3: "D",
        4: "E",
        5: "F",
        6: "G"
    }
    return (dayswitch.get(d, "ERROR"))

dic_ris={'Á':'A2','É':'B2','Í':'C2','Ó':'H2','Ú':'I2','Ü':'J2','A':'F3','B':'E3','C':'G3','D':'D3','E':'H3','F':'C3','G':'I3','H':'B3','I':'JA','J':'A3','K':'A+','L':'C+','M':'E+','N':'G+','O':'I+','P':'J+','Q':'H+','R':'F+','S':'D+','T':'B+','U':'GA','V':'FA','W':'IA','X':'HA','Y':'EA','Z':'DA','.':'BA',',':'AA',':':'CA',' ':'J3','0':'EK','1':'FK','2':'AK','3':'GK','4':'BK','5':'HK','6':'CK','7':'IK','8':'DK','9':'JK','!':'F2','?':'G2','¿':'E2','¡':'D2','á':'A2','é':'B2','í':'C2','ó':'H2','ú':'I2','ü':'J2','a':'F3','b':'E3','c':'G3','d':'D3','e':'H3','f':'C3','g':'I3','h':'B3','i':'JA','j':'A3','k':'A+','l':'C+','m':'E+','n':'G+','o':'I+','p':'J+','q':'H+','r':'F+','s':'D+','t':'B+','u':'GA','v':'FA','w':'IA','x':'HA','y':'EA','z':'DA'}
dic_trad={'J2':'Ü','I2':'Ú','H2':'Ó','C2':'Í','B2':'É','A2':'Á','F3':'A','E3':'B','G3':'C','D3':'D','H3':'E','C3':'F','I3':'G','B3':'H','JA':'I','A3':'J','A+':'K','C+':'L','E+':'M','G+':'N','I+':'O','J+':'P','H+':'Q','F+':'R','D+':'S','B+':'T','GA':'U','FA':'V','IA':'W','HA':'X','EA':'Y','DA':'Z','BA':'.','AA':',','CA':':','J3':' ','EK':'0','FK':'1','AK':'2','GK':'3','BK':'4','HK':'5','CK':'6','IK':'7','DK':'8','JK':'9','F2':'!','G2':'?','E2':'¿','D2':'¡'}
heute = date.today()
day = date.weekday(heute)
while True:
    print("-- Rising Sun --")
    print("Please choose one option: [E] - Encode. [D] - Decode.")
    chok = cho(input("> "))
    if chok == "E" or chok == "e":
        levels = int(input("Please enter the encryption layers [1, 2]: "))
        if (levels == 1):
            legtels = "D"
        elif (levels == 2):
            legtels = "R"
        usinput = input("Please enter some text to encode: ")
        risen = []
        for i in usinput:
            if i in dic_ris:
                risen.append(dic_ris[i])
            else:
                print("There is no translation for character " + i + " so it has been ignored.")
    
        risen_complete = ("").join(risen)
        if (levels  == 1):
            print("")
            print("Final translation: " + str(legtels) + risen_complete)
            print("")
            print("")
        elif (levels > 1):
            dawnen = []
            cform = control(day)
            if (cform == "A"):
                    dic_daw = {'A':'+', 'B':'I', 'C':'J', 'D':'A', 'E':'G', 'F':'H', 'G':'E', 'H':'F', 'I':'C', 'J':'D', 'K':'2', '+':'B', '2':'3', '3':'K'}#control1
            elif (cform == "B"):
                    dic_daw = {'A':'E', 'B':'A', 'C':'K', 'D':'+', 'E':'2', 'F':'F', 'G':'B', 'H':'C', 'I':'3', 'J':'G', 'K':'D', '+':'I', '2':'H', '3':'J'} #control2
            elif (cform == "C"):
                    dic_daw = {'A':'J', 'B':'L', 'C':'C', 'D':'3', 'E':'+', 'F':'A', 'G':'D', 'H':'G', 'I':'U', 'J':'I', 'K':'F', '+':'K', '2':'2', '3':'E'}#control3
            elif (cform == "D"):
                    dic_daw = {'A':'U', 'B':'A', 'C':'2', 'D':'K', 'E':'F', 'F':'E', 'G':'L', 'H':'-', 'I':'B', 'J':'D', 'K':'C', '+':'4', '2':'G', '3':'H'}#control4
            elif (cform == "E"):
                    dic_daw = {'A':'+', 'B':'J', 'C':'I', 'D':'4', 'E':'U', 'F':'C', 'G':'F', 'H':'K', 'I':'-', 'J':'Z', 'K':'3', '+':'G', '2':'H', '3':'2'}#control5
            elif (cform == "F"):
                    dic_daw = {'A':'Z', 'B':'E', 'C':'D', 'D':'+', 'E':'2', 'F':'K', 'G':'G', 'H':'A', 'I':'L', 'J':'U', 'K':'B', '+':'-', '2':'3', '3':'C'}#control6
            elif (cform == "G"):
                    dic_daw = {'A':'A', 'B':'K', 'C':'4', 'D':'F', 'E':'G', 'F':'D', 'G':'E', 'H':'U', 'I':'Z', 'J':'-', 'K':'+', '+':'B', '2':'I', '3':'H'}#control7
            for i in risen_complete:
                if (i in dic_daw):
                    dawnen.append(dic_daw[i])
                else:
                    print("There is no translation for character " + i + " so it has been ignored.") #case default, error
            dawnen_complete_reverse = ("").join(dawnen)
            dawnen_complete = dawnen_complete_reverse[: : -1]
            if (levels == 2):
                print("")
                print("Final translation: " + str(legtels) + str(cform) + dawnen_complete)
                print("")
                print("")

    elif chok == "D" or chok == "d":
        usermessage = input("Please enter some text to decode: ")
        messlist = list(usermessage)
        head = messlist[0]
        if (head == "D"):
            leveli = 1
        elif (head == "R"):
            leveli = 2
        if (leveli > 1):
            local = 2
            header = messlist[1]
            dawnentrans = []
            if (header == "A"):
                trans_dawn = {'K':'3' ,'3':'2' ,'B':'+' ,'2':'K' ,'D':'J' ,'C':'I' ,'F':'H' ,'E':'G' ,'H':'F' ,'G':'E' ,'A':'D' ,'J':'C' ,'I':'B' ,'+':'A'}
            elif (header == "B"):
                trans_dawn = {'J':'3' ,'H':'2' ,'I':'+' ,'D':'K' ,'G':'J' ,'3':'I' ,'C':'H' ,'B':'G' ,'F':'F' ,'2':'E' ,'+':'D' ,'K':'C' ,'A':'B' ,'E':'A'}
            elif (header == "C"):
                trans_dawn = {'E':'3' ,'2':'2' ,'K':'+' ,'F':'K' ,'I':'J' ,'U':'I' ,'G':'H' ,'D':'G' ,'A':'F' ,'+':'E' ,'3':'D' ,'C':'C' ,'L':'B' ,'J':'A'}
            elif (header == "D"):
                trans_dawn = {'H':'3' ,'G':'2' ,'4':'+' ,'C':'K' ,'D':'J' ,'B':'I' ,'-':'H' ,'L':'G' ,'E':'F' ,'F':'E' ,'K':'D' ,'2':'C' ,'A':'B' ,'U':'A'}
            elif (header == "E"):
                trans_dawn = {'2':'3' ,'H':'2' ,'G':'+' ,'3':'K' ,'Z':'J' ,'-':'I' ,'K':'H' ,'F':'G' ,'C':'F' ,'U':'E' ,'4':'D' ,'I':'C' ,'J':'B' ,'+':'A'}
            elif (header == "F"):
                trans_dawn = {'C':'3' ,'3':'2' ,'-':'+' ,'B':'K' ,'U':'J' ,'L':'I' ,'A':'H' ,'G':'G' ,'K':'F' ,'2':'E' ,'+':'D' ,'D':'C' ,'E':'B' ,'Z':'A'}
            elif (header == "G"):
                trans_dawn = {'H':'3' ,'I':'2' ,'B':'+' ,'+':'K' ,'-':'J' ,'Z':'I' ,'U':'H' ,'E':'G' ,'D':'F' ,'G':'E' ,'F':'D' ,'4':'C' ,'K':'B' ,'A':'A'}
            while (local < len(messlist)):
                char = messlist[local]
                if char in trans_dawn:
                    dawnentrans.append(trans_dawn[char])
                else:
                    print("There is no translation for character " + i + " so it has been ignored.")
                local += 1
            dawtrans_complete_reverse = ("").join(dawnentrans)
            dawtrans_complete = dawtrans_complete_reverse[: : -1]
        if (leveli == 1):
            messlist.pop(0) #obtiene la primera D, que no va a retraducirse.
            noheadermessage = ("").join(messlist) #reconvierte la lista sin el elemento 0 (la cabecera) a cadena de texto.
            usinput2 = noheadermessage
        elif (leveli == 2):
            usinput2 = dawtrans_complete
        realinput = wrap(usinput2, 2)
        trans = []
        for i in realinput:
            if i in dic_trad:
                trans.append(dic_trad[i])
            else:
                print("There is no translation for character " + i + " so it has been ignored.")
    
        trans_complete = ("").join(trans)
        print("")
        print("Final translation: ", trans_complete)
        print("")
        print("")
    
    anoda = ns(input("Restart?"))
    if anoda == "N" or anoda == "n":
        break
    subprocess.call(["cmd.exe", "/C", "cls"])
    
    
