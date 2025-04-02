from concessionnaire import Concessionnaire, Auto
import json

def afficher_menu():
    print("\n=== Menu Concessionnaire ===")
    print("1. Voir toutes les autos")
    print("2. Filtrer les autos")
    print("3. Vendre une auto")
    print("4. Ajouter une auto")
    print("5. Quitter")
    return input("Choisissez une option (1-5): ")

def afficher_autos(autos):
    if not autos:
        print("\nAucune auto correspondante trouvée")
        return
    for i, auto in enumerate(autos):
        print(f"\nAuto #{i + 1}")
        print(auto)

def saisir_prix(message):
    while True:
        valeur = input(message)
        if not valeur:  # Si l'utilisateur appuie sur Entrée
            return None
        try:
            return float(valeur)
        except ValueError:
            print("Veuillez entrer un nombre valide ou appuyer sur Entrée pour ignorer")

def main():
    concessionnaire = Concessionnaire("AutoPlus Québec")
    
    # Le concessionnaire charge déjà l'inventaire dans son __init__
    
    while True:
        try:
            choix = afficher_menu()
        except KeyboardInterrupt:
            print("\n\nInterruption détectée - veuillez choisir une option valide")
            continue
        
        if choix == "1": # Voir toutes les autos
            afficher_autos(concessionnaire.autos)
            
        elif choix == "2": # Filtrer
            print("\nFiltres disponibles (appuyez sur Entrée pour ignorer)")
            couleur = input("Couleur: ")
            prix_min = saisir_prix("Prix minimum: ") or None
            prix_max = saisir_prix("Prix maximum: ") or None
            moteur_type = input("Type de moteur (essence/electrique/hybride): ") or None
            
            resultats = concessionnaire.filtrer_autos(
                couleur=couleur,
                prix_min=prix_min,
                prix_max=prix_max,
                moteur_type=moteur_type
            )
            afficher_autos(resultats)
            
        elif choix == "3": # Vendre
            try:
                index = int(input("Numéro de l'auto à vendre: ")) - 1
                if concessionnaire.vendre_auto(index):
                    print("Auto vendue avec succès!")
                else:
                    print("Numéro d'auto invalide")
            except ValueError:
                print("Veuillez entrer un nombre valide")
                
        elif choix == "4": # Ajouter
            try:
                print("\nNouvelle auto:")
                marque = input("Marque: ")
                modele = input("Modèle: ")
                couleur = input("Couleur: ")
                prix = float(input("Prix: "))
                km = int(input("Kilométrage: "))
                
                # Saisie moteur
                moteur_type = input("Type moteur (essence/electrique/hybride): ").lower()
                moteur = {"type": moteur_type}
                if moteur_type != "electrique":
                    moteur["capacite"] = float(input("Capacité moteur (L): "))
                    moteur["cylindres"] = int(input("Nombre de cylindres: "))
                else:
                    moteur["capacite"] = None
                    moteur["cylindres"] = None
                
                try:
                    spot_input = input("Numéro de place (0-99, laisser vide pour auto): ")
                    spot = int(spot_input) if spot_input else None
                except ValueError:
                    print("Numéro invalide - attribution automatique")
                    spot = None
                
                nouvelle_auto = Auto(marque, modele, couleur, prix, km, moteur, -1)
                if concessionnaire.ajouter_auto(nouvelle_auto, spot):
                    print("Auto ajoutée avec succès!")
                else:
                    print("Erreur lors de l'ajout - place déjà occupée")
            except ValueError:
                print("Erreur de saisie - veuillez entrer des valeurs valides")
                
        elif choix == "5": # Quitter
            print("Sauvegarde de l'inventaire...")
            concessionnaire.sauvegarder_inventaire("inventaire_final.json")
            print("Au revoir!")
            break
            
        else:
            print("Option invalide - veuillez choisir entre 1 et 5")
        
        try:
            input("\nAppuyez sur Entrée pour continuer...")
        except KeyboardInterrupt:
            print("\n\nInterruption détectée - retour au menu principal")

if __name__ == "__main__":
    main()
