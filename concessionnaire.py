import json

class Auto:
    def __init__(self, marque, modele, couleur, prix, kilometrage, moteur, parking_spot):
        self.marque = marque
        self.modele = modele
        self.couleur = couleur
        self.prix = prix
        self.kilometrage = kilometrage
        self.moteur = moteur
        self.parking_spot = parking_spot
        self.vendu = False

    def __str__(self):
        moteur_info = f"{self.moteur['type'].capitalize()}"
        if self.moteur['type'] != 'electrique':
            moteur_info += f" {self.moteur['capacite']}L {self.moteur['cylindres']} cyl"
        return (f"{self.marque} {self.modele} ({self.couleur})\n"
                f"Prix: {self.prix}$ | Km: {self.kilometrage}\n"
                f"Moteur: {moteur_info} | Place: #{self.parking_spot}")

class Concessionnaire:
    def __init__(self, nom):
        self.nom = nom
        self.autos = []
        self.parking_spots = [None] * 100  # 100 places de stationnement
        
        # Charger l'inventaire initial depuis JSON
        self.charger_inventaire_initial('inventaire_init.json')

    def charger_inventaire_initial(self, fichier):
        try:
            with open(fichier, 'r') as f:
                data = json.load(f)
                for auto_data in data:
                    # Valider la place de parking
                    spot = auto_data.get('parking_spot')
                    if 0 <= spot < 100 and self.parking_spots[spot] is None:
                        auto = Auto(
                            marque=auto_data['marque'],
                            modele=auto_data['modele'],
                            couleur=auto_data['couleur'],
                            prix=auto_data['prix'],
                            kilometrage=auto_data['kilometrage'],
                            moteur=auto_data['moteur'],
                            parking_spot=spot
                        )
                        self.autos.append(auto)
                        self.parking_spots[spot] = auto
        except FileNotFoundError:
            print("Fichier d'inventaire initial introuvable")

    def ajouter_auto(self, auto, spot=None):
        # Si spot spécifié
        if spot is not None:
            if 0 <= spot < 100:
                if self.parking_spots[spot] is None:
                    auto.parking_spot = spot
                    self.autos.append(auto)
                    self.parking_spots[spot] = auto
                    return True
                print(f"La place {spot} est déjà occupée!")
                return False
            print("Numéro de place invalide (0-99)")
            return False
        
        # Sinon trouver première place libre
        for spot in range(len(self.parking_spots)):
            if self.parking_spots[spot] is None:
                auto.parking_spot = spot
                self.autos.append(auto)
                self.parking_spots[spot] = auto
                return True
        print("Aucune place de parking disponible!")
        return False

    def vendre_auto(self, index):
        if 0 <= index < len(self.autos):
            auto = self.autos[index]
            auto.vendu = True
            self.parking_spots[auto.parking_spot] = None
            del self.autos[index]
            return True
        return False

    def filtrer_autos(self, couleur=None, prix_min=None, prix_max=None, moteur_type=None):
        resultats = []
        for auto in self.autos:
            if couleur and auto.couleur.lower() != couleur.lower():
                continue
            if prix_min and auto.prix < prix_min:
                continue
            if prix_max and auto.prix > prix_max:
                continue
            if moteur_type and auto.moteur['type'].lower() != moteur_type.lower():
                continue
            resultats.append(auto)
        return resultats

    def sauvegarder_inventaire(self, fichier):
        data = []
        for auto in self.autos:
            auto_data = {
                'marque': auto.marque,
                'modele': auto.modele,
                'couleur': auto.couleur,
                'prix': auto.prix,
                'kilometrage': auto.kilometrage,
                'moteur': auto.moteur,
                'parking_spot': auto.parking_spot
            }
            data.append(auto_data)
        
        with open(fichier, 'w') as f:
            json.dump(data, f, indent=2)
