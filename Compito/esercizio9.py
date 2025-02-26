pi_greco:float = 4 - 4/3 + 4/5 - 4/7
term = 4
i = 9
while pi_greco < 3.14:
    pi_greco = pi_greco + 4/i - 4/(i+2) # ... +4/9 - 4/11 + 4/13
    term += 2
    i+=4
print(f"pi greco vale {pi_greco:.2f}")
print(f"I termini neccesari per arrivare all'appossimazione di pi greco sono {term}")

#metodo 3.141
pi_greco:float = 4 - 4/3 + 4/5 - 4/7
term = 4
i = 9
while pi_greco < 3.141:
    pi_greco = pi_greco + 4/i - 4/(i+2)
    term += 2
    i+=4
print(f"pi greco vale {pi_greco:.3f}")
print(f"I termini neccesari per arrivare all'appossimazione di pi greco sono {term}")

#metodo 3.1415
pi_greco:float = 4 - 4/3 + 4/5 - 4/7
term = 4
i = 9
while pi_greco < 3.1415:
    pi_greco = pi_greco + 4/i - 4/(i+2)
    term += 2
    i+=4
print(f"pi greco vale {pi_greco:.4f}")
print(f"I termini neccesari per arrivare all'appossimazione di pi greco sono {term}")

#metodo 3.14159
pi_greco:float = 4 - 4/3 + 4/5 - 4/7
term = 4
i = 9
while pi_greco < 3.14159:
    pi_greco = pi_greco + 4/i - 4/(i+2)
    term += 2
    i+=4
print(f"pi greco vale {pi_greco:.5f}")
print(f"I termini neccesari per arrivare all'appossimazione di pi greco sono {term}")