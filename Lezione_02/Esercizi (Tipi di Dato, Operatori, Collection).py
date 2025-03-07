3.1
names: list = ["Camillla", "Matteo", "Thomas", "Silvia", "Luca"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

3.2
print(f"Ciao {names[0]} come va?")
print(f"Ciao {names[1]} come va?")
print(f"Ciao {names[2]} come va?")
print(f"Ciao {names[3]} come va?")
print(f"Ciao {names[4]} come va?")

3.3
trasporti: list = ["Seicento", "Tesla", "Ferrari"]
print(f"Vorrei avere una {trasporti[0]}")
print(f"Vorrei avere una {trasporti[1]}")
print(f"Vorrei avere una {trasporti[2]}")

3.4
invitati: list = ["Camillla", "Matteo", "Thomas", "Silvia", "Luca"]
print(f"Ciao {invitati[0]} vuoi venire a cena da me stasera?")
print(f"Ciao {invitati[1]} vuoi venire a cena da me stasera?")
print(f"Ciao {invitati[2]} vuoi venire a cena da me stasera?")
print(f"Ciao {invitati[3]} vuoi venire a cena da me stasera?")
print(f"Ciao {invitati[4]} vuoi venire a cena da me stasera?")

3.5
print(f"{invitati[2]} non può venire")
invitati.insert(2, "Andrea")
print(f"Ciao {invitati[0]} vuoi venire a cena da me stasera?")
print(f"Ciao {invitati[1]} vuoi venire a cena da me stasera?")
print(f"Ciao {invitati[2]} vuoi venire a cena da me stasera?")
print(f"Ciao {invitati[3]} vuoi venire a cena da me stasera?")
print(f"Ciao {invitati[4]} vuoi venire a cena da me stasera?")

3.6
print("Ragazzi ho trovato un tavolo più grande")     #
invitati.insert(0, "Alessio")
invitati.insert(len(invitati)//2, "Lorenzo")
invitati.append("Nicholas")
print(f"Ciao {invitati[0]} vuoi venire a cena da me stasera?")
print(f"Ciao {invitati[1]} vuoi venire a cena da me stasera?")
print(f"Ciao {invitati[2]} vuoi venire a cena da me stasera?")
print(f"Ciao {invitati[3]} vuoi venire a cena da me stasera?")
print(f"Ciao {invitati[4]} vuoi venire a cena da me stasera?")
print(f"Ciao {invitati[5]} vuoi venire a cena da me stasera?")
print(f"Ciao {invitati[6]} vuoi venire a cena da me stasera?")

3.7
print("Mi dispiace purtroppo il tavolo non è più disponibile")
print(f"Eliminato: {invitati.pop(7)}")
print(f"Eliminato: {invitati.pop(5)}")
print(f"Eliminato: {invitati.pop(4)}")
print(f"Eliminato: {invitati.pop(2)}")
print(f"Eliminato: {invitati.pop(1)}")
print(f"Eliminato: {invitati.pop(0)}")
print(f"Ciao {invitati[0]} sei ancora invitato!")
print(f"Ciao {invitati[1]} sei ancora invitata!")
del invitati[1]
del invitati[0]
print(invitati)

3.8
luoghi: list = ["Barcellona", "Parigi", "New York", "Amsterdam", "Brno"]
print(luoghi)
print(sorted(luoghi))
print(luoghi)
print(sorted(luoghi, reverse=True))
print(luoghi)
luoghi.reverse()
print(luoghi)
luoghi.reverse()
print(luoghi)
luoghi.sort()
print(luoghi)
luoghi.sort(reverse=True)
print(luoghi)

3.9
n_invitati = len(invitati)
print(n_invitati)