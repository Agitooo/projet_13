.. OCLettings documentation master file, created by
   sphinx-quickstart on Tue Oct 31 14:38:08 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to OCLettings's documentation!
======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Guide de Développement OCLettings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. contents:: Table des matières

Résumé
======

Ce guide explique la configuration et le développement du site web Orange County Lettings

Ce projet es la version améliore du projet "Python OC Lettings FR", qui est sur GitHub a l'adresse : https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git.

Les améliorations sont :

1. **Refactorisation de la dette technique :** Reduction la dette technique et amelioration de la qualité globale du code.

2. **Refactorisation de l'architecture modulaire :** L'architecture du projet a été repensée pour être plus modulaire, afin de faciliter la maintenance, l'extension et la compréhension du code.

3. **Surveillance des applications et des erreurs via Sentry :** L'intégration de Sentry permet une surveillance proactive des erreurs et des performances de l'application, offrant ainsi une meilleure visibilité sur les problèmes potentiels.

4. **Pipeline CI/CD utilisant CircleCI :** Un pipeline de CI/CD (Intégration Continue / Déploiement Continu) a été mis en place en utilisant CircleCI. Cela garantit des tests automatisés et un déploiement en continu du code.

5. **Déploiement sur DigitalOcean :** L'application est déployée sur la plateforme DigitalOcean, ce qui la rend accessible au public sur internet.

Ce guide vous accompagnera tout au long du processus pour que vous puissiez tirer pleinement parti de ces améliorations dans le cadre de votre développement avec Django.

Cloner le dépôt
~~~~~~~~~~~~~~~

.. code-block:: shell

   git clone https://github.com/Agitooo/projet_13.git

Créer l'environnement virtuel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   cd /chemin/vers/projet/
   python -m venv venv

Activer l'environnement
~~~~~~~~~~~~~~~~~~~~~~~

**Windows**

.. code-block:: shell

   venv\Scripts\activate

**MacOS and Linux**

.. code-block:: shell

   source venv/bin/activate

Désactiver l'environnement
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   deactivate

Exécuter le site
~~~~~~~~~~~~~~~~~

.. code-block:: shell

   cd /chemin/vers/projet/
   source venv/bin/activate
   pip install -r requirements.txt
   python manage.py runserver

Linting
-------

**Flake8**

.. code-block:: shell

   cd /chemin/vers/projet/
   source venv/bin/activate
   flake8

**Tests unitaires**

.. code-block:: shell

   cd /chemin/vers/projet/
   source venv/bin/activate
   pytest

Panel d'administration
----------------------

- Ouvrez http://localhost:8000 dans un navigateur pour vérifier que le site fonctionne correctement.
- Accédez au panel d'administration en ouvrant http://localhost:8000/admin dans un navigateur.
- Connectez-vous avec l'utilisateur admin et le mot de passe Abc1234!

Déploiement
===========

Le déploiement nécessite :

- Compte CircleCi
- Compte Docker
- Compte DigitalOcean
- Compte Sentry

Le déploiement est géré par le fichier ``config.yml`` présent dans le dossier ``./.circleci``.
Ce fichier est déclenché lors d'un push vers le dépôt GitHub. Un push sur la branche ``main`` déclenche les
tests pytest et flake8.
Ensuite, l'application est conteneurisée avec Docker et déployée en ligne via DigitalOcean.

URL de l'application en ligne : https://ocl-app-yvnhl.ondigitalocean.app/

Dans le dépôt CircleCi, configurez les variables d'environnement (Project Settings > Environment Variables) :

- ``DO_REGISTRY`` : Votre registry de DigitalOcean
- ``DO_API_TOKEN`` : Votre token de DigitalOcean
- ``DROPLET_USER`` Nom du user sur votre machine DigitalOcean
- ``DROPLET_IP`` : Adresse IP de votre Droplet de DigitalOcean
- ``PORT`` : Port sur lequel sera votre application sur la machine de DigitalOcean
