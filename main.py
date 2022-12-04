import csv

def getTitles(row):
    """
        Cette fonction est appelée pour nettoyer une ligne de titre dans le CSV
        et l'ajouter à la liste de données.
    """
    
    thisRow = [] # Contiendra la ligne nettoyée

    ## Nettoyer la rangée et l'ajouter à la liste thisRow
    thisRow.append(row[0])
    thisRow.append(row[2] + ' + ' + row[3])
    thisRow.append(row[4])

    ## Placez la nouvelle ligne nettoyée (thisRow) dans la liste de données
    titles.append(thisRow)

def getRow(row):
    """
        Cette fonction est appelée pour nettoyer une ligne de données du CSV 
        et l'ajouter à la liste de données.
    """

    ## Vérifiez si la ligne n'a pas de valeurs manquantes.
    if row[0]!='' and row[2]!='' and row[3]!='' and row[4]!='':

        ## Vérifiez si les valeurs des colonnes de consommation sont des nombres.
        try:
            
            thisRow = [] # Contiendra la ligne nettoyée

            ## Dire à Python que ces valeurs sont des nombres flottants et non des chaînes de caractères.
            r2 = row[2].replace(',','.')
            r3 = row[3].replace(',','.')

            ## Nettoie la rangée et l'ajouter à la liste thisRow
            c = float(r2) + float(r3)
            thisRow.append(row[0])
            thisRow.append(c)
            thisRow.append(row[4])

            ## Place la nouvelle ligne nettoyée (thisRow) dans la liste de données.
            data.append(thisRow)

        ## Si les valeurs ne sont pas des chiffres, nous ne les utilisons pas.
        except:
            pass


data = [] # Cette liste stockera toutes les données, sauf les titres du fichier CSV.
titles = [] # Cette liste stockera les titres du fichier CSV.

with open('conso-annuelles_v1.csv') as file:
    reader = csv.reader(file, delimiter=';')
    """
        Ouvrir le fichier CSV et le lire
    """
    rowCounter = 0 # compte les lignes du fichier CSV
    
    for row in reader:
        """
            Prends chaque ligne, les nettoie et les ajoutes à la liste des données.
        """
        if rowCounter == 0:
            getTitles(row) # Ajouter des titres propres à la liste de données
        else:
            getRow(row) # Ajouter les données propres à la liste des données

        rowCounter += 1

with open('conso-clean.csv', 'w') as newFile:
    writer = csv.writer(newFile, delimiter=';')
    """
        Créez un nouveau fichier CSV vide et écrit
    """
    for row in titles:
        """
            Écrire les titres dans le nouveau fichier CSV
        """
        writer.writerow(row)
    
    while data != []:
        """
            La liste des données est vidée au fur et à mesure que nous ajoutons des données dans le nouveau fichier CSV.
            Donc, si la liste est vide, nous avons terminé. !
        """
        rowCounter = 0 # comptera les lignes de la liste de données
        thisType = "" # Contiendra le type de données sur lesquelles nous travaillons.
        dataType = [] # Contiendra toutes les données ayant le même type : thisType
        
        for row in data:
            """
                Regarde dans la liste des données
            """
            if rowCounter == 0:
                """
                    Si la ligne est une donnée, on enregistre son type et on le met dans la liste dataType.
                    nous le mettons dans la liste dataType
                """
                thisType = row[2]
                dataType.append(row)
                
            elif rowCounter > 0 and row[2] == thisType:
                """
                    Ensuite, si la rangée est une donnée et a le même type que la première, nous l'ajoutons à la liste dataType.
                """
                dataType.append(row)
                
            rowCounter += 1
            
        while dataType != []:
            """
                Une fois que la liste des dataType est totalement remplie, nous ordonnons les données par
                consommation (de la plus élevée à la plus faible) et nous les écrivons dans le nouveau fichier CSV.
                
                Comme précédemment, la liste dataType est vidée au fur et à mesure que nous ajoutons des données dans le nouveau fichier CSV.
                nouveau fichier CSV. Donc si la liste est vide, nous avons terminé !
            """
            cMax = 0.0 # Contient la valeur de la consommation maximale
            
            for row in dataType:
                """
                    Détermine la valeur de consommation la plus élevée
                """
                if cMax < row[1]:
                    cMax = row[1]
                    
            for row in dataType:
                """
                    Ajoute les données ayant la valeur de consommation la plus élevée au CSV
                    et les retire des listes de type de données et de données.
                    Retire également les titres de la liste de données.
                """
                if row[1] >= cMax:
                    writer.writerow(row)
                    dataType.remove(row)
                    data.remove(row)

        "print(data)"
