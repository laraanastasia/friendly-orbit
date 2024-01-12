import discord
def get_response(user_input:str)-> str:
    lowered: str = user_input.lower()
    if lowered == '':
        return "Dein Schweigen ist purr-fekt..."
    elif "hallo" in lowered:
        return "miau! =^-^= "
    elif "tschüss" in lowered:
        return "es war katazisch mit dir zu reden ^^"
    elif "catbunny" in lowered:
        return "https://tenor.com/view/cats-cat-bunny-shake-head-gif-24738682"
    elif "catscream" in lowered:
        return "https://tenor.com/view/cry-crying-cat-crying-cat-cry-why-gif-27571714"
    elif "catno" in lowered:
        return "https://tenor.com/view/no-nope-cat-cute-gif-4544032"
    elif "catyes" in lowered:
        return "https://tenor.com/view/yes-yescat-cat-nodding-nod-gif-21702876"
    else: "Ich hab dich wohl hiss-verstanden"