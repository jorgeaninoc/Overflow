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
-- Table structure for table `tsciap_noticia_imagenes`
--

DROP TABLE IF EXISTS `tsciap_noticia_imagenes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tsciap_noticia_imagenes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `noticia_id` int(11) NOT NULL,
  `imagen_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `TSCIAP_noticia_imagenes_noticia_id_imagen_id_93214928_uniq` (`noticia_id`,`imagen_id`),
  KEY `TSCIAP_noticia_imagenes_imagen_id_fd1ba2f3_fk_TSCIAP_imagen_id` (`imagen_id`),
  CONSTRAINT `TSCIAP_noticia_imagenes_imagen_id_fd1ba2f3_fk_TSCIAP_imagen_id` FOREIGN KEY (`imagen_id`) REFERENCES `tsciap_imagen` (`id`),
  CONSTRAINT `TSCIAP_noticia_imagenes_noticia_id_e90d4921_fk_TSCIAP_noticia_id` FOREIGN KEY (`noticia_id`) REFERENCES `tsciap_noticia` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tsciap_noticia_imagenes`
--

LOCK TABLES `tsciap_noticia_imagenes` WRITE;
/*!40000 ALTER TABLE `tsciap_noticia_imagenes` DISABLE KEYS */;
INSERT INTO `tsciap_noticia_imagenes` VALUES (2,1,4),(3,1,5),(1,1,6),(4,2,3),(5,2,4),(6,2,5),(7,2,6);
/*!40000 ALTER TABLE `tsciap_noticia_imagenes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-24 19:12:16
