def validate_password(password: str) -> bool:
    """Valida una password secondo tre criteri specifici.

    Parameters:
    password (str): La password da validare.

    Returns:
    bool: True se valida, altrimenti solleva ValueError.
    """
    errors:list[str] = []

    if len(password) < 20:
        errors.append("Lunghezza inferiore a 20 caratteri")

    maiuscole:int = 0
    for c in password:
        if c.isupper():
            maiuscole +=1
    if maiuscole < 3:
        errors.append("Meno di 3 lettere maiuscole")
    
    speciali:int=0
    for c in password:
        if c.isalnum() == False:
            speciali +=1
    if speciali < 4:
        errors.append("Meno di 4 caratteri speciali")

    if errors:
        raise ValueError("Password non valida: " + ", ".join(errors))
    return True

# Test
try:
    print(validate_password("AB!@#defghijklmnopqrstuv"))
except ValueError as e:
    print(e)
