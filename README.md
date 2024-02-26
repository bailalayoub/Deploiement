# Guide de déploiement pour l'application FastAPI sur Google Cloud Platform avec Cloud Run

Ce guide détaille les étapes à suivre pour déployer une application FastAPI sur Google Cloud Platform en utilisant Cloud Run.

## Étapes de préparation

1. **Créer un Dockerfile :**  
   Assurez-vous d'avoir un fichier `Dockerfile` à la racine de votre projet avec le contenu suivant :
   ```
   # Use the official Python image as base image
   FROM python:3.9-slim

   # Set the working directory in the container
   WORKDIR /app

   # Copy the content of the local src directory to the working directory
   COPY . /app

   # Install dependencies
   RUN pip install -r requirement.txt

   # Command to run on container start
   CMD uvicorn main:app --port=8000 --host=0.0.0.0
   ```

2. **Créer un fichier requirement.txt :**  
   Créez un fichier `requirement.txt` à la racine de votre projet avec les dépendances nécessaires pour votre application :
   ```
   fastapi
   uvicorn
   python-multipart
   ```

3. **Créer un repository DockerHub :**  
   Assurez-vous de créer un repository DockerHub pour stocker votre image Docker.

## Déploiement sur DockerHub

1. **Construction de l'image Docker :**  
   Exécutez la commande suivante dans votre terminal pour construire l'image Docker :
   ```
   docker build -t bailalayoub/fastapi-project:1.0.0 .
   ```

2. **Connexion à Docker CLI :**  
   Connectez-vous à Docker CLI en utilisant la commande :
   ```
   docker login
   ```

3. **Pousser l'image Docker :**  
   Poussez l'image Docker dans votre repository DockerHub :
   ```
   docker push bailalayoub/fastapi-project:1.0.0
   ```

## Déploiement sur Cloud Run

1. **Accéder à Google Cloud Console :**  
   Accédez à la console Google Cloud Platform.

2. **Sélectionner Cloud Run :**  
   Sélectionnez "Cloud Run" dans le menu de navigation.

3. **Créer un nouveau service :**  
   Cliquez sur "CREATE SERVICE" et sélectionnez "Deploy one revision from an existing container image".

4. **Spécifier les détails :**  
   - entrer le nom et le tag de l'image Docker que vous avez poussée sur DockerHub.
   - Activez l'option "Allow unauthenticated invocations".
   - Spécifiez le port du conteneur "Container port".
   - Choisissez la capacité nécessaire en termes de mémoire et de CPU.

5. **Déployer :**  
   Cliquez sur "CREATE" pour lancer le déploiement de votre application sur Cloud Run.
