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
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add imagen',1,'add_imagen'),(2,'Can change imagen',1,'change_imagen'),(3,'Can delete imagen',1,'delete_imagen'),(4,'Can view imagen',1,'view_imagen'),(5,'Can add comunidad',2,'add_comunidad'),(6,'Can change comunidad',2,'change_comunidad'),(7,'Can delete comunidad',2,'delete_comunidad'),(8,'Can view comunidad',2,'view_comunidad'),(9,'Can add producto',3,'add_producto'),(10,'Can change producto',3,'change_producto'),(11,'Can delete producto',3,'delete_producto'),(12,'Can view producto',3,'view_producto'),(13,'Can add noticia',4,'add_noticia'),(14,'Can change noticia',4,'change_noticia'),(15,'Can delete noticia',4,'delete_noticia'),(16,'Can view noticia',4,'view_noticia'),(17,'Can add video',5,'add_video'),(18,'Can change video',5,'change_video'),(19,'Can delete video',5,'delete_video'),(20,'Can view video',5,'view_video'),(21,'Can add inicio imagen',6,'add_inicioimagen'),(22,'Can change inicio imagen',6,'change_inicioimagen'),(23,'Can delete inicio imagen',6,'delete_inicioimagen'),(24,'Can view inicio imagen',6,'view_inicioimagen'),(25,'Can add galeria imagen',7,'add_galeriaimagen'),(26,'Can change galeria imagen',7,'change_galeriaimagen'),(27,'Can delete galeria imagen',7,'delete_galeriaimagen'),(28,'Can view galeria imagen',7,'view_galeriaimagen'),(29,'Can add log entry',8,'add_logentry'),(30,'Can change log entry',8,'change_logentry'),(31,'Can delete log entry',8,'delete_logentry'),(32,'Can view log entry',8,'view_logentry'),(33,'Can add permission',9,'add_permission'),(34,'Can change permission',9,'change_permission'),(35,'Can delete permission',9,'delete_permission'),(36,'Can view permission',9,'view_permission'),(37,'Can add group',10,'add_group'),(38,'Can change group',10,'change_group'),(39,'Can delete group',10,'delete_group'),(40,'Can view group',10,'view_group'),(41,'Can add user',11,'add_user'),(42,'Can change user',11,'change_user'),(43,'Can delete user',11,'delete_user'),(44,'Can view user',11,'view_user'),(45,'Can add content type',12,'add_contenttype'),(46,'Can change content type',12,'change_contenttype'),(47,'Can delete content type',12,'delete_contenttype'),(48,'Can view content type',12,'view_contenttype'),(49,'Can add session',13,'add_session'),(50,'Can change session',13,'change_session'),(51,'Can delete session',13,'delete_session'),(52,'Can view session',13,'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
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
