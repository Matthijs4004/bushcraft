dieselprijs = float(input("Wat is de dieselprijs op dit moment in euro? "))
firesteel = 3.36
lucifers = 0.21
vuursteen = 2.23
sisaltouw = 0.58
vijgenplakken = 1.24
scheepsbiscuit = 2.67
pemmican = 3.45
rollen = ["Beer", "Vos", "Bever", "Uil"]
geschikt = "Je bent in aanmerking gekomen voor de rol: "
ngeschikt = "Helaas ben je niet geschikt voor de rol: "
x = (244 / 12) * (dieselprijs) * 2 + 80
noodvoedsel = (30 / 4 * pemmican) + (3 * 5 * vijgenplakken) + (scheepsbiscuit * 2)
overig = (2 * firesteel) + (5 * lucifers) + (4 * vuursteen) + (10 * sisaltouw)
materialen = noodvoedsel + overig
totaalbedrag = materialen + x
deel = totaalbedrag / 5

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
    sterk = True
else:
    sterk = False

if iq > 130 and kast < 300:
    slim = True
else:
    slim = False

if sloot > 3 and vuur < 60:
    handig = True
else:
    handig = False

if paddestoelen > 10 and kruiden > 20 and mos == "W" and zuiveren == "J":
    kennis = True
else:
    kennis = False


def beer():
    if sterk == True:
        print(geschikt, rollen[0])
    else:
        print(ngeschikt, rollen[0])
def vos():
    if slim == True:
        print(geschikt, rollen[1])
    else:
        print(ngeschikt, rollen[1])
def bever():
    if handig == True:
        print(geschikt, rollen[2])
    else:
        print(ngeschikt, rollen[2])
def uil():
    if kennis == True:
        print(geschikt, rollen[3])
    else:
        print(ngeschikt, rollen[3])

print("\nUitslag: ")
beer()
vos()
bever()
uil()

print("\nTenslotte nog hebben we nog 1 vraag die bepaalt of u mee kan of niet.")
def geldInleggen():
    inleggen = int(input("\nHoeveel euro bent u bereid om in te leggen voor het bushcraften? "))
    if inleggen > 45:
        print("Gefeliciteerd. Als u voor 1 van de 4 rollen geschikt bent dan kunt u mee met bushcraften.")
    elif inleggen < 45:
        print("Het bedrag wat u bereid bent in te leggen is helaas te weinig en dus kunt u niet mee met het bushcraften.")
    else:
        print("Probeer op nieuw.")
        geldInleggen()

geldInleggen()

# print("\nMateriaalbedrag:", round(materialen, 2))
# print("Reisbedrag:", round(x, 2))
# print("Totaalbedrag:", round(x + materialen, 2))