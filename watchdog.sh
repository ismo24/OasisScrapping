#!/bin/bash

# Nom du script à surveiller
SCRIPT_NAME="Main.py"
# Chemin complet du script à surveiller
SCRIPT_PATH=$(dirname "$0")/$SCRIPT_NAME
# Nom du fichier nohup.out pour enregistrer les logs
LOG_FILE=$(dirname "$0")/nohup.out

# Vérifier si le script est en cours d'exécution
if ! pgrep -f "$SCRIPT_PATH" > /dev/null
then
    # Si le script n'est pas en cours d'exécution, le relancer
    echo "Le script $SCRIPT_NAME n'est pas en cours d'exécution. Redémarrage..."
    nohup python3 "$SCRIPT_PATH" > "$LOG_FILE" 2>&1 &
else
    echo "Le script $SCRIPT_NAME est en cours d'exécution."
fi

