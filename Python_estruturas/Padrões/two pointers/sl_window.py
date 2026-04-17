# 3️⃣ 🪟 SLIDING WINDOW (variação de two pointers)
# 📍 Quando usar:
# substring
# subarray contínuo
# sem repetição
# 🧠 Exemplo:

left = 0
seen = set()

for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1

    seen.add(s[right])
    
# 💡 Ideia:
# right expande janela
# left encolhe quando precisa