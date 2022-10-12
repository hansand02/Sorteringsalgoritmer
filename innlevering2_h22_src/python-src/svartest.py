import sys
#Simple program to check if list is 100% sorted, can be run manually through terminal, 
#But also runs automatic on all used algorithms in innlevering2.py

def testRekkefolge(filNavn):
    with open(filNavn,  'r') as fil:
        liste = fil.readlines()
        for tall in liste[1:]:
            if int(tall) < int(liste[liste.index(tall)-1]):
                return(filNavn + " ikke sortert")
        return (filNavn + " sortert")

if __name__ == '__main__':
    testRekkefolge(sys.argv[1])