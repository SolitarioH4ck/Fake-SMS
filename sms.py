#!/usr/bin/env python
#code by SolitarioH4ck23

#Modulos
import time, os, requests

#COLORES
dr='\033[1;34m'
rd='\033[1;30m'
nv='\033[1;39m'


os.system("clear")
print(f"""{dr}
█████▒  ▄▄▄       ██ ▄█▀▓█████     ██████  ███▄ ▄███▓  ██████
▓██   ▒▒████▄     ██▄█▒ ▓█   ▀    ▒██    ▒ ▓██▒▀█▀ ██▒▒██    ▒
▒████ ░▒██  ▀█▄  ▓███▄░ ▒███      ░ ▓██▄   ▓██    ▓██░░ ▓██▄
{rd}░▓█▒  ░░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄      ▒   ██▒▒██    ▒██   ▒   ██
░▒█░    ▓█   ▓██▒▒██▒ █▄░▒████▒   ▒██████▒▒▒██▒   ░██▒▒██████▒▒
▒ ░    ▒▒   ▓▒█░▒ ▒▒ ▓▒░░ ▒░ ░   ▒ ▒▓▒ ▒ ░░ ▒░   ░  ░▒ ▒▓▒ ▒ ░
░       ▒   ▒▒ ░░ ░{rd}code by {nv}@SolitarioH4ck23{rd}▒  ░ ░░  ░  ░░        
░ ░     ░   ▒   ░ ░░ ░    ░      ░  ░  ░  ░      ░   ░  ░  ░
            ░  ░░  ░      ░  ░         ░         ░""")

num = input(f"""
{rd}┌══════════════════════┐
{rd}█ {dr}NUMERO DE LA VICTIMA{rd} █
{rd}└══════════════════════┘
 ┃
 └═► {nv}""")

sms = input(f"""
{rd}┌════════════════════┐
{rd}█ {dr}ESCRIBE EL MENSAJE{rd} █
{rd}└════════════════════┘
 ┃
 └═► {nv}""")

resp = requests.post('https://textbelt.com/text', {
    'phone': f'{num}',
    'message': f'{sms}',
    'key': 'textbelt',
    })
print(f"""
{rd}┌══════════════════┐
{rd}█ {dr}ENVIANDO SMS..👻{rd} █
{rd}└══════════════════┘""")
time.sleep(1.8)

input(f"""
{rd}┌════════════════════════════┐
{rd}█ {dr}SMS ENVIADO PRESIONA ENTER{rd} █
{rd}└════════════════════════════┘
""")
os.system("python w.py")
