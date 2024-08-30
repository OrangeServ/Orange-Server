import configparser

# Créer un objet ConfigParser
config = configparser.ConfigParser()

# Définir les sections et les paires clé/valeur
config['Service'] = {
    'Nom': 'Orange',
    'Description': 'Service d\'outils réseaux de pointe',
    'Année de création': '2024'
}

config['Réseau'] = {
    'Surveillance': 'Active',
    'Sécurité': 'Haute',
    'Optimisation de la bande passante': 'Optimisée'
}

config['Support'] = {
    'Assistance technique': '24/7',
    'Maintenance': 'Incluse'
}

# Enregistrer le fichier de configuration
with open('orange_config.ini', 'w') as configfile:
    config.write(configfile)

print("Le fichier de configuration 'orange_config.ini' a été créé avec succès.")
