lavoro:dict[str,int] = {"Nome": input("Inserire nome: "), "Ruolo": input("Inserire ruolo: "), "Età": int(input("Inserire età: "))}
match lavoro: 
    case {"ruolo": "admin"}:
        print("Accesso completo a tutte le funzionalità.")
    case {"ruolo": "moderatore"}:
        print("Può gestire i conetnuti ma non modificare le impostazioni.")
    case {"ruolo": "utente adulto", "età": età} if età >= 18:
        print("Accesso standard a tutti i servizi.")
    case {"ruolo": "utente minorenne", "età": età} if età < 18:
        print("Accesso limitato! Alcune funzionalità sono bloccate.")
    case {"ruolo": "ospite"}:
        print("Accesso ristretto! Solo visualizzazione dei contenuti.")
    case _:
        print("Attenzione! Ruolo non riconosciuto! Accesso negato!")