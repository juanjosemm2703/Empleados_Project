from datetime import datetime

personas = [
    {"idPersona": "1", "Nombre": "Juan", "Apellido": "Infante", "correo": "juaninfante", "CC": 123456789, "Rol": 3,
     "Contrasena": "212125"},
    {"idPersona": "2", "Nombre": "Carlos", "Apellido": "Pinilla", "correo": "carlospinilla", "CC": 1012151316,
     "Rol": 2, "Contrasena": "212124"},
    {"idPersona": "3", "Nombre": "Sebastian", "Apellido": "Jimenez", "correo": "sebastianjimenez", "CC": 132544653,
     "Rol": 1, "Contrasena": "212123"},
    {"idPersona": "4", "Nombre": "Rene", "Apellido": "Curiel", "correo": "renecuriel", "CC": 21646216412,
     "Rol": 3, "Contrasena": "12345"}
]

rol = {1: "Superadministrador", 2: "administradores", 3: "empleados"}

empleados = [{"idempleados": "1", "FechaIngreso": "27/03/2022", "TipoContrato": "Prestacion de Servicios",
              "FechaTerminoContrato": "27/03/2025", "Cargo": "Ingeniero", "Dependencia": "Ingenieria",
              "Salario": 2500000},
                {"idempleados": "4", "FechaIngreso": "15/06/1996", "TipoContrato": "Prestacion de Servicios",
              "FechaTerminoContrato": "28/11/2030", "Cargo": "vendedor", "Dependencia": "Finanzas",
              "Salario": 2500000},
             ]

administradores = [{"idadministradores": "2", "FechaIngreso": "16/02/2000", "TipoContrato": "Termino Fijo",
                    "FechaTerminoContrato": "28/03/2025", "Cargo": "Contador", "Dependencia": "Finanzas",
                    "Salario": 3500000}]

Superadministrador = [
    {"idSuperadministrador": "3", "FechaIngreso": "20/03/2022", "Cargo": "Gerente", "Dependencia": "Finanzas",
     "Salario": 25000000}]

def buscar_persona(id):
    for persona in personas:
        if str(id) == persona["idPersona"]:
            datos_persona = list(persona.values())
            exist = True
            break
        else:
            exist = False

    if exist:
        for rol_usuario in rol:
            if persona["Rol"] == rol_usuario:
                rol_usuario = rol[rol_usuario]
                if rol_usuario == "empleados":
                    tabla = empleados
                if rol_usuario == "administradores":
                    tabla = administradores
                if rol_usuario == "Superadministrador":
                    tabla = Superadministrador
                break
  
   
    for persona in tabla:
        
        if persona["id"+rol_usuario] == datos_persona[0]:
            for clave, valor in persona.items():
                datos_persona.append(valor)

    usuario = {
        "id": datos_persona[0],
        "nombre": datos_persona[1],
        "apellido": datos_persona[2],
        "correo": datos_persona[3],
        "cedula": datos_persona[4],
        "rol_id": datos_persona[5],
        "rol": rol_usuario,
        "fecha_ingreso": datetime.strptime(datos_persona[8], '%d/%m/%Y').date(),
        "contrato": datos_persona[9],
        "fecha_contrato": datetime.strptime(datos_persona[10], '%d/%m/%Y').date(),
        "cargo": datos_persona[11],
        "dependencia": datos_persona[12]
    }
    
    return usuario

buscar_persona(2)


listaTablaEmpleados = []
listaTablaAdministradores = []

for persona in personas:
    for empleado in empleados:
        if empleado["idempleados"] == persona["idPersona"]:
            listaTablaEmpleados.append([persona["Nombre"], persona["Apellido"], persona['Rol'], empleado["Cargo"],
                                        empleado["Dependencia"], empleado["FechaIngreso"], empleado["idempleados"]])
for persona in personas:
    for administrador in administradores:
        if administrador["idadministradores"] == persona["idPersona"]:
            listaTablaAdministradores.append(
                [persona["Nombre"], persona["Apellido"], persona['Rol'], administrador["Cargo"],
                 administrador["Dependencia"], administrador["FechaIngreso"], administrador["idadministradores"]])

Lista = []
for i in listaTablaEmpleados:
    Lista.append(i)
for i in listaTablaAdministradores:
    Lista.append(i)


