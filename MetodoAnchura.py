lista=['a','b','c','d','e','f','g','h']
grafo={
    'a':['b','c','g'],
    'b':['a','d','g'],
    'c':['a','d','e'],
    'd':['b','c','f'],
    'e':['c','f','g'],
    'f':['d','e','h'],
    'g':['a','b','e'],
    'h':['f'],
}

def retornaNuevosNodos(listaBusqueda,grafo):
    nuevosVertices=[]
    iteracciones=[]
    for nodoPadre in listaBusqueda:
        for nodoHijo in grafo[nodoPadre]:
            if nodoHijo not in listaBusqueda and nodoHijo not in nuevosVertices:
                print("Nueva iteracion: ",nodoPadre,nodoHijo)
                iteracciones.append([nodoPadre,nodoHijo])
                nuevosVertices.append(nodoHijo)
    return nuevosVertices,iteracciones

def anchura(v,raiz,grafo):
    listaBusqueda=[raiz]
    nuevosVertices = listaBusqueda
    iteracciones = []
    while len(listaBusqueda)!=len(v):
        nuevosVertices,nuevaIteracion = retornaNuevosNodos(listaBusqueda,grafo)
        listaBusqueda += nuevosVertices
        iteracciones += nuevaIteracion 

    print("\nIteraciones: ",iteracciones)

raiz=input("Digite el valor raiz: ")
anchura(lista,raiz,grafo)

