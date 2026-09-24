# import hashlib
import pathlib
import string
import random
import os 
import json


CUR_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(CUR_DIR, "mot_de_pass")


class GenerateurMdp:
    dico = {}

    def __init__(self):

        if not isinstance(self.dico, dict):
            self.dico = dict(self.dico)


    def __genere_mdp__(self, longeur=20):
        mdp = ""
        mdp_sting = string.ascii_letters + string.punctuation + string.digits
        for i in range(longeur):
            mdp += random.choice(mdp_sting)

        return mdp

    """
    :keyword decommenter le import du hashlib et la ligne (37) 
    :parameter pour activer le hash
    """
    
    def generer_un_mot_de_pass(self, motif:str):
        if motif is None or motif == "":
            return False
        mdp = str(self.__genere_mdp__())
        # mdp_hasher = hashlib.sha256(mdp.encode()).hexdigest()
        self.dico[motif] = mdp

        return mdp

    def sauvegarder_le_mdp(self):
        chemin = self.__dir_file__()


        with open(chemin, "r") as f:
            resul = json.load(f)
        resul.append(self.dico)
        with open(chemin, "w") as f:
            json.dump(resul, f, indent=4)
        return str(chemin)


    def les_sauvegarde(self):
        chemin = self.__dir_file__()
        with open(chemin, "r") as f:
            resul = json.load(f)
        return [i for i in resul ]


    def obtenir_recherche(self, filter_text):
        chemin = self.__dir_file__()
        query = (filter_text or '').strip().lower()
        with open(chemin, "r") as f:
            resul = [json.load(f)]
        liste = []
        if resul:
            for i in resul[0]:
                if query in str(i.keys()).lower():
                    liste.append(i)

        return liste




    @staticmethod
    def __dir_file__():
        chemin = pathlib.Path(DATA_DIR) / "mot_de_pass.json"
        try:
            if not os.path.exists(DATA_DIR):
                pathlib.Path(DATA_DIR).mkdir(parents=True, exist_ok=True)
        except Exception as e:
            return str(e)
        return str(chemin)





if __name__ == '__main__':
    
    c = GenerateurMdp()

    #print(c.generer_un_mot_de_pass(''))
    print(c.obtenir_recherche('p'))

# mdf = "/:%o>{U6t!#Vjx70GMaN"
# h_mdp = "98dc2026048a72af55a4c5d1c0802f477abdaa2b1397ab6f67b37ffe6d1e4998"
#
# mdf = hashlib.sha256(mdf.encode()).hexdigest()
#
# print(mdf == h_mdp)