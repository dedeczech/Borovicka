soubor = "polednice.txt"
with open(soubor, "r", encoding="utf-8") as f:

    text = f.read()
    from collections import Counter

text = input("Zadej text: ")

# odstranění mezer a převod na malá písmena
text = text.lower().replace(" ", "")

# spočítání výskytu písmen
counts = Counter(text)

# nejčastější písmeno
nejcastejsi = counts.most_common(1)[0]

print("Nejčastější písmeno:", nejcastejsi[0])
print("Počet výskytů:", nejcastejsi[1])