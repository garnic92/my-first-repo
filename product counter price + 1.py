
produs = 0
max_produse = 50
status = False #Lista cu statutul de client
preț = 0

plata = ['plătit', 'neplătit ', 'în așteptare', ]

for status in plata:
    if status == 'plătit':
       print( "status plată: plătit")
    elif not status == 'plătit':  # Verificam daca clientul este membru
       print("Comanda nu este plătită, nu poate fi procesată.")
    else:
       print("Eroare: Status de plată necunoscut.")
 
while  produs <= 50:
 produs = produs +1

produs = int(input(f"introduce cite produse {produs}"))
preț = int(input(f"introduce preț produsul {preț} "))
achitare = plata 
plata = int(input(f" introduce daca a plătit, neplătit sau în așteptare {achitare} "))

if produs >= 0 and produs <= 50 :
   print(("Numar de produse: {produs}, preț: {preț},  status plată: {status} "))
else:
   print(" Eroare: Număr de produse invalid.")
if preț <= 0 :
   print("Eroare: Prețul trebuie să fie mai mare decât 0.")
else:
   print(("Numar de produse: {preț} "))
