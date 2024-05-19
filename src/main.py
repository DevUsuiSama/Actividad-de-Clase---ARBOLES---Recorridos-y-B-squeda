#
# Actividad de Clase - ARBOLES - Recorridos y Búsqueda
#
# Alumnos: José Fernando Usui
#

import os
import timeit

# Función para limpiar la pantalla
clear = lambda: os.system('cls')

class Persona:
    def __init__(self, idi, nombre, apellido, pais, ciudad, genero) -> None:
        self.idi = idi
        self.nombre = nombre
        self.apellido = apellido
        self.pais = pais
        self.ciudad = ciudad
        self.genero = genero

class Nodo:
    def __init__(self, dato: Persona) -> None:
        self.dato = dato
        self.izquierda: Nodo = None
        self.derecha: Nodo = None

class Tree:
    def __init__(self) -> None:
        self.root = None
        self.contar_dfs: int = 0
        self.contar_bfs: int = 0
    # Aquí ocurre la magia
    def insertar(self, nodo: Nodo) -> None:
        self.root = self.insertar_aux(self.root, nodo)
    # El propósito de está función es de servir de auxiliar para que solo podamos insertar un único argumento.
    def insertar_aux(self, root: Nodo, nodo: Nodo) -> None:
        if root is None:
            return nodo
        else:
            if len(root.dato.apellido) > len(nodo.dato.apellido):
                root.izquierda = self.insertar_aux(root.izquierda, nodo)
            else:
                root.derecha = self.insertar_aux(root.derecha, nodo)
            return root
    # Obtener la altura del árbol
    def height(self, root: Nodo) -> int:
        if root is None:
            return 0
        else:
            izq_height = self.height(root.izquierda)
            der_height = self.height(root.derecha)
            if izq_height > der_height:
                return izq_height + 1
            else:
                return der_height + 1
    # 1: búsqueda DFS 2: búsqueda BFS
    def buscar(self, apellido: str, tipo: int) -> Nodo:
        self.contar_dfs = 0
        self.contar_bfs = 0
        if tipo == 1:
            return self.buscar_dfs(self.root, apellido)
        elif tipo == 2:
            aux = None
            for i in range(self.height(self.root)):
                aux = self.buscar_bfs(self.root, apellido, 0, i)
                if aux is not None:
                    break
            return aux
        else:
            print('Tipo de recorrido no valido')
            return None
    # búsqueda en profundidad DFS
    def buscar_dfs(self, root: Nodo, apellido: str) -> Nodo:
        if root is not None:
            aux = None
            self.contar_dfs = self.contar_dfs + 1
            aux = self.buscar_dfs(root.izquierda, apellido)
            if aux is None:
                aux = self.buscar_dfs(root.derecha, apellido)
            if root.dato.apellido == apellido:
                return root
            return aux
        else:
            return root
    # búsqueda en anchura o amplitud BFS
    def buscar_bfs(self, root: Nodo, apellido: str, level: int, lvaux: int) -> Nodo:
        if root is not None:
            aux = None
            if root.dato.apellido == apellido:
                return root
            if level > lvaux:
                return None
            self.contar_bfs = self.contar_bfs + 1
            aux = self.buscar_bfs(root.izquierda, apellido, level + 1, lvaux) 
            if aux is None:
                aux = self.buscar_bfs(root.derecha, apellido, level + 1, lvaux)
            return aux
        else:
            return root
    def mostrar_preorden(self, root: Nodo) -> None:
        if root is not None:
            print(f'[{root.dato.idi}; {root.dato.apellido}],', end=' ')
            self.mostrar_preorden(root.izquierda)
            self.mostrar_preorden(root.derecha)
    def mostrar_inorden(self, root: Nodo) -> None:
        if root is not None:
            self.mostrar_inorden(root.izquierda)
            print(f'[{root.dato.idi}; {root.dato.apellido}],', end=' ')
            self.mostrar_inorden(root.derecha)
    def mostrar_postorden(self, root: Nodo) -> None:
        if root is not None:
            self.mostrar_postorden(root.izquierda)
            self.mostrar_postorden(root.derecha)
            print(f'[{root.dato.idi}; {root.dato.apellido}],', end=' ')
    # 1: preorden 2: inorden 3: postorden 4: mostrar en forma gráfica
    def mostrar(self, tipo: int) -> None:
        if tipo == 1:
            self.mostrar_preorden(self.root)
        elif tipo == 2:
            self.mostrar_inorden(self.root)
        elif tipo == 3:
            self.mostrar_postorden(self.root)
        elif tipo == 4:
            self.mostrar_en_forma_grafica(self.root)
        else:
            print('Tipo de recorrido no válido')
    def mostrar_en_forma_grafica(self, root: Nodo, level=0, prefix="Root: "):
        if root is not None:
            print("." * (level * 2) + prefix + str(level) + '. ' + root.dato.apellido)
            self.mostrar_en_forma_grafica(root.izquierda, level + 1, "[Izq]: ")
            self.mostrar_en_forma_grafica(root.derecha, level + 1, "[Der]: ")
    def esta_vacio(self):
        return (self.root is None)

# Nos permite verificar si la opción está dentro del conjunto "lista_de_opcion"
def controlar_opcion(opcion: int, conjunto: list):
    for x in conjunto:
        if opcion == x:
            return True
    return False

def main():
    tree = Tree()
    while True:
        print('Menu:')
        print('1> Insertar Archivo')
        print('2> Recorrido Pre-Orden')
        print('3> Recorrido In-Orden')
        print('4> Recorrido Post-Orden')
        print('5> DFS')
        print('6> BFS')
        print('7> Mostrar Gráfico')
        print('8> Salir')
        print()
        try:
            opcion = int(input('Ingrese una opcion: '))
        except ValueError:
            print('-- Error -- Ingrese un opción valida')
            input('Presione cualquier tecla para continuar...')
            clear()
            continue
        print()
        if controlar_opcion(opcion, [1, 2, 3, 4, 5, 6, 7, 8]):
            if opcion == 1:
                clear()
                dir_archivo = input('Ingresar la dirección del archivo: ')
                '''
                Teniendo en cuenta que el csv esta separando los campos por medio de una coma.
                Establecemos:
                    valores[0] = {x|x sea un identificador}
                    valores[1] = {x|x sea un nombre}
                    valores[2] = {x|x sea un apellido}
                    valores[3] = {x|x sea un país}
                    valores[4] = {x|x sea un ciudad}
                    valores[5] = {x|x sea un genero tipo binario}
                '''
                try:
                    with open(dir_archivo, encoding="utf8") as csvfile:
                        for x in csvfile:
                            valores = x.strip().split(',')
                            tree.insertar(Nodo(Persona(valores[0], valores[1], valores[2], valores[3], valores[4], valores[5])))
                        csvfile.close()
                        print('✔Archivo cargado e insertado en el árbol binario✔')
                except FileExistsError as e:
                    print('Error 😱: ' + e)
                input('Presione cualquier tecla para continuar...')
                clear()
            elif opcion == 2:
                clear()
                print('Pre-Orden:')
                print('---------------------------------------------------------------')
                if tree.esta_vacio():
                    print('❌No hay archivo cargado❌')
                else:
                    tree.mostrar(1)
                print('\n---------------------------------------------------------------')
                input('Presione cualquier tecla para continuar...')
                clear()
            elif opcion == 3:
                clear()
                print('In-Orden:')
                print('---------------------------------------------------------------')
                if tree.esta_vacio():
                    print('❌No hay archivo cargado❌')
                else:
                    tree.mostrar(2)
                print('\n---------------------------------------------------------------')
                input('Presione cualquier tecla para continuar...')
                clear()
            elif opcion == 4:
                clear()
                print('Post-Orden:')
                print('------------------------------------------------')
                if tree.esta_vacio():
                    print('❌No hay archivo cargado❌')
                else:
                    tree.mostrar(3)
                print('\n------------------------------------------------')
                input('Presione cualquier tecla para continuar...')
                clear()
            elif opcion == 5:
                clear()
                print('DFS Búsqueda en Profundidad 😜')
                print('------------------------------------------------')
                if tree.esta_vacio():
                    print('❌No hay archivo cargado❌')
                else:
                    apellido = input('Ingresar apellido: ')
                    start = timeit.default_timer()
                    nodo = tree.buscar(apellido, 1)
                    if nodo is not None:
                        print(f'[{nodo.dato.idi}; {nodo.dato.apellido}]')
                    else:
                        print('Lastimosamente no encontramos el apellido que indicas 😥')
                    print("Tiempo de ejecución: ", timeit.default_timer() - start)
                    print('Total de nodo recorridos: ', tree.contar_dfs)
                print('\n------------------------------------------------')
                input('Presione cualquier tecla para continuar...')
                clear()
            elif opcion == 6:
                clear()
                print('BFS Búsqueda en anchura o amplitud 🧐')
                print('------------------------------------------------')
                if tree.esta_vacio():
                    print('❌No hay archivo cargado❌')
                else:
                    apellido = input('Ingresar apellido: ')
                    start = timeit.default_timer()
                    nodo = tree.buscar(apellido, 2)
                    if nodo is not None:
                        print(f'[{nodo.dato.idi}; {nodo.dato.apellido}]')
                    else:
                        print('Lastimosamente no encontramos el apellido que indicas 😥')
                    print("Tiempo de ejecución :", timeit.default_timer() - start)
                    print('Total de nodo recorridos: ', tree.contar_bfs)
                print('\n------------------------------------------------')
                input('Presione cualquier tecla para continuar...')
                clear()
            elif opcion == 7:
                clear()
                print('------------------------------------------------')
                if tree.esta_vacio():
                    print('❌No hay archivo cargado❌')
                else:
                    tree.mostrar(4)
                print('\n------------------------------------------------')
                input('Presione cualquier tecla para continuar...')
                clear()
            elif opcion == 8:
                break
        else:
            print('-- Error -- La opcion ingresada no existe')
            input('Presione cualquier tecla para continuar...')
            clear()


if __name__ == '__main__':
    main()