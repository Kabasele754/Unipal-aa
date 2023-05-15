class Vehicule:
    nom_vehicule : str
    #constructeur
    def __init__(self, V_nom, V_moteur, V_marque,):
        self.nom_vehicule =V_nom
        self.moteur =V_moteur
        self.marque=V_marque
    def afficher(self):
        print(f"c(c'est la voiture {self.nom_vehicule}moteur {self.moteur} de la marque {self.marque}")
v1= Vehicule("Tundra ","Diesel ","Nissan ")

print(v1.afficher())