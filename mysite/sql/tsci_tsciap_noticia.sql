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
-- Table structure for table `tsciap_noticia`
--

DROP TABLE IF EXISTS `tsciap_noticia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tsciap_noticia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(255) NOT NULL,
  `texto` longtext NOT NULL,
  `fechaFin` date NOT NULL,
  `fechaInicio` date NOT NULL,
  `comunidad_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `TSCIAP_noticia_comunidad_id_105c0689_fk_TSCIAP_comunidad_id` (`comunidad_id`),
  CONSTRAINT `TSCIAP_noticia_comunidad_id_105c0689_fk_TSCIAP_comunidad_id` FOREIGN KEY (`comunidad_id`) REFERENCES `tsciap_comunidad` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tsciap_noticia`
--

LOCK TABLES `tsciap_noticia` WRITE;
/*!40000 ALTER TABLE `tsciap_noticia` DISABLE KEYS */;
INSERT INTO `tsciap_noticia` VALUES (1,'Prueba','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris quis turpis vitae nunc mollis pretium. Vivamus nec vehicula arcu, ac pretium risus. Pellentesque quam lectus, tincidunt a orci non, egestas consectetur diam. Morbi accumsan sem massa, eget placerat justo luctus finibus. Ut accumsan ipsum ac dui scelerisque, non fermentum arcu efficitur. Curabitur varius ex commodo enim pharetra tristique. Aenean lobortis vel risus nec euismod. Donec pretium velit non tincidunt varius. Nunc scelerisque nisi a velit vestibulum posuere. Pellentesque sagittis mi a risus ornare fermentum sed ac est. Sed sodales velit at felis eleifend, ut venenatis mi posuere. Integer sem urna, lacinia sed mauris et, elementum iaculis metus. Sed luctus et quam eu blandit.','2018-10-23','2018-09-23',1),(2,'Prueba 2','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris quis turpis vitae nunc mollis pretium. Vivamus nec vehicula arcu, ac pretium risus. Pellentesque quam lectus, tincidunt a orci non, egestas consectetur diam. Morbi accumsan sem massa, eget placerat justo luctus finibus. Ut accumsan ipsum ac dui scelerisque, non fermentum arcu efficitur. Curabitur varius ex commodo enim pharetra tristique. Aenean lobortis vel risus nec euismod. Donec pretium velit non tincidunt varius. Nunc scelerisque nisi a velit vestibulum posuere. Pellentesque sagittis mi a risus ornare fermentum sed ac est. Sed sodales velit at felis eleifend, ut venenatis mi posuere. Integer sem urna, lacinia sed mauris et, elementum iaculis metus. Sed luctus et quam eu blandit.','2018-10-23','2018-09-23',1);
/*!40000 ALTER TABLE `tsciap_noticia` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-24 19:12:14
