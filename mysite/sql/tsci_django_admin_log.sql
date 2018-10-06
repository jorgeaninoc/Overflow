-- MySQL dump 10.13  Distrib 8.0.12, for Win64 (x86_64)
--
-- Host: localhost    Database: tsci
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-09-23 22:08:55.572502','1','https://www.youtube.com/watch?v=qaRamphf8SM',1,'[{\"added\": {}}]',5,1),(2,'2018-09-23 22:08:57.832277','1','https://www.youtube.com/watch?v=qaRamphf8SM',2,'[]',5,1),(3,'2018-09-23 23:42:52.606063','3','CG',1,'[{\"added\": {}}]',1,1),(4,'2018-09-23 23:43:01.097995','4','CG1',1,'[{\"added\": {}}]',1,1),(5,'2018-09-23 23:43:09.336930','5','CG2',1,'[{\"added\": {}}]',1,1),(6,'2018-09-23 23:43:23.992372','1','Cerro de Gallo',1,'[{\"added\": {}}]',2,1),(7,'2018-09-23 23:43:41.773960','6','2018-09-23 18:42:40.881191',1,'[{\"added\": {}}]',1,1),(8,'2018-09-23 23:43:45.514998','1','Prueba',1,'[{\"added\": {}}]',4,1),(9,'2018-09-24 00:28:18.343806','1','Prueba',2,'[{\"changed\": {\"fields\": [\"imagenes\"]}}]',4,1),(10,'2018-09-24 00:29:02.536900','2','Prueba 2',1,'[{\"added\": {}}]',4,1),(11,'2018-09-24 00:29:29.850133','1','InicioImagen object (1)',1,'[{\"added\": {}}]',6,1),(12,'2018-09-24 00:31:44.997970','7','taza',1,'[{\"added\": {}}]',1,1),(13,'2018-09-24 00:31:49.186050','1','Taza de cafe',1,'[{\"added\": {}}]',3,1),(14,'2018-09-24 06:12:17.057693','8','t2',1,'[{\"added\": {}}]',1,1),(15,'2018-09-24 06:12:20.284425','2','Taza 2',1,'[{\"added\": {}}]',3,1),(16,'2018-09-24 06:12:31.634757','3','Taza 3',1,'[{\"added\": {}}]',3,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-24 19:12:07
