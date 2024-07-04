import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# État des mois (ouvert ou fermé)
etat_mois = {mois: "Fermé" for mois in [
    "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
    "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"
]}

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

    btn_matiere = ttk.Button(fenetre_principale, text="Article", width=20, command=ouvrir_fenetre_article)
    btn_matiere.pack(pady=10)

    btn_solde = ttk.Button(fenetre_principale, text="Solde", width=20, command=ouvrir_fenetre_solde)
    btn_solde.pack(pady=10)

    btn_solde = ttk.Button(fenetre_principale, text="Bon", width=20)
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

    btn_modifier = ttk.Button(fenetre_article, text="Modifier article", width=20, command=ouvrir_fenetre_modification)
    btn_modifier.pack(pady=10)

    btn_supprimer = ttk.Button(fenetre_article, text="Supprimer article", width=20, command=ouvrir_fenetre_suppression)
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

    # Fonction pour ajouter un article au tableau et à la base de données
    def ajouter_article(code, designation, categorie, lpc, tree):
        # Créer une connexion à la base de données SQLite
        conn = sqlite3.connect('comptabilit_matiere.db')
        cursor = conn.cursor()
        if code and designation and categorie and lpc:
            # Insérer l'article dans la base de données
            try:
                cursor.execute("INSERT INTO Article (code_article, Designation, Categorie, LPC) VALUES (?, ?, ?, ?)",
                            (code, designation, categorie, lpc))
                conn.commit()
                # Ajouter l'article au tableau
                tree.insert("", tk.END, values=(code, designation, categorie, lpc))
                # Réinitialiser les champs de saisie après ajout
                entry_code.delete(0, tk.END)
                entry_designation.delete(0, tk.END)
                entry_categorie.delete(0, tk.END)
                entry_lpc.delete(0, tk.END)
            except sqlite3.IntegrityError:
                messagebox.showerror("Erreur", "Un article avec ce code existe déjà.")
        else:
            messagebox.showwarning("Champs manquants", "Veuillez remplir tous les champs.")
        
        # Fermer la connexion à la base de données à la fin de l'application
        conn.close()

    # Fonction pour charger les articles existants dans le tableau
    def charger_articles(tree):
        # Créer une connexion à la base de données SQLite
        conn = sqlite3.connect('comptabilit_matiere.db')
        cursor = conn.cursor()

        # Supprimer les articles actuels du tableau
        for item in tree.get_children():
            tree.delete(item)

        # Récupérer tous les articles de la base de données
        cursor.execute("SELECT code_article, Designation, Categorie, LPC FROM Article")
        articles = cursor.fetchall()

        # Insérer les articles dans le tableau
        for article in articles:
            tree.insert("", tk.END, values=article)

        # Fermer la connexion à la base de données
        conn.close()

    # Charger les articles existants lors de l'ouverture de la fenêtre
    charger_articles(tree)

   

    


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

    tree.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

    # Fonction pour charger les articles depuis la base de données
    def charger_articles(tree):
        # Créer une connexion à la base de données SQLite
        conn = sqlite3.connect('comptabilit_matiere.db')
        cursor = conn.cursor()

        # Supprimer les articles actuels du tableau
        for item in tree.get_children():
            tree.delete(item)

        # Récupérer tous les articles de la base de données
        cursor.execute("SELECT code_article, Designation, Categorie, LPC FROM Article")
        articles = cursor.fetchall()

        # Insérer les articles dans le tableau
        for article in articles:
            tree.insert("", tk.END, values=article)

        # Fermer la connexion à la base de données
        conn.close()

    # Charger les articles existants lors de l'ouverture de la fenêtre
    charger_articles(tree)


# Fonction pour supprimer un article
def ouvrir_fenetre_suppression():
    fenetre_suppression = tk.Toplevel()
    fenetre_suppression.title("Supprimer un Article")
    fenetre_suppression.geometry("400x200")
    fenetre_suppression.configure(bg="#ffffff")

    # Label et combobox pour le code article
    label_code = ttk.Label(fenetre_suppression, text="Code Article:")
    label_code.pack(pady=10)
    
    # Créer un combobox pour les codes d'articles
    combobox_code = ttk.Combobox(fenetre_suppression, width=30)
    combobox_code.pack(pady=10)

    # Charger les codes d'articles depuis la base de données
    def charger_codes_articles():
        # Créer une connexion à la base de données SQLite
        conn = sqlite3.connect('comptabilit_matiere.db')
        cursor = conn.cursor()

        # Récupérer tous les codes d'articles de la base de données
        cursor.execute("SELECT code_article FROM Article")
        codes = [row[0] for row in cursor.fetchall()]

        # Ajouter les codes au combobox
        combobox_code['values'] = codes

        # Fermer la connexion à la base de données
        conn.close()

    # Charger les codes d'articles existants lors de l'ouverture de la fenêtre
    charger_codes_articles()

    # Fonction pour supprimer l'article
    def supprimer_article():
        code_article = combobox_code.get()
        if code_article:
            # Créer une connexion à la base de données SQLite
            conn = sqlite3.connect('comptabilit_matiere.db')
            cursor = conn.cursor()
            try:
                # Supprimer l'article de la base de données
                cursor.execute("DELETE FROM Article WHERE code_article = ?", (code_article,))
                if cursor.rowcount == 0:
                    messagebox.showwarning("Article non trouvé", "Aucun article trouvé avec ce code.")
                else:
                    conn.commit()
                    messagebox.showinfo("Succès", f"L'article avec le code {code_article} a été supprimé.")
                    # Mettre à jour les codes dans le combobox
                    charger_codes_articles()
            except sqlite3.Error as e:
                messagebox.showerror("Erreur", f"Erreur lors de la suppression de l'article: {e}")
            finally:
                # Fermer la connexion à la base de données
                conn.close()
        else:
            messagebox.showwarning("Champ vide", "Veuillez entrer un code article.")

    # Bouton Supprimer
    btn_supprimer = ttk.Button(fenetre_suppression, text="Supprimer", command=supprimer_article)
    btn_supprimer.pack(pady=20)


# Fonction pour modifier un article
def ouvrir_fenetre_modification():
    fenetre_modification = tk.Toplevel()
    fenetre_modification.title("Modifier un Article")
    fenetre_modification.geometry("400x300")
    fenetre_modification.configure(bg="#ffffff")

    # Label et combobox pour le code article
    label_code = ttk.Label(fenetre_modification, text="Code Article:")
    label_code.pack(pady=10)
    
    # Créer un combobox pour les codes d'articles
    combobox_code = ttk.Combobox(fenetre_modification, width=30)
    combobox_code.pack(pady=10)

    # Charger les codes d'articles depuis la base de données
    def charger_codes_articles():
        # Créer une connexion à la base de données SQLite
        conn = sqlite3.connect('comptabilit_matiere.db')
        cursor = conn.cursor()

        # Récupérer tous les codes d'articles de la base de données
        cursor.execute("SELECT code_article FROM Article")
        codes = [row[0] for row in cursor.fetchall()]

        # Ajouter les codes au combobox
        combobox_code['values'] = codes

        # Fermer la connexion à la base de données
        conn.close()

    # Charger les codes d'articles existants lors de l'ouverture de la fenêtre
    charger_codes_articles()

    # Labels et champs de saisie pour les attributs
    label_designation = ttk.Label(fenetre_modification, text="Désignation:")
    label_designation.pack(pady=5)
    entry_designation = ttk.Entry(fenetre_modification, width=30)
    entry_designation.pack(pady=5)

    label_categorie = ttk.Label(fenetre_modification, text="Catégorie:")
    label_categorie.pack(pady=5)
    entry_categorie = ttk.Entry(fenetre_modification, width=30)
    entry_categorie.pack(pady=5)

    label_lpc = ttk.Label(fenetre_modification, text="LPC:")
    label_lpc.pack(pady=5)
    entry_lpc = ttk.Entry(fenetre_modification, width=30)
    entry_lpc.pack(pady=5)

    # Fonction pour charger les détails de l'article sélectionné
    def charger_details_article(event):
        code_article = combobox_code.get()
        if code_article:
            # Créer une connexion à la base de données SQLite
            conn = sqlite3.connect('comptabilit_matiere.db')
            cursor = conn.cursor()

            # Récupérer les détails de l'article
            cursor.execute("SELECT Designation, Categorie, LPC FROM Article WHERE code_article = ?", (code_article,))
            article = cursor.fetchone()

            if article:
                entry_designation.delete(0, tk.END)
                entry_designation.insert(0, article[0])
                entry_categorie.delete(0, tk.END)
                entry_categorie.insert(0, article[1])
                entry_lpc.delete(0, tk.END)
                entry_lpc.insert(0, article[2])

            # Fermer la connexion à la base de données
            conn.close()

    # Lier l'événement de sélection du combobox au chargement des détails
    combobox_code.bind("<<ComboboxSelected>>", charger_details_article)

    # Fonction pour modifier l'article
    def modifier_article():
        code_article = combobox_code.get()
        designation = entry_designation.get()
        categorie = entry_categorie.get()
        lpc = entry_lpc.get()

        if code_article and designation and categorie and lpc:
            # Créer une connexion à la base de données SQLite
            conn = sqlite3.connect('comptabilit_matiere.db')
            cursor = conn.cursor()
            try:
                # Mettre à jour l'article dans la base de données
                cursor.execute("UPDATE Article SET Designation = ?, Categorie = ?, LPC = ? WHERE code_article = ?",
                               (designation, categorie, lpc, code_article))
                conn.commit()
                messagebox.showinfo("Succès", f"L'article avec le code {code_article} a été modifié.")
                # Réinitialiser les champs de saisie après modification
                entry_designation.delete(0, tk.END)
                entry_categorie.delete(0, tk.END)
                entry_lpc.delete(0, tk.END)
                charger_codes_articles()
            except sqlite3.Error as e:
                messagebox.showerror("Erreur", f"Erreur lors de la modification de l'article: {e}")
            finally:
                # Fermer la connexion à la base de données
                conn.close()
        else:
            messagebox.showwarning("Champs manquants", "Veuillez remplir tous les champs.")

    # Bouton Modifier
    btn_modifier = ttk.Button(fenetre_modification, text="Modifier", command=modifier_article)
    btn_modifier.pack(pady=20)


    

# Fonction pour ouvrir la fenêtre des soldes
def ouvrir_fenetre_solde():
    fenetre_solde = tk.Toplevel()
    fenetre_solde.title("Gestion des Soldes")
    fenetre_solde.geometry("400x200")
    fenetre_solde.configure(bg="#ffffff")

    # Frame pour les boutons
    frame_boutons = tk.Frame(fenetre_solde, bg="#ffffff")
    frame_boutons.pack(expand=True, padx=20, pady=20)

    # Bouton Consulter solde
    btn_consulter = ttk.Button(frame_boutons, text="Consulter solde", width=20, command=consulter_solde)
    btn_consulter.pack(pady=10)

    # Bouton Ouvrir/Clôturer
    btn_ouvrir_cloturer = ttk.Button(frame_boutons, text="Ouvrir/Clôturer", width=20, command=ouvrir_cloturer)
    btn_ouvrir_cloturer.pack(pady=10)

    # Stock Magasin
    btn_consulter = ttk.Button(frame_boutons, text="Stock Magasin", width=20)
    btn_consulter.pack(pady=10)

    # Bouton Stock REBUTE
    btn_consulter = ttk.Button(frame_boutons, text="Stock Rebuté", width=20)
    btn_consulter.pack(pady=10)

    fenetre_solde.mainloop()

# Liste pour stocker les boutons des mois
buttons = []

# Fonction pour ouvrir/clôturer les soldes
def ouvrir_cloturer():
    global buttons  # Référence globale aux boutons des mois
    fenetre_ouvrir_cloturer = tk.Toplevel()
    fenetre_ouvrir_cloturer.title("Ouvrir/Clôturer les Soldes")
    fenetre_ouvrir_cloturer.geometry("400x400")
    fenetre_ouvrir_cloturer.configure(bg="#ffffff")

    # Création d'une grille pour les boutons des mois
    row = 0
    col = 0
    for m in etat_mois.keys():
        etat = etat_mois[m]
        btn_text = f"{m} ({etat})"
        btn = ttk.Button(fenetre_ouvrir_cloturer, text=btn_text, width=15, command=lambda m=m: toggle_mois(m))
        btn.grid(row=row, column=col, padx=10, pady=10)
        buttons.append(btn)  # Ajouter le bouton à la liste
        col += 1
        if col > 2:  # Passer à la ligne suivante après 3 boutons
            col = 0
            row += 1
# Suivi des boutons par mois
buttons = []
# Fonction pour basculer l'état d'un mois
def toggle_mois(mois):
    if etat_mois[mois] == "Fermé":
        etat_mois[mois] = "Ouvert"
        messagebox.showinfo("Mois Ouvert", f"Le mois de {mois} est maintenant ouvert.")
    else:
        etat_mois[mois] = "Fermé"
        messagebox.showinfo("Mois Fermé", f"Le mois de {mois} est maintenant fermé.")
    # Mettre à jour le texte du bouton correspondant au mois
    update_button_text(mois)

def update_button_text(mois):
    global buttons  # Référence globale aux boutons des mois

    for btn in buttons:
        if btn.cget("text").startswith(mois):
            new_text = f"{mois} ({etat_mois[mois]})"
            btn.config(text=new_text)
            break


# Fonction pour consulter les soldes avec calendrier des mois
def consulter_solde():
    fenetre_solde = tk.Toplevel()
    fenetre_solde.title("Solde des Matières")
    fenetre_solde.geometry("800x400")
    fenetre_solde.configure(bg="#ffffff")

    # Création d'une grille pour les boutons des mois
    row = 0
    col = 0
    for m in etat_mois.keys():
        etat = etat_mois[m]
        state = tk.DISABLED if etat == "Fermé" else tk.NORMAL
        btn = ttk.Button(fenetre_solde, text=m, width=10, state=state, command=lambda m=m: afficher_solde_mois(m))
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


# Fonction pour ouvrir la fenêtre des entrées
def ouvrir_fenetre_entrees():
    fenetre_entrees = tk.Toplevel()
    fenetre_entrees.title("Gestion des Entrées")
    fenetre_entrees.geometry("400x200")
    fenetre_entrees.configure(bg="#ffffff")

    # Frame pour les boutons
    frame_boutons = tk.Frame(fenetre_entrees, bg="#ffffff")
    frame_boutons.pack(expand=True, padx=20, pady=20)

    # Bouton Consulter entrées
    btn_consulter = ttk.Button(frame_boutons, text="Consulter entrées", width=20)
    btn_consulter.grid(row=0, column=0, padx=10, pady=10)

    # Bouton Ajouter entrée
    btn_ajouter = ttk.Button(frame_boutons, text="Ajouter entrée", width=20, command=afficher_fenetre_entrees)
    btn_ajouter.grid(row=0, column=1, padx=10, pady=10)

def afficher_fenetre_entrees():
    fenetre_entrees = tk.Tk()
    fenetre_entrees.title("Gestion des Entrées")
    fenetre_entrees.geometry("1000x600")
    fenetre_entrees.configure(bg="#ffffff")

    # Tableau pour afficher les données
    columns = ("code_entre", "quantite_entre", "valeur_entre", "date", "code_article", "code_br")
    tree = ttk.Treeview(fenetre_entrees, columns=columns, show="headings")

    # Configuration des colonnes du tableau
    for col in columns:
        tree.heading(col, text=col.replace("_", " ").capitalize())
        tree.column(col, width=150)
    conn = sqlite3.connect("comptabilit_matiere.db")
    cursor = conn.cursor()

    # Charger les données de la base de données
    cursor.execute("SELECT code_entre, quantite_entre, valeur_entre, date, code_article, code_br FROM Entree")
    entrees = cursor.fetchall()

    for entree in entrees:
        tree.insert("", tk.END, values=entree)

    tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Frame pour les champs de saisie et le bouton Ajouter
    frame_ajout = tk.Frame(fenetre_entrees, bg="#ffffff")
    frame_ajout.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

    # Labels et champs de saisie pour les attributs
    labels_text = ["Code Entrée", "Quantité Entrée", "Valeur Entrée", "Date", "Code Article", "Code BR"]
    entries = {}

    for idx, text in enumerate(labels_text):
        label = ttk.Label(frame_ajout, text=text + ":")
        label.grid(row=idx, column=0, padx=10, pady=5, sticky=tk.W)
        entry = ttk.Entry(frame_ajout, width=30)
        entry.grid(row=idx, column=1, padx=10, pady=5)
        entries[text] = entry

    # Fonction pour ajouter une entrée à la base de données et au tableau
    def ajouter_entree():
        code_entre = entries["Code Entrée"].get()
        quantite_entre = entries["Quantité Entrée"].get()
        valeur_entre = entries["Valeur Entrée"].get()
        date = entries["Date"].get()
        code_article = entries["Code Article"].get()
        code_br = entries["Code BR"].get()

        if code_entre and quantite_entre and valeur_entre and date and code_article and code_br:
            try:
                conn = sqlite3.connect("comptabilit_matiere.db")
                cursor = conn.cursor()
                cursor.execute("INSERT INTO Entree (code_entre, quantite_entre, valeur_entre, date, code_article, code_br) VALUES (?, ?, ?, ?, ?, ?)",
                               (code_entre, quantite_entre, valeur_entre, date, code_article, code_br))
                conn.commit()
                # Ajouter l'entrée au tableau
                tree.insert("", tk.END, values=(code_entre, quantite_entre, valeur_entre, date, code_article, code_br))
                # Réinitialiser les champs de saisie après ajout
                for entry in entries.values():
                    entry.delete(0, tk.END)
            except sqlite3.IntegrityError:
                messagebox.showerror("Erreur", "Une entrée avec ce code existe déjà.")
        else:
            messagebox.showwarning("Champs manquants", "Veuillez remplir tous les champs.")
    conn.close()
    # Bouton Ajouter
    btn_ajouter = ttk.Button(frame_ajout, text="Ajouter", command=ajouter_entree)
    btn_ajouter.grid(row=len(labels_text), column=0, columnspan=2, padx=10, pady=10)

 



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
