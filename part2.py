import numpy as np


class FichierStl :

    def __init__(self,chemin):
        self.__chemin=chemin
        liste_de_valeurs = []
        fichier = open(self.__chemin, "r")
        lignes = fichier.readlines() #fourni le texte en chaines de caractères
        for i in lignes:
            k = i.split()
            for j in k:
                if j.isalpha() == False:
                    liste_de_valeurs.append(j)
        liste_des_vecteurs = []

        while len(liste_de_valeurs) != 0:
            vecteur = [liste_de_valeurs[0], liste_de_valeurs[1], liste_de_valeurs[2]]
            liste_des_vecteurs.append(vecteur)
            liste_de_valeurs = liste_de_valeurs[3:]
        liste_des_facettes = []
        liste_vecteurs_normaux = []
        while len(liste_des_vecteurs) != 0:
            facette = [ liste_des_vecteurs[1], liste_des_vecteurs[2], liste_des_vecteurs[3]]
            #print(facette)
            liste_vecteurs_normaux.append(liste_des_vecteurs[0])
            liste_des_facettes.append(facette)
            liste_des_vecteurs = liste_des_vecteurs[4:]
        fichier.close()
        print(liste_des_facettes) # liste des valeurs des coordonnées des facettes
        print(liste_vecteurs_normaux)
        self.__normal = liste_vecteurs_normaux
        self.__facette = liste_des_vecteurs


    def ProdVect(self,u,v):
        #retourne les coordonnées de w=(wx,wy,wz)=u ^v
        wx = u[1]*v[2]-u[2]*v[1] #les indices sont numérotés de 0 à 2
        wy = u[2]*v[0]-u[0]*v[2]
        wz = u[0]*v[1]-u[1]*v[0]
        w = np.array([wx, wy, wz])
        return(w)

    def Norme(self,u):
        return (u[0]**2+u[1]**2+u[2]**2)**(1/2)





    def Surface(self,A, B, C):
        AB = np.array([B[0]-A[0], B[1]-A[1], B[2]-A[2]])
        AC = np.array([C[0]-A[0], C[1]-A[1], C[2]-A[2]])
        DsFk = self.Norme(self.ProdVect(AB, AC))/2
        return DsFk

    def CalculFacette(self,vecteur_normal, A, B, C):
        ro = 1000
        g = 9.81
        Fk = ro*g*np.array([(A[0]+B[0]+C[0])/3, (A[1]+B[1]+C[1])/3, (A[2]+B[2]+C[2])/3])[2]*self.Surface(A, B, C)*vecteur_normal
        return Fk




#programme principal
C= FichierStl(r"V_HULL.stl")
C.CalculFacette(np.array([0, 1, 0]), np.array([0, 0, 0]), np.array([1, 0, 0]), np.array([0, 0, 1]))

