# Classe da Árvore Binária
class No:
     
     def __init__(self, key, dir, esq, dados):
          self.item = key
          self.dir = dir
          self.esq = esq
          self.dados = dados

class Tree:

     def __init__(self):
          self.root = No(None,None,None,None)
          self.root = None

     def setaFilhos(self, atual, esq, dir):
          atual.esq = esq
          atual.dir = dir

     def buscar(self, chave):
         if self.root == None:
              return None 
         atual = self.root 

         while atual.item != chave: 
               if chave < atual.item:
                    atual = atual.esq 
               else:
                    atual = atual.dir 
               if atual == None:
                    return None 
         return atual

     # O sucessor é o Nó mais a esquerda da subarvore a direita do No que foi passado como parametro do metodo
     def nosucessor(self, apaga): # O parametro é a referencia para o No que deseja-se apagar
          paidosucessor = apaga
          sucessor = apaga
          atual = apaga.dir # vai para a subarvore a direita

          while atual != None: # enquanto nao chegar no Nó mais a esquerda
               paidosucessor = sucessor
               sucessor = atual
               atual = atual.esq # caminha para a esquerda

          if sucessor != apaga.dir: 
               paidosucessor.esq = sucessor.dir 
               sucessor.dir = apaga.dir 

          return sucessor

     def remover(self, v):
         if self.root == None:
               return False # se arvore vazia
         atual = self.root
         pai = self.root
         filho_esq = True
         # ****** Buscando o valor **********
         while atual.item != v: # enquanto nao encontrou
               pai = atual
               if v < atual.item: # caminha para esquerda
                    atual = atual.esq
                    filho_esq = True # é filho a esquerda? sim
               else: # caminha para direita
                    atual = atual.dir 
                    filho_esq = False # é filho a esquerda? NAO
               if atual == None:
                    return False # encontrou uma folha -> sai
         # fim laço while de busca do valor

         # **************************************************************
         # se chegou aqui quer dizer que encontrou o valor (v)
         # "atual": contem a referencia ao No a ser eliminado
         # "pai": contem a referencia para o pai do No a ser eliminado
         # "filho_esq": é verdadeiro se atual é filho a esquerda do pai
         # **************************************************************

         # Se nao possui nenhum filho (é uma folha), elimine-o
         if atual.esq == None and atual.dir == None:
               if atual == self.root:
                    self.root = None # se raiz
               else:
                    if filho_esq:
                         pai.esq =  None # se for filho a esquerda do pai
                    else:
                         pai.dir = None # se for filho a direita do pai

         # Se é pai e nao possui um filho a direita, substitui pela subarvore a direita
         elif atual.dir == None:
               if atual == self.root:
                    self.root = atual.esq # se raiz
               else:
                    if filho_esq:
                         pai.esq = atual.esq # se for filho a esquerda do pai
                    else:
                         pai.dir = atual.esq # se for filho a direita do pai
         
         # Se é pai e nao possui um filho a esquerda, substitui pela subarvore a esquerda
         elif atual.esq == None:
               if atual == self.root:
                    self.root = atual.dir # se raiz
               else:
                    if filho_esq:
                         pai.esq = atual.dir # se for filho a esquerda do pai
                    else:
                         pai.dir = atual.dir # se for  filho a direita do pai

         # Se possui mais de um filho, se for um avô ou outro grau maior de parentesco
         else:
               sucessor = self.nosucessor(atual)
               # Usando sucessor que seria o Nó mais a esquerda da subarvore a direita do No que deseja-se remover
               if atual == self.root:
                    self.root = sucessor # se raiz
               else:
                    if filho_esq:
                         pai.esq = sucessor # se for filho a esquerda do pai
                    else:
                         pai.dir = sucessor # se for filho a direita do pai
               sucessor.esq = atual.esq # acertando o ponteiro a esquerda do sucessor agora que ele assumiu 
                                        # a posição correta na arvore   

         return True
  
     def inOrder(self, atual):
         if atual != None:
              self.inOrder(atual.esq)
              print(atual.item,end=" ")
              self.inOrder(atual.dir)
  
     def preOrder(self, atual):
         if atual != None:
              print(atual.item,end=" ")
              self.preOrder(atual.esq)
              self.preOrder(atual.dir)
       
     def posOrder(self, atual):
         if atual != None:
              self.posOrder(atual.esq)
              self.posOrder(atual.dir)
              print(atual.item,end=" ")

     def altura(self, atual):
          alt_esq = 0
          if atual.esq:
               alt_esq = self.altura(atual.esq)
          alt_dir = 0
          if atual.dir:
               alt_dir = self.altura(atual.dir)
          return 1 + max(alt_esq, alt_dir)
  
     def balanco(self, atual):
          prof_esq = 0
          if atual.esq:
               prof_esq = self.altura(atual.esq)
          prof_dir = 0
          if atual.dir:
               prof_dir = self.altura(atual.dir)
          return prof_esq - prof_dir     


     def rotacaoEsquerda(self, atual):
          atual.item, atual.dir.item = atual.dir.item, atual.item
          old_esquerda = atual.esq
          self.setaFilhos(atual, atual.dir, atual.dir.dir)
          self.setaFilhos(atual.esq, old_esquerda, atual.esq.esq)

     def rotacaoDireita(self, atual):
          atual.item, atual.esq.item = atual.esq.item, atual.item
          old_direita = atual.dir
          self.setaFilhos(atual, atual.esq.esq, atual.esq)
          self.setaFilhos(atual.dir,atual.dir.dir, old_direita)

     def rotacaoEsquerdaDireita(self, atual):
          self.rotacaoEsquerda(atual.esq)
          self.rotacaoDireita(atual)

     def rotacaoDireitaEsquerda(self, atual):
          self.rotacaoDireita(atual.dir)
          self.rotacaoEsquerda(atual)

     def executaBalanco(self, atual):
        bal = self.balanco(atual)
        if bal > 1:
            if self.balanco(atual.esq) > 0:
                self.rotacaoDireita(atual)
            else:
                self.rotacaoEsquerdaDireita(atual)
        elif bal < -1:
            if self.balanco(atual.dir) < 0:
                self.rotacaoEsquerda(atual)
            else:
                self.rotacaoDireitaEsquerda(atual)

     def inserir(self, v, dados):
          novo = No(v,None,None, dados) # cria um novo Nó
          if self.root == None:
               self.root = novo
          else: # se nao for a raiz
               atual = self.root
               while True:
                    anterior = atual
                    if v <= atual.item: # ir para esquerda
                         atual = atual.esq
                         if atual == None:
                                anterior.esq = novo
                                self.executaBalanco(self.root)
                                return
                    # fim da condição ir a esquerda
                    else: # ir para direita
                         atual = atual.dir
                         if atual == None:
                                 anterior.dir = novo
                                 self.executaBalanco(self.root)
                                 return
                    # fim da condição ir a direita

     def folhas(self, atual):
         if atual == None:
              return 0
         if atual.esq == None and atual.dir == None:
              return 1
         return self.folhas(atual.esq) + self.folhas(atual.dir)

  
     def contarNos(self, atual):
        if atual == None:
             return 0
        else:
             return  1 + self.contarNos(atual.esq) + self.contarNos(atual.dir)

     def minn(self):
         atual = self.root
         anterior = None
         while atual != None:
              anterior = atual
              atual = atual.esq
         return anterior

     def maxx(self):
         atual = self.root
         anterior = None
         while atual != None:
              anterior = atual
              atual = atual.dir
         return anterior

     def caminhar(self):
          print(" Exibindo em ordem: ",end="")
          self.inOrder(self.root)
          print("\n Exibindo em pos-ordem: ",end="")
          self.posOrder(self.root)
          print("\n Exibindo em pre-ordem: ",end="")
          self.preOrder(self.root)
          print("\n Altura da arvore: %d" %(self.altura(self.root)))
          print(" Quantidade de folhas: %d"  %(self.folhas(self.root)))
          print(" Quantidade de Nós: %d" %(self.contarNos(self.root)))
          if self.root != None: # se arvore nao esta vazia
             print(" Valor minimo: %d" %(self.minn().item))
             print(" Valor maximo: %d" %(self.maxx().item))

     def descrever(self):
          print("\n Altura da arvore: %d" %(self.altura(self.root)))
          print(" Quantidade de folhas: %d"  %(self.folhas(self.root)))
          print(" Quantidade de Nós: %d" %(self.contarNos(self.root)))
