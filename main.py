import time

meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado"
            }

def process():
    if word in meme_dict.keys():
        print("¡Esa palabra está en nuestro diccionario! Su significado es:", (meme_dict[word]))
    else:
        print("Lo siento, esa palabra no esta en nuestro diccionario, ¡pero tal vez sea añadida en un futuro!")

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
process()
for i in range(4):
    time.sleep(2)
    word = input("Escribe otra palabra que no entiendas su significado (¡con mayúsculas!)")
    process()
    
    
    
    
    
