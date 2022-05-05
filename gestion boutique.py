print("\t---programme de gestion d'une boutique alimentaire---\n")

print("\tsaisi information de vente:\n")
code = input("\tEntrer le code du produit vendu:")
nom = input("\tEntrer le nom du produit vendu:")
categorie = input("\tEntrer la categorie du produit vendu:")
prix = int(input("\tEntrer le prix du produit vendu:"))
quantite = int(input("\tEntrer la quantite du produit vendu:"))

print("\tLe code du produit vendu est:",code)
print("\tLe nom du produit vendu est:",nom)
print("\tLa categore du produit vendu est:",categorie)
print("\tLe prix du produit vendu est:",prix,"FCFA")
print("\tLa quantite du produit vendu est:",quantite)

montant_vente = prix * quantite
print("\tLe montant de la vente du produit est:",montant_vente,"FCFA")

montant_encaisse = int(input("\tEntrer le montant encaisse pour le règlement de la vente:"))
monnaie = montant_encaisse - montant_vente
print("\tLa monnaie à rendre suite à la vente est:",monnaie)

print("\t-------------Merci à la prochaine----------------------")


                       



