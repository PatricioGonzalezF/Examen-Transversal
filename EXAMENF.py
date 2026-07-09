#diccionario inicial 
Planes = {
    #CodigoDelPlan: [Nombre/TipoDePlan, DuracionEnMeses, AccesoPiscina(T/F), IncluyeClases(T/F), Horario]
    'F001': ['Plan Basico', 'Mensual', 1, False, False, 'Libre'],
    'F002': ['Plan Full', 'Mensual', 1, True, True, 'Libre'],
    'F003': ['Plan Estudiante', 'Trimestral', 3, False, True, 'Tarde'],
    'F004': ['Plan Senior', 'Trimestral', 3, True, False, 'Mañana'],
    'F005': ['Plan Anual Pro', 'Anual', 12, True, True, 'Libre'],
    'f006': ['Plan Nocturno', 'Mensual', 1, False, True, 'Noche']
};

Inscripciones = {
    #CodigoDelPlan: [PrecioMensualPlan, CuposInscripcionDisponibles]
    'F001': [14990, 30],
    'F002': [22990, 10],
    'F003': [39990, 0],
    'F004': [35990, 6],
    'F005': [15990, 2],
    'F006': [18990, 15]
};

def Menu():
    print("")
    print("====== MENÚ PRINCIPAL ======");
    print("1. Cupos por Tipo de Plan ");
    print("2. Busqueda de Planes por Rango de Precio ");
    print("3. Actualizar Precio de Plan ");
    print("4. Agregar Plan ");
    print("5. Eliminar Plan");
    print("6. Salir ");
    print("===========================");
    print("");

def Leer_opc():
    try:
        opc = int(input("Ingrese una opcion(entre 1y6): "));
        return opc;
    except ValueError:
        return -1;

def Cupos_Tipo(Tipo, Planes):
    Total_Cupos = 0;
    for NombrePlan in Planes:

        if(Planes[NombrePlan][0].Lower() == Tipo.Lower()):
            if(NombrePlan in Inscripciones):
                Total_Cupos += Inscripciones[NombrePlan][1];

    print(f"El Stock es: {Total_Cupos}");

def BusquedaDePrecio(P_min, P_max, Inscripciones):
    encontrados = [];
    for NombrePlan in Inscripciones:
            precio = Inscripciones[NombrePlan][0];
            cantidad = Inscripciones[NombrePlan][1];

            if(precio >= P_min and precio <= P_max and cantidad > 0):
                Tipo = Planes[NombrePlan][0];

                encontrados.append(f"{Tipo}--{NombrePlan}");

    if(len(encontrados) == 0):
        print("no hay planes en ese rango de precios.");
    else:
        encontrados.sort();
        print((f"los planes entre los precios que consultas son: {encontrados}"));

def buscar_codigo(codigo, inscripciones):
    return codigo in inscripciones

def actualizar_precio(NombrePlan, p, Inscripciones ):
    if(NombrePlan in Inscripciones):
        Inscripciones[NombrePlan][0] = p;
        return True;

    return False;

def validar_codigo(codigo, inscripciones):
    return(codigo.strip() != "" and codigo not in inscripciones)

def validar_plan(plan):
    return(plan.strip() != "")

def validar_tipo(tipo):
    return(tipo == "mensual", tipo == "trimestral" and tipo == "anual")

def validar_duracion(duracion):
    return(duracion > 0)

def validar_acceso_piscina(acceso, s, n):
    if (acceso == s):
        return True
    elif (acceso == n):
        return False
    
def validar_incluye_clases(acceso, s, n):
    if (acceso == s):
        return True
    elif (acceso == n):
        return False
    
def validar_horario(horario):
    return(horario.strip() != "")

def validar_cupos(cupos):
    return(cupos > 0)

def validar_precio(precio):
    return(precio >= 0)

while True:
    Menu();
    opc = Leer_opc();

    if(opc == 1):
        Tipo = input("ingrese el plan a consultar: ");
        Cupos_Tipo(Tipo);
    elif(opc == 2):
        while True:
            try:
                P_min = int(input("ingrese precio minimo: "));
                P_max = int(input("Ingrese el precio maximo: "));
                break;
            except ValueError:
                print("Debe ingresar Valores Enteros!!")

        BusquedaDePrecio(P_min, P_max, Inscripciones);
    elif(opc == 3):
        while True:
            NombrePlan = input("Ingrese el modelo a actualizar: ");
            try:
                Precio_nuevo = int(input("Ingrese precio Nuevo: "));
                Resultado = actualizar_precio(NombrePlan, Precio_nuevo);

                if(Resultado):
                    print("Precio Actualizado!!");
                else:
                    print("El modelo no existe!");
            except ValueError:
                print("Debe ingresar valores enteros");
                continue;

            resp = input("\nDesea actualizar otro precio (s/n): ");
            if(resp.lower() != 'Si' and resp.lower() != 's'):
                    break;
            print("");
    
    elif(opc == 4):
        nuevoCodigo = input("Ingrese el codigo: ");
        validar_codigo
        nuevoNombre = input("ingrese el nuevo nombre: ");
        nuevoTipo = input("ingrese el nuevo tipo: ");
        validar_tipo
        nuevoDuracion = input("ingrese la duracion: ");
        validar_duracion
        nuevoAccPiscina = input("ingrese el acceso a piscina: ");
        validar_acceso_piscina
        nuevoIncluyeClases = input("ingrese si incluye clases: ");
        validar_incluye_clases
        nuevoHorario = input("ingrese el horario: ");
        validar_horario
        nuevoPrecio = int(input("ingrese el precio nuevo: "));
        validar_precio
        nuevoCupos = int(input("ingrese los cupos del nuevo programa: "));
        validar_cupos

    elif(opc == 6):
        print("programa Finalizado.");
        break;
    else:
        print("Debe seleccionar una opcion valida!")
