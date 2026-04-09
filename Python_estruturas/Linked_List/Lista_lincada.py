# 1. CLASSE NÓ (cada "caixinha")
class Node:
    def __init__(self, data):           # Construtor do nó
        self.data = data                # Conteúdo do nó
        self.next = None                # Ponteiro (inicialmente None)
    
    def __repr__(self):                 # Como mostrar no print
        return f"[{self.data}|next={self.next}]"

# 2. CLASSE LISTA (controla tudo)
class LinkedList:
    def __init__(self):
        self.head = None  # CABEÇA da lista (inicia vazia)
    
    # Método pra mostrar lista
    def print_list(self):
        current = self.head  # Ponteiro de percurso
        print("Lista:", end=" ")
        while current:      # Enquanto não chegou no fim
            print(repr(current), end=" → ")
            current = current.next  # Avança
        print("None")

# ========================================
# DEMO PASSO A PASSO (SINTAXE COMPLETA!)
# ========================================

print("=== PASSO 1: Criar LISTA VAZIA ===")
ll = LinkedList()           # INSTANCIA a lista (head=None)
ll.print_list()             # Lista:  → None

print("\n=== PASSO 2: Criar 1º NÓ ===")
node1 = Node("ANA")         # INSTANCIA nó1
ll.head = node1             # LISTA.head APONTA pro nó1
ll.print_list()             # [ANA|next=None] → None

print("\n=== PASSO 3: Criar 2º NÓ ===")
node2 = Node("Beto")        # INSTANCIA nó2
node1.next = node2          # nó1.next APONTA pro nó2
ll.print_list()             # [ANA|next=node2] → [Beto|next=None] → None

print("\n=== PASSO 4: Criar 3º NÓ ===")
node3 = Node("Cris")        # INSTANCIA nó3
node2.next = node3          # nó2.next APONTA pro nó3
ll.print_list()             # ANA→Beto→Cris → None

print("\n=== PASSO 5: Método AUTOMÁTICO ===")
# ll.add_node("Dani")         # MÉTODO adiciona sozinho
ll.print_list()             # ANA→Beto→Cris→Dani → None

