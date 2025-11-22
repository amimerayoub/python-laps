class CompteurPage:
    # Attribut de classe
    total_visites = 0

    def __init__(self, url: str):
        # Attribut d’instance
        self.url = url

        # Incrémentation du compteur global
        CompteurPage.total_visites += 1

        # Extension : compteur propre à chaque page
        self.visites_par_page = 0

    def afficher_stats(self) -> str:
        return f"Page {self.url} — visites globales : {CompteurPage.total_visites}"

    # Extension : incrémentation du compteur d’instance
    def enregistrer_lecture(self):
        self.visites_par_page += 1


# -----------------------
# Code de test (même fichier)
# -----------------------

if __name__ == "__main__":
    p1 = CompteurPage("https://example.com/")
    p2 = CompteurPage("https://example.com/blog")
    p3 = CompteurPage("https://example.com/contact")

    for p in (p1, p2, p3):
        print(p.afficher_stats())

    print("Total visites globales :", CompteurPage.total_visites)

    # Test de l’extension
    p1.enregistrer_lecture()
    p1.enregistrer_lecture()
    print("Visites de la page 1 :", p1.visites_par_page)
