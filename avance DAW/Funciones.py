from Area import Area
from Usuario import Usuario
from Tique import Tique
from DAO import DAO
from os import system
from Cliente import Cliente
from beautifultable import BeautifulTable
import getpass
import os
from datetime import datetime

class Funciones:

    d = DAO()
    sesion = Usuario()

    def __init__(self):
        pass

#--------------------------------------------------------------------

    def menuInicial(self):
        while True:
            try:
                system("cls")               
                print("--- MENU INICIAL ---")
                print("1.Iniciar Sesion")
                print("2.Salir")
                op = int(input("Digite Una opcion : "))
                if(op == 1):
                    self.__login()
                elif(op == 2):
                    print("\n--- Gracias Por Utilizar El Sistema!! ---")
                    os._exit(1)
                else:
                    print("\n--- Error De Opcion!! ---\n")
                    system("pause")
            except:
                print("\n--- Error Al Digitar Opcion (Menu Inicial)!! ---\n")
                system("pause")

#--------------------------------------------------------------------

    def menuJefeMesa(self):
        try:
            system("cls")
            print("\n--- MENU JEFE DE MESA "+self.sesion.getNomUsuario().upper()+" ---")
            print("1.Crear Ususario")
            print("2.Administrar Areas")
            print("3.Administrar Tipo de tiques")
            print("4.Administrar Criticidades")
            print("5.Listar Tiques")
            print("6.Cerrar Sesión")
            op = int(input("Digite Una Opcion : "))
            if op == 1:
                self.__crearUsuario()
            elif op == 2:
                self.__adminAreas()
            elif op == 3:
                self.__adminTipoTique()
            elif op == 4:
                print(4)
                system("pause")
                self.menuJefeMesa()
            elif op == 5:
                print(5)
                system("pause")
                self.menuJefeMesa()
            elif op== 6:
                print("\n--- Cerrando Sesión... ---")
                system("pause")	
                self.menuInicial()
                #self.__salir()
                #os._exit(1)
            else:
                print("\n--- Opcion Invalida ---")
        except:
            print("\n--- Error De Opcion Del Menu (MenuAdmin-try)!! ---")
            system("pause")
            self.menuJefeMesa()


    def menuEjecutivoMesa(self):
        while True:
            try:
                system("cls")
                print("\n--- MENU EJECUTIVO DE MESA "+self.sesion.getNomUsuario().upper()+" ---")
                print("1.Crear Tique")
                print("2.Crear Cliente")
                print("3.Cerrar Sesión")
                op = int(input("Digite Una Opcion : "))
                if op == 1:
                    self.__crearTique()
                elif op == 2:
                    self.__crearCliente()
                elif op== 3:
                    print("\n--- Cerrando Sesión... ---")
                    system("pause")	
                    self.menuInicial()
                    #self.__salir()
                    #os._exit(1)
                else:
                    print("\n--- Opcion Invalida (Try Menu Mesa) ---") 
            except:
                print("\n--- Error De Opcion Del Menu (MenuMesa-try) ---")
                system("pause")
                self.menuEjecutivoMesa()

#---------MENU AREAS-------------------------------------------------

    def __adminAreas(self):
        while True:
            try:
                system("cls")
                print("\n--- ADMINISTRAR AREAS ["+self.sesion.getNomUsuario().upper()+"] ---")
                print("1.Crear Area")
                print("2.Editar Area")
                print("3.Eliminar Area")
                print("4.Volver")
                op = int(input("Digite Una Opcion : "))
                if op == 1:
                    self.__crearArea()
                elif op == 2:
                    self.__editarArea()
                elif op == 3:
                    self.__eliminarArea()
                elif op == 4:
                    self.menuJefeMesa()
                else:
                    print("\n--- Error De Opcion Del Menu ---")	
            except:
                print("\n--- Error De Opcion Del Menu (Areas-try) ---")
                system("pause")
                self.adminAreas()

#--------------------------------------------------------------------

    def __adminTipoTique(self):
        while True:
            try:
                system("cls")
                print("\n--- ADMINISTRAR TIPO TIQUE ["+self.sesion.getNomUsuario().upper()+"] ---")
                print("1.Editar Tipo Tique")
                print("2.Volver")
                op = int(input("Digite Una Opcion : "))
                if op == 1:
                    self.__editarTipoTique()
                elif op == 2:
                    self.__menuJefeMesa()
                else:
                    print("\n--- Error De Opcion Del Menu ---")	
            except:
                print("\n--- Error De Opcion Del Menu (Areas-try) ---")
                system("pause")
                self.adminAreas()

#--------------------------------------------------------------------

    def __login(self):
        while True:
            try:
                system("cls")               
                print("--- LOGIN ---")
                ema = input("Digite El Email de Usuario : ")
                if len(ema)<1 or len(ema)>30:
                    print("\n--- Debe Tener Entre 1 y 30 Caracteres!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error Al Ingresar Nombre De Usuario (LOGIN)!! ---")
                system("pause")

        while True:
            try:
                system("cls")               
                print("--- LOGIN ---")
                #pas = input("Digite La Contraseña Del Usuario ("+nom.upper()+") : ")
                pas = getpass.getpass("Digite La Contraseña Del Usuario ("+ema.upper()+") : ")
                if len(pas)<1 or len(pas)>50:
                    print("\n--- Debe Tener Entre 1 y 50 Caracteres!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error Al Ingresar Contraseña (Login)!! ---")
                system("pause")
    
        system("cls")
        r = self.d.iniciarSesion(ema, pas)
        print(r)
        if r is None:
            print("\n--- Error De Usuario y/o Contraseña!! ---\n")
            system("pause")
            self.menuInicial()
        
        else:
            print(145)
            self.sesion.setIdUsuario(r[0])
            print(147)
            self.sesion.setNomUsuario(r[1])
            print(149)
            self.sesion.setApeUsuario(r[2])
            print(151)
            self.sesion.setPasUsuario(r[3])
            print(153)
            self.sesion.setEmaUsuario(r[4])
            print(155)
            self.sesion.setRolUsuario(r[5])
            print(157)
            if self.sesion.getRolUsuario() == 1:
                print(159)
                system("cls")
                print("\n--- Bienvenido "+self.sesion.getEmaUsuario().upper()+" ---")
                system("pause")
                self.menuJefeMesa()

            elif self.sesion.getRolUsuario() == 2:
                print(157)
                system("cls")
                print("\n--- Bienvenido "+self.sesion.getEmaUsuario().upper()+" ---")
                system("pause")
                self.menuEjecutivoArea()

            else:
                print(164)
                system("cls")
                print("\n--- Bienvenido "+self.sesion.getEmaUsuario().upper()+" ---")
                system("pause")
                self.menuEjecutivoMesa()

#--------------------------------------------------------------------

    def __crearUsuario(self):
        """ EMAIL """
        while True:
            try:
                system("cls")
                ema= input("Digite El Email del Usuario a Registrar : ")
                if len(ema.strip())<1 or len(ema.strip())>50:
                    print("\n--- El Email Debe Tener Entre 1 y 50 Caracteres!! ---")
                    system("pause")
                else:
                    r = self.d.comprobarEmailUsuario(ema)
                    if r is not None:
                        print("\n--- El Email de Usuario (",ema,") Ya Existe!! ---\n")
                        system("pause")
                    else:
                        break
            except:
                print("\n--- Error Al Intentar Almacenar El Nombre De Usuario!! ---")
                system("pause")

        """ NOMBRE """
        while True:
            try:
                system("cls")
                nom = input("Digite El Nombre del Usuario a Registrar : ")
                if len(nom.strip())<1 or len(nom.strip())>50:
                    print("\n--- El Nombre Debe Tener Entre 1 y 50 Caracteres!! ---")
                    system("pause")
                else:
                    break

            except:
                print("\n--- Error Al Intentar Almacenar El Nombre De Usuario!! ---")
                system("pause")

        """ APELLIDO """
        while True:
            try:
                system("cls")
                ape = input("Digite El Apellido del Usuario a Registrar : ")
                if len(ape.strip())<1 or len(ape.strip())>50:
                    print("\n--- El Apellido Debe Tener Entre 1 y 50 Caracteres!! ---")
                    system("pause")
                else:
                    break

            except:
                print("\n--- Error Al Intentar Almacenar El Nombre De Usuario!! ---")
                system("pause")

        """ ROL"""
        while True:
            try:
                system("cls")
                rol = int(input("Digite El Rol del Usuario a Registrar :\n1.Jefe de Mesa. \n2.Ejecutivo de Area.\n3.Ejecutivo de Mesa.\n "))
                if rol != 1 and rol != 2 and rol != 3:
                    print("\n--- Error Al Digitar El Rol!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error Al Digitar El Rol!! (try)---")
                system("pause")

        """ CONTRASEÑA """
        while True:
            try:
                system("cls")
                pas1 = getpass.getpass("Digite La Password Del Usuario ("+str(ema.upper())+") : ")
                if len(pas1.strip())<1 or len(pas1.strip())>50:
                    print("\n--- Debe Tener Entre 1 y 50 Caracteres!! ---\n")
                    system("pause")
                else:
                    pas2 = getpass.getpass("Repita La Password Del Usuario ("+str(ema.upper())+") : ")
                    if pas1 != pas2:
                        print("\n--- Las Contraseñas No Coinciden!! ---\n")
                        system("pause")
                    else:
                        break
            except:
                print("\n--- Error Al Intentar Almacenar La Password!! ---")
                system("pause")

        u = Usuario()
        u.setEmaUsuario(ema.upper())
        u.setNomUsuario(nom.upper())
        u.setApeUsuario(ape.upper())
        u.setRolUsuario(rol)
        u.setPasUsuario(pas1.upper())
        
        self.d.agregarUsuario(u)
        system("cls")
        print("\n--- Cuenta de Usuario (",ema,") Creada Correctamente!! ---\n")
        system("pause")
        self.menuJefeMesa()

#--------------------------------------------------------------------

    def __crearArea(self):
        """ NOMBRE AREA"""
        while True:
            try:
                system("cls")
                nom= input("Digite El Nombre del Area a Crear : ")
                if len(nom.strip())<1 or len(nom.strip())>50:
                    print("\n--- El Nombre de Area Debe Tener Entre 1 y 50 Caracteres!! ---")
                    system("pause")
                else:
                    r = self.d.comprobarNombreArea(nom)
                    if r is not None:
                        print("\n--- El Nombre de Area (",nom,") Ya Existe!! ---\n")
                        system("pause")
                    else:
                        break
            except:
                print("\n--- Error Al Intentar Almacenar El Nombre De Area ---")
                system("pause")

        """ SELECCIONAR EJECUTIVO AREA"""
        while True:
            gente = self.d.obtenerEjecutivoArea()
            print("\n--- Ejecutivos de Area ---")	
            tabla = BeautifulTable()
            for x in gente:
                tabla.rows.append([x[0], x[1] , x[2], x[3]])
                tabla.columns.header = ["ID", "NOMBRE", "APELLIDO", "EMAIL"]
            print(tabla)

            try:
                eje = int(input("\n--- Digite El ID del Ejecutivo de Area a Asignar ---\n"))
                if eje<0 or eje>99999:
                    print("\n--- Debe Tener Entre 1 y 5 Digitos ---")
                    system("pause")
                
                else: 
                    res = self.d.comprobarIdEjecutivo(eje) 
                    if res is None: 
                        print("\n--- El ID (",eje,") No Existe ---")
                        system("pause")
                    else:
                        print("Break else")
                        break
            except:
                print("\n--- Error Al Intentar Almacenar El ID!! ---")
                system("pause")
        
        a = Area()
        a.setNomArea(nom.upper())
        a.setNomEje(res[0] + " "+res[1])
        self.d.agregarArea(a)
        system("cls")
        print("--- Area (",nom,") Agregada Correctamente ---")
        system("pause")
        self.menuJefeMesa()

#--------------------------------------------------------------------

    def __editarArea(self):
        """ NOMBRE AREA"""
        while True:
            gente = self.d.obtenerArea()
            print("\n--- Area ---")	
            tabla = BeautifulTable()
            for x in gente:
                tabla.rows.append([x[0], x[1] , x[2]])
                tabla.columns.header = ["ID", "NOMBRE", "EJECUTIVO"]
            print(tabla)
            system
            try:
                are= int(input("Digite El ID del Area a Editar : \n"))
                if are<0 or are>99999:
                    print("\n--- El ID de Area Debe ser mayor a 0 y menor a 99999 ---")
                    system("pause")
                else:
                    r = self.d.comprobarIdArea(are)
                    if r is None:
                        print("\n--- El Id de Area (",are,") No Existe ---")
                        system("pause")
                    else:
                        break
            except:
                print("\n--- Error Al Intentar Almacenar El Nombre De Area ---")
                system("pause")

        """ SELECCIONAR EJECUTIVO AREA"""
        while True:
            gente = self.d.obtenerEjecutivoArea()
            print("\n--- Ejecutivos de Area ---")	
            tabla = BeautifulTable()
            for x in gente:
                tabla.rows.append([x[0], x[1] , x[2], x[3]])
                tabla.columns.header = ["ID", "NOMBRE", "APELLIDO", "EMAIL"]
            print(tabla)

            try:
                eje = int(input("\n--- Digite El ID del Ejecutivo de Area a Asignar ---\n"))
                if eje<0 or eje>99999:
                    print("\n--- Debe Tener Entre 1 y 5 Digitos ---")
                    system("pause")
                
                else:
                    res = self.d.comprobarIdEjecutivo(eje)                  
                    if res is None: 
                        print("\n--- El ID (",eje,") No Existe ---")
                        system("pause")
                    else:
                        break
            except:
                print("\n--- Error Al Intentar Almacenar El ID!! ---")
        a = Area() 
        a.setNomEje(res[0] + " "+res[1])
        a.setIdArea(are)
        self.d.editarArea(a)
        system("cls")
        print("--- Area Editada Correctamente ---")
        system("pause")
        self.menuJefeMesa()

#--------------------------------------------------------------------

    def __eliminarArea(self):
        """ NOMBRE AREA"""
        while True:
            gente = self.d.obtenerArea()
            print("\n--- Area ---")	
            tabla = BeautifulTable()
            for x in gente:
                tabla.rows.append([x[0], x[1] , x[2]])
                tabla.columns.header = ["ID", "NOMBRE", "EJECUTIVO"]
            print(tabla)
            system
            try:
                are= int(input("Digite El ID del Area a Eliminar : \n"))
                if are<0 or are>99999:
                    print("\n--- El ID de Area Debe ser mayor a 0 y menor a 99999 ---")
                    system("pause")
                else:
                    print(388)
                    r = self.d.comprobarIdArea(are)
                    print(390)
                    if r is None:
                        print("\n--- El Id de Area (",are,") No Existe ---")
                        system("pause")
                    else:
                        break
            except:
                print("\n--- Error Al Intentar Eliminar Area ---")
                system("pause")
        print(399)
        self.d.eliminarArea(are)
        print(401)
        system("cls")
        print("--- Area Eliminada Correctamente ---")
        system("pause")
        self.menuJefeMesa()

#--------------------------------------------------------------------

    def __crearCliente(self):
        system("cls")
        while True:
            try:
                system("cls")
                nom= input("Digite El Nombre del Cliente a Registrar : ")
                if len(nom.strip())<1 or len(nom.strip())>50:
                    print("\n--- El Email Debe Tener Entre 1 y 50 Caracteres!! ---")
                    system("pause")
                else:
                    r = self.d.comprobarNombrelUsuario(nom)
                    if r is not None:
                        print("\n--- El Email de Usuario (",nom,") Ya Existe!! ---\n")
                        system("pause")
                    else:
                        break
            except:
                print("\n--- Error al crear cliente ---")
                system("pause")

        while True:
            try:
                system("cls")
                rut = input("Digite El Rut del Cliente a Registrar : ")
                if len(rut.strip())<9 or len(rut.strip())>10:
                    print("\n--- El Email Debe Tener Entre 9 y 10 Caracteres!! ---")
                    system("pause")
                else:
                    r = self.d.comprobarRutCliente(rut)
                    if r is not None:
                        print("\n--- El Rut de Cliente (",rut,") Ya Existe!! ---\n")
                        system("pause")
                    else:
                        break
        
            except:
                print("\n--- Error al crear cliente ---")
                system("pause")

        while True:
            try:
                system("cls")
                dir = input("Digite La Direccion del Cliente a Registrar : ")
                if len(dir.strip())<1 or len(dir.strip())>50:
                    print("\n--- El Email Debe Tener Entre 1 y 50 Caracteres!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error al Guardar Direccion cliente ---")
                system("pause")
        
        while True:
            try:
                system("cls")
                con = input("Digite El Contacto del Cliente a Registrar : ")
                if len(con.strip())<1 or len(con.strip())>50:
                    print("\n--- El Email Debe Tener Entre 1 y 50 Caracteres!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error al Guardar Telefono cliente ---")
                system("pause")
                
        c = Cliente()
        c.setNomCliente(nom)
        c.setRutCliente(rut)
        c.setDireccion(dir)
        c.setContacto(con)
        self.d.crearCliente(c)
        system("cls")
        print("--- Cliente Creado Correctamente ---")
        system("pause")
        self.menuEjecutivoMesa()

#--------------------------------------------------------------------

    def __crearTique(self):
        system("cls")

        """ SELECCIONAR CLIENTE"""
        while True:
            gente = self.d.obtenerClientes()
            print("\n--- CLIENTES ---")	
            tabla = BeautifulTable()
            for x in gente:
                tabla.rows.append([x[0], x[1] , x[2], x[3], x[4]])
                tabla.columns.header = ["ID", "NOMBRE", "RUT", "DIRECCION", "CONTACTO"]
            print(tabla)

            try:
                cli = int(input("\n--- Digite El ID del Cliente a Usar ---\n"))
                if cli<0 or cli>99999:
                    print("\n--- Debe Tener Entre 1 y 5 Digitos ---")
                    system("pause")
                
                else:
                    res_cli = self.d.comprobarIdCliente(cli)                  
                    if res_cli is None: 
                        print("\n--- El ID (",cli,") No Existe ---")
                        system("pause")
                    else:
                        break
            except:
                print("\n--- Error Al Intentar Almacenar El ID ---")
                system("pause")	


        """ ASUNTO """
        while True:
            try:
                system("cls")
                asu = input("Digite el Asunto del Tique a Registrar : \n")
                if len(asu.strip())<1 or len(asu.strip())>50:
                    print("\n--- El Asunto Debe Tener Entre 1 y 50 Caracteres!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error al guardar Asunto ---")
                system("pause")
        
        """ DETALLE """
        while True:
            try:
                system("cls")
                det = input("Digite el detalle del Tique a Registrar : \n")
                if len(det.strip())<1 or len(det.strip())>100:
                    print("\n--- El Detalle Debe Tener Entre 1 y 100 Caracteres!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error al guardar Fecha ---")
                system("pause")

        """ PROBLEMA """
        while True:
            try:
                system("cls")
                pro = input("Digite el Problema del Tique a Registrar : \n")
                if len(pro.strip())<1 or len(pro.strip())>100:
                    print("\n--- El Problema Debe Tener Entre 1 y 100Caracteres!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error al guardar Fecha ---")
                system("pause")

        """ AREA """
        while True:
            print(621)
            areas = self.d.obtenerAreas()
            print(623)
            print("\n--- AREAS ---")	
            tabla = BeautifulTable()
            for x in areas:
                tabla.rows.append([x[0], x[1] , x[2]])
                tabla.columns.header = ["ID", "NOMBRE", "EJECUTIVO"]
            print(tabla)

            try:
                are = int(input("\n--- Digite El ID del Area ---\n"))
                if are<0 or are>99999:
                    print("\n--- Debe Tener Entre 1 y 5 Digitos ---")
                    system("pause")
                
                else:
                    res = self.d.comprobarIdArea(are)                  
                    if res is None: 
                        print("\n--- El ID (",are,") No Existe ---")
                        system("pause")
                    else:
                        break
            except:
                print("\n--- Error Al Intentar Almacenar El ID ---")
                system("pause")

        res_area = self.d.obtenerEjeAre(res)
        print(res_area)
        system("pause")

        """ ESTADO """
        while True:
            try:
                system("cls")
                print("1. A RESOLUCION")
                print("2. RESUELTO")
                est = int(input("Digite el Estado del Tique a Registrar : \n"))
                if est != 1 and est != 2:
                    print("\n--- Debe elegir opcion 1 o 2  ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error al guardar Estado---")
                system("pause")
        
        """ CRITICIDAD """
        while True:
            try:
                system("cls")
                print("1. BAJA")
                print("2. NORMAL")
                print("3. URGENTE")
                cri = int(input("Digite la criticidad del Tique a Registrar : \n"))
                if cri != 1 and cri != 2 and cri != 3:
                    print("\n--- Debe elegir opcion 1, 2 o 3.  ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error al guardar Criticidad---")
                system("pause")
        
        """ TIPO """
        while True:
            try:
                system("cls")
                print("1. PROBLEMA")
                print("2. RECLAMO")
                print("3. CONSULTA")
                print("4. FELICITACION")
                tip = int(input("Digite el Tipo del Tique a Registrar : \n"))
                if tip != 1 and tip != 2 and tip != 3 and tip != 4:
                    print("\n--- Debe elegir opcion 1, 2, 3 o 4.  ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error al guardar Tipo---")
                system("pause")

        """ DATE """
        print(702)
        now = datetime.now()
        print(704)
        """ EJECUTIVO DE MESA """
        id = self.sesion.getIdUsuario()
        print(id)
        ejem = self.d.obtenerEjecutivoMesa(id)
        print(709)

        t = Tique()
        print(712)
        t.setIdCliente(res_cli[0])
        print(714)
        t.setIdUsuario (id)
        print(716)
        t.setIdArea(res[0])
        print(718)
        t.setAsuTique(asu)
        print(720)
        t.setDetServicio(det)
        print(722)
        t.setDetProblema(pro)
        print(724)
        t.setEjeArea(res_area)
        print(726)
        t.setEstTique(est)
        print(728)
        t.setCriticidad(cri)
        print(730)
        t.setTipTique(tip)
        print(732)
        t.setFecCreacion(now)
        print(734)
        t.setEjeMesa(ejem[1] + " " + ejem[2])
        print(736)
        self.d.crearTique(t)
        print(738)
        system("cls")	
        print("\n--- Tique Creado Exitosamente ---")
        system("pause")
        self.menuEjecutivoMesa()

#--------------------------------------------------------------------

    def __editarTipoTique(self):
        """ OBTENER TIQUES """
        while True:
            tiques = self.d.obtenerTiques()
            print("\n--- TIQUES ---")	
            tabla = BeautifulTable()
            for x in tiques:
                tabla.rows.append([x[0], x[1] , x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9]])
                tabla.columns.header = ["ID", "ASUNTO", "SERVICIO", "PROBLEMA", "EJECUTIVO AREA", "CRITICIDAD", "EJECUTIVO MESA", "CLIENTE", "AREA", "TIPO"]
            print(tabla)
            try:
                tiq = int(input("Digite el ID del Tique a Editar : \n"))
                if tiq<0 or tiq>99999:
                    print("\n--- Debe Tener Entre 1 y 5 Digitos ---")
                    system("pause")
                else:
                    r = self.d.comprobarIdTique(tiq)
                    if r is None:
                        print("\n--- El El Tique de ID (",tiq,") No Existe ---")
                        system("pause")
                    else:
                        break            
            except:
                print("\n--- Error al Editar Tipo de Tique ---")
                system("pause")
        
        """ ELEGIR TIPO DE TIQUE """
        while True:
            try:
                system("cls")
                print("1. PROBLEMA")
                print("2. RECLAMO")
                print("3. CONSULTA")
                print("4. FELICITACION")
                tip = int(input("Digite el  Nuevo Tipo del Tique : \n"))
                if tip != 1 and tip != 2 and tip != 3 and tip != 4:
                    print("\n--- Debe elegir opcion 1, 2, 3 o 4.  ---")
                    system("pause")
                else:
                    break
            
            except:
                print("\n--- Error al Editar Tipo de Tique ---")
                system("pause")

        t = Tique()
        t.setIdTique(tiq)
        t.setTipTique(tip)
        self.d.editarTipoTique(t)
        system("cls")
        print("\n--- Tipo de Tique Editado Exitosamente ---")
        system("pause")
        self.menuJefeMesa()










