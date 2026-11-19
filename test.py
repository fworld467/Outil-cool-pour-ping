import os
cible = input("Entre une adresse IP ou un nom domaine : ")

print(f"[*] Test de la cible : {cible} en cours...")

reponse = os.system (f"ping -c 4 {cible}")

if reponse == 0 :
    print(f"[+] Succès : {cible} est en ligne !")
else :
    print(f"[-] Attention : {cible} ne répond pas. ")
