print("Hallo! Dieses Programm weiß, welcher Job am besten zu Ihnen passt.")

# Fragen
fragen = [
    "Welche Schulabschlüsse braucht man?",
    "Wie lange dauert die Ausbildung?",
    "Wie viel verdient man?"
]

# Antworten
antworten = [
    ["1. Man braucht Realschulabschluss", "2. Man braucht dualen Abschluss", "3. Man braucht Ausbildung"],
    ["1. Es dauert 4,5 Jahre", "2. Es dauert 4 Jahre", "3. Es dauert 3,5 Jahre"],
    ["1. Man verdient 6000 pro Monat", "2. Man verdient 4000 pro Monat", "3. Man verdient 3000 pro Monat"]
]

# Beruf
#jobs = ["Architekt", "Informatiker", "Webdesigner"]

# Antworten for Job
expected_answers = [
    [3, 1, 1],  # Architekt
    [2, 2, 2],  # Informatiker
    [1, 3, 3]   # Webdesigner
]

user_antworten = []

for i in range(len(fragen)):
    print(fragen[i])
    for j in range(len(antworten[i])):
        print(antworten[i][j])

    user_ant = int(input("Wählen Sie eine Antwort, drücken Sie eine Nummer: "))
    user_antworten.append(user_ant)

if user_antworten == expected_answers[0]:
   # print (jobs[0])
   print ('Architekt')
elif user_antworten == expected_answers[1]:
   # print (jobs[1])
   print ('Informatiker')
elif user_antworten == expected_answers[2]:
   # print (jobs[2])
   print ('Webdesigner')
else:
    print ("Kein passender Job gefunden")