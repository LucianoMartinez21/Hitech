-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         8.0.30 - MySQL Community Server - GPL
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para django
CREATE DATABASE IF NOT EXISTS `django` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `django`;

-- Volcando estructura para tabla django.auth_group
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla django.auth_group: ~0 rows (aproximadamente)

-- Volcando estructura para tabla django.auth_group_permissions
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla django.auth_group_permissions: ~0 rows (aproximadamente)

-- Volcando estructura para tabla django.auth_permission
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla django.auth_permission: ~52 rows (aproximadamente)
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(1, 'Can add log entry', 1, 'add_logentry'),
	(2, 'Can change log entry', 1, 'change_logentry'),
	(3, 'Can delete log entry', 1, 'delete_logentry'),
	(4, 'Can view log entry', 1, 'view_logentry'),
	(5, 'Can add permission', 2, 'add_permission'),
	(6, 'Can change permission', 2, 'change_permission'),
	(7, 'Can delete permission', 2, 'delete_permission'),
	(8, 'Can view permission', 2, 'view_permission'),
	(9, 'Can add group', 3, 'add_group'),
	(10, 'Can change group', 3, 'change_group'),
	(11, 'Can delete group', 3, 'delete_group'),
	(12, 'Can view group', 3, 'view_group'),
	(13, 'Can add user', 4, 'add_user'),
	(14, 'Can change user', 4, 'change_user'),
	(15, 'Can delete user', 4, 'delete_user'),
	(16, 'Can view user', 4, 'view_user'),
	(17, 'Can add content type', 5, 'add_contenttype'),
	(18, 'Can change content type', 5, 'change_contenttype'),
	(19, 'Can delete content type', 5, 'delete_contenttype'),
	(20, 'Can view content type', 5, 'view_contenttype'),
	(21, 'Can add session', 6, 'add_session'),
	(22, 'Can change session', 6, 'change_session'),
	(23, 'Can delete session', 6, 'delete_session'),
	(24, 'Can view session', 6, 'view_session'),
	(25, 'Can add tabla_test', 7, 'add_tabla_test'),
	(26, 'Can change tabla_test', 7, 'change_tabla_test'),
	(27, 'Can delete tabla_test', 7, 'delete_tabla_test'),
	(28, 'Can view tabla_test', 7, 'view_tabla_test'),
	(29, 'Can add fotos', 8, 'add_fotos'),
	(30, 'Can change fotos', 8, 'change_fotos'),
	(31, 'Can delete fotos', 8, 'delete_fotos'),
	(32, 'Can view fotos', 8, 'view_fotos'),
	(33, 'Can add usuarios', 9, 'add_usuarios'),
	(34, 'Can change usuarios', 9, 'change_usuarios'),
	(35, 'Can delete usuarios', 9, 'delete_usuarios'),
	(36, 'Can view usuarios', 9, 'view_usuarios'),
	(37, 'Can add contraseñas', 10, 'add_contraseñas'),
	(38, 'Can change contraseñas', 10, 'change_contraseñas'),
	(39, 'Can delete contraseñas', 10, 'delete_contraseñas'),
	(40, 'Can view contraseñas', 10, 'view_contraseñas'),
	(41, 'Can add notificaciones', 11, 'add_notificaciones'),
	(42, 'Can change notificaciones', 11, 'change_notificaciones'),
	(43, 'Can delete notificaciones', 11, 'delete_notificaciones'),
	(44, 'Can view notificaciones', 11, 'view_notificaciones'),
	(45, 'Can add autos', 12, 'add_autos'),
	(46, 'Can change autos', 12, 'change_autos'),
	(47, 'Can delete autos', 12, 'delete_autos'),
	(48, 'Can view autos', 12, 'view_autos'),
	(49, 'Can add registros_visitas', 13, 'add_registros_visitas'),
	(50, 'Can change registros_visitas', 13, 'change_registros_visitas'),
	(51, 'Can delete registros_visitas', 13, 'delete_registros_visitas'),
	(52, 'Can view registros_visitas', 13, 'view_registros_visitas');

-- Volcando estructura para tabla django.auth_user
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla django.auth_user: ~1 rows (aproximadamente)
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
	(1, 'pbkdf2_sha256$600000$BquljX4AjcMowboOsOkNgB$0AJfdpHH2VVifZY49rooslioP5BcBVj/Wz5x/ikMzIg=', '2023-12-08 21:31:42.681498', 1, 'marco', '', '', 'marcoschallapa@gmail.com', 1, 1, '2023-12-08 21:31:13.586204');

-- Volcando estructura para tabla django.auth_user_groups
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla django.auth_user_groups: ~0 rows (aproximadamente)

-- Volcando estructura para tabla django.auth_user_user_permissions
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla django.auth_user_user_permissions: ~0 rows (aproximadamente)

-- Volcando estructura para tabla django.django_admin_log
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla django.django_admin_log: ~0 rows (aproximadamente)

-- Volcando estructura para tabla django.django_content_type
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla django.django_content_type: ~13 rows (aproximadamente)
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(1, 'admin', 'logentry'),
	(3, 'auth', 'group'),
	(2, 'auth', 'permission'),
	(4, 'auth', 'user'),
	(5, 'contenttypes', 'contenttype'),
	(12, 'pagina', 'autos'),
	(10, 'pagina', 'contraseñas'),
	(8, 'pagina', 'fotos'),
	(11, 'pagina', 'notificaciones'),
	(13, 'pagina', 'registros_visitas'),
	(7, 'pagina', 'tabla_test'),
	(9, 'pagina', 'usuarios'),
	(6, 'sessions', 'session');

-- Volcando estructura para tabla django.django_migrations
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla django.django_migrations: ~25 rows (aproximadamente)
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(1, 'contenttypes', '0001_initial', '2023-11-21 23:43:02.807690'),
	(2, 'auth', '0001_initial', '2023-11-21 23:43:03.101793'),
	(3, 'admin', '0001_initial', '2023-11-21 23:43:03.195513'),
	(4, 'admin', '0002_logentry_remove_auto_add', '2023-11-21 23:43:03.201040'),
	(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-11-21 23:43:03.207542'),
	(6, 'contenttypes', '0002_remove_content_type_name', '2023-11-21 23:43:03.256650'),
	(7, 'auth', '0002_alter_permission_name_max_length', '2023-11-21 23:43:03.293363'),
	(8, 'auth', '0003_alter_user_email_max_length', '2023-11-21 23:43:03.311420'),
	(9, 'auth', '0004_alter_user_username_opts', '2023-11-21 23:43:03.317413'),
	(10, 'auth', '0005_alter_user_last_login_null', '2023-11-21 23:43:03.362954'),
	(11, 'auth', '0006_require_contenttypes_0002', '2023-11-21 23:43:03.364953'),
	(12, 'auth', '0007_alter_validators_add_error_messages', '2023-11-21 23:43:03.370468'),
	(13, 'auth', '0008_alter_user_username_max_length', '2023-11-21 23:43:03.417831'),
	(14, 'auth', '0009_alter_user_last_name_max_length', '2023-11-21 23:43:03.456260'),
	(15, 'auth', '0010_alter_group_name_max_length', '2023-11-21 23:43:03.473329'),
	(16, 'auth', '0011_update_proxy_permissions', '2023-11-21 23:43:03.478836'),
	(17, 'auth', '0012_alter_user_first_name_max_length', '2023-11-21 23:43:03.519246'),
	(18, 'sessions', '0001_initial', '2023-11-21 23:43:03.545086'),
	(19, 'pagina', '0001_initial', '2023-11-22 00:05:34.962569'),
	(20, 'pagina', '0002_tabla_test_numeros', '2023-11-22 00:38:31.929893'),
	(21, 'pagina', '0003_autos_usuarios_registros_visitas_notificaciones_and_more', '2023-12-11 20:49:07.125560'),
	(22, 'pagina', '0004_alter_autos_color_alter_autos_motor_and_more', '2023-12-13 23:40:45.316580'),
	(23, 'pagina', '0005_alter_autos_id', '2023-12-20 14:25:36.252855'),
	(24, 'pagina', '0006_alter_autos_id', '2023-12-20 14:25:36.809990'),
	(25, 'pagina', '0007_alter_usuarios_options_alter_usuarios_managers_and_more', '2023-12-20 15:02:48.074185');

-- Volcando estructura para tabla django.django_session
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla django.django_session: ~5 rows (aproximadamente)
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
	('a6iwbs8ikidka5mdzezzzbzsykrj0ovo', 'e30:1rFxbs:gg9jJi0aeTcx4FU4FmSjiExfwtr-sBm-l6m4CsivH0U', '2024-01-03 14:31:44.562569'),
	('by5iie70el64vbqxyukcmhx0odp6dwnj', '.eJxVjEEOwiAQAP_C2RDbwgIevfsGsstupWogKe3J-HdD0oNeZybzVhH3Lce9yRoXVhc1gjr9QsL0lNINP7Dcq061bOtCuif6sE3fKsvrerR_g4wt9-_kWQwMNkFw5GcUY5jwHKwxVhJPY5iMtUIOCGiAMXhgJyAJHJLM6vMFBJQ4VQ:1rFy7X:wxiZLYiHp0BRGTySSlzTvBHmju-joBZvBmDXYI5ssRQ', '2024-01-03 15:04:27.574329'),
	('f5nqg6u1kwvr3amzffiytgp08qkgr7me', 'e30:1rDZP2:Tn6QI5RNYMoTtJWLjyCSjhdfQerB3vqVt3L72d-w9_o', '2023-12-28 00:16:36.566273'),
	('n92qyc8lc86gfjk7spaq5gykmwb4ctvb', '.eJxVjEEOgjAQRe_StWmETqetS_ecoZnpDIIaSCisjHdXEha6_e-9_zKZtnXIW9Ulj2IuxoE5_Y5M5aHTTuRO0222ZZ7WZWS7K_ag1Xaz6PN6uH8HA9XhW7cuigI2vmAKHHtSAGE6Jw_gtYhrkwPvlQMycoNtiihBUQsGYu3N-wMD_DhU:1rFyI7:IgP_-suLBob59pD-k1h8oGhtNYDgErGzIQtBn-LJO28', '2024-01-03 15:15:23.215565'),
	('pkrdvgm0wgrkardk5cqgkpee954ruelg', 'e30:1rDZVG:iXX-IyDLMRzJdimrUL0sti2k01nM3E1G43j6g_7Frn0', '2023-12-28 00:23:02.065179');

-- Volcando estructura para tabla django.pagina_autos
CREATE TABLE IF NOT EXISTS `pagina_autos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `marca` varchar(20) NOT NULL,
  `modelo` varchar(20) NOT NULL,
  `ano` int NOT NULL,
  `precio` int NOT NULL,
  `tipo_gasolina` varchar(1) DEFAULT NULL,
  `motor` varchar(1) DEFAULT NULL,
  `transmision` tinyint(1) DEFAULT NULL,
  `color` varchar(1) DEFAULT NULL,
  `cambio_volante` tinyint(1) DEFAULT NULL,
  `tipo_auto` varchar(1) DEFAULT NULL,
  `numero_asientos` int DEFAULT NULL,
  `descripcion` longtext,
  `auto_delete` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla django.pagina_autos: ~0 rows (aproximadamente)

-- Volcando estructura para tabla django.pagina_contraseñas
CREATE TABLE IF NOT EXISTS `pagina_contraseñas` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `contra` varchar(600) NOT NULL,
  `contra_delete` datetime(6) DEFAULT NULL,
  `usuario_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `pagina_contraseñas_usuario_id_id_b09d67f1_fk_pagina_usuarios_id` (`usuario_id_id`),
  CONSTRAINT `pagina_contraseñas_usuario_id_id_b09d67f1_fk_pagina_usuarios_id` FOREIGN KEY (`usuario_id_id`) REFERENCES `pagina_usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla django.pagina_contraseñas: ~3 rows (aproximadamente)
INSERT INTO `pagina_contraseñas` (`id`, `contra`, `contra_delete`, `usuario_id_id`) VALUES
	(5, '1010', NULL, 26),
	(6, '2220', NULL, 33),
	(7, '22202', NULL, 34);

-- Volcando estructura para tabla django.pagina_fotos
CREATE TABLE IF NOT EXISTS `pagina_fotos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `path_foto` varchar(100) NOT NULL,
  `auto_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `pagina_fotos_auto_id_id_cc42bc8b_fk` (`auto_id_id`),
  CONSTRAINT `pagina_fotos_auto_id_id_cc42bc8b_fk` FOREIGN KEY (`auto_id_id`) REFERENCES `pagina_autos` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla django.pagina_fotos: ~0 rows (aproximadamente)

-- Volcando estructura para tabla django.pagina_notificaciones
CREATE TABLE IF NOT EXISTS `pagina_notificaciones` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fecha_inicio` datetime(6) NOT NULL,
  `fecha_final` datetime(6) NOT NULL,
  `auto_notificacion_id_id` bigint NOT NULL,
  `usuario_notificacion_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `pagina_notificacione_usuario_notificacion_677715c5_fk_pagina_us` (`usuario_notificacion_id_id`),
  KEY `pagina_notificaciones_auto_notificacion_id_id_b753d013_fk` (`auto_notificacion_id_id`),
  CONSTRAINT `pagina_notificacione_usuario_notificacion_677715c5_fk_pagina_us` FOREIGN KEY (`usuario_notificacion_id_id`) REFERENCES `pagina_usuarios` (`id`),
  CONSTRAINT `pagina_notificaciones_auto_notificacion_id_id_b753d013_fk` FOREIGN KEY (`auto_notificacion_id_id`) REFERENCES `pagina_autos` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla django.pagina_notificaciones: ~0 rows (aproximadamente)

-- Volcando estructura para tabla django.pagina_registros_visitas
CREATE TABLE IF NOT EXISTS `pagina_registros_visitas` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fecha_registro` datetime(6) NOT NULL,
  `registro_delete` datetime(6) DEFAULT NULL,
  `auto_registro_id_id` bigint NOT NULL,
  `usuario_registro_id_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `pagina_registros_vis_usuario_registro_id__b2960abe_fk_pagina_us` (`usuario_registro_id_id`),
  KEY `pagina_registros_visitas_auto_registro_id_id_3fc6481b_fk` (`auto_registro_id_id`),
  CONSTRAINT `pagina_registros_vis_usuario_registro_id__b2960abe_fk_pagina_us` FOREIGN KEY (`usuario_registro_id_id`) REFERENCES `pagina_usuarios` (`id`),
  CONSTRAINT `pagina_registros_visitas_auto_registro_id_id_3fc6481b_fk` FOREIGN KEY (`auto_registro_id_id`) REFERENCES `pagina_autos` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla django.pagina_registros_visitas: ~0 rows (aproximadamente)

-- Volcando estructura para tabla django.pagina_tabla_test
CREATE TABLE IF NOT EXISTS `pagina_tabla_test` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `columna_uno` varchar(200) NOT NULL,
  `columna_dos` varchar(200) NOT NULL,
  `columna_tres` varchar(200) NOT NULL,
  `columna_cuatro` varchar(200) NOT NULL,
  `numeros` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla django.pagina_tabla_test: ~0 rows (aproximadamente)

-- Volcando estructura para tabla django.pagina_usuarios
CREATE TABLE IF NOT EXISTS `pagina_usuarios` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(60) NOT NULL,
  `edad` int NOT NULL,
  `sexo` int NOT NULL,
  `email` varchar(255) NOT NULL,
  `administrador` tinyint(1) NOT NULL,
  `usuario_delete` datetime(6) DEFAULT NULL,
  `date_joined` datetime(6) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `last_name` varchar(150) NOT NULL,
  `password` varchar(128) NOT NULL,
  `username` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `pagina_usuarios_email_d0200b6b_uniq` (`email`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla django.pagina_usuarios: ~3 rows (aproximadamente)
INSERT INTO `pagina_usuarios` (`id`, `nombre`, `edad`, `sexo`, `email`, `administrador`, `usuario_delete`, `date_joined`, `first_name`, `is_active`, `is_staff`, `is_superuser`, `last_login`, `last_name`, `password`, `username`) VALUES
	(26, 'Marcos', 2, 3, 'marcoschallapa@gmail.com', 0, NULL, '2023-12-20 15:04:27.552106', '', 1, 0, 0, '2023-12-20 15:04:27.568322', '', '', ''),
	(33, 'marco2', 2, 1, 'marcos@gmail.com', 0, NULL, '2023-12-20 15:14:49.557616', '', 1, 0, 0, '2023-12-20 15:14:49.573661', '', '', 'marco2'),
	(34, 'marco3', 2, 1, 'marcoss@gmail.com', 0, NULL, '2023-12-20 15:15:23.187834', '', 1, 0, 0, '2023-12-20 15:15:23.207960', '', '', 'marco3');

-- Volcando estructura para tabla django.pagina_usuarios_groups
CREATE TABLE IF NOT EXISTS `pagina_usuarios_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `usuarios_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `pagina_usuarios_groups_usuarios_id_group_id_80126e2f_uniq` (`usuarios_id`,`group_id`),
  KEY `pagina_usuarios_groups_group_id_090a58ce_fk_auth_group_id` (`group_id`),
  CONSTRAINT `pagina_usuarios_grou_usuarios_id_f57d5a00_fk_pagina_us` FOREIGN KEY (`usuarios_id`) REFERENCES `pagina_usuarios` (`id`),
  CONSTRAINT `pagina_usuarios_groups_group_id_090a58ce_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla django.pagina_usuarios_groups: ~0 rows (aproximadamente)

-- Volcando estructura para tabla django.pagina_usuarios_user_permissions
CREATE TABLE IF NOT EXISTS `pagina_usuarios_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `usuarios_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `pagina_usuarios_user_per_usuarios_id_permission_i_aca13f74_uniq` (`usuarios_id`,`permission_id`),
  KEY `pagina_usuarios_user_permission_id_8feaecce_fk_auth_perm` (`permission_id`),
  CONSTRAINT `pagina_usuarios_user_permission_id_8feaecce_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `pagina_usuarios_user_usuarios_id_09563c10_fk_pagina_us` FOREIGN KEY (`usuarios_id`) REFERENCES `pagina_usuarios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla django.pagina_usuarios_user_permissions: ~0 rows (aproximadamente)

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
