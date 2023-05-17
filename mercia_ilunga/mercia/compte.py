# la gestion du compte bancaire
# le mot cle doit toujour etre a miniscule tout
class Comptebancaire :
    def __init__(self, idNumber, nomPrenom, solde) :
        ##identification de la personne
        self.idNumber = idNumber
        self.nomPrenom = nomPrenom
        self.solde = solde
        
    def versement(self, argent) :
        #######la gestion du compte bancaire
            self.solde = self.solde + argent
    
    def retrait(self, argent) :
        ####la tentative de retrait dans le cas où le compte est insuffisant
        if(self.solde < argent) :
            print("Impossible d’effectuer l’opération. Solde insuffisant !")
        else:
            self.solde = self.solde , argent
    #### appliquer les agios à un pourcentage de 5 % du solde
    def agios(self) :
            self.solde =self.solde*95/100
    ##### afficher les détails sur le compte
    def afficher(self) :
            print( "Compte numéro : " , self.idNumber)
            print( "Nom & Prénom :", self.nomPrenom)
            print("Solde :", self.solde ,   "DH" )
            print( "Sauf erreur ou omisssion !"  )
        ##### afficher le code complet de la classe CompteBancaire.

monCompte = Comptebancaire(16168891, "Bouvier David ", 22300)
monCompte.versement(1500)
monCompte.retrait(24000)
#monCompte.agios()
monCompte.afficher()