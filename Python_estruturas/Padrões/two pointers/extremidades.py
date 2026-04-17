# 1️⃣ 👈👉 PONTEIROS NAS EXTREMIDADES
# 📍 Quando usar:
# array ordenado
# comparar soma
# palíndromo

# 🧠 Exemplo clássico:
nums = [1,2,3,4,6]
target = 6
left = 0
right = len(nums) - 1

def Solucao():
    while left < right:
        soma = nums[left] + nums[right]

        if soma == target:
            return True
        elif soma < target:
            left += 1
        else:
            right -= 1
        

# 💡 Regra:
# soma pequena → anda esquerda
# soma grande → anda direita