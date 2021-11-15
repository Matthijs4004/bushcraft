dieselprijs = float(input("Wat is de dieselprijs op dit moment in euro? "))
firesteel = 3.36
lucifers = 0.21
vuursteen = 2.23
sisaltouw = 0.58
vijgenplakken = 1.24
scheepsbiscuit = 2.67
pemmican = 3.45

x = (244 / 12) * (dieselprijs) * 2 + 80
noodvoedsel = (30 / 4 * pemmican) + (3 * 5 * vijgenplakken) + (scheepsbiscuit * 2)
overig = (2 * firesteel) + (5 * lucifers) + (4 * vuursteen) + (10 * sisaltouw)
materialen = noodvoedsel + overig


print("Aanmeldformulier Bushcraft team\n")

drukken = int(input("Hoeveel kg kunt u drukken? "))
spijker = int(input("Wat is de maximale dikte van een spijker in mm die u kunt buigen? "))
iq = int(input("Hoe hoog is uw IQ? "))
kast = int(input("In hoeveel seconden kunt u een IKEA Larsfrid buffetkast in elkaar zetten zonder handleiding? "))
sloot = int(input("Wat is de maximale breedte van een sloot die u kunt springen in meters? "))
vuur = int(input("Binnen hoeveel seconden kunt u met vuurstenen en hooi vuurmaken? "))
paddestoelen = int(input("Hoeveel soorten eetbare paddenstoelen kunt u herkennen? "))
kruiden = int(input("Hoeveel soorten giftige kruiden kunt u herkennen? "))
mos = input("In welke richting groeit mos in Nederland? N/O/Z/W ")
zuiveren = input("Heeft u kennis van het zuiveren van water? J/N ")

if drukken > 100 and spijker > 10:
    print("Je bent in aanmerking gekomen voor de rol 'Beer' in het team.")

if iq > 130 and kast < 300:
    print("Je bent in aanmerking gekomen voor de rol 'Vos' in het team")

if sloot > 3 and vuur < 60:
    print("Je bent in aanmerking gekomen voor de rol 'Bever' in het team")

if paddestoelen > 10 and kruiden > 20 and mos == "W" and zuiveren == "J":
    print("Je bent in aanmerking gekomen voor de rol 'Uil' in het team")

print("\nMateriaalbedrag:", round(materialen, 2))
print("Reisbedrag:", round(x, 2))
print("Totaalbedrag:", round(x + materialen, 2))