#Melanie R. Morataya
#Arbol Binario
import os

class node():
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None

class arbol():
    def __init__(self):
        self.raiz = None
        
    def ingresar(self, nodo, dato):
        if nodo == None:
            nodo = node(dato)
        else:
            nodo2 = nodo.dato
            if dato < nodo2:
                nodo.izquierdo = self.ingresar(nodo.izquierdo, dato)
            else:
                nodo.derecho = self.ingresar(nodo.derecho, dato)
        return nodo

    def inorder(self, nodo):
        if nodo == None:
            return None
        else:
            self.inorder(nodo.izquierdo)
            print(nodo.dato)
            self.inorder(nodo.derecho)

    def preorder(self, nodo):
        if nodo == None:
            return None
        else:
            print(nodo.dato)
            self.preorder(nodo.izquierdo)
            self.preorder(nodo.derecho)

    def postorder(self, nodo):
        if nodo == None:
            return None
        else:
            self.postorder(nodo.izquierdo)
            self.postorder(nodo.derecho)
            print(nodo.dato)

    def buscar(self, dato, nodo):
        if nodo == None:
            return None
        else:
            if dato == nodo.dato:
                return nodo.dato
            else:
                if dato < nodo.dato:
                    return self.buscar(dato, nodo.izquierdo)
                else:
                    return self.buscar(dato, nodo.derecho)

tree = arbol()

while True:
    os.system("cls")
    print("EXAMEN ARBOL BINARIO")
    opc = input("\n1.-Ingresar nodo \n2.-Recorrido Inorden \n3.-Recorrido Preorden \n4.-Recorrido Postorden \n5.-Buscar \n6.-Salir \n\nIngresa una opcion -> ")

    if opc == '1':
        nodos = input("\nIngrese un nodo: ")
        if nodos.isdigit():
            nodos = int(nodos)
            tree.raiz = tree.ingresar(tree.raiz, nodos)
        else:
            print("\nIngrese solo numeros")
    elif opc == '2':
        if tree.raiz == None:
            print("Vacio")
        else:
            tree.inorder(tree.raiz)
    elif opc == '3':
        if tree.raiz == None:
            print("Vacio")
        else:
            tree.preorder(tree.raiz)
    elif opc == '4':
        if tree.raiz == None:
            print("Vacio")
        else:
            tree.postorder(tree.raiz)
    elif opc == '5':
        nodos = input("\nCual es el nodo a encontrar?: ")
        if nodos.isdigit():
            nodos = int(nodos)
            if tree.buscar(nodos, tree.raiz) == None:
                print("\nNodo no encontrado")
            else:
                print("\nNodo ",tree.buscar(nodos, tree.raiz), " si existe")
        else:
            print("\nIngrese solo numeros")        
    elif opc == '6':
        print("\nSALIENDO\n")
        os.system("pause")
        break
    else:
        print("\nElige una opcion de 1 a 6")
    print()
    os.system("pause")

print()