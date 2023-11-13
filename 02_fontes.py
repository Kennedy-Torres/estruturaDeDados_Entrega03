# Exemplos em código:

# ----------------- 01. PARA LISTA ENCADEADA -----------------
class NodoLista:
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo


    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)


class ListaEncadeada:
    def __init__(self):
        self.cabeca = None


    def __repr__(self):
        return " [" + str (self.cabeca) + "]"
    
lista = ListaEncadeada()
nodo1 = NodoLista(1)
nodo2 = NodoLista(2)
nodo3 = NodoLista(3)

lista.cabeca = nodo1

nodo1.proximo = nodo2
nodo2.proximo = nodo3
print("+=====================================+")
print("|            Lista encadeada          |")
print("+=====================================+")
print(lista)


# ----------------- 02. PARA LISTA CIRCULAR -----------------
class Node():
    def __init__(self,data : str):
        self.data : str = data
        self.next : Node = None
        self.prev : Node = None

class double_linked():

    def __init__(self):
        self.head : Node = None
        self.end  : Node = None
    
    def append(self,data: str):

        new_node = Node(data)
        
        if self.end != None:
            new_node.prev = self.end
            self.end.next = new_node
            self.end = new_node
            return
        
        self.head = new_node
        self.end  = new_node
    
    def __str__(self):
        result = ""
        temp_node = self.head
        
        while temp_node != None:
            result += temp_node.data + ","
            temp_node = temp_node.next
        return result 

    def find(self,data : str) -> Node:
     
        temp_node = self.head

        while temp_node != None:
            if temp_node.data == data:
                return temp_node
            
            temp_node = temp_node.next

        return None

    def print_reverse(self) -> str:
  
        result = ""
        temp_node = self.end

        while temp_node != None:
            result += temp_node.data + ","
            temp_node = temp_node.prev
        
        return result
        

if __name__ == "__main__":
    list_double = double_linked()
    list_double.append("Python")
    list_double.append("JavaScript")
    list_double.append("Java")

print("+=====================================+")
print("|            Lista circular           |")
print("+=====================================+")
print("List :  " , str(list_double))
print("List reverse: ", list_double.print_reverse())
print("Find ", list_double.find("Java").data)



# ----------------- 03. PARA ESTRUTURA DE ÁRVORE -----------------
# Em específico uma árvore binária balanceada
class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita
        
    def __repr__(self, nivel=0, prefixo='Raiz: '):
        ret = ' ' * nivel * 4 + prefixo + repr(self.chave) + '\n'
        if self.esquerda:
            ret += self.esquerda.__repr__(nivel + 1, 'Esquerda: ')
        if self.direita:
            ret += self.direita.__repr__(nivel + 1, 'Direita: ')
        return ret
        
def insere(raiz, nodo): 
    if raiz is None:
        raiz = nodo 

    elif raiz.chave < nodo.chave:
        if raiz.direita is None:
            raiz.direita = nodo
        else:
            insere(raiz.direita, nodo)

    else:
        if raiz.esquerda is None:
            raiz.esquerda = nodo
        else:
            insere(raiz.esquerda, nodo)        

def altura(nodo):
    if nodo is None:
        return 0
    return 1 + max(altura(nodo.esquerda), altura(nodo.direita))

def is_balanced(nodo):
    if nodo is None:
        return True

    esquerda_altura = altura(nodo.esquerda)
    direita_altura = altura(nodo.direita)

    if abs(esquerda_altura - direita_altura) <= 1 and is_balanced(nodo.esquerda) and is_balanced(nodo.direita):
        return True

    return False


raiz = NodoArvore(10)
chaves = [5, 15, 3, 7, 12, 17]
for chave in chaves:
	nodo = NodoArvore(chave)
	insere(raiz, nodo)

print("+=====================================+")
print("|         Estrutura de árvore         |")
print("+=====================================+")
print(raiz)

if is_balanced(raiz):
    print("A árvore é balanceada.")
else:
    print("A árvore não é balanceada.")

print("+=====================================+")

# ----------------- 04. PARA BUSCA SEQUÊNCIAL -----------------
def busca_sequencial_string(lista, alvo):
    for i, nome in enumerate(lista):
        if nome == alvo:
            return i  # Retorna o índice do nome alvo se encontrado

    return -1  # Retorna -1 se o nome alvo não for encontrado na lista

# Exemplo de uso
lista_nomes = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"]
nome_alvo = "Eva"
resultado = busca_sequencial_string(lista_nomes, nome_alvo)

print("+=====================================+")
print("|            Busca sequêncial         |")
print("+=====================================+")
print("Minha lista = ",lista_nomes)
print("OBJETIVO: SABER A POSIÇÃO QUE Eva está na lista\n")

if resultado != -1:
    print(f'O nome {nome_alvo} está na posição {resultado} da lista.')
else:
    print(f'O nome {nome_alvo} não está na lista.')




# ----------------- 05. PARA BUSCA BINÁRIA -----------------

def busca_binaria(lista, alvo):

    inicio, fim = 0, len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2  

      
        if lista[meio] == alvo:
            return meio  

       
        elif lista[meio] > alvo:
            fim = meio - 1


        else:
            inicio = meio + 1

    return -1  

minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
alvo = 5
resultado = busca_binaria(minha_lista, alvo)
print("+=====================================+")
print("|            Busca binária            |")
print("+=====================================+")
print("Minha lista = ",minha_lista)
print("OBJETIVO: SABER A POSIÇÃO QUE ESTÁ O NUMERO 5\n")

if resultado != -1:
    print(f'O elemento {alvo} está na posição {resultado} da lista.')
else:
    print(f'O elemento {alvo} não está na lista.')
    
print("+=====================================+")