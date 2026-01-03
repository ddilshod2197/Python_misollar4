# 1-PAROL GENERATORI
import random
import string

uzunlik = int(input("Parol uzunligini kiriting: "))

belgilar = string.ascii_letters + string.digits + string.punctuation
parol = ""

for i in range(uzunlik):
    parol += random.choice(belgilar)

print("Yaratilgan parol:", parol)

# 2-LOTO O‘YIN (1–50 dan 6 ta son)
import random

loto = random.sample(range(1, 51), 6)
print("Loto raqamlari:", loto)

# 3-MATN FAYL O‘QISH
from collections import Counter

with open("matn.txt", "r", encoding="utf-8") as fayl:
    matn = fayl.read().lower()

sozlar = matn.split()
sanoq = Counter(sozlar)

eng_kop_5 = sanoq.most_common(5)

print("Eng ko‘p ishlatilgan 5 ta so‘z:")
for soz, soni in eng_kop_5:
    print(soz, "→", soni)

# 4-RO‘YXATDAN DUBLIKATLARNI O‘CHIRISH
sonlar = list(map(int, input("Sonlarni kiriting: ").split()))
yangi = []

for son in sonlar:
    if son not in yangi:
        yangi.append(son)

print("Dublikatsiz ro'yxat:", yangi)

# 5-SONLARNI SO‘Z BILAN YOZISH (0–999)
birlar = ["nol", "bir", "ikki", "uch", "to‘rt", "besh", "olti", "yetti", "sakkiz", "to‘qqiz"]
onlar = ["", "o‘n", "yigirma", "o‘ttiz", "qirq", "ellik", "oltmish", "yetmish", "sakson", "to‘qson"]

son = int(input("0 dan 999 gacha son kiriting: "))

if son < 10:
    print(birlar[son])
elif son < 100:
    print(onlar[son // 10], birlar[son % 10])
else:
    yuz = son // 100
    qolgan = son % 100
    if qolgan == 0:
        print(birlar[yuz], "yuz")
    else:
        print(birlar[yuz], "yuz", onlar[qolgan // 10], birlar[qolgan % 10])


