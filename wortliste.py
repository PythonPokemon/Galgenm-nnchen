
woerter = []

umlaut = {
    'ä': 'ae',
    'ö': 'oe',
    'ü': 'ue',
    'Ä': 'Ae',
    'Ö': 'Oe',
    'Ü': 'Ue',
    'ß': 'ss'
}


with open('Wortsammlung.txt', 'r') as datei:
    inhalt = datei.read()


for umlaut, ersatz in umlaut.items():
        inhalt = inhalt.replace(umlaut, ersatz)

woerter = inhalt.split()


# print(woerter)