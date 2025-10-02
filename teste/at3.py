amigo_a = ["FIFA", "LOL", "PUBG", "CS:GO"]
amigo_b = ["Valorant", "CS:GO", "FIFA", "Overwatch"]

set_a = set(amigo_a)
set_b = set(amigo_b)

# Descubra os jogos em comum
jogos_comuns = set_a.intersection(set_b)

print(jogos_comuns)