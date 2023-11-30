#Actividad 6 - Juan Miguel Durango Posada
#Nota: Mientras terminaba el código me di cuenta que pude haber hecho que
#Cada boton al ser presionado borrara también los campos de texto de Nombre y Número
#Sin embargo no sabia si seria lo mas intuitivo o si seria una molestia
#Asi que, por decisión personal: las cajas de texto deben ser borradas a mano y los labels no se borrarán amenos que se actualicen con nueva información.
import tkinter
import os

#Ventana
ventana = tkinter.Tk()
ventana.geometry("500x700")
ventana.resizable(0,0)

#LabelsNota
labNombre = tkinter.Label(ventana, text= "Nombre")
labNombre.place(x=90,y=30,width=70,height=25)
labCodigo = tkinter.Label(ventana, text= "Numero")
labCodigo.place(x=90,y=60,width=70,height=25)

#CajasTextoNota
txtNombre = tkinter.Entry(ventana)
txtNombre.place(x=180,y=30,width=200,height=25)
txtCodigo = tkinter.Entry(ventana)
txtCodigo.place(x=180,y=60,width=200,height=25)

#LabelsResultados
labMensaje = tkinter.Label(ventana, text= "")
labMensaje.place(x=20,y=150,width=450,height=25)
labDatos = tkinter.Label(ventana, text= "")
labDatos.place(x=20,y=180,width=450,height=600)


#Funciones
#Funcion create para crear y añadir a la lista
def create():
    try:
        new_name = txtNombre.get()
        new_number = int(txtCodigo.get())

        name_number_string = ''
        name = ''
        number = 0
        found = False

        file_name = "friendsContact.txt"

        if not os.path.exists(file_name):
            open(file_name, 'w').close()

        with open(file_name, 'r+') as file:

            while file.tell() < os.path.getsize(file_name):

                name_number_string = file.readline().rstrip('\n')

                line_split = name_number_string.split("!")

                name = line_split[0]
                number = int(line_split[1])

                if name == new_name or number == new_number:
                    found = True
                    break

            if not found:

                name_number_string = f"{new_name}!{new_number}"

                file.write(name_number_string + "\n")

                labMensaje.config(text="Amigo añadido.")
            else:

                labMensaje.config(text="El nombre ingresado ya existe.")

    except Exception as e:
        print(e)

#Funcion read que lee y muestra en interfaz los contactos con nombre y numero
def read():
    try:
        name_number_string = ''
        name = ''
        number = 0
        file_name = "friendsContact.txt"

        if not os.path.exists(file_name):

            open(file_name, 'w').close()
        result_string = ""

        with open(file_name, 'r') as file:
        
            for line in file:
                
                name_number_string = line.rstrip('\n')
                line_split = name_number_string.split("!")

                if len(line_split) >= 2:

                    name = line_split[0]
                    number = int(line_split[1])

                    result_string += (
                        "Nombre del amigo: " + name + "\n"
                        "Número de contacto: " + str(number) + "\n\n"
                    )
                    labDatos.config(text=result_string)

    except Exception as e:
        print(e)

#Funcion Update que cambia el numero del contacto especificado
def update():
    try:
        new_name = txtNombre.get()
        new_number = int(txtCodigo.get())

        name_number_string = ''
        name = ''
        number = 0
        index = 0

        file_name = "friendsContact.txt"
        temp_file_name = "temp.txt"

        if not os.path.exists(file_name):
        
            open(file_name, 'w').close()

        with open(file_name, 'r') as file, open(temp_file_name, 'w') as temp_file:
            found = False

            while file.tell() < os.path.getsize(file_name):
                name_number_string = file.readline().rstrip('\n')
                line_split = name_number_string.split("!")

                name = line_split[0]
                number = int(line_split[1])

                if name == new_name:
                    found = True
                    labMensaje.config(text=f"El contacto: {name} - {number} ha sido cambiado")
                    name_number_string = f"{name}!{new_number}"

                temp_file.write(name_number_string + '\n')

            if not found:
                labMensaje.config(text="El nombre ingresado no existe")
        os.replace(temp_file_name, file_name)

    except Exception as e:
        print(e)

#Función delete que borra los datos del nombre especificado
def delete():
    try:
        new_name = txtNombre.get()
        name_number_string = ''
        name = ''
        number = 0
        index = 0

        file_name = "friendsContact.txt"
        temp_file_name = "temp.txt"

        if not os.path.exists(file_name):
            open(file_name, 'w').close()

        with open(file_name, 'r') as file, open(temp_file_name, 'w') as temp_file:
            found = False

            while file.tell() < os.path.getsize(file_name):
                name_number_string = file.readline().rstrip('\n')

                line_split = name_number_string.split("!")

                name = line_split[0]

                if name == new_name:
                    found = True
                    labMensaje.config(text=f"Se ha eliminado {name}")

                    continue

                temp_file.write(name_number_string + '\n')

            if not found:
                labMensaje.config(text="El nombre ingresado no existe.")

        os.replace(temp_file_name, file_name)

    except Exception as e:
        print(e)

#Botones
btnCreate = tkinter.Button(ventana, text= "Crear", command=create)
btnCreate.place(x=110,y=110,width=70,height=25)
btnRead = tkinter.Button(ventana, text= "Leer", command=read)
btnRead.place(x=190,y=110,width=70,height=25)
btnUpdate = tkinter.Button(ventana, text= "Actualizar", command=update)
btnUpdate.place(x=270,y=110,width=70,height=25)
btnDelete = tkinter.Button(ventana, text= "Borrar", command=delete)
btnDelete.place(x=350,y=110,width=70,height=25)


#mainloop
ventana.mainloop()