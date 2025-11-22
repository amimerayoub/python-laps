# carnet_adresses.py


class Contact:
    def __init__(self, nom: str, telephone: str, email: str):
        self.nom = nom
        self.telephone = telephone
        self.email = email

    @property
    def initiale(self) -> str:
        """Retourne la première lettre du nom, en majuscule."""
        return self.nom[0].upper()

    def __str__(self) -> str:
        return f"{self.nom} — {self.telephone} — {self.email}"


class Carnet:
    def __init__(self):
        self._contacts = []

    def ajouter(self, contact: Contact):
        """Ajoute un contact au carnet."""
        self._contacts.append(contact)

    def recherche(self, fragment: str):
        """Retourne tous les contacts dont le nom contient 'fragment' (insensible à la casse)."""
        fragment = fragment.lower()
        return [c for c in self._contacts if fragment in c.nom.lower()]

    def afficher_tous(self):
        """Affiche tous les contacts, un par ligne."""
        for c in self._contacts:
            print(c)

    @property
    def nombre_contacts(self):
        """Propriété en lecture seule : nombre total de contacts."""
        return len(self._contacts)



if __name__ == "__main__":
    c = Carnet()
    c.ajouter(Contact("Amina Saidi", "0612345678", "amina@example.com"))
    c.ajouter(Contact("Youssef Belkhou", "0699988877", "youssef@example.com"))
    c.ajouter(Contact("Said Toumi", "0677001122", "said@example.com"))

    # Recherche
    resultat = c.recherche("sa")
    for contact in resultat:
        print(contact.nom, contact.telephone)

    # Nombre total
    print("\nNombre total de contacts :", c.nombre_contacts)
