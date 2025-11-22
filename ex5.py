from datetime import datetime
from time import sleep

class JournalTaches:
    def __enter__(self):
        self.f = open("journal.txt", "a", encoding="utf-8")
        return self

    def enregistrer(self, tache: str):
        ligne = f"{datetime.now().isoformat()} - {tache}\n"
        self.f.write(ligne)

    def __exit__(self, exc_type, exc, tb):
        self.f.close()

    @classmethod
    def lire(cls):
        try:
            with open("journal.txt", "r", encoding="utf-8") as f:
                lignes = f.readlines()
                for l in reversed(lignes):
                    print(l.rstrip())
        except FileNotFoundError:
            print("Aucun journal trouvé.")


if __name__ == "__main__":
    with JournalTaches() as journal:
        journal.enregistrer("Préparer la réunion du projet X")
        sleep(1)
        journal.enregistrer("Faire la revue de code")
        sleep(1)
        journal.enregistrer("Envoyer le rapport hebdomadaire")

    print("\nHistorique (ordre inverse) :")
    JournalTaches.lire()
