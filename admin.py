import hashlib
import json
import os
import pathlib
from unittest import result

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(CUR_DIR, "mot_de_pass")


class Admin:
    def __init__(self,nom, mdp):
        self.nom = nom
        self.mdp = hashlib.md5(mdp.encode()).hexdigest()


    def creer_un_admin(self):

        dico = {

            self.nom : self.mdp
        }
        if self.__sauvegarder_le_mdp__(dico):
            return dico
        return False

    def __sauvegarder_le_mdp__(self, dico):
        chemin = self.__dir_file__()

        with open(chemin, "r") as f:
            resul = json.load(f)
        resul.append(dico)
        with open(chemin, "w") as f:
            json.dump(resul, f, indent=4)
        return str(chemin)

    def check(self, nom, mdp):

        chemin = self.__dir_file__()
        with open(chemin, "r") as f:
            resul = json.load(f)
        if resul:
            mdp =  hashlib.md5(mdp.encode()).hexdigest()
            for i in resul:
                resultat = [i for x, y in i.items() if x.lower() == nom.lower() and y == mdp]
            return resultat
        return False






    @staticmethod
    def __dir_file__():
        chemin = pathlib.Path(DATA_DIR) / "mot_de_pass_admin.json"
        try:
            if not os.path.exists(DATA_DIR):
                pathlib.Path(DATA_DIR).mkdir(parents=True, exist_ok=True)
        except Exception as e:
            return str(e)
        return str(chemin)

if __name__ == '__main__':
    a = Admin('ali', 'ali')
    print(a.check('ali', 'ali'))

