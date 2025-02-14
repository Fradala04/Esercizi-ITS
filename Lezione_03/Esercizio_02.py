soglia = int(input("inserisci la soglia: ")) 
Veicoli_Nord_Sud = int(input("quanti veicoli ci stanno nella direzione Nord-Sud ? : "))
Veicoli_Est_Ovest = int(input("quanti veicoli ci stanno nella direzione Est-Ovest ? : "))
Tempo_Nord_Sud: int = None
Tempo_Est_Ovest: int = None
if Veicoli_Nord_Sud  > soglia:
    Tempo_Nord_Sud = 60
    Tempo_Est_Ovest = 40
if Veicoli_Est_Ovest  > soglia:
    Tempo_Est_Ovest  = 60
    Tempo_Nord_Sud = 40
if (Veicoli_Nord_Sud  > soglia) and (Veicoli_Est_Ovest > soglia):
    Tempo_Nord_Sud = 50
    Tempo_Est_Ovest = 50
if (Veicoli_Nord_Sud < soglia) and  (Veicoli_Est_Ovest < soglia):
    Tempo_Nord_Sud = (Veicoli_Nord_Sud) / (Veicoli_Nord_Sud + Veicoli_Est_Ovest) * (100)
    Tempo_Est_Ovest = (Veicoli_Est_Ovest) / (Veicoli_Nord_Sud + Veicoli_Est_Ovest) * (100)
print(Tempo_Nord_Sud)
print(Tempo_Est_Ovest)

