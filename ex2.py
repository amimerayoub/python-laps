
# inventaire.py


from datetime import datetime
from typing import List

LOG_FILE = "mouvements.log"

class Article:
    def __init__(self, reference: str, designation: str, prix_ht: float, stock: int):
        self.reference = str(reference)
        self.designation = str(designation)
        self.prix_ht = float(prix_ht)
        self.stock = int(stock)

    def valeur_stock(self) -> float:
        """
        Retourne la valeur du stock pour cet article (prix HT * quantite).
        """
        return self.prix_ht * self.stock

    def __str__(self) -> str:
        """
        Représentation lisible de l'article.
        Exemple : "Réf A123 — Stylo : 50 unités à 1.20 € HT"
        """
        return f"Réf {self.reference} — {self.designation} : {self.stock} unités à {self.prix_ht:.2f} € HT"

    def approvisionner(self, qte: int, log_file: str = LOG_FILE):
        """
        Augmente le stock de qte (doit être > 0) et journalise l'opération dans log_file.
        Le log contient datetime, référence, qte ajoutée, ancien_stock -> nouveau_stock.
        """
        if not isinstance(qte, int):
            raise TypeError("qte doit être un entier.")
        if qte <= 0:
            raise ValueError("qte doit être strictement positive pour un approvisionnement.")

        ancien_stock = self.stock
        self.stock += qte
        nouvel_stock = self.stock

        timestamp = datetime.now().isoformat(sep=' ', timespec='seconds')
        log_line = f"{timestamp} - Approvisionnement - Réf {self.reference} - +{qte} - {ancien_stock} -> {nouvel_stock}\n"

        
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(log_line)

def valeur_inventaire(articles: List[Article]) -> float:
    """
    Calcule la valeur totale de l'inventaire.
    """
    return sum(a.valeur_stock() for a in articles)

def main():
    
    a1 = Article("A100", "Stylo bille", 1.20, 50)
    a2 = Article("B200", "Cahier A4 80p", 2.50, 30)
    a3 = Article("C300", "Trousse", 5.75, 10)

    articles = [a1, a2, a3]

    
    print("Liste des articles :")
    for a in articles:
        print(a)

    total = valeur_inventaire(articles)
    print(f"\nValeur d'inventaire : {total:.2f} €")

    print("\nApprovisionnement : +20 sur A100")
    try:
        a1.approvisionner(20) 
    except Exception as e:
        print("Erreur lors de l'approvisionnement :", e)
    print(a1)  

   
    total_apres = valeur_inventaire(articles)
    print(f"\nValeur d'inventaire après approvisionnement : {total_apres:.2f} €")

    
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
            print("\n--- 5 dernières lignes de", LOG_FILE, "---")
            for line in lines[-5:]:
                print(line.rstrip())
    except FileNotFoundError:
        print(f"\nFichier de log '{LOG_FILE}' introuvable (aucun approvisionnement journalisé pour l'instant).")

if __name__ == "__main__":
    main()
