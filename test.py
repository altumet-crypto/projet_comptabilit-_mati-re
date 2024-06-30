import tkinter as tk
from tkinter import ttk, messagebox

# Fonction pour vérifier les informations de connexion
def verifier_connexion():
    username = entry_username.get()
    password = entry_password.get()
    if username == "admin" and password == "password":
        ouvrir_fenetre_principale()
    else:
        messagebox.showerror("Erreur de connexion", "Nom d'utilisateur ou mot de passe incorrect")

# Fonction pour ouvrir la fenêtre principale après la connexion
def ouvrir_fenetre_principale():
    fenetre_connexion.destroy()
    fenetre_principale = tk.Tk()
    fenetre_principale.title("Fenêtre Principale")

    style = ttk.Style(fenetre_principale)
    style.configure("TButton", font=("Helvetica", 16), padding=20, background="#f0f0f0", foreground="#333333")
    style.map("TButton", background=[("active", "#e0e0e0")])

    fenetre_principale.geometry("500x400")
    fenetre_principale.configure(bg="#ffffff")

    btn_matiere = ttk.Button(fenetre_principale, text="Matière", width=20, command=ouvrir_fenetre_article)
    btn_matiere.pack(pady=10)

    btn_solde = ttk.Button(fenetre_principale, text="Solde", width=20, command=ouvrir_fenetre_solde)
    btn_solde.pack(pady=10)

    btn_entrees = ttk.Button(fenetre_principale, text="Entrées", width=20, command=ouvrir_fenetre_entrees)
    btn_entrees.pack(pady=10)

    btn_sorties = ttk.Button(fenetre_principale, text="Sorties", width=20)
    btn_sorties.pack(pady=10)

    fenetre_principale.mainloop()

# Fonction pour ouvrir la fenêtre des articles
def ouvrir_fenetre_article():
    fenetre_article = tk.Toplevel()
    fenetre_article.title("Gestion des Articles")

    style = ttk.Style(fenetre_article)
    style.configure("TButton", font=("Helvetica", 16), padding=20, background="#f0f0f0", foreground="#333333")
    style.map("TButton", background=[("active", "#e0e0e0")])

    fenetre_article.geometry("600x500")
    fenetre_article.configure(bg="#ffffff")

    btn_ajouter = ttk.Button(fenetre_article, text="Ajouter article", width=20, command=ouvrir_fenetre_ajout_article)
    btn_ajouter.pack(pady=10)

    btn_modifier = ttk.Button(fenetre_article, text="Modifier article", width=20)
    btn_modifier.pack(pady=10)

    btn_supprimer = ttk.Button(fenetre_article, text="Supprimer article", width=20)
    btn_supprimer.pack(pady=10)

    btn_consulter = ttk.Button(fenetre_article, text="Consulter les articles", width=20, command=consulter_articles)
    btn_consulter.pack(pady=10)

    fenetre_article.mainloop()

def ouvrir_fenetre_ajout_article():
    fenetre_ajout_article = tk.Toplevel()
    fenetre_ajout_article.title("Ajouter un Article")
    fenetre_ajout_article.geometry("800x400")
    fenetre_ajout_article.configure(bg="#ffffff")

    # Frame pour le tableau à gauche et les champs de saisie à droite
    frame_principal = tk.Frame(fenetre_ajout_article, bg="#ffffff")
    frame_principal.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

    # Tableau à gauche
    columns = ("Code Article", "Désignation", "Catégorie", "LPC")
    tree = ttk.Treeview(frame_principal, columns=columns, show="headings", height=10)

    # Configuration des colonnes du tableau
    tree.heading("Code Article", text="Code Article")
    tree.heading("Désignation", text="Désignation")
    tree.heading("Catégorie", text="Catégorie")
    tree.heading("LPC", text="LPC")

    # Exemple d'articles fictifs pour le tableau
    articles = [
        ("001", "Article 1", "Catégorie A", "LPC1"),
        ("002", "Article 2", "Catégorie B", "LPC2"),
        ("003", "Article 3", "Catégorie C", "LPC3")
    ]

    for article in articles:
        tree.insert("", tk.END, values=article)

    tree.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill=tk.BOTH)

    # Frame pour les champs de saisie à droite
    frame_saisie = tk.Frame(frame_principal, bg="#ffffff")
    frame_saisie.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH)

    # Labels et champs de saisie pour les attributs
    label_code = ttk.Label(frame_saisie, text="Code Article:")
    label_code.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

    entry_code = ttk.Entry(frame_saisie, width=30)
    entry_code.grid(row=0, column=1, padx=10, pady=10)

    label_designation = ttk.Label(frame_saisie, text="Désignation:")
    label_designation.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

    entry_designation = ttk.Entry(frame_saisie, width=30)
    entry_designation.grid(row=1, column=1, padx=10, pady=10)

    label_categorie = ttk.Label(frame_saisie, text="Catégorie:")
    label_categorie.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

    entry_categorie = ttk.Entry(frame_saisie, width=30)
    entry_categorie.grid(row=2, column=1, padx=10, pady=10)

    label_lpc = ttk.Label(frame_saisie, text="LPC:")
    label_lpc.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

    entry_lpc = ttk.Entry(frame_saisie, width=30)
    entry_lpc.grid(row=3, column=1, padx=10, pady=10)

    # Bouton Ajouter
    btn_ajouter = ttk.Button(frame_saisie, text="Ajouter", command=lambda: ajouter_article(
        entry_code.get(), entry_designation.get(), entry_categorie.get(), entry_lpc.get(), tree))
    btn_ajouter.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    # Fonction pour ajouter un article au tableau
    def ajouter_article(code, designation, categorie, lpc, tree):
        if code and designation and categorie and lpc:
            tree.insert("", tk.END, values=(code, designation, categorie, lpc))
            # Optionnel: Réinitialiser les champs de saisie après ajout
            entry_code.delete(0, tk.END)
            entry_designation.delete(0, tk.END)
            entry_categorie.delete(0, tk.END)
            entry_lpc.delete(0, tk.END)
        else:
            messagebox.showwarning("Champs manquants", "Veuillez remplir tous les champs.")

    fenetre_ajout_article.mainloop()


# Fonction pour consulter les articles
def consulter_articles():
    fenetre_consulter = tk.Toplevel()
    fenetre_consulter.title("Liste des Articles")
    fenetre_consulter.geometry("800x400")
    fenetre_consulter.configure(bg="#ffffff")

    columns = ("code", "designation", "categorie", "lpc")
    tree = ttk.Treeview(fenetre_consulter, columns=columns, show="headings")

    tree.heading("code", text="Code Article")
    tree.heading("designation", text="Désignation")
    tree.heading("categorie", text="Catégorie")
    tree.heading("lpc", text="LPC")

    # Ajouter des articles fictifs pour exemple
    articles = [
        ("001", "Article 1", "Catégorie A", "LPC1"),
        ("002", "Article 2", "Catégorie B", "LPC2"),
        ("003", "Article 3", "Catégorie C", "LPC3")
    ]

    for article in articles:
        tree.insert("", tk.END, values=article)

    tree.pack(expand=True, fill=tk.BOTH)

# Fonction pour ouvrir la fenêtre des soldes avec calendrier des mois
def ouvrir_fenetre_solde():
    fenetre_solde = tk.Toplevel()
    fenetre_solde.title("Solde des Matières")
    fenetre_solde.geometry("800x400")
    fenetre_solde.configure(bg="#ffffff")

    # Création d'une grille pour les boutons des mois
    mois = [
        "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
        "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"
    ]

    row = 0
    col = 0
    for m in mois:
        btn = ttk.Button(fenetre_solde, text=m, width=10, command=lambda m=m: afficher_solde_mois(m))
        btn.grid(row=row, column=col, padx=10, pady=10)
        col += 1
        if col > 3:  # Passer à la ligne suivante après 4 boutons
            col = 0
            row += 1

def afficher_solde_mois(mois):
    fenetre_solde_mois = tk.Toplevel()
    fenetre_solde_mois.title(f"Solde des Matières pour {mois}")
    fenetre_solde_mois.geometry("800x400")
    fenetre_solde_mois.configure(bg="#ffffff")

    columns = ("code_matiere", "quantite_initiale", "valeur_initiale", "quantite_finale", "valeur_finale")
    tree = ttk.Treeview(fenetre_solde_mois, columns=columns, show="headings")

    tree.heading("code_matiere", text="Code Matière")
    tree.heading("quantite_initiale", text="Quantité Solde Initiale")
    tree.heading("valeur_initiale", text="Valeur Solde Initiale")
    tree.heading("quantite_finale", text="Quantité Solde Finale")
    tree.heading("valeur_finale", text="Valeur Solde Finale")

    # Ajouter des soldes fictifs pour exemple
    soldes = [
        ("M001", 100, 5000, 80, 4000),
        ("M002", 200, 10000, 150, 7500),
        ("M003", 300, 15000, 250, 12500)
    ]

    for solde in soldes:
        tree.insert("", tk.END, values=solde)

    tree.pack(expand=True, fill=tk.BOTH)

def ouvrir_fenetre_entrees():
    fenetre_entrees = tk.Toplevel()
    fenetre_entrees.title("Gestion des Entrées")
    fenetre_entrees.geometry("400x200")
    fenetre_entrees.configure(bg="#ffffff")

    # Frame pour les boutons
    frame_boutons = tk.Frame(fenetre_entrees, bg="#ffffff")
    frame_boutons.pack(expand=True, padx=20, pady=20)

    # Bouton Consulter les entrées
    btn_consulter = ttk.Button(frame_boutons, text="Consulter les entrées", width=20, command=consulter_entrees)
    btn_consulter.grid(row=0, column=0, padx=10, pady=10)

    # Bouton Ajouter entrée
    btn_ajouter = ttk.Button(frame_boutons, text="Ajouter entrée", width=20, command=ajouter_entree)
    btn_ajouter.grid(row=0, column=1, padx=10, pady=10)

    fenetre_entrees.mainloop()

def consulter_entrees():
    # Ici vous pouvez implémenter la fonction pour consulter les entrées existantes
    pass

def ajouter_entree():
    # Ici vous pouvez implémenter la fonction pour ajouter une nouvelle entrée
    pass



# Création de la fenêtre de connexion
fenetre_connexion = tk.Tk()
fenetre_connexion.title("Connexion")

style = ttk.Style(fenetre_connexion)
style.configure("TLabel", font=("Helvetica", 16), background="#ffffff", foreground="#333333")
style.configure("TEntry", font=("Helvetica", 16), padding=5)
style.configure("TButton", font=("Helvetica", 16), padding=20, background="#f0f0f0", foreground="#333333")
style.map("TButton", background=[("active", "#e0e0e0")])

fenetre_connexion.geometry("400x300")
fenetre_connexion.configure(bg="#ffffff")

label_username = ttk.Label(fenetre_connexion, text="Nom d'utilisateur:")
label_username.pack(pady=10)
entry_username = ttk.Entry(fenetre_connexion, width=30)
entry_username.pack(pady=10)

label_password = ttk.Label(fenetre_connexion, text="Mot de passe:")
label_password.pack(pady=10)
entry_password = ttk.Entry(fenetre_connexion, show="*", width=30)
entry_password.pack(pady=10)

btn_connexion = ttk.Button(fenetre_connexion, text="Connexion", command=verifier_connexion)
btn_connexion.pack(pady=20)

fenetre_connexion.mainloop()
