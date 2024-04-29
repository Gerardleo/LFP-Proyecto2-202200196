from tkinter import *
import tkinter as tk
from tkinter import Tk, Menu, scrolledtext, messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from analizadores.lexico import instruccion, operar_
from printer import *
import webbrowser
from Error.Errores import Errores


erroresLexicos = None
erroresSintaticos = None
tokens = None

class VentanaPrincipal:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Proyecto2 | 202200196 ")
        self.centrar(self.ventana, 825, 650)
        self.ventana.configure(bg="RoyalBlue3")  # Cambiado el color de fondo a blanco
        self.pantallas()
        self.crear_menu()

    def centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        anchura_pantalla = r.winfo_screenwidth()
        x = (anchura_pantalla//2)-(ancho//2)
        y = (altura_pantalla//2)-(alto//2)
        r.geometry(f"+{x}+{y}")

    def pantallas(self):
        self.Frame = Frame(height=500, width=1200)
        self.Frame.config(bg="white")  # Cambiado el color de fondo a blanco
        self.Frame.pack(padx=25, pady=25)
        self.text = ''
        posiciony1 = 265
        self.cuadroTexto = scrolledtext.ScrolledText(self.Frame, font=(
            "Times New Roman", 15), fg='black', bg="white", width=150, height=10)
        self.cuadroTexto2 = scrolledtext.ScrolledText(self.Frame, font=(
            "Times New Roman", 15), fg='black', bg="white", width=150, height=10)
        self.cuadroTexto.place(x=0, y=0)
        self.cuadroTexto2.place(x=0, y=posiciony1)
        self.cuadroTexto2.config(state='disabled')


    def crear_menu(self):
        menu_principal = Menu(self.ventana)
        self.ventana.config(menu=menu_principal)
        menu_archivo = Menu(menu_principal, tearoff=0)
        menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
        menu_archivo.add_command(label="Abrir Archivo", command=self.abrir_archivo)
        menu_archivo.add_command(label="Analizar archivo", command=self.analizar_archivo)
        menu_archivo.add_command(label="Guardar", command=self.guardar_archivo)
        menu_archivo.add_command(label="Limpiar", command=self.limpiar)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.ventana.quit)

        menu_editar = Menu(menu_principal, tearoff=0)
        menu_principal.add_cascade(label="Reportes", menu=menu_editar)
        menu_editar.add_command(label="Reporte de tokens", command=lambda: abrirReporteTokens())
        menu_editar.add_command(label="Reporte de Errores Lexicos ", command=lambda: abrirReporteErrores())
        menu_editar.add_command(label="Reporte de Errores Sintatictos", command=lambda: abrirReporteErroresSintaticos())

    def abrir_archivo(self):
        x = ""
        self.archivo_seleccionado = ''
        Tk().withdraw()
        try:
            self.archivo_seleccionado = filename = askopenfilename(
                title="Seleccione un archivo", filetypes=[("Archivos lfp", f"*.lfp")])
            with open(filename, encoding="utf-8") as infile:
                x = infile.read()   
            self.texto = x
            # Elimina contenido del cuadro
            self.cuadroTexto.delete(1.0, "end")
            # set contenido
            self.cuadroTexto.insert(1.0, self.texto)
            self.ventana.title(f"Proyecto 2 - {self.archivo_seleccionado}")

        except:
            messagebox.showerror(
                "Error", "Archivo no soportado", exception=Exception)
            return        

    def analizar_archivo(self):
        global tokens, erroresLexicos, erroresSintaticos
        prin = Printer()
        try:
            entrada = open(self.archivo_seleccionado, "r").read()

            tokens,erroresLexicos,erroresSintaticos = instruccion(entrada)
            generar_reporte_tokens(tokens)
            reporteErroresLexicos(erroresLexicos)
            

            for token in tokens:
                print(token.lexema)

            resultado_instrucciones = operar_()


            for respuesta in resultado_instrucciones:
                valor,error,fila,columna,char= respuesta.ejecutarT()
                if error != None:
                    erroresSintaticos.append(Errores('Sintactico',char,error,fila,columna))
                else:
                    prin.addLine(valor)
            reporteSintatico(erroresSintaticos)
            texto = prin.print()
            print(texto)
                #color del texto
            if len(erroresLexicos) > 0 or len(erroresSintaticos) > 0:
                texto = ">>" + "Se encontraron Errores" + "\n"
            self.cuadroTexto2.tag_configure("red", foreground="red")
            self.cuadroTexto2.config(state='normal', bg="snow2")  # Habilita la edición del widget de texto
            self.cuadroTexto2.delete(1.0, END)  # Borra cualquier contenido previo
            self.cuadroTexto2.insert(END, texto, 'red')  # Inserta el contenido del archivo
            self.cuadroTexto2.config(state='disabled')  # Deshabilita la edición del widget de texto
            return

        except Exception as e:
            texto = ">>" + "Error en el sistema" + "\n"
            self.cuadroTexto2.tag_configure("red", foreground="red")
                #insertar en el cuadro de texto
            self.cuadroTexto2.config(state='normal', bg="snow2")  # Habilita la edición del widget de texto
            self.cuadroTexto2.delete(1.0, END)  # Borra cualquier contenido previo
            self.cuadroTexto2.insert(END, texto, 'red')  # Inserta el contenido del archivo
            self.cuadroTexto2.config(state='disabled')
            return



    def guardar_archivo(self):
        if self.archivo_seleccionado:
            contenido = self.cuadroTexto.get("1.0", "end-1c")
            with open(self.archivo_seleccionado, 'w') as archivo:
                archivo.write(contenido)
            messagebox.showinfo(
                title="Guardado",
                message=f"El contenido se ha guardado en {self.archivo_seleccionado}."
            )
            self.ventana.title(f"Proyecto 2 - {self.archivo_seleccionado}")
        else:
            messagebox.showwarning(
                title="Advertencia",
                message="No se ha abierto ningún archivo para guardar."
            )
            return
        
    def limpiar(self):
        global erroresLexicos, erroresSintaticos, tokens
        self.cuadroTexto.delete(1.0, END)
        self.cuadroTexto2.config(state='normal', bg="snow2")  # Habilita la edición del widget de texto
        self.cuadroTexto2.delete(1.0, END)  # Borra cualquier contenido previo
        self.cuadroTexto2.config(state='disabled')        
        self.ventana.title("Proyecto2 | 202200196 ")
        self.archivo_seleccionado = ''
        self.texto = ''
        tokens = []
        erroresLexicos = None
        erroresSintaticos = None
        messagebox.showinfo("Limpiar", "Se limpiaron los datos")

    
    def mainloop(self):
        self.ventana.mainloop()

def generar_reporte_tokens(tokens):
        # Estilos CSS para la tabla
    css = """
        <style>
            body {
                font-family: Arial, sans-serif;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 20px;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
            tr:nth-child(even) {
                background-color: #f9f9f9;
            }
            tr:hover {
                background-color: #f1f1f1;
            }
        </style>
        """

        # Encabezado y apertura de tabla
    html = f"""
    <!DOCTYPE html>
        <html>
        <head>
            <title>Reporte de Tokens</title>
            {css}
        </head>
        <body>
            <h1 style="text-align: center;">Reporte de Tokens</h1>
            <table>
                <tr>
                    <th>Token</th>
                    <th>Lexema</th>
                    <th>Fila</th>
                    <th>Columna</th>
                </tr>
        """

        # Generar filas para cada token
    for token in tokens:
        html += f"""
            <tr>
                <td>{token.tipo}</td>
                <td>{token.lexema}</td>
                <td>{token.fila}</td>
                <td>{token.columna}</td>
            </tr>
        """

        # Cerrar tabla y archivo HTML
    html += """
        </table>
    </body>
    </html>
        """

        # Escribir HTML en un archivo
    with open('tokens.html', 'w') as f:
        f.write(html)

def abrirReporteTokens():
    webbrowser.open('tokens.html')

def abrirReporteErrores():
    webbrowser.open('erroresLexicos.html')

def abrirReporteErroresSintaticos():
    webbrowser.open('erroresSintaticos.html')


def reporteErroresLexicos(erroresLexicos):
    contadorn = 1
    # Estilos CSS para la tabla
    css = """
        <style>
            body {
                font-family: Arial, sans-serif;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 20px;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
            tr:nth-child(even) {
                background-color: #f9f9f9;
            }
            tr:hover {
                background-color: #f1f1f1;
            }
        </style>
        """

        # Encabezado y apertura de tabla
    html = f"""
    <!DOCTYPE html>
        <html>
        <head>
            <title>Reporte de Errores Lexicos</title>
            {css}
        </head>
        <body>
            <h1 style="text-align: center;">Reporte de Errores Lexicos</h1>
            <table>
                <tr>
                    <th>N.</th>
                    <th>tipo</th>
                    <th>Mensaje</th>
                    <th>Lexema</th>
                    <th>Fila</th>
                    <th>Columna</th>
                </tr>
        """

        # Generar filas para cada token
    for error in erroresLexicos:
        html += f"""
            <tr>
                <td>{contadorn}</td>
                <td>{error.tipo}</td>
                <td>{error.mensaje}</td>
                <td>{error.lexema}</td>
                <td>{error.fila}</td>
                <td>{error.columna}</td>
            </tr>
        """
        contadorn += 1
        # Cerrar tabla y archivo HTML
    html += """
        </table>
    </body>
    </html>
        """

        # Escribir HTML en un archivo
    with open('erroresLexicos.html', 'w') as f:
        f.write(html)

def reporteSintatico(erroresSintaticos):
    # Estilos CSS para la tabla
    contadorn = 1
    css = """
        <style>
            body {
                font-family: Arial, sans-serif;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 20px;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
            tr:nth-child(even) {
                background-color: #f9f9f9;
            }
            tr:hover {
                background-color: #f1f1f1;
            }
        </style>
        """

        # Encabezado y apertura de tabla
    html = f"""
    <!DOCTYPE html>
        <html>
        <head>
            <title>Reporte de Errores Sintaticos</title>
            {css}
        </head>
        <body>
            <h1 style="text-align: center;">Reporte de Errores Sintaticos</h1>
            <table>
                <tr>
                    <th>N.</th>
                    <th>tipo</th>
                    <th>Mensaje</th>
                    <th>Lexema</th>
                    <th>Fila</th>
                    <th>Columna</th>
                </tr>
        """

        # Generar filas para cada token
    for error in erroresSintaticos:
        html += f"""
            <tr>
                <td>{contadorn}</td>
                <td>{error.tipo}</td>
                <td>{error.mensaje}</td>
                <td>{error.lexema}</td>
                <td>{error.fila}</td>
                <td>{error.columna}</td>
            </tr>
        """
        contadorn += 1
        # Cerrar tabla y archivo HTML
    html += """
        </table>
    </body>
    </html>
        """

        # Escribir HTML en un archivo
    with open('erroresSintaticos.html', 'w') as f:
        f.write(html)
            








 


 


if __name__ == "__main__":
    vista=VentanaPrincipal()
    vista.mainloop()
