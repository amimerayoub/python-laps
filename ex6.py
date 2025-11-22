class Convertisseur:
    taux_eur_dh = 10.9

    @staticmethod
    def vers_dh(euros: float) -> float:
        return euros * Convertisseur.taux_eur_dh

    @staticmethod
    def vers_eur(dirhams: float) -> float:
        return dirhams / Convertisseur.taux_eur_dh

    @classmethod
    def mettre_a_jour_taux(cls, nv_taux: float):
        cls.taux_eur_dh = nv_taux


if __name__ == "__main__":
    montant = 100
    print("Avant mise à jour :", Convertisseur.vers_dh(montant))

    Convertisseur.mettre_a_jour_taux(11.2)
    print("Après mise à jour  :", Convertisseur.vers_dh(montant))

    print("100 DH en EUR :", Convertisseur.vers_eur(100))

