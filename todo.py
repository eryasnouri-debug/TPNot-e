taches = []

print("Bienvenue dans votre gestionnaire de tâches !")

while True:
  action = input("Ajouter (a) / Voir (v) / Enregistrer (e) / Quitter (q): ")

  if action == "a":
    t = input("Nouvelle tâche : ")
    taches.append(t)
  elif action == "v":
    for i in range(0, len(taches)):
      print(f"{taches[i]}")
  elif action == "e":
    print("Action non-implémentée")
  elif action == "q":
    break
  else:
    print("Erreur") 

print("Merci ! À très vite !")
