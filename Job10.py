Montant_Initial = 1000
Rendement_Initial = 0.03
Gain = Montant_Initial*Rendement_Initial
print(f"Pour un montant initial de 1000 euros a 3% le gain est de= {Gain}")
Montant_Total = Montant_Initial+5000
Rendement_Total = Rendement_Initial+0.02
Gain_Total = Montant_Total*Rendement_Total
print(f"Le client augmente sont capital de 5000 euros, il est maintenant de {Montant_Total} euros")
print(f"Le rendement du client a augmenter de 2%, il est donc maintenant a {Rendement_Total}")
print(f"Pour un montantn total de 6000 euros a 5%, le gain est de= {Gain_Total}")
Montant_Final = Montant_Total-600
Rendement_Final=Rendement_Total-0.01
Gain_Final=Montant_Final*Rendement_Final
print(f"Le client décide de retirer 10% de sont Montant, il reste donc 5400 euros investis,")
print(f"Suite a un probleme financier le rendement diminue de 1%, ce qui nous laisse 4%")
print(f"Le montant final de l'investisseur est de {Montant_Final} et le gain sur l'année est de {Gain_Final}")