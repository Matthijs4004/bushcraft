# Noodvoedsel per persoon:
# 6 pemmican-repen (bevatten: noten, zaden, vet en eiwitten)
# 3 vijgenplakken (bevatten gedroogde vijgen)
# Noodvoedsel algemeen:
# 2 scheepsbiscuit rollen
# Pemmican-repen worden verkocht in pakjes van 4. Een pemmican pakje kost: € 3,45


# 2 firesteels (vuurmakers)
# 5 pakjes lucifers
# 4 originele vuurstenen
# 1 rol sisaltouw van 20 meter


firesteel = 3.36
lucifers = 0.21
vuursteen = 2.23
sisaltouw = 0.58
vijgenplakken = 1.24
scheepsbiscuit = 2.67
pemmican = 3.45

noodvoedsel = (30 / 4 * pemmican) + (3 * 5 * vijgenplakken) + (scheepsbiscuit * 2)
overig = (2 * firesteel) + (5 * lucifers) + (4 * vuursteen) + (10 * sisaltouw)
materialen = noodvoedsel + overig

print("Totaalbedrag:", round(materialen, 2))