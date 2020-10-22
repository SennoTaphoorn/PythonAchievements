import time


a = True
while a == True:
    hello = "Hello You! \nik ben {owner}. hoe heet jij?"
    print(hello.format(owner = "Senno"))

    time.sleep (1)

    username = input("Mijn naam is:")
    print("Hallo " + username, "hier is je datum ")

    time.sleep (1)

    import datetime

    x = datetime.datetime.now()

    print("vandaag is het " + x.strftime("%d ") + x.strftime ("%B"))
    while True:
     time.sleep( 2 )

     antwoord1 = input("In de ochtend eet je \n A Cornflakes \n B Boterham \n C Tosti \n antwoord: ")
     if ( antwoord1 == "a"):
        print("Same")
    elif ( antwoord1 == "b"):
        print("Lekker hoor")
    elif ( antwoord1 == "c"):
        print("Ik soms ook")
     time.sleep( 2 )

     antwoord2 = input("Hoe ga je naar school? \n A Fiets \n B Trein  \n C Bus \n antwoord: ")
     if ( antwoord1 == "a"):
        print("Woon je dichtbij ofzo?")
    elif ( antwoord1 == "b"):
        print("Same")
    elif ( antwoord1 == "c"):
        print("Ik kan geen bus meer zien na de afgelopen 5 jaar")
     time.sleep( 2 )

     antwoord3 = input("Hoelaat kom je op school? \n Veel te vroeg \n net op tijd \n C Te laat \n antwoord:")
     if ( antwoord3 == "a"):
         print("Braaf")
     elif ( antwoord3 == "b"):
        print("Same")
    elif ( antwoord3 == "c"):
        print("Ietsje eerder weg gaan he")
     time.sleep( 2 )

     antwoord4 = input("Hoelaat sta je op voor de online les? \n A 1+ uur ervoor \n B Precies op tijd  \n C 1+ uur te laat \n antwoord: ")
     if ( antwoord1 == "a"):
        print("Braaf?")
    elif ( antwoord1 == "b"):
        print("Goed genoeg")
    elif ( antwoord1 == "c"):
        print("Stout")
     time.sleep( 2 )
