import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from PIL import Image, ImageTk



# Fonction pour vérifier les informations de connexion
def verifier_connexion():
    username = entry_username.get()
    password = entry_password.get()
    if username == "" and password == "":
        ouvrir_fenetre_principale()
    else:
        messagebox.showerror("Erreur de connexion", "Nom d'utilisateur ou mot de passe incorrect", parent=fenetre_connexion)

# Fonction pour ouvrir la fenêtre principale après la connexion
def ouvrir_fenetre_principale():
    fenetre_connexion.destroy()
    fenetre_principale = tk.Tk()
    fenetre_principale.title("Fenêtre Principale")



    style = ttk.Style(fenetre_principale)
    style.configure("TButton", font=("Helvetica", 16), padding=20, background="#f0f0f0", foreground="#333333")
    style.map("TButton", background=[("active", "#e0e0e0")])

    fenetre_principale.geometry("800x800")
    fenetre_principale.configure(bg="#ffffff")

    btn_matiere = ttk.Button(fenetre_principale, text="Article", width=20, command=ouvrir_fenetre_article)
    btn_matiere.pack(pady=10)

    btn_solde = ttk.Button(fenetre_principale, text="Solde", width=20, command=ouvrir_fenetre_solde)
    btn_solde.pack(pady=10)

    btn_solde = ttk.Button(fenetre_principale, text="Bon", width=20, command=ouvrir_fenetre_bon)
    btn_solde.pack(pady=10)

    btn_entrees = ttk.Button(fenetre_principale, text="Entrées", width=20, command=ouvrir_fenetre_entrees)
    btn_entrees.pack(pady=10)

    btn_sorties = ttk.Button(fenetre_principale, text="Sorties", width=20, command=ouvrir_fenetre_sortie)
    btn_sorties.pack(pady=10)

    fenetre_principale.mainloop()

#############################    ARTICLES ARTICLES ARTICLES ######################################################### 

 

def ouvrir_fenetre_article():
    fenetre_article = tk.Toplevel()
    fenetre_article.title("Gestion des Articles")

    style = ttk.Style(fenetre_article)
    style.configure("TButton", font=("Helvetica", 16), padding=20, background="#f0f0f0", foreground="#333333")
    style.map("TButton", background=[("active", "#e0e0e0")])

    fenetre_article.geometry("800x800")
    fenetre_article.configure(bg="#ffffff")

    btn_ajouter = ttk.Button(fenetre_article, text="Ajouter article", width=20, command=ouvrir_fenetre_ajout_article)
    btn_ajouter.pack(pady=10)

    btn_modifier = ttk.Button(fenetre_article, text="Modifier article", width=20, command=ouvrir_fenetre_modification)
    btn_modifier.pack(pady=10)

    btn_supprimer = ttk.Button(fenetre_article, text="Supprimer article", width=20, command=ouvrir_fenetre_suppression)
    btn_supprimer.pack(pady=10)

    btn_consulter = ttk.Button(fenetre_article, text="Consulter les articles", width=20, command=consulter_articles)
    btn_consulter.pack(pady=10)

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


def ouvrir_fenetre_ajout_article():
    fenetre_ajout_article = tk.Toplevel()
    fenetre_ajout_article.title("Ajouter un Article")
    fenetre_ajout_article.geometry("1200x800")
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

    
    # Charger les articles existants lors de l'ouverture de la fenêtre
    charger_articles(tree)



# Fonction pour consulter les articles
def consulter_articles():
    fenetre_consulter = tk.Toplevel()
    fenetre_consulter.title("Liste des Articles")
    fenetre_consulter.geometry("800x500")
    fenetre_consulter.configure(bg="#ffffff")

    columns = ("code", "designation", "categorie", "lpc")
    tree = ttk.Treeview(fenetre_consulter, columns=columns, show="headings")

    tree.heading("code", text="Code Article")
    tree.heading("designation", text="Désignation")
    tree.heading("categorie", text="Catégorie")
    tree.heading("lpc", text="LPC")

    tree.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

    # Charger les articles existants lors de l'ouverture de la fenêtre
    charger_articles(tree)


# Fonction pour supprimer un article
def ouvrir_fenetre_suppression():
    fenetre_suppression = tk.Toplevel()
    fenetre_suppression.title("Supprimer un Article")
    fenetre_suppression.geometry("800x500")
    fenetre_suppression.configure(bg="#ffffff")

    # Label et combobox pour le code article
    label_code = ttk.Label(fenetre_suppression, text="Code Article:")
    label_code.pack(pady=10)
    
    # Créer un combobox pour les codes d'articles
    combobox_code = ttk.Combobox(fenetre_suppression, width=30, state="readonly")
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
                    messagebox.showwarning("Article non trouvé", "Aucun article trouvé avec ce code.",parent=ouvrir_fenetre_suppression)
                else:
                    conn.commit()
                    messagebox.showinfo("Succès", f"L'article avec le code {code_article} a été supprimé.",parent=ouvrir_fenetre_suppression)
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
    fenetre_modification.geometry("800x500")
    fenetre_modification.configure(bg="#ffffff")

    # Label et combobox pour le code article
    label_code = ttk.Label(fenetre_modification, text="Code Article:")
    label_code.pack(pady=10)
    
    # Créer un combobox pour les codes d'articles
    combobox_code = ttk.Combobox(fenetre_modification, width=30, state="readonly")
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


#############################    ARTICLES ARTICLES ARTICLES #########################################################  

#############################    SOLDE SOLDE SOLDE    SOLDE  #########################################################  
def ouvrir_fenetre_solde():
    fenetre_solde = tk.Toplevel()
    fenetre_solde.title("Gestion des Soldes")
    fenetre_solde.geometry("800x500")
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

    btn_consulter = ttk.Button(frame_boutons, text="Stock Magasin", width=20, command=consulter_magasin)
    btn_consulter.pack(pady=10)

    # Bouton Stock REBUTE
    btn_consulter = ttk.Button(frame_boutons, text="Stock Rebuté", width=20, command=consulter_stock_rebute)
    btn_consulter.pack(pady=10)


# État des mois (ouvert ou fermé)
etat_mois = {mois: "Fermé" for mois in [
    "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
    "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"
]}



# Fonction pour ouvrir/clôturer les soldes
def ouvrir_cloturer():
    
    fenetre_ouvrir_cloturer = tk.Toplevel()
    fenetre_ouvrir_cloturer.title("Ouvrir/Clôturer les Soldes")
    fenetre_ouvrir_cloturer.geometry("800x500")
    fenetre_ouvrir_cloturer.configure(bg="#ffffff")
    
    # Suivi des boutons par mois
    buttons = []

    # Fonction pour basculer l'état d'un mois
    def toggle_mois(mois):
        if etat_mois[mois] == "Fermé":
            if messagebox.askyesno("Confirmation", f"Voulez-vous vraiment ouvrir le mois de {mois} ?", parent=fenetre_ouvrir_cloturer):
                etat_mois[mois] = "Ouvert"
                messagebox.showinfo("Mois Ouvert", f"Le mois de {mois} est maintenant ouvert.", parent=fenetre_ouvrir_cloturer)
        else:
            etat_mois[mois] = "Fermé"
            messagebox.showinfo("Mois Fermé", f"Le mois de {mois} est maintenant fermé.", parent=fenetre_ouvrir_cloturer)
        # Mettre à jour le texte du bouton correspondant au mois
        update_button_text(mois)

    def update_button_text(mois):
        for btn in buttons:
            if btn.cget("text").startswith(mois):
                new_text = f"{mois} ({etat_mois[mois]})"
                btn.config(text=new_text)
                break

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

# Fonction pour consulter les soldes avec calendrier des mois
def consulter_solde():
    fenetre_solde = tk.Toplevel()
    fenetre_solde.title("Solde des Matières")
    fenetre_solde.geometry("800x500")
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
    # Créer la fenêtre
    fenetre_solde_mois = tk.Toplevel()
    fenetre_solde_mois.title(f"Solde des Matières pour {mois}")
    fenetre_solde_mois.geometry("800x500")
    fenetre_solde_mois.configure(bg="#ffffff")

    # Création du tableau
    columns = ("code_matiere", "quantite_initiale", "valeur_initiale", "quantite_finale", "valeur_finale")
    tree = ttk.Treeview(fenetre_solde_mois, columns=columns, show="headings")

    # Configuration des colonnes
    tree.heading("code_matiere", text="Code Matière")
    tree.heading("quantite_initiale", text="Quantité Solde Initiale")
    tree.heading("valeur_initiale", text="Valeur Solde Initiale")
    tree.heading("quantite_finale", text="Quantité Solde Finale")
    tree.heading("valeur_finale", text="Valeur Solde Finale")

    tree.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

    # Connexion à la base de données
    conn = sqlite3.connect('comptabilit_matiere.db')
    cursor = conn.cursor()

    # Récupération des données du mois spécifié
    cursor.execute("SELECT Code_article, Solde_initiale_qte, Solde_initiale_val, Solde_finalee_qte, Solde_finale_val FROM Mois WHERE Nom_mois=?", (mois,))
    rows = cursor.fetchall()

    # Insertion des données dans le tableau
    for row in rows:
        tree.insert("", tk.END, values=row)

    # Fermeture de la connexion à la base de données
    conn.close()

#############################    SOLDE SOLDE SOLDE SOLDE #########################################################

##############################    ENTRES ENTRES ENTRES    #########################################################  

# Fonction pour ouvrir la fenêtre des entrées
def ouvrir_fenetre_entrees():
    fenetre_entrees = tk.Toplevel()
    fenetre_entrees.title("Gestion des Entrées")
    fenetre_entrees.geometry("800x500")
    fenetre_entrees.configure(bg="#ffffff")

    # Frame pour les boutons
    frame_boutons = tk.Frame(fenetre_entrees, bg="#ffffff")
    frame_boutons.pack(expand=True, padx=20, pady=20)

    # Bouton Consulter entrées
    btn_consulter = ttk.Button(frame_boutons, text="Consulter entrées", width=20, command=afficher_entrees)
    btn_consulter.grid(row=0, column=0, padx=10, pady=10)

    # Bouton Ajouter entrée
    btn_ajouter = ttk.Button(frame_boutons, text="Ajouter entrée", width=20, command=afficher_fenetre_entrees)
    btn_ajouter.grid(row=0, column=1, padx=10, pady=10)

# Fonction pour afficher les entrées et ajouter une nouvelle entrée
def afficher_fenetre_entrees():
    fenetre_entrees = tk.Tk()
    fenetre_entrees.title("Gestion des Entrées")
    fenetre_entrees.geometry("1000x600")
    fenetre_entrees.configure(bg="#ffffff")

    # Tableau pour afficher les données
    columns = ("code_entre", "quantite_entre", "valeur_entre", "code_article", "frais_approches", "code_br", "jour", "mois", "annee")
    tree = ttk.Treeview(fenetre_entrees, columns=columns, show="headings")

    # Configuration des colonnes du tableau
    for col in columns:
        tree.heading(col, text=col.replace("_", " ").capitalize())
        tree.column(col, width=150)

    conn = sqlite3.connect("comptabilit_matiere.db")
    cursor = conn.cursor()

    # Charger les données de la base de données
    cursor.execute("SELECT code_entre, quantite_entre, valeur_entre, code_article, frais_approches, code_br, jour, mois, annee FROM Entree")
    entrees = cursor.fetchall()

    for entree in entrees:
        tree.insert("", tk.END, values=entree)

    tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Frame pour les champs de saisie et le bouton Ajouter
    frame_ajout = tk.Frame(fenetre_entrees, bg="#ffffff")
    frame_ajout.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

    # Labels et champs de saisie pour les attributs
    

    label_code_entre = ttk.Label(frame_ajout, text="Code Entrée:")
    label_code_entre.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
    entry_code_entre = ttk.Entry(frame_ajout, width=30)
    entry_code_entre.grid(row=0, column=1, padx=10, pady=5)
    

    label_quantite_entre = ttk.Label(frame_ajout, text="Quantité Entrée:")
    label_quantite_entre.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
    entry_quantite_entre = ttk.Entry(frame_ajout, width=30)
    entry_quantite_entre.grid(row=1, column=1, padx=10, pady=5)
    

    label_valeur_entre = ttk.Label(frame_ajout, text="Valeur Entrée:")
    label_valeur_entre.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
    entry_valeur_entre = ttk.Entry(frame_ajout, width=30)
    entry_valeur_entre.grid(row=2, column=1, padx=10, pady=5)
    

    cursor.execute("SELECT DISTINCT code_article FROM Article")
    articles = cursor.fetchall()
    label_code_article = ttk.Label(frame_ajout, text="Code Article:")
    label_code_article.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
    entry_code_article = ttk.Combobox(frame_ajout, width=28, values=articles, state="readonly")
    entry_code_article.grid(row=3, column=1, padx=10, pady=5)
    

    label_frais_approches = ttk.Label(frame_ajout, text="Frais d'approches:")
    label_frais_approches.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
    entry_frais_approches = ttk.Entry(frame_ajout, width=30)
    entry_frais_approches.grid(row=4, column=1, padx=10, pady=5)
    

    label_code_br = ttk.Label(frame_ajout, text="Code BR:")
    label_code_br.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
    entry_code_br = ttk.Entry(frame_ajout, width=30)
    entry_code_br.grid(row=5, column=1, padx=10, pady=5)
    

    label_jour = ttk.Label(frame_ajout, text="Jour:")
    label_jour.grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)
    entry_jour = ttk.Entry(frame_ajout, width=30)
    entry_jour.grid(row=6, column=1, padx=10, pady=5)
    

    etat_mois =  [
    "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
    "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"
    ]


    label_mois = ttk.Label(frame_ajout, text="Mois:")
    label_mois.grid(row=7, column=0, padx=10, pady=5, sticky=tk.W)
    entry_mois = ttk.Combobox(frame_ajout, width=28, values=etat_mois, state="readonly")
    entry_mois.grid(row=7, column=1, padx=10, pady=5)
    

    label_annee = ttk.Label(frame_ajout, text="Annee:")
    label_annee.grid(row=8, column=0, padx=10, pady=5, sticky=tk.W)
    entry_annee = ttk.Entry(frame_ajout, width=30)
    entry_annee.grid(row=8, column=1, padx=10, pady=5)
    

    conn.close()

    # Fonction pour ajouter une entrée à la base de données et au tableau
    def ajouter_entree():
        code_entre = entry_code_entre.get()
        quantite_entre = entry_quantite_entre.get()
        valeur_entre = entry_valeur_entre.get()
        frais_approches = entry_frais_approches.get()
        code_article = entry_code_article.get()
        jour = entry_jour.get()
        mois = entry_mois.get()
        annee = entry_annee.get()
        code_br = entry_code_br.get()

        if code_entre and quantite_entre and valeur_entre and frais_approches and code_article and jour and mois and annee and code_br:
            try:
                conn = sqlite3.connect("comptabilit_matiere.db")
                cursor = conn.cursor()

                # Ajouter l'entrée dans la table Entree
                cursor.execute("INSERT INTO Entree (code_entre, quantite_entre, valeur_entre, frais_approches, code_article, jour, mois, annee, code_br) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (code_entre, quantite_entre, valeur_entre, frais_approches, code_article, jour, mois, annee, code_br))

                # Mettre à jour la table Mois
                cursor.execute("UPDATE Mois SET Solde_finalee_qte = Solde_finalee_qte + ? , Solde_finale_val = Solde_finale_val + ? + ? WHERE Nom_mois = ? AND Code_article = ?",
                            (quantite_entre, valeur_entre, frais_approches, mois, code_article))

                conn.commit()

                # Ajouter l'entrée au tableau
                tree.insert("", tk.END, values=(code_entre, quantite_entre, valeur_entre, frais_approches, code_article, jour, mois, annee, code_br))

                # Réinitialiser les champs de saisie après ajout
                entry_code_entre.delete(0, tk.END)
                entry_quantite_entre.delete(0, tk.END)
                entry_valeur_entre.delete(0, tk.END)
                entry_frais_approches.delete(0, tk.END)
                entry_code_article.delete(0, tk.END)
                entry_jour.delete(0, tk.END)
                entry_mois.delete(0, tk.END)
                entry_annee.delete(0, tk.END)
                entry_code_br.delete(0, tk.END)
                   

            except sqlite3.IntegrityError:
                messagebox.showerror("Erreur", "Une entrée avec ce code existe déjà.", parent=fenetre_entrees)
            finally:
                conn.close()
        else:
            messagebox.showwarning("Champs manquants", "Veuillez remplir tous les champs.", parent=fenetre_entrees)


    # Bouton Ajouter
    btn_ajouter = ttk.Button(frame_ajout, text="Ajouter", command=ajouter_entree)
    btn_ajouter.grid(row=9, column=0, columnspan=2, padx=10, pady=20)

    # Fonction pour afficher les entrées dans une nouvelle fenêtre
def afficher_entrees():
    fenetre_consulter = tk.Toplevel()
    fenetre_consulter.title("Consulter les Entrées")
    fenetre_consulter.geometry("800x500")
    fenetre_consulter.configure(bg="#ffffff")

    # Configuration du tableau
    columns = ("Code Entrée", "Quantité Entrée", "Valeur Entrée", "Code Article", "Frais d'approches", "Code BR", "Jour", "Mois", "Année")
    tree = ttk.Treeview(fenetre_consulter, columns=columns, show="headings", height=10)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    tree.pack(expand=True, fill=tk.BOTH)

    # Récupération des données de la base de données
    try:
        conn = sqlite3.connect("comptabilit_matiere.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Entree")
        for row in cursor.fetchall():
            tree.insert("", tk.END, values=row)
    except Exception as e:
        messagebox.showerror("Erreur", str(e), parent=fenetre_consulter)
    finally:
        conn.close()

##############################    ENTRES ENTRES ENTRES    ####################################################################
##############################   SORTIES SORTIES SORTIES   ########################################################################

# Fonction pour ouvrir la fenêtre des entrées
def ouvrir_fenetre_sortie():
    fenetre_sorties = tk.Toplevel()
    fenetre_sorties.title("Gestion des Sorties")
    fenetre_sorties.geometry("800x500")
    fenetre_sorties.configure(bg="#ffffff")

    # Frame pour les boutons
    frame_boutons = tk.Frame(fenetre_sorties, bg="#ffffff")
    frame_boutons.pack(expand=True, padx=20, pady=20)

    # Bouton Consulter entrées
    btn_consulter = ttk.Button(frame_boutons, text="Consulter sorties", width=20, command=afficher_sorties)
    btn_consulter.grid(row=0, column=0, padx=10, pady=10)

    # Bouton Ajouter entrée
    btn_ajouter = ttk.Button(frame_boutons, text="Ajouter sorties", width=20, command=afficher_fenetre_sorties)
    btn_ajouter.grid(row=0, column=1, padx=10, pady=10)

# Fonction pour afficher les entrées et ajouter une nouvelle entrée
def afficher_fenetre_sorties():
    fenetre_sorties = tk.Tk()
    fenetre_sorties.title("Gestion des Sorties")
    fenetre_sorties.geometry("1000x600")
    fenetre_sorties.configure(bg="#ffffff")

    # Tableau pour afficher les données
    columns = ("code_sortie", "quantite_sortie", "valeur_sortie", "code_article", "bon",  "code_bon")
    tree = ttk.Treeview(fenetre_sorties, columns=columns, show="headings")

    # Configuration des colonnes du tableau
    for col in columns:
        tree.heading(col, text=col.replace("_", " ").capitalize())
        tree.column(col, width=150)

    conn = sqlite3.connect("comptabilit_matiere.db")
    cursor = conn.cursor()

    # Charger les données de la base de données
    cursor.execute("SELECT code_sortie, quantite_sortie, valeur_sortie, bon, code_bon, code_article FROM Sortie")
    sorties = cursor.fetchall()

    for sortie in sorties:
        tree.insert("", tk.END, values=sortie)

    tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Frame pour les champs de saisie et le bouton Ajouter
    frame_ajout = tk.Frame(fenetre_sorties, bg="#ffffff")
    frame_ajout.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

    # Labels et champs de saisie pour les attributs
    

    label_code_sortie = ttk.Label(frame_ajout, text="Code Sortie:")
    label_code_sortie.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
    entry_code_sortie = ttk.Entry(frame_ajout, width=30)
    entry_code_sortie.grid(row=0, column=1, padx=10, pady=5)
    

    label_quantite_sortie = ttk.Label(frame_ajout, text="Quantité Sortie:")
    label_quantite_sortie.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
    entry_quantite_sortie = ttk.Entry(frame_ajout, width=30)
    entry_quantite_sortie.grid(row=1, column=1, padx=10, pady=5)
    

    label_valeur_sortie = ttk.Label(frame_ajout, text="Valeur Sortie:")
    label_valeur_sortie.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
    entry_valeur_sortie = ttk.Entry(frame_ajout, width=30)
    entry_valeur_sortie.grid(row=2, column=1, padx=10, pady=5)
    

    cursor.execute("SELECT DISTINCT code_article FROM Article")
    articles = cursor.fetchall()
    label_code_article = ttk.Label(frame_ajout, text="Code Article:")
    label_code_article.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
    entry_code_article = ttk.Combobox(frame_ajout, width=28, values=articles, state="readonly")
    entry_code_article.grid(row=3, column=1, padx=10, pady=5)
    
    values_bon = ["BSM", "BRM", "BRT"]

    label_bon = ttk.Label(frame_ajout, text="Bon :")
    label_bon.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
    entry_bon = ttk.Combobox(frame_ajout, width=30, values=values_bon, state="readonly")
    entry_bon.grid(row=4, column=1, padx=10, pady=5)
    
    if entry_bon.get() == "BSM" : 
       cursor.execute("SELECT DISTINCT code_bsm FROM BSM")
       values_code_bon = cursor.fetchall() 

    else :
        if  entry_bon.get() == "BRM" : 
            cursor.execute("SELECT DISTINCT code_brm FROM BRM")
            values_code_bon = cursor.fetchall()   
        else :
            cursor.execute("SELECT DISTINCT code_brt FROM BRT")
            values_code_bon = cursor.fetchall()
            
    label_code_bon = ttk.Label(frame_ajout, text="Code Bon :")
    label_code_bon.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
    entry_code_bon = ttk.Combobox(frame_ajout, width=30, values=values_code_bon, state="readonly")
    entry_code_bon.grid(row=5, column=1, padx=10, pady=5)
    


    conn.close()

    # Fonction pour ajouter une entrée à la base de données et au tableau
    def ajouter_sortie():
        code_sortie = entry_code_sortie.get()
        quantite_sortie = entry_quantite_sortie.get()
        valeur_sortie = entry_valeur_sortie.get()
        bon = entry_bon.get()
        code_article = entry_code_article.get()
        code_bon = entry_code_bon.get()

        if code_sortie and quantite_sortie and valeur_sortie and bon and code_article and code_bon:
            try:
                conn = sqlite3.connect("comptabilit_matiere.db")
                cursor = conn.cursor()

                # Ajouter l'entrée dans la table Entree
                cursor.execute("INSERT INTO Sortie (code_sortie, quantite_sortie, valeur_sortie, bon, code_bon, code_article) VALUES (?, ?, ?, ?, ?, ?)",
                            (code_sortie, quantite_sortie, valeur_sortie, bon, code_bon, code_bon))
                if bon == "BSM" : 
                    cursor.execute("SELECT mois FROM BSM WHERE Code_bsm = ?", bon)
                    mois = cursor.fetchone()
                    # Mettre à jour la table Mois
                    cursor.execute("UPDATE Mois SET Solde_finalee_qte = Solde_finalee_qte - ? , Solde_finale_val = Solde_finale_val - ? WHERE Nom_mois = ? AND Code_article = ?",
                                (quantite_sortie, valeur_sortie,  mois, code_article))
                    cursor.execute("UPDATE magasin SET quantite = quantite - ? , valeur = valeur - ? WHERE  Code_article = ?",
                                (quantite_sortie, valeur_sortie,  code_article))
                else:
                    if bon == "BRM" : 
                        cursor.execute("SELECT mois FROM BRM WHERE Code_brm = ?", bon)
                        mois = cursor.fetchone()
                        # Mettre à jour la table Mois
                        cursor.execute("UPDATE Mois SET Solde_finalee_qte = Solde_finalee_qte + ? , Solde_finale_val = Solde_finale_val + ? WHERE Nom_mois = ? AND Code_article = ?",
                                (quantite_sortie, valeur_sortie,  mois, code_article))
                        cursor.execute("UPDATE magasin SET quantite = quantite + ? , valeur = valeur + ? WHERE  Code_article = ?",
                                (quantite_sortie, valeur_sortie,  code_article))
                    else :
                        cursor.execute("SELECT mois FROM BRT WHERE Code_brt = ?", bon)
                        mois = cursor.fetchone()
                        # Mettre à jour la table Mois
                        cursor.execute("UPDATE Mois SET Solde_finalee_qte = Solde_finalee_qte - ? , Solde_finale_val = Solde_finale_val - ? WHERE Nom_mois = ? AND Code_article = ?",
                                (quantite_sortie, valeur_sortie,  mois, code_article))
                        cursor.execute("UPDATE magasin SET quantite = quantite - ? , valeur = valeur - ? WHERE  Code_article = ?",
                                (quantite_sortie, valeur_sortie,  code_article))
                        cursor.execute("UPDATE stockRBT SET quantite_rebute = quantite_rebute + ? , valeur_rebute = valeur_rebute + ? WHERE  Code_article = ?",
                                (quantite_sortie, valeur_sortie,  code_article))

                conn.commit()

                # Ajouter l'entrée au tableau
                tree.insert("", tk.END, values=(code_sortie, quantite_sortie, valeur_sortie,  code_article, bon, code_bon))

                # Réinitialiser les champs de saisie après ajout
                entry_code_sortie.delete(0, tk.END)
                entry_quantite_sortie.delete(0, tk.END)
                entry_valeur_sortie.delete(0, tk.END)
                entry_bon.delete(0, tk.END)
                entry_code_article.delete(0, tk.END)
                entry_code_bon.delete(0, tk.END)
                   

            except sqlite3.IntegrityError:
                messagebox.showerror("Erreur", "Une sortie avec ce code existe déjà.", parent=fenetre_sorties)
            finally:
                conn.close()
        else:
            messagebox.showwarning("Champs manquants", "Veuillez remplir tous les champs.", parent=fenetre_sorties)

    btn_ajouter = ttk.Button(frame_ajout, text="Ajouter", command= ajouter_sortie)
    btn_ajouter.grid(row=9, column=0, columnspan=2, padx=10, pady=20)

    # Fonction pour afficher les entrées dans une nouvelle fenêtre
def afficher_sorties():
    fenetre_consulter = tk.Toplevel()
    fenetre_consulter.title("Consulter les Sorties")
    fenetre_consulter.geometry("800x500")
    fenetre_consulter.configure(bg="#ffffff")

    # Configuration du tableau
    columns = ("Code Sortie", "Quantité Sorties", "Valeur Sortie", "Code Article", "Bon", "Code Bon")
    tree = ttk.Treeview(fenetre_consulter, columns=columns, show="headings", height=10)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    tree.pack(expand=True, fill=tk.BOTH)

    # Récupération des données de la base de données
    try:
        conn = sqlite3.connect("comptabilit_matiere.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Sortie")
        for row in cursor.fetchall():
            tree.insert("", tk.END, values=row)
    except Exception as e:
        messagebox.showerror("Erreur", str(e), parent=fenetre_consulter)
    finally:
        conn.close()




##############################      SORTIES SORTIES SORTIES ##############################################################
##############################    BON    BON     BON     ########################################################################
# BSM  BRT  BRM 
def ouvrir_fenetre_bon():
    fenetre_bon = tk.Toplevel()
    fenetre_bon.title("Bon")
    fenetre_bon.geometry("800x500")
    fenetre_bon.configure(bg="#ffffff")

    # Charger l'image de la flèche
    fleche_image = Image.open("img\\retour.png")  # Assurez-vous que le fichier est dans le bon répertoire
    fleche_image = fleche_image.resize((30, 30), Image.LANCZOS)  # Redimensionner l'image
    fleche_photo = ImageTk.PhotoImage(fleche_image)

    # Frame pour la flèche en haut à gauche
    frame_fleche = tk.Frame(fenetre_bon, bg="#ffffff")
    frame_fleche.pack(side=tk.TOP, anchor="nw", padx=10, pady=10)


    # Label pour l'icône de la flèche
    label_fleche = tk.Label(frame_fleche, image=fleche_photo, bg="#ffffff", cursor="hand2")
    label_fleche.image = fleche_photo  # Préserver une référence pour l'image
    label_fleche.pack()
    
    # Attacher l'événement de clic à l'icône de la flèche
    label_fleche.bind("<Button-1>", lambda e: fenetre_bon.destroy())

    # Frame pour les boutons
    frame_btn = tk.Frame(fenetre_bon, bg="#ffffff")
    frame_btn.pack(expand=True, padx=20, pady=20)

    # Bouton Consulter solde
    btn_bsm = ttk.Button(frame_btn, text="BSM", width=20, command=ouvrir_fenetre_bsm)
    btn_bsm.pack(pady=10)

    # Bouton Ouvrir/Clôturer
    btn_brt = ttk.Button(frame_btn, text="BRT", width=20, command=ouvrir_fenetre_brt)
    btn_brt.pack(pady=10)

    # Stock Magasin
    btn_brm = ttk.Button(frame_btn, text="BRM", width=20, command=ouvrir_fenetre_brm)
    btn_brm.pack(pady=10)

### BSM BSM BSM BSM BSM BSM BSM BSM################################################################
# Fonction pour consulter les BSM
def consulter_bsm():
    fenetre_consulter_bsm = tk.Toplevel()
    fenetre_consulter_bsm.title("Consulter les BSM")
    fenetre_consulter_bsm.geometry("800x500")
    fenetre_consulter_bsm.configure(bg="#ffffff")

    # Charger l'image de la flèche
    fleche_image = Image.open("img\\retour.png")  # Assurez-vous que le fichier est dans le bon répertoire
    fleche_image = fleche_image.resize((30, 30), Image.LANCZOS)  # Redimensionner l'image
    fleche_photo = ImageTk.PhotoImage(fleche_image)

    # Frame pour la flèche en haut à gauche
    frame_fleche = tk.Frame(fenetre_consulter_bsm, bg="#ffffff")
    frame_fleche.pack(side=tk.TOP, anchor="nw", padx=10, pady=10)


    # Label pour l'icône de la flèche
    label_fleche = tk.Label(frame_fleche, image=fleche_photo, bg="#ffffff", cursor="hand2")
    label_fleche.image = fleche_photo  # Préserver une référence pour l'image
    label_fleche.pack()
    
    # Attacher l'événement de clic à l'icône de la flèche
    label_fleche.bind("<Button-1>", lambda e: fenetre_consulter_bsm.destroy())

    # Création du tableau
    columns = ("Code BSM", "Jour", "Mois", "Année", "Nom", "Adresse")
    tree = ttk.Treeview(fenetre_consulter_bsm, columns=columns, show="headings", height=10)

    # Configuration des colonnes du tableau
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    # Connexion à la base de données et récupération des données
    conn = sqlite3.connect("comptabilit_matiere.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM BSM")
    rows = cursor.fetchall()

    # Insertion des données dans le tableau
    for row in rows:
        tree.insert("", tk.END, values=row)

    conn.close()
# Fonction pour ajouter un BSM
def ajouter_bsm():
    fenetre_ajout_bsm = tk.Toplevel()
    fenetre_ajout_bsm.title("Ajouter un BSM")
    fenetre_ajout_bsm.geometry("800x500")
    fenetre_ajout_bsm.configure(bg="#ffffff")



    # Labels et champs de saisie pour les attributs
    labels_text = ["Code BSM", "Jour", "Mois", "Année", "Nom", "Adresse"]
    entries = {}

    for i, text in enumerate(labels_text):
        label = ttk.Label(fenetre_ajout_bsm, text=text + ":")
        label.grid(row=i, column=0, padx=10, pady=10, sticky=tk.W)
        entry = ttk.Entry(fenetre_ajout_bsm, width=30)
        entry.grid(row=i, column=1, padx=10, pady=10)
        entries[text] = entry

    # Fonction pour ajouter un BSM à la base de données
    def ajouter_bsm_bd():
        code_bsm = entries["Code BSM"].get()
        jour = entries["Jour"].get()
        mois = entries["Mois"].get()
        annee = entries["Année"].get()
        nom = entries["Nom"].get()
        adresse = entries["Adresse"].get()

        if code_bsm and jour and mois and annee and nom and adresse:
            try:
                conn = sqlite3.connect("comptabilit_matiere.db")
                cursor = conn.cursor()
                cursor.execute("INSERT INTO BSM (Code_bsm, jour, mois, annee, nom, adresse) VALUES (?, ?, ?, ?, ?, ?)",
                               (code_bsm, jour, mois, annee, nom, adresse))
                conn.commit()
                messagebox.showinfo("Succès", "Le BSM a été ajouté avec succès.", parent=fenetre_ajout_bsm)
                # Réinitialiser les champs de saisie après ajout
                for entry in entries.values():
                    entry.delete(0, tk.END)
            except sqlite3.IntegrityError:
                messagebox.showerror("Erreur", "Un BSM avec ce code existe déjà.", parent=fenetre_ajout_bsm)
            finally:
                conn.close()
        else:
            messagebox.showwarning("Champs manquants", "Veuillez remplir tous les champs.", parent=fenetre_ajout_bsm)

    # Bouton Ajouter
    btn_ajouter = ttk.Button(fenetre_ajout_bsm, text="Ajouter", command=ajouter_bsm_bd)
    btn_ajouter.grid(row=len(labels_text), column=0, columnspan=2, padx=10, pady=10)

# Fonction pour ouvrir la fenêtre de gestion des bons
def ouvrir_fenetre_bsm():
    fenetre_bsm = tk.Toplevel()
    fenetre_bsm.title("BSM")
    fenetre_bsm.geometry("800x500")
    fenetre_bsm.configure(bg="#ffffff")

    # Charger l'image de la flèche
    fleche_image = Image.open("img\\retour.png")  # Assurez-vous que le fichier est dans le bon répertoire
    fleche_image = fleche_image.resize((30, 30), Image.LANCZOS)  # Redimensionner l'image
    fleche_photo = ImageTk.PhotoImage(fleche_image)

    # Frame pour la flèche en haut à gauche
    frame_fleche = tk.Frame(fenetre_bsm, bg="#ffffff")
    frame_fleche.pack(side=tk.TOP, anchor="nw", padx=10, pady=10)


    # Label pour l'icône de la flèche
    label_fleche = tk.Label(frame_fleche, image=fleche_photo, bg="#ffffff", cursor="hand2")
    label_fleche.image = fleche_photo  # Préserver une référence pour l'image
    label_fleche.pack()
    
    # Attacher l'événement de clic à l'icône de la flèche
    label_fleche.bind("<Button-1>", lambda e: fenetre_bsm.destroy())


    # Frame pour les boutons
    frame_boutons = tk.Frame(fenetre_bsm, bg="#ffffff")
    frame_boutons.pack(expand=True, padx=20, pady=20)


    # Bouton AJOUTER BSM
    ajouter_bsm_btn = ttk.Button(frame_boutons, text="Ajouter BSM", width=20, command=ajouter_bsm)
    ajouter_bsm_btn.pack(pady=10)

    # Bouton Consulter BSM
    consulter_bsm_btn = ttk.Button(frame_boutons, text="Consulter BSM", width=20, command=consulter_bsm)
    consulter_bsm_btn.pack(pady=10)
    


### brt  ##############################################################################
# Fonction pour consulter les BRT
def consulter_brt():
    fenetre_consulter_brt = tk.Toplevel()
    fenetre_consulter_brt.title("Consulter les BRT")
    fenetre_consulter_brt.geometry("800x500")
    fenetre_consulter_brt.configure(bg="#ffffff")

    # Charger l'image de la flèche
    fleche_image = Image.open("img\\retour.png")  # Assurez-vous que le fichier est dans le bon répertoire
    fleche_image = fleche_image.resize((30, 30), Image.LANCZOS)  # Redimensionner l'image
    fleche_photo = ImageTk.PhotoImage(fleche_image)

    # Frame pour la flèche en haut à gauche
    frame_fleche = tk.Frame(fenetre_consulter_brt, bg="#ffffff")
    frame_fleche.pack(side=tk.TOP, anchor="nw", padx=10, pady=10)


    # Label pour l'icône de la flèche
    label_fleche = tk.Label(frame_fleche, image=fleche_photo, bg="#ffffff", cursor="hand2")
    label_fleche.image = fleche_photo  # Préserver une référence pour l'image
    label_fleche.pack()
    
    # Attacher l'événement de clic à l'icône de la flèche
    label_fleche.bind("<Button-1>", lambda e: fenetre_consulter_brt.destroy())

    # Création du tableau
    columns = ("Code BRT", "Jour", "Mois", "Année", "Nom")
    tree = ttk.Treeview(fenetre_consulter_brt, columns=columns, show="headings", height=10)

    # Configuration des colonnes du tableau
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    # Connexion à la base de données et récupération des données
    conn = sqlite3.connect("comptabilit_matiere.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM BRT")
    rows = cursor.fetchall()

    # Insertion des données dans le tableau
    for row in rows:
        tree.insert("", tk.END, values=row)

    conn.close()


# Fonction pour ajouter un BRT
def ajouter_brt():
    fenetre_ajout_brt = tk.Toplevel()
    fenetre_ajout_brt.title("Ajouter un BRT")
    fenetre_ajout_brt.geometry("800x500")
    fenetre_ajout_brt.configure(bg="#ffffff")


    # Labels et champs de saisie pour les attributs
    labels_text = ["Code BRT", "Jour", "Mois", "Année", "Nom"]
    entries = {}

    for i, text in enumerate(labels_text):
        label = ttk.Label(fenetre_ajout_brt, text=text + ":")
        label.grid(row=i, column=0, padx=10, pady=10, sticky=tk.W)
        entry = ttk.Entry(fenetre_ajout_brt, width=30)
        entry.grid(row=i, column=1, padx=10, pady=10)
        entries[text] = entry

    # Fonction pour ajouter un BRT à la base de données
    def ajouter_brt_bd():
        code_brt = entries["Code BRT"].get()
        jour = entries["Jour"].get()
        mois = entries["Mois"].get()
        annee = entries["Année"].get()
        nom = entries["Nom"].get()


        if code_brt and jour and mois and annee and nom :
            try:
                conn = sqlite3.connect("comptabilit_matiere.db")
                cursor = conn.cursor()
                cursor.execute("INSERT INTO BRT (code_brt, jour, mois, annee, nom) VALUES (?, ?, ?, ?, ?)",
                               (code_brt, jour, mois, annee, nom))
                conn.commit()
                messagebox.showinfo("Succès", "Le BRT a été ajouté avec succès.", parent=fenetre_ajout_brt)
                # Réinitialiser les champs de saisie après ajout
                for entry in entries.values():
                    entry.delete(0, tk.END)
            except sqlite3.IntegrityError:
                messagebox.showerror("Erreur", "Un BRT avec ce code existe déjà.", parent=fenetre_ajout_brt)
            finally:
                conn.close()
        else:
            messagebox.showwarning("Champs manquants", "Veuillez remplir tous les champs.", parent=fenetre_ajout_brt)

    # Bouton Ajouter
    btn_ajouter = ttk.Button(fenetre_ajout_brt, text="Ajouter", command=ajouter_brt_bd)
    btn_ajouter.grid(row=len(labels_text), column=0, columnspan=2, padx=10, pady=10)

# Fonction pour ouvrir la fenêtre de gestion des bons
def ouvrir_fenetre_brt():
    fenetre_brt = tk.Toplevel()
    fenetre_brt.title("BRT")
    fenetre_brt.geometry("800x500")
    fenetre_brt.configure(bg="#ffffff")

    # Charger l'image de la flèche
    fleche_image = Image.open("img\\retour.png")  # Assurez-vous que le fichier est dans le bon répertoire
    fleche_image = fleche_image.resize((30, 30), Image.LANCZOS)  # Redimensionner l'image
    fleche_photo = ImageTk.PhotoImage(fleche_image)

    # Frame pour la flèche en haut à gauche
    frame_fleche = tk.Frame(fenetre_brt , bg="#ffffff")
    frame_fleche.pack(side=tk.TOP, anchor="nw", padx=10, pady=10)


    # Label pour l'icône de la flèche
    label_fleche = tk.Label(frame_fleche, image=fleche_photo, bg="#ffffff", cursor="hand2")
    label_fleche.image = fleche_photo  # Préserver une référence pour l'image
    label_fleche.pack()
    
    # Attacher l'événement de clic à l'icône de la flèche
    label_fleche.bind("<Button-1>", lambda e: fenetre_brt .destroy())

    # Frame pour les boutons
    frame_boutons = tk.Frame(fenetre_brt, bg="#ffffff")
    frame_boutons.pack(expand=True, padx=20, pady=20)

    # Bouton AJOUTER BSM
    ajouter_brt_btn = ttk.Button(frame_boutons, text="Ajouter BRT", width=20, command=ajouter_brt)
    ajouter_brt_btn.pack(pady=10)

    # Bouton Consulter BSM
    consulter_brt_btn = ttk.Button(frame_boutons, text="Consulter BRT", width=20, command=consulter_brt)
    consulter_brt_btn.pack(pady=10)
### brm ######################################################################
# Fonction pour consulter les BSM
def consulter_brm():
    fenetre_consulter_brm = tk.Toplevel()
    fenetre_consulter_brm.title("Consulter les BRM")
    fenetre_consulter_brm.geometry("800x500")
    fenetre_consulter_brm.configure(bg="#ffffff")

    # Charger l'image de la flèche
    fleche_image = Image.open("img\\retour.png")  # Assurez-vous que le fichier est dans le bon répertoire
    fleche_image = fleche_image.resize((30, 30), Image.LANCZOS)  # Redimensionner l'image
    fleche_photo = ImageTk.PhotoImage(fleche_image)

    # Frame pour la flèche en haut à gauche
    frame_fleche = tk.Frame(fenetre_consulter_brm , bg="#ffffff")
    frame_fleche.pack(side=tk.TOP, anchor="nw", padx=10, pady=10)


    # Label pour l'icône de la flèche
    label_fleche = tk.Label(frame_fleche, image=fleche_photo, bg="#ffffff", cursor="hand2")
    label_fleche.image = fleche_photo  # Préserver une référence pour l'image
    label_fleche.pack()
    
    # Attacher l'événement de clic à l'icône de la flèche
    label_fleche.bind("<Button-1>", lambda e: fenetre_consulter_brm .destroy())
    

    # Création du tableau
    columns = ("Code BRM", "Jour", "Mois", "Année", "Nom")
    tree = ttk.Treeview(fenetre_consulter_brm, columns=columns, show="headings", height=10)

    # Configuration des colonnes du tableau
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    # Connexion à la base de données et récupération des données
    conn = sqlite3.connect("comptabilit_matiere.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM BRM")
    rows = cursor.fetchall()

    # Insertion des données dans le tableau
    for row in rows:
        tree.insert("", tk.END, values=row)

    conn.close()


# Fonction pour ajouter un BRM
def ajouter_brm():
    fenetre_ajout_brm = tk.Toplevel()
    fenetre_ajout_brm.title("Ajouter un BRM")
    fenetre_ajout_brm.geometry("800x500")
    fenetre_ajout_brm.configure(bg="#ffffff")


    # Labels et champs de saisie pour les attributs
    labels_text = ["Code BRM", "Jour", "Mois", "Année", "Nom"]
    entries = {}

    for i, text in enumerate(labels_text):
        label = ttk.Label(fenetre_ajout_brm, text=text + ":")
        label.grid(row=i, column=0, padx=10, pady=10, sticky=tk.W)
        entry = ttk.Entry(fenetre_ajout_brm, width=30)
        entry.grid(row=i, column=1, padx=10, pady=10)
        entries[text] = entry

    # Fonction pour ajouter un BRM à la base de données
    def ajouter_brm_bd():
        code_brm = entries["Code BRM"].get()
        jour = entries["Jour"].get()
        mois = entries["Mois"].get()
        annee = entries["Année"].get()
        nom = entries["Nom"].get()


        if code_brm and jour and mois and annee and nom :
            try:
                conn = sqlite3.connect("comptabilit_matiere.db")
                cursor = conn.cursor()
                cursor.execute("INSERT INTO BRM (code_brm, jour, mois, annee, nom) VALUES (?, ?, ?, ?, ?)",
                               (code_brm, jour, mois, annee, nom))
                conn.commit()
                messagebox.showinfo("Succès", "Le BRM a été ajouté avec succès.", parent=fenetre_ajout_brm)
                # Réinitialiser les champs de saisie après ajout
                for entry in entries.values():
                    entry.delete(0, tk.END)
            except sqlite3.IntegrityError:
                messagebox.showerror("Erreur", "Un BRM avec ce code existe déjà.", parent=fenetre_ajout_brm)
            finally:
                conn.close()
        else:
            messagebox.showwarning("Champs manquants", "Veuillez remplir tous les champs.", parent=fenetre_ajout_brm)

    # Bouton Ajouter
    btn_ajouter = ttk.Button(fenetre_ajout_brm, text="Ajouter", command=ajouter_brm_bd)
    btn_ajouter.grid(row=len(labels_text), column=0, columnspan=2, padx=10, pady=10)

# Fonction pour ouvrir la fenêtre de gestion des bons
def ouvrir_fenetre_brm():
    fenetre_brm = tk.Toplevel()
    fenetre_brm.title("BRM")
    fenetre_brm.geometry("800x800")
    fenetre_brm.configure(bg="#ffffff")

    # Charger l'image de la flèche
    fleche_image = Image.open("img\\retour.png")  # Assurez-vous que le fichier est dans le bon répertoire
    fleche_image = fleche_image.resize((30, 30), Image.LANCZOS)  # Redimensionner l'image
    fleche_photo = ImageTk.PhotoImage(fleche_image)

    # Frame pour la flèche en haut à gauche
    frame_fleche = tk.Frame(fenetre_brm , bg="#ffffff")
    frame_fleche.pack(side=tk.TOP, anchor="nw", padx=10, pady=10)


    # Label pour l'icône de la flèche
    label_fleche = tk.Label(frame_fleche, image=fleche_photo, bg="#ffffff", cursor="hand2")
    label_fleche.image = fleche_photo  # Préserver une référence pour l'image
    label_fleche.pack()
    
    # Attacher l'événement de clic à l'icône de la flèche
    label_fleche.bind("<Button-1>", lambda e: fenetre_brm .destroy())


    # Frame pour les boutons
    frame_boutons = tk.Frame(fenetre_brm, bg="#ffffff")
    frame_boutons.pack(expand=True, padx=20, pady=20)

    # Bouton AJOUTER BSM
    ajouter_brm_btn = ttk.Button(frame_boutons, text="Ajouter BRM", width=20, command=ajouter_brm)
    ajouter_brm_btn.pack(pady=10)

    # Bouton Consulter BRM
    consulter_brm_btn = ttk.Button(frame_boutons, text="Consulter BRM", width=20, command=consulter_brm)
    consulter_brm_btn.pack(pady=10)

############################### BON    BON     BON    #####################################################
############################### MAGASIN  MAGASIN MAGASIN ##################################################################
def consulter_magasin():
    # Connexion à la base de données
    conn = sqlite3.connect('comptabilit_matiere.db')
    cursor = conn.cursor()
    
    # Création de la fenêtre
    fenetre_magasin = tk.Toplevel()
    fenetre_magasin.title("Données du Magasin")
    fenetre_magasin.geometry("800x400")
    fenetre_magasin.configure(bg="#ffffff")
    
    # Création du tableau
    columns = ("Code Article", "Quantité", "Valeur")
    tree = ttk.Treeview(fenetre_magasin, columns=columns, show="headings", height=15)
    
    # Configuration des colonnes du tableau
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor=tk.CENTER)
    
    tree.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

    # Récupération des données de la table magasin
    cursor.execute("SELECT code_article, quantite, valeur FROM magasin")
    rows = cursor.fetchall()
    
    # Insertion des données dans le tableau
    for row in rows:
        tree.insert("", tk.END, values=row)
    
    conn.close()
##########################################################################################################
############################### MAGASIN  MAGASIN MAGASIN ##################################################################
def consulter_stock_rebute():
    # Connexion à la base de données
    conn = sqlite3.connect('comptabilit_matiere.db')
    cursor = conn.cursor()
    
    # Création de la fenêtre
    fenetre_magasin = tk.Toplevel()
    fenetre_magasin.title("Données du Stock Rebuté")
    fenetre_magasin.geometry("800x400")
    fenetre_magasin.configure(bg="#ffffff")
    
    # Création du tableau
    columns = ("Code Article", "Quantité", "Valeur")
    tree = ttk.Treeview(fenetre_magasin, columns=columns, show="headings", height=15)
    
    # Configuration des colonnes du tableau
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor=tk.CENTER)
    
    tree.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

    # Récupération des données de la table magasin
    cursor.execute("SELECT code_article, quantite_rebute, valeur_rebute FROM stockRBT")
    rows = cursor.fetchall()
    
    # Insertion des données dans le tableau
    for row in rows:
        tree.insert("", tk.END, values=row)
    
    conn.close()
##################################################################################################


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
