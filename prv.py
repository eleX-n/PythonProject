from logging import getLevelName

print ("vaffaculo")

msg = "ciao"
print (msg + " " + "ele")

print (type(msg))

nome = "ele"
eta = 30
print (f"mi chiamo {nome} e ho {eta} anni")
print()

nome = input ("qual è il mio nome?")
print ("ciao mi chiamo " + nome)




###if while

anno = 2026
eta = 18

birth= int(input("in che anno sei nato?"))
if 2026 - birth > eta:
    print("welcome")

nome_user = "ele"
nome_utente= str(input("come ti chiami utente?"))
if nome_user == nome_utente:
    print("ti chiami come me")