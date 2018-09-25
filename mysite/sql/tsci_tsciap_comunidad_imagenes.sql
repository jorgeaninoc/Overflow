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
-- Table structure for table `tsciap_comunidad_imagenes`
--

DROP TABLE IF EXISTS `tsciap_comunidad_imagenes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tsciap_comunidad_imagenes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comunidad_id` int(11) NOT NULL,
  `imagen_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `TSCIAP_comunidad_imagenes_comunidad_id_imagen_id_e7dc15a1_uniq` (`comunidad_id`,`imagen_id`),
  KEY `TSCIAP_comunidad_imagenes_imagen_id_4a9ec59a_fk_TSCIAP_imagen_id` (`imagen_id`),
  CONSTRAINT `TSCIAP_comunidad_ima_comunidad_id_eba0bfab_fk_TSCIAP_co` FOREIGN KEY (`comunidad_id`) REFERENCES `tsciap_comunidad` (`id`),
  CONSTRAINT `TSCIAP_comunidad_imagenes_imagen_id_4a9ec59a_fk_TSCIAP_imagen_id` FOREIGN KEY (`imagen_id`) REFERENCES `tsciap_imagen` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tsciap_comunidad_imagenes`
--

LOCK TABLES `tsciap_comunidad_imagenes` WRITE;
/*!40000 ALTER TABLE `tsciap_comunidad_imagenes` DISABLE KEYS */;
INSERT INTO `tsciap_comunidad_imagenes` VALUES (1,1,3),(2,1,4),(3,1,5);
/*!40000 ALTER TABLE `tsciap_comunidad_imagenes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-24 19:12:11
