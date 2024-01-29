import random

def pull(x):
    amount=int(x)
    karten= []
    meanings= []
    for _ in range(amount):
        
        with open("card.txt", "r") as file1:
            card_options = file1.read().splitlines()
            response_card = random.choice(card_options)
            card = str(response_card)
            karten.append(card)
        #compare card to find corresponding description for the card chosen
        with open("upright.txt", "r") as file2, open("reversed.txt", "r") as file3:
            uprights=file2.readlines()
            reverseds=file3.readlines()

            for line in reverseds:
                if (card+" : ") in line:
                    description = str(line)
                    reading = (description.split(':', 1)[-1])
                    meanings.append(reading)
                else:
                    for line in uprights:
                        if (card+" : ") in line:
                            description = str(line)
                            reading = (description.split(':', 1)[-1])
                            meanings.append(reading)
    return karten, meanings
    