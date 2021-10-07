personas = [
    {"idPersona": "1", "Nombre": "Juan", "Apellido": "Infante", "correo": "juaninfante", "CC": 00000000000, "Rol": 3,
     "Contrasena": "212125"},
    {"idPersona": "2", "Nombre": "Carlos", "Apellido": "Pinilla", "correo": "carlospinilla", "CC": 120000000000,
     "Rol": 2, "Contrasena": "212124"},
    {"idPersona": "3", "Nombre": "Sebastian", "Apellido": "Jimenez", "correo": "sebastianjimenez", "CC": 12340000000,
     "Rol": 1, "Contrasena": "212123"},
    {"idPersona": "4", "Nombre": "Rene", "Apellido": "Curiel", "correo": "renecuriel", "CC": 12340000000,
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

# def buscar_persona(id):
#     for persona in personas:
#         if str(id) == persona["idPersona"]:
#             datos_persona = list(persona.keys())
#             exist = True
#             break
#         else:
#             exist = False
#
#     if exist:
#         for rol_usuario in rol:
#             if persona["Rol"] == rol_usuario:
#                 rol_usuario = rol[rol_usuario]
#                 if rol_usuario == "empleados":
#                     tabla = empleados
#                 if rol_usuario == "administradores":
#                     tabla = administradores
#                 if rol_usuario == "Superadministrador":
#                     tabla = Superadministrador
#
#     for persona in tabla:
#         print(persona)
#         if persona["id"+rol_usuario] == datos_persona[0]:
#             for clave, valor in persona.iteritems():
#                 datos_persona.append(valor)
#
#     print(datos_persona)
#
# buscar_persona(1)


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

