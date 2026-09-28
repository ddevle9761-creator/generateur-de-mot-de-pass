# class ToolBox:
#     """Boite à outils."""

#     def __init__(self):
#         """Initialise les outils."""
#         self.tools = []

#     def add_tool(self, tool):
#         """Ajoute un outil."""
#         self.tools.append(tool)

#     def remove_tool(self, tool):
#         """Enleve un outil."""
#         index = self.tools.index(tool)
#         del self.tools[index]

#     def show_tools(self):
#         return self.tools

 

# class Screwdriver:
#     """Tournevis."""

#     def __init__(self, size=3):
#         """Initialise la taille."""
#         self.size = size
    
#     def tighten(self, screw):
#         """Serrer une vis."""
#         screw.tighten()
    
#     def loosen(self, screw):
#         """Desserre une vis."""
#         screw.loosen()
    
#     def __repr__(self):
#         """Représentation de l'objet."""
#         return f"Tournevis de taille {self.size}"


# class Hammer:
#     """Marteau."""

#     def __init__(self, color="red"):
#         """Initialise la couleur."""
#         self.color = color
    
#     def paint(self, color):
#         """Paint le marteau."""
#         self.color = color
    
#     def hammer_in(self, nail):
#         """Enfonce un clou."""
#         nail.nail_in()
    
#     def remove(self, nail):
#         """Enleve un clou."""
#         nail.remove()
    
#     def __repr__(self):
#         """Représentation de l'objet."""
#         return f"Marteau de couleur {self.color}"


# class Screw:
#     """Vis."""
     
#     MAX_TIGHTNESS = 5
    
#     def __init__(self):
#         """Initialise son degré de serrage."""
#         self.tightness = 0
    
#     def loosen(self):
#         """Déserre le vis."""
#         if self.tightness > 0:
#             self.tightness -= 1
    
#     def tighten(self):
#         """Serre le vis."""
#         if self.tightness < self.MAX_TIGHTNESS:
#             self.tightness += 1
    
#     def __str__(self):
#         """Retourne une forme lisible de l'objet."""
#         return "Vis avec un serrage de {}".format(self.tightness)


# class Nail:
#     """Clou."""
    
#     def __init__(self):
      
#         """Initialise son statut "dans le mur"."""
#         self.in_wall = False
    
#     def nail_in(self):
#         """Enfonce le clou dans un mur."""
#         if not self.in_wall:
#             self.in_wall = True
    
#     def remove(self):
#         """Enlève le clou du mur."""
#         if self.in_wall:
#             self.in_wall = False
    
#     def __str__(self):
#         """Retourne une forme lisible de l'objet."""
#         wall_state = "dans le mur" if self.in_wall else "hors du mur"
#         return f"Clou {wall_state}."


    
# boite_a_outils = ToolBox()
# marteaux = Hammer()
# vis = Screw()
# clou =  Nail()

# # serrer le vis
# vis.tighten()

# # Enfonce le clou 
# marteaux.hammer_in(clou)

# boite_a_outils.add_tool(marteaux)
# boite_a_outils.add_tool(vis)
# boite_a_outils.add_tool(clou)


# for i in boite_a_outils.tools:
#     print(i)

# marteaux.color = 'cyan'
# vis.loosen()
# marteaux.remove(clou)
# clou.remove()


# for i in boite_a_outils.tools:
# #     print(i)

# def calculer_total_addition(montant, pourcentage_pourboire):
#     '''
#     Retourne le montant total à payer (montant + pourboire).
#     - montant: nombre >= 0
#     - pourcentage_pourboire: pourcentage du pourboire (ex: 10 pour 10%)
#     À faire:
#     1) Valider les entrées (lever ValueError si négatives)
#     2) Calculer le pourboire et le total
#     3) Arrondir le résultat à 2 décimales
#     '''
#     # TODO: implémenter la fonction
#     if montant < 0 or pourcentage_pourboire < 0:
#         raise ValueError("Les valeurs doivent être positives.")

#     try:
#         pourboire = montant * (pourcentage_pourboire / 100)
#         total = montant + pourboire
#         print(f"Montant: {montant}, Pourboire: {pourboire}, Total: {total}")
#         return round(total, 2)
#     except Exception as e:
#         raise ValueError("Erreur lors du calcul: " + str(e))

    
        


# if __name__ == '__main__':
#     # Quelques exemples à tester quand votre fonction sera prête:
#     print(calculer_total_addition(50, 10))         # attendu: 55.0
#     print(calculer_total_addition(48.9, 12.5))     # attendu: 55.01
#     #print(calculer_total_addition(0, 15))          # attendu: 0.0
#     #calculer_total_addition(-5, 10)                # devrait lever ValueError
    


def liste_remove(liste, n):
    while n < 0:
        list1.pop(n)
        list1.pop(-n)
        n -= 1
    return list1


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(liste_remove(liste=list1, n=3))
