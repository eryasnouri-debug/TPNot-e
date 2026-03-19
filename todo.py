taches = []

print("Bienvenue dans votre gestionnaire de tâches !")

while True:
  action = input("Ajouter (a) / Voir (v) / Enregistrer (e) / Supprimer (x) / Quitter (q): ")

  if action == "a":
    t = input("Nouvelle tâche : ")
    taches.append(t)
  elif action == "v":
    if len(taches) == 0:
        print("Liste a tache vide")
    else:
      for i, tache in enumerate(taches):
        print(f"({i}) {tache}")
  elif action == "x": 
    tache = int(input("position: "))
    if tache >= 0 and tache < len(taches):
      taches.pop(tache)
  elif action == "e":
    with open("tasks.txt", "w+") as f: 
     for tache in taches:
       f.write(tache + "\n")
    print("Action non-implémentée")
  elif action == "q":
    break
  else:
    print("Erreur") 

print("Merci ! À très vite !")
