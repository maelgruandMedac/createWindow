from setuptools import setup, find_packages # type: ignore

setup(
    name="windowTkinter",  # Nom de ton module
    version="0.1",         # Version de ton module
    packages=find_packages(),  # Recherche tous les packages dans ton projet
    py_modules=["windowTk"],
    install_requires=[],    # Liste des dépendances (laisses vide si aucune)
    author="Mael",      # Ton nomz
    author_email="maelgruand23@gmail.com",  # Ton email
    description="Un module simple pour créer des fenêtres Tkinter",
    long_description=open('README.md').read(),  # Lire la description longue du module depuis le README
    long_description_content_type="text/markdown",  # Type du contenu du README
    classifiers=[          # Liste des classificateurs pour PyPI
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Adapté à la licence de ton choix
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Version Python minimale requise
)
