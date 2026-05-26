"""
gep={"brand": "Canon", "model":"G5x", "type":"Mirrorless"}

gep["type"]="Kompakt"
print(gep["model"])

gep["model"]="HG2"
print(gep["model"])

gep["colour"]="black"
print(gep)

del gep["model"]
print (gep)


# Ez itt a "Táblázatunk", ami egy lista
raktar = [
    {"brand": "Canon", "model": "G5x", "type": "Kompakt"}, # 1. sor
    {"brand": "Sony", "model": "A7III", "type": "Mirrorless"}, # 2. sor
    {"brand": "Nikon", "model": "Z6", "type": "Mirrorless"}  # 3. sor
]
print(raktar[1]["model"])

# BEÁGYAZÁS
konyv = {
    "cim": "Az ember tragédiája",
    "szerzo": {
        "nev": "Madách Imre",
        "szuletes": 1823,
        "nemzetiseg": "magyar"
    },
    "ev": 1861
}
print(konyv["szerzo"]["szuletes"])

# gyakorlat
filozofus={"név":"Arthur Schopenhauer","fo_mu":{"cim": "XY" ,"kiadas_eve":"xxxx"} }
#print(filozofus["fo_mu"]["cim"])

filozofus["fo_mu"]["cim"]="Világ mint akarat és képzet"
filozofus["fo_mu"]["kiadas_eve"]="1818"
#print(filozofus)

for kulcs, ertek in filozofus.items():
    print(f" {kulcs} - {ertek}")

for kulcs, ertek in filozofus.items():
    if type(ertek) == dict:
        for i,y in ertek.items():
            print(f"{i} - {y}")
    else:
        print(f"{kulcs} - {ertek}")
"""

filozofusok=[
    {
        "név":"Arthur Schopenhauer",
        "fo_mu":{"cim": "Világ mint akarat és képzet" ,"kiadas_eve":"1818"} 
        },
        {
        "név":"Friedrich Nietzsche",
        "fo_mu":{"cim": "Így szólott Zarathustra","kiadas_eve":"1883"} 
        }
]

for sor in filozofusok:
    print("Név: " + sor["név"] + ', '+"Cím: " + sor["fo_mu"]["cim"])

    