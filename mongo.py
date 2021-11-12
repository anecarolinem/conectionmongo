from pymongo import MongoClient


client= MongoClient("localhost", 27017)
db= client.config

colection =db["tete3"]

post={
            "name": "ane",
            "idade": 16,
            "nume":154724}
colection.insert_one(post)
testa=db.tete3.find()
for result in testa:
    print(result)

