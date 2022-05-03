#hangman

#imports

import random


sanat = [
'omena',
'lohi',
'kana',
'soija',
'tofu',
'kahvi',
'päärynä',
'banaani',
'riisi',
'peruna',
'sorsa',
'vittu',
'saatana',
'helvetti'
]


#funktiolla otetaan listasta random sana ja muutetaan kirjaimet isoiksi
def sana_rand():
    sana = random.choice(sanat)
    return sana.upper()



#funktio pelille
def peli(sana):
    arvattu_sana = "_" * len(sana)
    arvattu = False
    yritykset = 6
    print("Pelataan hirsipuuta !")
    print(hirsipuu(yritykset))
    print(arvattu_sana)
    print("\n")



    #pari listaa eka pitaa sisällään sanat jotka käyttäjä on yrittanyt arvata ja toinen pitää sanat
    arvatut_sanat = []
    arvatut_kirjaimet = []



#hirsipuun eri vaiheet :D 
def hirsipuu(yritykset):
    kohdat = [  
                # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   -
                """,
                # pää, rinta, molemmat kädet ja yks jalka
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
                # pää, rinta ja molemmat kädet
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
                # pää rinta ja yks käsi
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
                # pää ja rinta
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # pää
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # alotus kohta köysi
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return kohdat[yritykset]
