import random
import time

questions = [
    {"Fråga": "Vad heter Sveriges näst största stad?", "Svar": "Göteborg"},
    {"Fråga": "Vilket år grundades företaget Nintendo?", "Svar": "1889"},
    {"Fråga": "Vad är den kemiska symbolen för guld?", "Svar": "Au"},
    {"Fråga": "Vilket land kom Hawaii Pizzan ifrån?", "Svar": "Kanada"},
    {"Fråga": "Innan Sverige gick med i NATO, hur många år av fred exakt hade vi?", "Svar": "210"},
    {"Fråga": "Vad heter Microsofts grundare?", "Svar": "Bill Gates"},
    {"Fråga": "Hur många gånger har Sverige vunnit Eurovision?", "Svar": "7"},
    {"Fråga": "Vilket land har mest invånare?", "Svar": "Indien"},
    {"Fråga": "Hur många kontinenter har Jorden?", "Svar": "7"},
    {"Fråga": "Hur många kapitel har Bibeln?", "Svar": "1346"},
    {"Fråga": "Vad heter Napoleon i efternamn?", "Svar": "Bonaparte"},
    {"Fråga": "Hur många avsnitt har Breaking Bad och Better Call Saul tillsammans?", "Svar": "125"},
    {"Fråga": "Vad heter Pixars första film?", "Svar": "Toy Story"},
]

def kör_quiz():
    correct_answers_in_a_row = 0
    selected_questions = random.sample(questions, 5)

    for q in selected_questions:
        print(f"\nFråga: {q['Fråga']}")
        
        start_time = time.time()

        try:
            user_answer = input("Du har 30 sekunder på dig att svara: " ).strip()

            if time.time() - start_time > 30:
                print("Tiden är ute")
                return False
            
            if user_answer.lower() == q["Svar"].lower():
                correct_answers_in_a_row += 1
                print("Rätt svar!")
            else:
                print("Fel svar!")
                return False
        
        except TimeoutError:
            print("Tiden är ute")
            return False
        
        if correct_answers_in_a_row == 5:
            print("\nGrattis, du har vunnit min frågesport genom att svarat rätt 5 gånger i rad!")
            return True
        
    print("\nDu lyckades inte svara rätt 5 gånger i rad, YOU LOSE!")
    return False

def spela_igen():
    while True:
        resultatet = kör_quiz()

        spela_igen = input("\nVill du spela igen? (ja/nej): ").strip().lower()

        if spela_igen != "ja":
            print("Tack för att du spelade! Hej då!")
            break

spela_igen()