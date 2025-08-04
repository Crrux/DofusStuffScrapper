class Equipement:
    def __init__(self, name):
        self.name = name
        self.compos = []

    def add_compos(self, compo):
        """
        Ajoute un composant à l'équipement.
        Args:
            compo: tuple contenant le nom du composant et sa quantité.

        Returns:
            bool: True si l'ajout est réussi, False sinon.
        Raises:
            TypeError: Si le composant n'est pas un tuple de (nom, quantité).
            ValueError: Si le composant n'est pas un tuple de longueur 2.
            error: Si une erreur se produit lors de l'ajout du composant.
        Description:
            Cette méthode permet d'ajouter un composant à l'équipement.
            Le composant doit être un tuple contenant le nom du composant et sa quantité.
            La quantité peut être un entier ou une chaîne convertible en entier.
        """

        try:
            if isinstance(compo, tuple) and len(compo) == 2:
                nom_compo, qty_compo = compo
                if isinstance(nom_compo, str) and isinstance(qty_compo, (int, str)):
                    if isinstance(qty_compo, str):
                        try:
                            qty_compo = int(compo[1])
                        except ValueError:
                            raise TypeError("La quantité doit être un entier ou convertible en entier.")
                    self.compos.append({nom_compo: int(qty_compo)})
            else:
                raise ValueError("Composant doit être un tuple de (nom, quantité).")
        except Exception as e:
             print(f"Erreur lors de l'ajout du composant: {e}")
        return True


    def __repr__(self):
        return f"Equipement(nom={self.nom}, compos={self.compos})"

if __name__ == '__main__':
    equip = Equipement("Epée de feu")
    equip.add_compos(("Fer", 10))
    equip.add_compos(("Bois", '5'))
    print(equip)
    # Output: Equipement(nom=Epée de feu, compos=[{'Fer': 10}, {'Bois': 5}])