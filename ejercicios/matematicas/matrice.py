# Matrices
import flet as ft

def main(page: ft.Page):
    class Matriz:
        def __init__(self) -> None:
            pass

        def conseguir_ceros_renglon(self, list):
            listZero = []
            for i in range(len(list)):
                listZero.append(0)
                for k in range(len(list[i])):
                    if list[i][k] == 0:
                        listZero[i] += 1
            return listZero
        
        def es_cuadro_magico(self,matriz,resultado):
            n = len(matriz)
            if n == 0:
                return False
            for fila in matriz:
                if len(fila) != n:
                    return False
            
            suma_objetivo = sum(matriz[0])
            
            for fila in matriz:
                if sum(fila) != suma_objetivo:
                    return False
            
            suma = 0 
            for i in range(n):
                for j in range(n):
                    suma += matriz[j][i]
                if suma != suma_objetivo:
                    return False
                suma = 0
                    
            suma_diagonal_principal = 0
            suma_diagonal_secundaria = 0
            for i in range(n):
                suma_diagonal_principal += matriz[i][i]
                suma_diagonal_secundaria += matriz[i][len(matriz)-i-1]
            if suma_diagonal_principal != suma_objetivo:
                return False
            if suma_diagonal_secundaria != suma_objetivo:
                return False
            resultado.controls.append(ft.Text(f"Esta es la constante mágica {suma_objetivo}"))
            return True
        
        def suma_matrices(self,lista1,lista2):
            lista = []
            for i in range(len(lista1)):
                lista.append([])
                for k in range(len(lista2)):
                    lista[i].append(0)
                    lista[i][k] = lista1[i][k] + lista2[i][k]
            return lista
        
        def resta_matrices(self,lista1,lista2):
            lista = []
            for i in range(len(lista1)):
                lista.append([])
                for k in range(len(lista2)):
                    lista[i].append(0)
                    lista[i][k] = lista1[i][k] - lista2[i][k]
            return lista
        
        def mult_matrices(self,lista1,lista2):
            lista = []
            for i in range(len(lista1)):
                lista.append([])
                for k in range(len(lista2)):
                    lista[i].append(0)
                    lista[i][k] = lista1[i][k] * lista2[i][k]
            return lista
        
        def div_matrices(self,lista1,lista2):
            lista = []
            for i in range(len(lista1)):
                lista.append([])
                for k in range(len(lista2)):
                    lista[i].append(0)
                    lista[i][k] = lista1[i][k] / lista2[i][k]
            return lista
        
        def hacer_simetria(self, n):
            lista_simetrica = []
            for i in range(n):
                lista_simetrica.append([])
                for k in range(n):
                    lista_simetrica[i].append(0)
                lista_simetrica[i][i] = 1
            return lista_simetrica

                    
    #   Empezo Programa Gráfico  
    columna_cero = ft.Column()
    def handle_btn_conseguir_ceros(e):
        list = []
        columna_cero.controls.clear()
        for i in range(len(inputs.controls)):
            list.append([])
            for j in range(len(inputs.controls[i].controls)):
                list[i].append(float(inputs.controls[i].controls[j].value))
        listZero = matriz.conseguir_ceros_renglon(list)

        for i in range(len(listZero)):
            columna_cero.controls.append(ft.Text(f"Renglón {i}: {listZero[i]}"))
        page.update()        
        
    def handle_conseguir_ceros(e):
        page.controls[0].content.controls.pop()
        btn_cal.visible = False
        columna_cero.controls.clear()
        n = int(inputs.controls[0].value)
        m = int(inputs.controls[1].value)
        inputs.controls.clear()

        for i in range(n):
            inputs.controls.append(ft.Row())
            for j in range(m):
                inputs.controls[i].controls.append(ft.TextField(label="Numero"))
        fila = ft.Row([
            ft.ElevatedButton("Enviar matriz",on_click=handle_btn_conseguir_ceros),
            columna_cero
        ])
        page.controls[0].content.controls.append(fila)
        page.update()

    columna_uno = ft.Column()  
    def handle_btn_c_m(e):
        list = []
        columna_uno.controls.clear()
        n = len(inputs.controls)
        for i in range(n):
            list.append([])
            for j in range(n):
                list[i].append(int(inputs.controls[i].controls[j].value))

        btn_cal.visible = False
        resultado = matriz.es_cuadro_magico(list,columna_uno)
        suma = 0
        for i in range(n):
            columna_uno.controls.append(ft.Text(f"Fila {i}: {sum(list[i])}"))
        for i in range(n):
            for j in range(n):
                suma += list[j][i]
            columna_uno.controls.append(ft.Text(f"Columna {i}: {suma}"))
            suma = 0
        suma_diagonal_principal = 0
        suma_diagonal_secundaria = 0
        for i in range(n):
            suma_diagonal_principal += list[i][i]
            suma_diagonal_secundaria += list[i][n-i-1]
        columna_uno.controls.append(ft.Text(f"Diagonal principal: {suma_diagonal_principal}"))
        columna_uno.controls.append(ft.Text(f"Diagonal secundaria: {suma_diagonal_secundaria}"))

        if resultado:
            columna_uno.controls.append(
                ft.Text(f"La matriz si es un cuadro mágico :D")
            )
        else:
            columna_uno.controls.append(
                ft.Text(f"No es cuadro mágico")
            )
        page.update()

    def handle_cuadro_magico(e):
        page.controls[0].content.controls.pop()
        columna_uno.controls.clear()
        btn_cal.visible = False

        n = int(inputs.controls[0].value)
        inputs.controls.clear()

        for i in range(n):
            inputs.controls.append(ft.Row())
            for j in range(n):
                inputs.controls[i].controls.append(ft.TextField(label="Numero"))
        fila = ft.Row([
            ft.ElevatedButton("Enviar matriz",on_click=handle_btn_c_m),
            columna_uno
        ])
            
        page.controls[0].content.controls.append(fila)
        page.update()

    col_suma = ft.Column()
    col_res = ft.Column()
    col_div = ft.Column()
    col_mult = ft.Column()
    columna_OBM = ft.Container()

    def handle_btn_OBM(e):
        lista1 = []
        lista2 = []
        col_suma.controls.clear()
        col_res.controls.clear()
        col_div.controls.clear()
        col_mult.controls.clear()
        n = int(len(inputs.controls)/2)
        
        for i in range(n):
            lista1.append([])
            lista2.append([])
            for j in range(n):
                lista1[i].append(float(inputs.controls[i].controls[j].value))
                lista2[i].append(float(inputs.controls[i+n].controls[j].value))
        suma = matriz.suma_matrices(lista1,lista2)
        resta = matriz.resta_matrices(lista1,lista2)
        div = matriz.div_matrices(lista1,lista2)
        mult = matriz.mult_matrices(lista1,lista2)
        for i in range(n):
            col_suma.controls.append(ft.Row())
            col_res.controls.append(ft.Row())
            col_div.controls.append(ft.Row())
            col_mult.controls.append(ft.Row())
            for j in range(len(suma)):
                col_suma.controls[i].controls.append(ft.Text(f"{round(suma[i][j],2)}"))
                col_res.controls[i].controls.append(ft.Text(f"{round(resta[i][j],2)}"))
                col_div.controls[i].controls.append(ft.Text(f"{round(div[i][j],2)}"))
                col_mult.controls[i].controls.append(ft.Text(f"{round(mult[i][j],2)}"))
        columna_OBM.content = ft.Column([
            ft.Text("Suma de la matriz"), col_suma,
            ft.Text("Resta de la matriz"), col_res,
            ft.Text("División de la matriz"), col_div,
            ft.Text("Multiplicación de la matriz"), col_mult
        ], scroll=ft.ScrollMode.ALWAYS, height=100)
        page.update()

    def handle_OBM(e):
        page.controls[0].content.controls.pop()
        col_suma.controls.clear()
        col_res.controls.clear()
        col_div.controls.clear()
        col_mult.controls.clear()
        btn_cal.visible = False

        n = int(inputs.controls[0].value)
        m = int(inputs.controls[0].value)
        inputs.controls.clear()

        for i in range(n):
            inputs.controls.append(ft.Row())
            for j in range(m):
                inputs.controls[i].controls.append(ft.TextField(label="Primera Matriz",width=150))

        for i in range(n):
            inputs.controls.append(ft.Row())
            for j in range(m):
                inputs.controls[i+n].controls.append(ft.TextField(label="Segunda Matriz",width=150))

        fila = ft.Row([
            ft.ElevatedButton("Enviar matriz",on_click=handle_btn_OBM),
            columna_OBM
        ])
            
        page.controls[0].content.controls.append(fila)
        page.update()

    def handle_matriz_simetrica(e):
        page.controls[0].content.controls.pop()
        columna = ft.Column(width=100)
        n = int(inputs.controls[0].value)
        inputs.controls[0].value = ""

        lista_simetrica = matriz.hacer_simetria(n)
        for i in range(n):
            columna.controls.append(ft.Row())
            for k in range(n):
                columna.controls[i].controls.append(ft.Text(f"{lista_simetrica[i][k]}"))

        page.controls[0].content.controls.append(columna)
        page.update()

    def cambiar_interfaz(e):
        inputs.controls.clear()
        btn_cal.visible = True
        page.controls[0].content.controls.pop()
        page.controls[0].content.controls.append(ft.Text())
        if menu_options.value == "Contar ceros":
            title.value = "Contar ceros"

            inputs.controls.append(ft.TextField(label="Número de Filas", width=350))
            inputs.controls.append(ft.TextField(label="Número de Columnas", width=350))

            btn_cal.on_click=handle_conseguir_ceros

        if menu_options.value == "Cuadro Mágico":
            title.value = "Tamaño del Cuadro Mágico"

            inputs.controls.append(ft.TextField(label="Tamaño del Cuadro", width=350))

            btn_cal.on_click=handle_cuadro_magico

        if menu_options.value == "Operaciones basicas con matrices":
            title.value = "Operaciones basicas con matrices"
            btn_cal.on_click=handle_OBM
            inputs.controls.append(ft.TextField(label="Tamaño de las Matrices Cuadradas", width=350))

        if menu_options.value == "Matriz simétrica":
            title.value = "Matriz simétrica"
            inputs.controls.append(ft.TextField(label="¿De qué tamaño quieres la matriz?", width=350))
            btn_cal.on_click=handle_matriz_simetrica
        
        page.update()
    
    matriz = Matriz()

    menu_options = ft.Dropdown(options=[
        ft.dropdown.Option("Contar ceros"),
        ft.dropdown.Option("Cuadro Mágico"),
        ft.dropdown.Option("Operaciones basicas con matrices"),
        ft.dropdown.Option("Matriz simétrica")
    ], width=350,border_color="#2267a8", border_width=5,on_change=cambiar_interfaz)
    btn_cal = ft.ElevatedButton("Empezar")
    title = ft.Text("Elige una actividad con matrices",size=20,weight="bold")

    inputs = ft.Column()
    container = ft.Container(
        ft.Column([
            title, menu_options,inputs, btn_cal,ft.Text()]),alignment=ft.alignment.center,
            margin=25)

    page.add(container)

ft.app(main)