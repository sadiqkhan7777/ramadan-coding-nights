from fastapi import FastAPI
import random

app = FastAPI()

# List of Pakistani jokes in Roman Urdu
jokes = [
    "Pathan: Doctor sahab, jab mein sota hoon toh aankhein band ho jati hain! Doctor: Bhai shukar mana! Agar khuli rehti toh bhoot lagta!",
    "Munna: Ammi mujhe chocolate chahiye! Ammi: Beta, dua maango. Munna: Ya Allah, Ammi ko samajh ajaye!",
    "Teacher: 2 aur 2 kitne hote hain? Student: Sir, agr deal achi ho toh 5 bhi ho sakte hain!",
    "Baba ji: Beta, izzat kamao. Beta: Baba ji, izzat Google Pay par aati hai?",
    "Boy: Mein apko apni jaan se bhi zyada pyar karta hoon! Girl: Jhoot mat bolo! Boy: Pakka! Kyunki jaan sirf ek hai, magar tumse 3rd love hai!"
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the Random Pakistani Joke Generator! Go to /joke to get a random joke."}

@app.get("/joke")
def get_joke():
    return {"joke": random.choice(jokes)}
