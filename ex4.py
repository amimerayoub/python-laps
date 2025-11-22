# cercle_complet.py

from math import pi

class Cercle:
    def __init__(self, rayon: float):
        
        self.rayon = rayon

    @property
    def rayon(self) -> float:
        return self._rayon

    @rayon.setter
    def rayon(self, valeur: float):
        if valeur <= 0:
            raise ValueError("Le rayon doit être strictement positif.")
        self._rayon = float(valeur)

    @property
    def perimetre(self) -> float:
        return 2 * pi * self._rayon

    @property
    def surface(self) -> float:
        return pi * (self._rayon ** 2)

    def agrandir(self, pourcentage: float):
        """Augmente le rayon de 'pourcentage'%."""
        if pourcentage < 0:
            raise ValueError("Le pourcentage doit être positif.")
        facteur = 1 + (pourcentage / 100)
        self.rayon = self._rayon * facteur


if __name__ == "__main__":
    c = Cercle(3)
    print("Périmètre :", c.perimetre)   # 2πr
    print("Surface :", c.surface)       # πr²

    try:
        c.rayon = -5
    except ValueError as e:
        print("Erreur capturée :", e)

   
    c2 = Cercle(10)
    c2.agrandir(50)   
    print("Nouveau rayon après agrandissement :", c2.rayon)
