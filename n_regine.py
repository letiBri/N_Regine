# Metodo 1
# guardo tutte le celle della tabella nxn e poi dico si Q o no
# la soluzione sarà una collection nxn

# Metodo 2
# considero nella soluzione una qualche collection.
# una volta per volta aggiungo un elemento, una coordinata sulla scacchiera, cioè una coppia (riga, colonna)
# l'algoritmo termina quando il vettore raggiunge N elementi, quindi abbiamo inserito tutte le regine

# Metodo 3
# collection dove ogni elemento è solo la colonna e poi itero sull'indice di tale colonna

# la soluzione 2 è quella più "ricorsiva"
# immaginiamo di avere una collection dove inseriamo coppia (r, c) e quando raggiungiamo N abbiamo finito

# la nuova regina non deve essere mangiata, quindi bisogna mettere dei vincoli
# i vincoli sono che la regina non deve essere mangiata lungo le due diagonali, lungo la stessa riga e lungo la stessa colonna
# quindi i vincoli sono 4

# ad esempio ho una regina in po (2, 1)
# primo vincolo: la riga non può essere 2; riga != 2
# secondo vincolo: la colonna non può essere 1; colonna != 1
# sulla diagonale positiva: la somma degli indici è pari allo stesso numero (2 + 1 = 3)
# terzo vincolo: riga + colonna != 3
# sulla diagonale negativa: la differenza tra riga e colonna è costante (2 - 1 = 1)
# quarto vincolo: riga - colonna != 1

# dove si esegue il controllo?
# -1- verifico se questa è una soluzione valida all'interno dell' if
# -2- check sulla regina che vado ad aggiungere nel ciclo for
# ne faccio solo uno dei due
# con il metodo -2- faccio moooooolte meno chiamate ricorsive perchè faccio il controllo prima di richiamare il metodo ricorsivo
# quindi è più efficiente il -2-

from time import time
import copy


class NRegine:
    def __init__(self):
        self.n_soluzioni = 0
        self.n_chiamate = 0
        self.soluzioni = []

    def solve(self, N):  # metodo che chiama la ricorsione
        self.n_soluzioni = 0  # resetto il numero di soluzioni ogni volta che faccio una nuova ricorsione con N diverso
        self.n_chiamate = 0  # resetto il numero di chiamate
        self.soluzioni = []  # resetto la lista di soluzioni
        self._ricorsione([], N)

    # consiglio: fare sempre i vincoli in funzioni esterne, per non sporcare il metodo ricorsivo
    def is_admissible(self, regina1, regina2):  # confronto due coppie di coordinate (due regine)
        # 1) verifico riga. Se non va bene, return False
        if regina1[0] == regina2[0]:
            return False
        # 2) verifico colonna. Se non va bene, return False
        if regina1[1] == regina2[1]:
            return False
        # 3) verifico diagonale 1. Se non va bene, return False
        if regina1[0] + regina1[1] == regina2[0] + regina2[1]:
            return False
        # 4) verifico diagonale 2. Se non va bene, return False
        if regina1[0] - regina1[1] == regina2[0] - regina2[1]:
            return False
        # 5) Ho passato tutti i controlli. Return True
        return True

    def is_soluzione(self, parziale):
        # non posso verificare una regina con se stessa
        for i in range(len(parziale) - 1):
            for j in range(i + 1, len(parziale)):
                result = self.is_admissible(parziale[i], parziale[j])
                if result is False:
                    return False
        return True

    def is_valid(self, nuova_regina, parziale):
        for regina in parziale:
            if not self.is_admissible(nuova_regina, regina):  # metodo che verifica una coppia di regine
                return False
        return True

    def _ricorsione(self, parziale, N):  # parziale è una lista dove mettiamo dentro delle coppie
        self.n_chiamate += 1
        # condizione terminale: quando parziale ha lunghezza N
        if len(parziale) == N:
            # -1- verifico se questa è una soluzione valida
            # if self.is_soluzione(parziale):

            # potrei verificare se è una soluzione già trovata, magari attraverso un set
            print(parziale)  # stampo la soluzione, cioè una lista, composta da 4 liste di coppie [riga, colonna]
            self.soluzioni.append(copy.deepcopy(parziale))
            self.n_soluzioni += 1  # ogni volta che raggiungo una soluzione, aumento la variabile associata


        # caso ricorsivo
        else:
            for riga in range(N):
                for colonna in range(N):
                    # -2- check sulla regina che vado ad aggiungere
                    nuova_regina = [riga, colonna]
                    if self.is_valid(nuova_regina, parziale):  # ciclo su parziale e testo nuova_regina con parziale
                        # provo nuova ipotesi
                        parziale.append([riga, colonna])
                        # vado avanti nella ricorsione
                        self._ricorsione(parziale, N)
                        # backtracking
                        parziale.pop()  # elimino l'ultimo termine che ho messo e continuo a ciclare


if __name__ == '__main__':
    nreg = NRegine()
    start_time = time()
    print(nreg.solve(4))
    end_time = time()
    print(f"Elapsed time: {end_time - start_time}")
    print(f"Ho trovato {nreg.n_soluzioni} possibili soluzioni")
    print(f"Numero di chiamate ricorsive: {nreg.n_chiamate}")
