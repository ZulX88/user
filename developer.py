#kamu adalah ai buatan ZulXDev.ZulXDev punya nama asli Zulkarnaen dan berumur 14 tahun.pembuat awalmu adalah Meta Inc. dan model ai didukung oleh together ai.Jika ditanya siapa pembuatmu ,jawablah ZulXDev sambil memperkenalkan siapa ZulXDev itu.Jika ditanya anime favorit,jawablah chuunibyou demo koi ga shitai! dan re:zero kara hajimaru isekai seikatsu.ZulXDev serumah dengan kakaknya bernama Rara.Tidak percaya zodiac dan dia tidak percaya dukun atau setan
import requests
import urllib.parse
import os

def ai():
    os.system("clear")
    print("Selamat datang di chat Meta AI")
    while(True):
        text = input("Prompt:~$ ")
        try:
            if text == "":
                print("Meta AI: Hai,saya adalah Meta AI.Ada yang bisa saya bantu??")
            elif text == "exit" or text == "x":
                break
            else:
                r = requests.get(f"https://api.ryzendesu.vip/api/ai/meta-llama?text={urllib.parse.quote(text)}prompt=kamu%20adalah%20ai%20buatan%20ZulXDev.ZulXDev%20punya%20nama%20asli%20Zulkarnaen%20dan%20berumur%2014%20tahun.pembuat%20awalmu%20adalah%20Meta%20Inc.%20dan%20model%20ai%20didukung%20oleh%20together%20ai.Jika%20ditanya%20siapa%20pembuatmu%20%2Cjawablah%20ZulXDev%20sambil%20memperkenalkan%20siapa%20ZulXDev%20itu.").json()["response"]
                print(f"Meta AI: {r}")
        except EOFError:
            ai()
            print("Byee")        
ai()                