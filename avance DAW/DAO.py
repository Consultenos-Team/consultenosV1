from Usuario import Usuario
from Tique import Tique
from os import system
import pymysql

class DAO:

    def __init__(self):
        pass

#----------------------------------------------------------------------

    def conectar(self):
        self.con = pymysql.connect(
            host = "localhost",
            user = "root",
            password = "",        
            db = "db_consultenos"
        )

        self.cursor = self.con.cursor()
        
#----------------------------------------------------------------------

    def desconectar(self):
        self.con.close()

#----------------------------------------------------------------------

    def iniciarSesion(self, ema, pas):
        u = Usuario()
        try:
            self.conectar()
            sql = "select * from usuario where email_usua=%s and pass_usua=%s"
            val = (ema, pas)
            self.cursor.execute(sql, val)
            rs = self.cursor.fetchone()
            return rs 
            # retorna None o una tupla con los datos.
        except:
            print("\n--- Error Al Iniciar Sesion (DAO)!! ---")

#----------------------------------------------------------------------

    def comprobarEmailUsuario(self, ema):
        try:
            sql = "select email_usua from usuario where email_usua=%s"
            self.conectar()
            self.cursor.execute(sql, ema)
            rs = self.cursor.fetchone()
            self.desconectar()
            return rs
        except:
            print("\n--- Error Al Comprobar Nombre Del Usuario a Registrar (DAO)!! ---")
            system("pause")

#----------------------------------------------------------------------

    def agregarUsuario(self, u):
        try:
            sql = "insert into usuario (nom_usua, ape_usua, pass_usua, email_usua, rol_id) values (%s, %s, %s, %s, %s)"
            val = (u.getNomUsuario(), u.getApeUsuario() ,u.getPasUsuario(), u.getEmaUsuario(), u.getRolUsuario())
            self.conectar()
            self.cursor.execute(sql, val)
            self.con.commit()
            self.desconectar()
        except:
            print("\n--- Error Al Agregar Nuevo Usuario (DAO)!! ---")
            system("pause")

#----------------------------------------------------------------------

    def comprobarNombreArea(self, nom):
        try:
            sql = "select nombre_area from area where nombre_area=%s"
            self.conectar()
            self.cursor.execute(sql, nom)
            rs = self.cursor.fetchone()
            self.desconectar()
            return rs
        except:
            print("\n--- Error Al Comprobar Nombre De Area (DAO) ---")
            system("pause")
#----------------------------------------------------------------------

    def comprobarIdArea(self, are):
        try:
            sql = "select id_area from area where id_area=%s"
            self.conectar()
            self.cursor.execute(sql, are)
            rs = self.cursor.fetchone()
            self.desconectar()
            return rs
        except:
            print("\n--- Error Al Comprobar ID De Area (DAO) ---")
            system("pause")

#----------------------------------------------------------------------

    def obtenerEjecutivoArea(self):
        try:
            #sql = "select id_eje, nom_eje, nom_tip from ejercicios, tipos where ejercicios.id_tip=tipos.id_tip and id_est=1"
            sql = "select id_usua, nom_usua, ape_usua, email_usua from usuario where rol_id=2"
            self.conectar()
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.desconectar()
            return rs
        except:
            print("\n--- Error Al Obtener Ejecutivos de Area (DAO) ---")
            system("pause")

#----------------------------------------------------------------------

    def comprobarIdEjecutivo(self, eje):
        try:
            sql = "select nom_usua, ape_usua from usuario where id_usua=%s and rol_id=2"
            self.conectar()
            self.cursor.execute(sql, eje)
            rs = self.cursor.fetchone()
            self.desconectar()
            return rs
        except:
            print("\n--- Error Al Comprobar ID de Ejecutivo (DAO)!! ---")
            system("pause")

#----------------------------------------------------------------------

    def agregarArea(self, a):
        try:
            sql = "insert into area (nombre_area, ejecutivo_area) values (%s, %s)"
            val = (a.getNomArea(), a.getNomEje())
            self.conectar()
            self.cursor.execute(sql, val)
            self.con.commit()
            self.desconectar()
        except:
            print("\n--- Error Al Agregar Area (DAO)!! ---")
            system("pause")

#----------------------------------------------------------------------

    def obtenerArea(self):
        try:
            sql = "select * from area"
            self.conectar()
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.desconectar()
            return rs
        except:
            print("\n--- Error Al Obtener Area (DAO) ---")
            system("pause")

#----------------------------------------------------------------------

    def editarArea(self, a):
        try:
            sql = "update area set ejecutivo_area = (%s) where id_area=%s"
            val = (a.getNomEje(), a.getIdArea())
            self.conectar()
            self.cursor.execute(sql, val)
            self.con.commit()
            self.desconectar()
        except:
            print("\n--- Error Al Editar Area (DAO)!! ---")
            system("pause")

#----------------------------------------------------------------------

    def eliminarArea(self, are):
        try:
            print(174)
            sql = "delete from area where id_area=%s"
            print(176)
            self.conectar()
            print(178)
            self.cursor.execute(sql, are)
            print(180)
            self.con.commit()
            self.desconectar()
        except:
            print("\n--- Error Al Eliminar Area (DAO)!! ---")
            system("pause")

#----------------------------------------------------------------------

    def obtenerClientes(self):
        try:
            sql = "select * from cliente"
            self.conectar()
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.desconectar()
            return rs
        except:
            print("\n--- Error Al Obtener Clientes (DAO) ---")
            system("pause")

#----------------------------------------------------------------------

    def comprobarNombreCliente(self, nom):
        try:
            sql = "select nom_cliente from cliente where nom_cliente=%s"
            self.conectar()
            self.cursor.execute(sql, nom)
            rs = self.cursor.fetchone()
            self.desconectar()
            return rs
        except:
            print("\n--- Error Al Comprobar Nombre De Area (DAO) ---")
            system("pause")

#----------------------------------------------------------------------

    def comprobarRutCliente(self, rut):
        try:
            sql = "select rut_cliente from cliente where rut_cliente=%s"
            self.conectar()
            self.cursor.execute(sql, rut)
            rs = self.cursor.fetchone()
            self.desconectar()
            return rs
        except:
            print("\n--- Error Al Comprobar Nombre De Area (DAO) ---")
            system("pause")

#----------------------------------------------------------------------

    def comprobarIdCliente(self, cli):
        try:
            sql = "select * from cliente where id_cliente=%s"
            self.conectar()
            self.cursor.execute(sql, cli)
            rs = self.cursor.fetchone()
            self.desconectar()
            return rs
        except:
            print("\n--- Error Al Comprobar ID de CLiente (DAO)!! ---")
            system("pause")

#----------------------------------------------------------------------

    def obtenerEjecutivoMesa(self, id):
        try:
            #sql = "select id_eje, nom_eje, nom_tip from ejercicios, tipos where ejercicios.id_tip=tipos.id_tip and id_est=1"
            sql = "select * from usuario where id_usua=%s and rol_id=3"
            self.conectar()
            self.cursor.execute(sql, id)
            rs = self.cursor.fetchone()
            self.desconectar()
            return rs
        except:
            print("\n--- Error Al Obtener Ejecutivos de Mesa (DAO) ---")
            system("pause")

#----------------------------------------------------------------------

    def obtenerAreas(self):
        try:
            sql = "select * from area"
            self.conectar()
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.desconectar()
            return rs
        except:
            print("\n--- Error Al Obtener Areas (DAO) ---")
            system("pause")

#----------------------------------------------------------------------

    def crearTique(self, t):
        try:
            print(275)
            sql = "insert into tickets (id_cliente, id_usuario, id_area, asun_ticket, det_servicio, problema, ejecutivo_area, est_ticket, criticidad, tip_ticket, fec_creacion, ejecutivo_mesa) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            print(277)
            val = (t.getIdCliente(), t.getIdUsuario(), t.getIdArea(), t.getAsuTique(), t.getDetServicio(), t.getDetProblema(), t.getEjeArea(), t.getEstTique(), t.getCriticidad(), t.getTipTique(), t.getFecCreacion(), t.getEjeMesa())
            print(279)
            self.conectar()
            print(281)
            self.cursor.execute(sql, val)
            print(283)
            self.con.commit()
            print(285)
            self.desconectar()
        except:
            print("\n--- Error Al Crear Tique (DAO)!! ---")
            system("pause")

#----------------------------------------------------------------------

    def obtenerEjeAre(self, res):
        try:
            sql = "select ejecutivo_area from area where id_area = %s"
            self.conectar()
            self.cursor.execute(sql, res)
            rs = self.cursor.fetchall()
            self.desconectar()
            return rs
        except:
            print("\n--- Error Al Obtener Areas (DAO) ---")
            system("pause")

#----------------------------------------------------------------------

    def obtenerTiques(self):
        try:
            sql = "select tickets.id_ticket, tickets.asun_ticket, tickets.det_servicio, tickets.problema, tickets.ejecutivo_area, tickets.criticidad, tickets.ejecutivo_mesa, cliente.nom_cliente, area.nombre_area from tickets inner join cliente on tickets.id_cliente = cliente.id_cliente inner join area on tickets.id_area = area.id_area;"
            self.conectar()
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.desconectar()
            return rs
        except:
            print("\n--- Error Al Obtener Areas (DAO) ---")
            system("pause")

#----------------------------------------------------------------------

    def comprobarIdTique(self, tiq):
        try:
            sql = "select * from tickets where id_ticket=%s"
            self.conectar()
            self.cursor.execute(sql, tiq)
            rs = self.cursor.fetchone()
            self.desconectar()
            return rs
        except:
            print("\n--- Error Al Comprobar ID de CLiente (DAO)!! ---")
            system("pause")

#----------------------------------------------------------------------

    def editarTipoTique(self, t):
        try:
            sql = "update tickets set tip_ticket = (%s) where id_ticket=%s"
            val = (t.getTipTique(), t.getIdTique())
            self.conectar()
            self.cursor.execute(sql, val)
            self.con.commit()
            self.desconectar()
        except:
            print("\n--- Error Al Editar Tipo Tique (DAO)!! ---")
            system("pause")

#----------------------------------------------------------------------
