-- --------------------------------------------------------
-- Host:                         170.239.87.71
-- Versión del servidor:         10.4.24-MariaDB - Source distribution
-- SO del servidor:              Linux
-- HeidiSQL Versión:             12.0.0.6468
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para db_consultenos
CREATE DATABASE IF NOT EXISTS `db_consultenos` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_spanish_ci */;
USE `db_consultenos`;

-- Volcando estructura para tabla db_consultenos.area
CREATE TABLE IF NOT EXISTS `area` (
  `id_area` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_area` varchar(50) NOT NULL,
  `ejecutivo_area` varchar(50) NOT NULL,
  PRIMARY KEY (`id_area`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla db_consultenos.area: ~3 rows (aproximadamente)
INSERT INTO `area` (`id_area`, `nombre_area`, `ejecutivo_area`) VALUES
	(1, 'Soporte TI', 'Patrick Aguilar'),
	(2, 'Soporte BI', 'Miguel Rojas'),
	(3, 'Soporte Cloud', 'Jorge Canales'),
	(4, 'SUSHI', 'Patrick Aguilar');

-- Volcando estructura para tabla db_consultenos.cliente
CREATE TABLE IF NOT EXISTS `cliente` (
  `id_cliente` int(11) NOT NULL AUTO_INCREMENT,
  `nom_cliente` varchar(50) NOT NULL,
  `rut_cliente` varchar(10) NOT NULL,
  `direccion` varchar(50) NOT NULL,
  `contacto` varchar(50) NOT NULL,
  PRIMARY KEY (`id_cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla db_consultenos.cliente: ~2 rows (aproximadamente)
INSERT INTO `cliente` (`id_cliente`, `nom_cliente`, `rut_cliente`, `direccion`, `contacto`) VALUES
	(1, 'INACAP', '77.777.777', 'Av Vicuña Mackena, Santiago RM', '+569999999'),
	(2, 'CODELCO', '96.666.666', 'Av Millan, Rancagua, IV Región', '+5699999999'),
	(3, 'AGROSUPER', '99.666.555', 'Lo Miranda, Rancagua VI Región', '+5699765515');

-- Volcando estructura para tabla db_consultenos.criticidad
CREATE TABLE IF NOT EXISTS `criticidad` (
  `id_crit` int(11) NOT NULL,
  `desc_crit` varchar(50) NOT NULL,
  PRIMARY KEY (`id_crit`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla db_consultenos.criticidad: ~3 rows (aproximadamente)
INSERT INTO `criticidad` (`id_crit`, `desc_crit`) VALUES
	(1, 'BAJA'),
	(2, 'NORMAL'),
	(3, 'URGENTE');

-- Volcando estructura para tabla db_consultenos.estado
CREATE TABLE IF NOT EXISTS `estado` (
  `id_est` int(11) NOT NULL,
  `desc_est` varchar(50) NOT NULL,
  PRIMARY KEY (`id_est`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla db_consultenos.estado: ~3 rows (aproximadamente)
INSERT INTO `estado` (`id_est`, `desc_est`) VALUES
	(1, 'A RESOLUCION'),
	(2, 'RESUELTO'),
	(3, 'NO APLICA');

-- Volcando estructura para tabla db_consultenos.rol
CREATE TABLE IF NOT EXISTS `rol` (
  `id_rol` int(11) NOT NULL AUTO_INCREMENT,
  `des_rol` varchar(50) NOT NULL,
  PRIMARY KEY (`id_rol`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla db_consultenos.rol: ~2 rows (aproximadamente)
INSERT INTO `rol` (`id_rol`, `des_rol`) VALUES
	(1, 'Jefe de mesa'),
	(2, 'Ejecutivo de area'),
	(3, 'Ejecutivo de mesa');


-- Volcando estructura para tabla db_consultenos.tipo
CREATE TABLE IF NOT EXISTS `tipo` (
  `id_tip` int(11) NOT NULL AUTO_INCREMENT,
  `desc_tip` varchar(50) NOT NULL,
  PRIMARY KEY (`id_tip`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla db_consultenos.tipo: ~4 rows (aproximadamente)
INSERT INTO `tipo` (`id_tip`, `desc_tip`) VALUES
	(1, 'PROBLEMA'),
	(2, 'RECLAMO'),
	(3, 'CONSULTA'),
	(4, 'FELICITACION');

-- Volcando estructura para tabla db_consultenos.usuario
CREATE TABLE IF NOT EXISTS `usuario` (
  `id_usua` int(11) NOT NULL AUTO_INCREMENT,
  `nom_usua` varchar(50) NOT NULL,
  `ape_usua` varchar(50) NOT NULL,
  `pass_usua` varchar(50) NOT NULL,
  `email_usua` varchar(50) NOT NULL,
  `rol_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_usua`),
  KEY `FK_usuario_rol` (`rol_id`),
  CONSTRAINT `FK_usuario_rol` FOREIGN KEY (`rol_id`) REFERENCES `rol` (`id_rol`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla db_consultenos.usuario: ~5 rows (aproximadamente)
INSERT INTO `usuario` (`id_usua`, `nom_usua`, `ape_usua`, `pass_usua`, `email_usua`, `rol_id`) VALUES
	(1, 'Miguel', 'Rojas', 'inacap2022', 'mrojas@inacapmail.cl', 1),
	(2, 'Jorge', 'Canales', 'inacap2022', 'jcanales@inacapmail.cl', 2),
	(3, 'Patrick', 'Aguilar', 'inacap2022', 'paguilar@inacapmail.cl', 2),
	(4, 'Esteban', 'Perez', 'inaacap2022', 'eperez@inacapmail.cl', 3),
	(5, 'A', 'A', 'A', 'A', 1);
	
-- Volcando estructura para tabla db_consultenos.tickets
CREATE TABLE IF NOT EXISTS `tickets` (
  `id_ticket` int(11) NOT NULL AUTO_INCREMENT,
  `id_cliente` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `id_area` int(11) NOT NULL,
  `asun_ticket` varchar(50) NOT NULL,
  `det_servicio` varchar(100) NOT NULL,
  `problema` varchar(100) NOT NULL,
  `ejecutivo_area` varchar(50) NOT NULL,
  `est_ticket` int(11) NOT NULL,
  `criticidad` int(11) NOT NULL,
  `tip_ticket` int(11) NOT NULL DEFAULT 0,
  `fec_creacion` datetime NOT NULL,
  `ejecutivo_mesa` varchar(50) NOT NULL,
  PRIMARY KEY (`id_ticket`),
  KEY `FK_tickets_cliente` (`id_cliente`),
  KEY `FK_tickets_area` (`id_area`),
  KEY `FK_tickets_usuario` (`id_usuario`),
  KEY `FK_tickets_tipo` (`tip_ticket`),
  KEY `FK_tickets_estado` (`est_ticket`),
  KEY `FK_tickets_criticidad` (`criticidad`),
  CONSTRAINT `FK_tickets_area` FOREIGN KEY (`id_area`) REFERENCES `area` (`id_area`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_tickets_cliente` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_tickets_criticidad` FOREIGN KEY (`criticidad`) REFERENCES `criticidad` (`id_crit`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_tickets_estado` FOREIGN KEY (`est_ticket`) REFERENCES `estado` (`id_est`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_tickets_tipo` FOREIGN KEY (`tip_ticket`) REFERENCES `tipo` (`id_tip`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_tickets_usuario` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usua`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla db_consultenos.tickets: ~3 rows (aproximadamente)
INSERT INTO `tickets` (`id_ticket`, `id_cliente`, `id_usuario`, `id_area`, `asun_ticket`, `det_servicio`, `problema`, `ejecutivo_area`, `est_ticket`, `criticidad`, `tip_ticket`, `fec_creacion`, `ejecutivo_mesa`) VALUES
	(2, 2, 2, 2, 'Necesitamos crear un DW', 'Necesitamos desarrollar un DW para nuestro servicio de facturación', 'Requerimiento', 'Miguel Rojas', 1, 1, 1, '2022-05-16 15:35:05', 'Miguel Rojas'),
	(3, 3, 4, 3, 'Desarrollo de appservices Tomcat', 'Se requiere un servicio Tomcat en la nube ', 'Requerimiento', 'Jorge Canales', 1, 2, 1, '2022-05-16 09:35:55', 'Miguel Rojas'),
	(5, 1, 4, 1, 'Mantenimiento a laboratorio', 'Requerimos el mantenimiento preventivo de pc de laboratorio', 'Mantenimiento', 'Patrick Aguilar', 2, 3, 1, '2022-05-16 22:22:21', 'Miguel Rojas');


/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
