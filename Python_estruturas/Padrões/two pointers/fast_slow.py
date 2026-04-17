# 2️⃣ 🏃 FAST & SLOW POINTER
# 📍 Quando usar:
# linked list
# ciclos
# encontrar meio
# 🧠 Exemplo:

slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

# 👉 slow vai 1 passo
# 👉 fast vai 2 passos

# 💡 Usa para:
# detectar ciclo
# encontrar meio