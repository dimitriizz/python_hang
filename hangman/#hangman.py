#hangman
import random

#lista sanoja joita käytetään pelissä :) listaan voi myös lisätä tai poistaa sanoja
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
#laitetaan myös sana muuttujaan jotta sitä voidaan käyttää itse pelissä
def sana_rand():
    sana = random.choice(sanat)
    return sana.upper()


#funktio pelille 
def peli(sana):
   #alla olevalla pätkällä tehdään terminaaliin alaviivoilla sanan pituinen kohta johon arvatut kirjaimet ilmestyvät
    word_completion = "_" * len(sana)

    #boolean arvo arvauksille
    guessed = False

    #pari listaa johon tallenetaan pelin aikana arvatut kirjaimet ja sanat
    guessed_letters = []
    guessed_words = []

    #muuttuja yrityksille
    tries = 6
    #tulostetaan tekstiä sekä hirsipuu 
    print("Pelataan hirsipuuta !")
    print(hirsipuu(tries))
    print(word_completion)
    print("\n")

    #tämä while looppi pyörii jos arvauksia on jäljellä
    #tarkistaa myös arvauksen pituuden ja sen että onko se kirjain
    #myös jos yritys kirjainta on jo koitettu niin tämä ilmoittaa sen käyttäjälle
    while not guessed and tries > 0:
        guess = input("Syötä sana tai kirjain: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Olet jo yrittänyt tätä kirjainta", guess)
            
            #jos arvaus ei ole sanassa otetaan yksi arvaus pois
            elif guess not in sana:
                print(guess, "Ei ole sanassa")
                tries -= 1
                guessed_letters.append(guess)

            #tämä pätkä ilmoittaa käyttäjälle onko arvaama kirjain sanassa evai ei
            #sekä tunkee arvauksen listaan
            else:
                print(guess, "on sanassa !")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(sana) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True

         #tää pätkä chekkaa onks arvaus sana ja ilmoittaa onko sanaa koitettu
        elif len(guess) == len(sana) and guess.isalpha():
            if guess in guessed_words:
                print("Olet jo arvannut sanan", guess)

            #tää ilmoittaa jos joku kirjain ei ole sanassa ja miinustaa yrityksen
            elif guess != sana:
                print(guess, "ei ole sanassa")
                tries -= 1
                guessed_words.append(guess)

            #muuten arvaus muuttuu boolean arvoltaan trueksi ja oikea sana tallenetaan muuttujaan
            else:
                guessed = True
                word_completion = sana

         #jos tulee esim numero tai jotain epämääräistä niin tämä pyörii
        else:
            print("Ei sovi arvaukseksi")
        print(hirsipuu(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Voitit !")

    else:
        print("Yritykset loppuiovat, oike sana oli:  " + sana )


#hirsipuun eri vaiheet funktiossa ja listassa. Eri vaiheet voidaan tulostaa indexin avulla
def hirsipuu(yritykset):
    kohdat = [  
                # pää, rinta, molemmat kädet ja jalat
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


#tällä fubktiolla aloitetaan peli sekä kysytään lopussa että haluaako käyttäjä pelata uudelleen
def main():
    sana = sana_rand()
    peli(sana)
    while input("pelaa uudestaan ? (Y/N) ").upper() == "Y":
        sana = sana_rand()
        peli(sana)


#tällä käynnistetään main funktio
if __name__ == "__main__":
    main()
