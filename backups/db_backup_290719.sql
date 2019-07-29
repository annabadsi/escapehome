-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: homeescape.mysql.pythonanywhere-services.com    Database: homeescape$homeescape
-- ------------------------------------------------------
-- Server version	5.7.21-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add action',7,'add_action'),(26,'Can change action',7,'change_action'),(27,'Can delete action',7,'delete_action'),(28,'Can view action',7,'view_action'),(29,'Can add active scenario',8,'add_activescenario'),(30,'Can change active scenario',8,'change_activescenario'),(31,'Can delete active scenario',8,'delete_activescenario'),(32,'Can view active scenario',8,'view_activescenario'),(33,'Can add command',9,'add_command'),(34,'Can change command',9,'change_command'),(35,'Can delete command',9,'delete_command'),(36,'Can view command',9,'view_command'),(37,'Can add device',10,'add_device'),(38,'Can change device',10,'change_device'),(39,'Can delete device',10,'delete_device'),(40,'Can view device',10,'view_device'),(41,'Can add ordered action',11,'add_orderedaction'),(42,'Can change ordered action',11,'change_orderedaction'),(43,'Can delete ordered action',11,'delete_orderedaction'),(44,'Can view ordered action',11,'view_orderedaction'),(45,'Can add ordered riddle',12,'add_orderedriddle'),(46,'Can change ordered riddle',12,'change_orderedriddle'),(47,'Can delete ordered riddle',12,'delete_orderedriddle'),(48,'Can view ordered riddle',12,'view_orderedriddle'),(49,'Can add riddle',13,'add_riddle'),(50,'Can change riddle',13,'change_riddle'),(51,'Can delete riddle',13,'delete_riddle'),(52,'Can view riddle',13,'view_riddle'),(53,'Can add scenario',14,'add_scenario'),(54,'Can change scenario',14,'change_scenario'),(55,'Can delete scenario',14,'delete_scenario'),(56,'Can view scenario',14,'view_scenario'),(57,'Can add hue lamp',15,'add_huelamp'),(58,'Can change hue lamp',15,'change_huelamp'),(59,'Can delete hue lamp',15,'delete_huelamp'),(60,'Can view hue lamp',15,'view_huelamp'),(61,'Can add hue remote control',16,'add_hueremotecontrol'),(62,'Can change hue remote control',16,'change_hueremotecontrol'),(63,'Can delete hue remote control',16,'delete_hueremotecontrol'),(64,'Can view hue remote control',16,'view_hueremotecontrol'),(65,'Can add knx lamp',17,'add_knxlamp'),(66,'Can change knx lamp',17,'change_knxlamp'),(67,'Can delete knx lamp',17,'delete_knxlamp'),(68,'Can view knx lamp',17,'view_knxlamp'),(69,'Can add knx shutter',18,'add_knxshutter'),(70,'Can change knx shutter',18,'change_knxshutter'),(71,'Can delete knx shutter',18,'delete_knxshutter'),(72,'Can view knx shutter',18,'view_knxshutter'),(73,'Can add modbus motor',19,'add_modbusmotor'),(74,'Can change modbus motor',19,'change_modbusmotor'),(75,'Can delete modbus motor',19,'delete_modbusmotor'),(76,'Can view modbus motor',19,'view_modbusmotor');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$120000$08zt1vGtz0fU$T+DlZpAcZ/Qny2JQCh+JcmVAH/p5rczCMkfeURFpUJU=','2019-07-17 14:04:06.918000',1,'jgiebelhausen','','','',1,1,'2019-07-17 11:56:42.252000'),(2,'pbkdf2_sha256$120000$RJjFCkifbo1D$0yp78BOHguNMeWyKbsQy+oh0/Q7V7EO+kb7rK5vrdVA=','2019-07-19 12:24:24.382742',1,'homeescape','','','',1,1,'2019-07-17 21:37:03.539447');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_action`
--

DROP TABLE IF EXISTS `core_action`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_action` (
  `name` varchar(255) NOT NULL,
  `function` varchar(255) NOT NULL,
  `parameters` longtext,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_action`
--

LOCK TABLES `core_action` WRITE;
/*!40000 ALTER TABLE `core_action` DISABLE KEYS */;
INSERT INTO `core_action` VALUES ('blink 5','blink','{\'tr_time\': 5, \'blink_count\': 5}'),('blink 9','blink','{\'tr_time\': 5, \'blink_count\': 9}'),('blinken dunkelgelb 2x','blink','{\'tr_time\': 5, \'blink_count\': 2, \'hex_color\': \'eeba30\'}'),('blinken dunkelrot 2x','blink','{\'tr_time\': 5, \'blink_count\': 2, \'hex_color\': \'740001\'}'),('blinken hellgelb 2x','blink','{\'tr_time\': 5, \'blink_count\': 2, \'hex_color\': \'d3a625\'}'),('blinken hellrot 2x','blink','{\'tr_time\': 5, \'blink_count\': 2, \'hex_color\': \'ae0001\'}'),('blinken rot','blink','{\'tr_time\': 5, \'blink_count\': 2, \'hex_color\': \'740001\'}'),('box öffnen','open','{\'value\': True}'),('box schließen','close','{\'value\': False}'),('Farbe dunkel rot','set_color','{\'hex_value\': \'740001\'}'),('Farbe Gelb','set_color','{\'hex_value\': \'f5ff00\'}'),('Farbe Grün','set_color','{\'hex_value\': 00f700}'),('Farbe hellrot','set_color','{\'hex_value\': \'ae0001\'}'),('Farbe Magenta','set_color','{\'hex_value\': \'ff00ff\'}'),('Farbe Orange','set_color','{\'hex_value\': \'ffa500\'}'),('Farbe Rot','set_color','{\'hex_value\': \'ff0000\'}'),('Jalousie dreiviertel','blind_up','{\'value\': \'?\'}'),('Jalousie runter','blind_down','{\'value\': \'?\'}'),('KNX Lampe an','turn_on','{\'value\':1}'),('KNX lampe aus','turn_off','{\'value\':0}'),('Lampe an','turn_on','{}'),('Lampe aus','turn_off','{}'),('warten 1','wait','{\'sleep_time\': 1}'),('Warten 3','wait','{\'sleep_time\': 3}'),('Warten 6','wait','{\'sleep_time\': 6}'),('Warten 9','wait','{\'sleep_time\': 9}');
/*!40000 ALTER TABLE `core_action` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_activescenario`
--

DROP TABLE IF EXISTS `core_activescenario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_activescenario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user` varchar(255) DEFAULT NULL,
  `players` int(11) DEFAULT NULL,
  `duration` bigint(20) DEFAULT NULL,
  `score` int(11) NOT NULL,
  `state` int(11) DEFAULT NULL,
  `box` tinyint(1) DEFAULT NULL,
  `riddle_id` int(11) DEFAULT NULL,
  `scenario_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_activescenario_riddle_id_41ac6e3f_fk_core_riddle_id` (`riddle_id`),
  KEY `core_activescenario_scenario_id_5b2b6d62_fk_core_scenario_id` (`scenario_id`),
  CONSTRAINT `core_activescenario_riddle_id_41ac6e3f_fk_core_riddle_id` FOREIGN KEY (`riddle_id`) REFERENCES `core_riddle` (`id`),
  CONSTRAINT `core_activescenario_scenario_id_5b2b6d62_fk_core_scenario_id` FOREIGN KEY (`scenario_id`) REFERENCES `core_scenario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_activescenario`
--

LOCK TABLES `core_activescenario` WRITE;
/*!40000 ALTER TABLE `core_activescenario` DISABLE KEYS */;
INSERT INTO `core_activescenario` VALUES (8,'amzn1.ask.account.AGV6BQF6VXNVPYZQIH7HNCH7DHIXBLYGQ5GPI6LEY4PKUEPHSL5QILTQNXMU3JP4YND2JKQTNNRECLQTI6CTTSBBFE6E2QVCYWTOZDCWWKSN3SWBGPY7JBJI3NLNNEGKXOZLW66KLKOWP2ATKAJABOBCSP7AF63WFHK4JNJOVCED547FMGZ7QAIENVBUZBWQGOINEG4AQKCGLRI',NULL,0,0,NULL,0,NULL,NULL);
/*!40000 ALTER TABLE `core_activescenario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_command`
--

DROP TABLE IF EXISTS `core_command`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_command` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `protocol` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_command`
--

LOCK TABLES `core_command` WRITE;
/*!40000 ALTER TABLE `core_command` DISABLE KEYS */;
INSERT INTO `core_command` VALUES (1,'Riddle1: Gryffindor Farbwechsel 1','PHue'),(2,'Riddle 2: neun mal blinken','PHue'),(3,'Riddle 2: Jalousie auf dreiviertel','KNX'),(4,'Riddle 3: Lampen alle aus','PHue'),(5,'Riddle 3: Jalousien ganz runter','KNX'),(6,'Riddle: 4 Jalousien ganz hoch','KNX'),(7,'Riddle 4: Lichter an','PHue'),(8,'modbus box schließen','Modbus'),(9,'modbus box öffnen','Modbus'),(10,'Riddle 1: Gryffindor Farbwechsel 2','PHue'),(11,'knx board lampe an','KNX'),(12,'knx board lampe aus','KNX');
/*!40000 ALTER TABLE `core_command` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_command_devices`
--

DROP TABLE IF EXISTS `core_command_devices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_command_devices` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `command_id` int(11) NOT NULL,
  `device_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `core_command_devices_command_id_device_id_b5181b32_uniq` (`command_id`,`device_id`),
  KEY `core_command_devices_device_id_618578ae_fk_core_device_id` (`device_id`),
  CONSTRAINT `core_command_devices_command_id_9ff141e9_fk_core_command_id` FOREIGN KEY (`command_id`) REFERENCES `core_command` (`id`),
  CONSTRAINT `core_command_devices_device_id_618578ae_fk_core_device_id` FOREIGN KEY (`device_id`) REFERENCES `core_device` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_command_devices`
--

LOCK TABLES `core_command_devices` WRITE;
/*!40000 ALTER TABLE `core_command_devices` DISABLE KEYS */;
INSERT INTO `core_command_devices` VALUES (1,1,18),(2,2,18),(3,3,11),(4,3,12),(5,3,13),(6,4,18),(7,5,11),(8,5,12),(9,5,13),(10,6,11),(11,6,12),(12,6,13),(13,7,18),(14,8,19),(15,9,19),(16,10,4),(17,11,20);
/*!40000 ALTER TABLE `core_command_devices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_device`
--

DROP TABLE IF EXISTS `core_device`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_device` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_device`
--

LOCK TABLES `core_device` WRITE;
/*!40000 ALTER TABLE `core_device` DISABLE KEYS */;
INSERT INTO `core_device` VALUES (1),(2),(3),(4),(5),(6),(7),(8),(9),(10),(11),(12),(13),(14),(15),(16),(17),(18),(19),(20);
/*!40000 ALTER TABLE `core_device` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_huelamp`
--

DROP TABLE IF EXISTS `core_huelamp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_huelamp` (
  `device_ptr_id` int(11) NOT NULL,
  `lamp_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `room` varchar(255) NOT NULL,
  PRIMARY KEY (`device_ptr_id`),
  CONSTRAINT `core_huelamp_device_ptr_id_08e95180_fk_core_device_id` FOREIGN KEY (`device_ptr_id`) REFERENCES `core_device` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_huelamp`
--

LOCK TABLES `core_huelamp` WRITE;
/*!40000 ALTER TABLE `core_huelamp` DISABLE KEYS */;
INSERT INTO `core_huelamp` VALUES (1,9,'Rechts','Küche'),(2,6,'Decke','Flur'),(4,1,'Sofa','Wohnzimmer'),(5,4,'Fenster','Wohnzimmer'),(6,7,'Decke','Zimmer'),(7,8,'Fenster','Zimmer'),(8,3,'Decke','Wohnzimmer'),(18,2,'Ecke','Zimmer');
/*!40000 ALTER TABLE `core_huelamp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_hueremotecontrol`
--

DROP TABLE IF EXISTS `core_hueremotecontrol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_hueremotecontrol` (
  `device_ptr_id` int(11) NOT NULL,
  `control_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`device_ptr_id`),
  CONSTRAINT `core_hueremotecontrol_device_ptr_id_362d7802_fk_core_device_id` FOREIGN KEY (`device_ptr_id`) REFERENCES `core_device` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_hueremotecontrol`
--

LOCK TABLES `core_hueremotecontrol` WRITE;
/*!40000 ALTER TABLE `core_hueremotecontrol` DISABLE KEYS */;
INSERT INTO `core_hueremotecontrol` VALUES (9,4,'Wohnzimmer Schalter');
/*!40000 ALTER TABLE `core_hueremotecontrol` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_knxlamp`
--

DROP TABLE IF EXISTS `core_knxlamp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_knxlamp` (
  `device_ptr_id` int(11) NOT NULL,
  `group_adddress` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`device_ptr_id`),
  CONSTRAINT `core_knxlamp_device_ptr_id_c55942b7_fk_core_device_id` FOREIGN KEY (`device_ptr_id`) REFERENCES `core_device` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_knxlamp`
--

LOCK TABLES `core_knxlamp` WRITE;
/*!40000 ALTER TABLE `core_knxlamp` DISABLE KEYS */;
INSERT INTO `core_knxlamp` VALUES (3,'0/0/1','Deckenlampe 1'),(17,'0/0/2','Deckenlampe 2'),(20,'0/0/3','knxboardlampe');
/*!40000 ALTER TABLE `core_knxlamp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_knxshutter`
--

DROP TABLE IF EXISTS `core_knxshutter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_knxshutter` (
  `device_ptr_id` int(11) NOT NULL,
  `group_adddress` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `modus` varchar(255) NOT NULL,
  PRIMARY KEY (`device_ptr_id`),
  CONSTRAINT `core_knxshutter_device_ptr_id_1f27de60_fk_core_device_id` FOREIGN KEY (`device_ptr_id`) REFERENCES `core_device` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_knxshutter`
--

LOCK TABLES `core_knxshutter` WRITE;
/*!40000 ALTER TABLE `core_knxshutter` DISABLE KEYS */;
INSERT INTO `core_knxshutter` VALUES (11,'3/1/1','Fahren','Jalousie 1'),(12,'3/1/2','Fahren','Jalousie 2'),(13,'3/1/3','Fahren','Jalousie 3'),(14,'3/2/1','Verstellen','Jalousie 1'),(15,'3/2/2','Verstellen','Jalousie 2'),(16,'3/2/3','Verstellen','Jalousie 3');
/*!40000 ALTER TABLE `core_knxshutter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_modbusmotor`
--

DROP TABLE IF EXISTS `core_modbusmotor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_modbusmotor` (
  `device_ptr_id` int(11) NOT NULL,
  `device_address` int(11) NOT NULL,
  PRIMARY KEY (`device_ptr_id`),
  CONSTRAINT `core_modbusmotor_device_ptr_id_baae38eb_fk_core_device_id` FOREIGN KEY (`device_ptr_id`) REFERENCES `core_device` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_modbusmotor`
--

LOCK TABLES `core_modbusmotor` WRITE;
/*!40000 ALTER TABLE `core_modbusmotor` DISABLE KEYS */;
INSERT INTO `core_modbusmotor` VALUES (19,1);
/*!40000 ALTER TABLE `core_modbusmotor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_orderedaction`
--

DROP TABLE IF EXISTS `core_orderedaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_orderedaction` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order` int(11) NOT NULL,
  `action_id` varchar(255) NOT NULL,
  `command_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_orderedaction_action_id_fabc0814_fk_core_action_name` (`action_id`),
  KEY `core_orderedaction_command_id_ddd67025_fk_core_command_id` (`command_id`),
  CONSTRAINT `core_orderedaction_action_id_fabc0814_fk_core_action_name` FOREIGN KEY (`action_id`) REFERENCES `core_action` (`name`),
  CONSTRAINT `core_orderedaction_command_id_ddd67025_fk_core_command_id` FOREIGN KEY (`command_id`) REFERENCES `core_command` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_orderedaction`
--

LOCK TABLES `core_orderedaction` WRITE;
/*!40000 ALTER TABLE `core_orderedaction` DISABLE KEYS */;
INSERT INTO `core_orderedaction` VALUES (1,1,'Warten 3',1),(2,2,'blinken hellrot 2x',1),(3,3,'Warten 3',1),(4,6,'blinken hellgelb 2x',1),(5,7,'Warten 3',1),(6,10,'Farbe Gelb',1),(7,4,'Lampe aus',1),(8,5,'warten 1',1),(9,8,'warten 1',1),(10,9,'Lampe aus',1),(11,11,'Warten 3',1),(12,12,'Lampe aus',1),(13,1,'blink 9',2),(14,2,'Warten 6',2),(15,1,'Jalousie dreiviertel',3),(16,1,'Lampe aus',4),(17,1,'Jalousie runter',5),(18,1,'Lampe an',7),(19,1,'box schließen',8),(20,1,'box öffnen',9),(21,1,'Warten 3',10),(22,2,'blinken dunkelrot 2x',10),(25,5,'warten 1',10),(26,6,'blinken dunkelgelb 2x',10),(27,1,'KNX Lampe an',11),(28,1,'KNX lampe aus',12);
/*!40000 ALTER TABLE `core_orderedaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_orderedriddle`
--

DROP TABLE IF EXISTS `core_orderedriddle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_orderedriddle` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order` int(11) NOT NULL,
  `riddle_id` int(11) NOT NULL,
  `scenario_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_orderedriddle_riddle_id_e4863f38_fk_core_riddle_id` (`riddle_id`),
  KEY `core_orderedriddle_scenario_id_b21736a9_fk_core_scenario_id` (`scenario_id`),
  CONSTRAINT `core_orderedriddle_riddle_id_e4863f38_fk_core_riddle_id` FOREIGN KEY (`riddle_id`) REFERENCES `core_riddle` (`id`),
  CONSTRAINT `core_orderedriddle_scenario_id_b21736a9_fk_core_scenario_id` FOREIGN KEY (`scenario_id`) REFERENCES `core_scenario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_orderedriddle`
--

LOCK TABLES `core_orderedriddle` WRITE;
/*!40000 ALTER TABLE `core_orderedriddle` DISABLE KEYS */;
INSERT INTO `core_orderedriddle` VALUES (1,1,4,1),(2,2,5,1),(3,3,6,1),(4,4,7,1),(5,1,8,2),(6,2,9,2),(7,3,10,2),(8,4,11,2);
/*!40000 ALTER TABLE `core_orderedriddle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_riddle`
--

DROP TABLE IF EXISTS `core_riddle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_riddle` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `task` longtext NOT NULL,
  `solution` longtext NOT NULL,
  `points` int(11) NOT NULL,
  `loop` int(11) NOT NULL,
  `hints` longtext NOT NULL,
  `correct` longtext NOT NULL,
  `incorrect` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_riddle`
--

LOCK TABLES `core_riddle` WRITE;
/*!40000 ALTER TABLE `core_riddle` DISABLE KEYS */;
INSERT INTO `core_riddle` VALUES (4,'<s>Schau dich im Raum um, an was erinnert dich das?</s>','Gryffindor, An die Farben von Gryffindor, Farben von Gryffindor,',3,99,'in Hogwarts gibt es davon 4 | jedes davon hat unterschiedliche Farben | die Farben sollen an eins der Häuser von Hogwarts erinnern, welches ist es?','<s>Vielleicht bist Du ein Gryffindor, sagt Euer alter Hut, denn dort regieren, wie man weiß, Tapferkeit und Mut</s>','Schade, dass war leider falsch, versuch es doch nochmal.\r\nDu kannst auch nach Hinweisen fragen, falls du mal nicht weiter weißt.'),(5,'<p>Der Raum scheint wirklich verhext zu sein. Was könnte das bedeuten?</p>','neundreiviertel',3,99,'Es wird eine merkwürdige, in Hogwarts allerdings bekannte Zahl, gesucht | An diesem Gleis fährt der Hogwarts Express.','Grandios, dass war richtig.','Schade, dass war leider falsch, versuch es doch nochmal.'),(6,'<p>Na endlich, das blinken hat aufgehört.</p>\r\n\r\n<p>Aber nun ist es so stockfinster, dass du nun garnichts mehr sehen kannst.</p>\r\n<p>Wie gehen die Lichter an?</p>','Lumos, Lumos Maxima, Lumos Solem',3,0,'Nutze deinen Zauberstab | Welchen Zauberspruch brauchst du um einen Raum zu erleuchten? | Komm her, ich flüstere es dir ins Ohr:  <amazon:effect name=\"whispered\">Lumos</amazon:effect>','<p><say-as interpret-as=\"interjection\">prima</say-as>, alles beim alten!</p>','<p><say-as interpret-as=\"interjection\">mist</say-as, es ist immer noch dunkel!</p>'),(7,'Vor uns liegen dunkle, schwere Zeiten. Schon bald müssen wir uns entscheiden zwischen dem richtigen Weg und dem leichten. Was würde ein wahrer Zauberer tun um aus dem Raum zu entkommen?','Alohomora',3,0,'Nagut von mir aus darfst du in dein Zaubersprüchebuch schauen | Immer noch nicht? streng dich doch mal an | nagut, die Lösung ist: <s>Alohomora</s>','<audio src=\"soundbank://soundlibrary/foley/amzn_sfx_wooden_door_creaks_open_01\"/>\r\n<say-as interpret-as=\"interjection\">Sesam öffne dich</say-as>\r\n<p>Und jetzt schnell raus hier!</p>','<say-as interpret-as=\"interjection\">kopf hoch</say-as> und dann probiere es erneut.'),(8,'Wie heißt ein Bumerang der nicht zurück kommt?','Stock',3,99,'Hunde spielen gerne damit | Kann ebenso als Gehhilfe verwendet werden','<audio src=\"soundbank://soundlibrary/human/amzn_sfx_laughter_giggle_02\"/>','<say-as interpret-as=\"interjection\">Nö</say-as>, das war nicht die richtige Antwort'),(9,'Was ist der Unterschied zwischen dir und mir?','der erste buchstabe, das d, das m, der buchstabe d, der buchstabe m, der 1. buchstabe',3,99,'Schau dir nur mal die Wörter an.','<say-as interpret-as=\"interjection\">hihi</say-as>','Schade, dass war leider falsch, versuch es doch nochmal.'),(10,'Wer hat Federn aber keine Flügel?','Dein Kopfkissen, das Kopfkissen, Kopfkissen, Kissen',3,99,'','<audio src=\"soundbank://soundlibrary/musical/amzn_sfx_drum_comedy_01\"/>','Schade, dass war leider falsch, versuch es doch nochmal.'),(11,'Was machen zwei wütende Schafe?','Sie kriegen sich in die Wolle, in die Wolle kriegen, kriegen sich in die wolle, sich in die Wolle kriegen',3,99,'','<audio src=\"soundbank://soundlibrary/horror/horror_05\"/>','Schade, dass war leider falsch, versuch es doch nochmal.');
/*!40000 ALTER TABLE `core_riddle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_riddle_commands`
--

DROP TABLE IF EXISTS `core_riddle_commands`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_riddle_commands` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `riddle_id` int(11) NOT NULL,
  `command_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `core_riddle_commands_riddle_id_command_id_45e7f2ac_uniq` (`riddle_id`,`command_id`),
  KEY `core_riddle_commands_command_id_9f4ab1d6_fk_core_command_id` (`command_id`),
  CONSTRAINT `core_riddle_commands_command_id_9f4ab1d6_fk_core_command_id` FOREIGN KEY (`command_id`) REFERENCES `core_command` (`id`),
  CONSTRAINT `core_riddle_commands_riddle_id_9ffb9841_fk_core_riddle_id` FOREIGN KEY (`riddle_id`) REFERENCES `core_riddle` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_riddle_commands`
--

LOCK TABLES `core_riddle_commands` WRITE;
/*!40000 ALTER TABLE `core_riddle_commands` DISABLE KEYS */;
INSERT INTO `core_riddle_commands` VALUES (1,4,1),(8,4,10),(2,5,2),(3,5,3),(4,6,4),(5,6,5),(10,6,12),(6,7,6),(7,7,7),(9,7,11);
/*!40000 ALTER TABLE `core_riddle_commands` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_scenario`
--

DROP TABLE IF EXISTS `core_scenario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_scenario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `other_names` varchar(255) DEFAULT NULL,
  `description` longtext NOT NULL,
  `severity` varchar(255) NOT NULL,
  `length` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_scenario`
--

LOCK TABLES `core_scenario` WRITE;
/*!40000 ALTER TABLE `core_scenario` DISABLE KEYS */;
INSERT INTO `core_scenario` VALUES (1,'Gefangen in Hogwarts','gefangen in hogwarts, harry Potter, hogwarts','<audio src=\"https://homeescape.pythonanywhere.com/static/harrypotter.mp3\"/>\r\n<p>Du wolltest nur kurz in den Klassenraum, in dem sonst immer “Verteidigung gegen die dunklen Künste” unterrichtet wird, um deinen Zauberstab zu holen, den du dort wohl vergessen hast.</p>\r\n<s>Plötzlich, fällt die Tür zu, <audio src=\"soundbank://soundlibrary/doors/doors_regular/regular_06\"/> sie ist verschlossen und lässt sich nicht mehr öffnen.</s>\r\n<p>Du bist eingeschlossen und selbst deine Hilferufe wird keiner hören, da die meisten so kurz vor den Sommerferien schon abgereist sind.</p>\r\n<p>Wie du ja weißt, kann in Hogwarts nicht appariert werden.</p>\r\n<p>Mit ein paar Zaubersprüchen und etwas Hokuspokus kommst du hier vielleicht wieder raus.</p>\r\n<say-as interpret-as=\"interjection\">Viel Glück</say-as>','MEDIUM',NULL),(2,'Scherz Fragen','scherz fragen, fragen, lustig, scherz, funny','<p>Scherzfragen sind mehrere kleine, witzige Rätsel, die sich aber nicht wirklich lösen lassen.</p>\r\n<p>Vielmehr soll die Antwort den Befragten amüsieren, verblüffen, auf den Arm nehmen oder veräppeln-</p>\r\n<s>Viel Spaß</s>','EASY',NULL);
/*!40000 ALTER TABLE `core_scenario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
) ENGINE=InnoDB AUTO_INCREMENT=133 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2019-07-17 11:59:13.467000','2','Riddle 2 - in welchem Monat hat Anna Geburtstag?',3,'',13,1),(2,'2019-07-17 11:59:13.469000','1','Riddle 1 - Was passiert hier?',3,'',13,1),(3,'2019-07-17 12:05:19.007000','1','Command Gryffindor Farbwechsel',1,'[{\"added\": {}}, {\"added\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (1)\"}}, {\"added\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (2)\"}}, {\"added\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (3)\"}}, {\"added\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (4)\"}}, {\"added\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (5)\"}}, {\"added\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (6)\"}}, {\"added\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (7)\"}}]',9,1),(4,'2019-07-17 12:05:35.994000','1','Command Gryffindor Farbwechsel',2,'[{\"changed\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (7)\", \"fields\": [\"order\"]}}, {\"changed\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (3)\", \"fields\": [\"order\"]}}]',9,1),(5,'2019-07-17 12:06:36.279000','warten 1','Action warten 1',1,'[{\"added\": {}}]',7,1),(6,'2019-07-17 12:06:55.830000','1','Command Gryffindor Farbwechsel',2,'[{\"added\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (8)\"}}]',9,1),(7,'2019-07-17 12:07:24.494000','1','Command Gryffindor Farbwechsel',2,'[{\"changed\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (8)\", \"fields\": [\"order\"]}}, {\"changed\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (5)\", \"fields\": [\"order\"]}}, {\"changed\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (6)\", \"fields\": [\"order\"]}}]',9,1),(8,'2019-07-17 12:07:35.971000','1','Command Gryffindor Farbwechsel',2,'[{\"changed\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (4)\", \"fields\": [\"order\"]}}, {\"changed\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (8)\", \"fields\": [\"order\"]}}]',9,1),(9,'2019-07-17 12:08:09.221000','1','Command Gryffindor Farbwechsel',2,'[{\"added\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (9)\"}}, {\"added\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (10)\"}}, {\"changed\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (6)\", \"fields\": [\"order\"]}}]',9,1),(10,'2019-07-17 12:08:47.942000','1','Command Gryffindor Farbwechsel',2,'[{\"added\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (11)\"}}, {\"added\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (12)\"}}]',9,1),(11,'2019-07-17 12:12:06.318000','4','Riddle 4 - Schau dich im Raum um, an was erinnert dich das?',2,'[{\"changed\": {\"fields\": [\"loop\", \"commands\"]}}]',13,1),(12,'2019-07-17 12:16:42.260000','1','Gefangen in Hogwarts',1,'[{\"added\": {}}, {\"added\": {\"name\": \"ordered riddle\", \"object\": \"OrderedRiddle object (1)\"}}, {\"added\": {\"name\": \"ordered riddle\", \"object\": \"OrderedRiddle object (2)\"}}, {\"added\": {\"name\": \"ordered riddle\", \"object\": \"OrderedRiddle object (3)\"}}, {\"added\": {\"name\": \"ordered riddle\", \"object\": \"OrderedRiddle object (4)\"}}]',14,1),(13,'2019-07-17 12:38:45.122000','1','Command Riddle1: Gryffindor Farbwechsel',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',9,1),(14,'2019-07-17 12:46:35.501000','blink 9','Action blink 9',1,'[{\"added\": {}}]',7,1),(15,'2019-07-17 13:30:28.474000','2','Command Riddle 2: neun mal blinken',1,'[{\"added\": {}}, {\"added\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (13)\"}}, {\"added\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (14)\"}}]',9,1),(16,'2019-07-17 13:32:24.441000','Jalousie dreiviertel','Action Jalousie dreiviertel',1,'[{\"added\": {}}]',7,1),(17,'2019-07-17 13:32:29.060000','3','Command Riddle 2: Jalousie auf dreiviertel',1,'[{\"added\": {}}]',9,1),(18,'2019-07-17 13:32:53.679000','3','Command Riddle 2: Jalousie auf dreiviertel',2,'[{\"added\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (15)\"}}]',9,1),(19,'2019-07-17 13:33:06.630000','2','Command Riddle 2: neun mal blinken',2,'[{\"changed\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (14)\", \"fields\": [\"order\"]}}, {\"changed\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (13)\", \"fields\": [\"order\"]}}]',9,1),(20,'2019-07-17 13:33:45.086000','4','Command Riddle 3: Lampen alle aus',1,'[{\"added\": {}}, {\"added\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (16)\"}}]',9,1),(21,'2019-07-17 13:34:31.858000','Jalousie runter','Action Jalousie runter',1,'[{\"added\": {}}]',7,1),(22,'2019-07-17 13:34:33.708000','5','Command Riddle 3: Jalousien ganz runter',1,'[{\"added\": {}}]',9,1),(23,'2019-07-17 13:34:39.824000','5','Command Riddle 3: Jalousien ganz runter',2,'[{\"added\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (17)\"}}]',9,1),(24,'2019-07-17 13:35:23.884000','6','Command Jalousien ganz hoch',1,'[{\"added\": {}}]',9,1),(25,'2019-07-17 13:35:45.373000','6','Command Jalousien ganz hoch',2,'[]',9,1),(26,'2019-07-17 13:36:01.151000','7','Command Lichter an',1,'[{\"added\": {}}, {\"added\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (18)\"}}]',9,1),(27,'2019-07-17 13:37:27.265000','6','Command Riddle: 4 Jalousien ganz hoch',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',9,1),(28,'2019-07-17 13:37:33.422000','7','Command Riddle 4: Lichter an',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',9,1),(29,'2019-07-17 13:37:45.216000','4','Riddle 4 - Schau dich im Raum um, an was erinnert dich das?',2,'[]',13,1),(30,'2019-07-17 13:40:15.501000','5','Riddle 5 - <p>Der Raum scheint wirklich verhext zu sein. Was könnte das bedeuten?</p>',2,'[{\"changed\": {\"fields\": [\"loop\", \"commands\", \"hints\", \"correct\", \"incorrect\"]}}]',13,1),(31,'2019-07-17 13:41:41.929000','4','Riddle 4 - Schau dich im Raum um, an was erinnert dich das?',2,'[{\"changed\": {\"fields\": [\"hints\", \"correct\", \"incorrect\"]}}]',13,1),(32,'2019-07-17 13:43:15.956000','6','Riddle 6 - <p>Na endlich, das blinken hat aufgehört.</p>\r\n<p>Aber nun ist es so stockfinster, dass du nun garnichts mehr sehen kannst.</p>\r\n<p>Wie gehen die Lichter an?</p>',2,'[{\"changed\": {\"fields\": [\"loop\", \"commands\", \"hints\", \"correct\", \"incorrect\"]}}]',13,1),(33,'2019-07-17 13:43:39.376000','6','Riddle 6 - <p>Na endlich, das blinken hat aufgehört.</p>\r\n\r\n<p>Aber nun ist es so stockfinster, dass du nun garnichts mehr sehen kannst.</p>\r\n<p>Wie gehen die Lichter an?</p>',2,'[{\"changed\": {\"fields\": [\"task\", \"hints\"]}}]',13,1),(34,'2019-07-17 13:46:52.936000','7','Riddle 7 - Vor uns liegen dunkle, schwere Zeiten. Schon bald müssen wir uns entscheiden zwischen dem richtigen Weg und dem leichten. Was würde ein wahrer Zauberer tun um aus dem Raum zu entkommen?',2,'[{\"changed\": {\"fields\": [\"loop\", \"hints\", \"correct\", \"incorrect\"]}}]',13,1),(35,'2019-07-17 13:47:06.399000','7','Riddle 7 - Vor uns liegen dunkle, schwere Zeiten. Schon bald müssen wir uns entscheiden zwischen dem richtigen Weg und dem leichten. Was würde ein wahrer Zauberer tun um aus dem Raum zu entkommen?',2,'[{\"changed\": {\"fields\": [\"commands\"]}}]',13,1),(36,'2019-07-17 13:47:22.765000','1','Gefangen in Hogwarts',2,'[]',14,1),(37,'2019-07-17 14:06:31.633000','19','ModbusMotor 1',1,'[{\"added\": {}}]',19,1),(38,'2019-07-17 14:07:09.018000','8','Command modbus box schließen',1,'[{\"added\": {}}, {\"added\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (19)\"}}]',9,1),(39,'2019-07-17 14:07:38.215000','9','Command modbus box öffnen',1,'[{\"added\": {}}, {\"added\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (20)\"}}]',9,1),(40,'2019-07-17 14:14:28.031000','7','Riddle 7 - Vor uns liegen dunkle, schwere Zeiten. Schon bald müssen wir uns entscheiden zwischen dem richtigen Weg und dem leichten. Was würde ein wahrer Zauberer tun um aus dem Raum zu entkommen?',2,'[{\"changed\": {\"fields\": [\"correct\"]}}]',13,1),(41,'2019-07-17 14:19:48.038000','1','Gefangen in Hogwarts',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',14,1),(42,'2019-07-17 14:20:20.664000','1','Gefangen in Hogwarts',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',14,1),(43,'2019-07-17 14:34:23.770000','1','Gefangen in Hogwarts',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',14,1),(44,'2019-07-17 14:34:33.318000','1','ActiveScenario object (1)',3,'',8,1),(45,'2019-07-17 14:34:39.824000','4','Riddle 4 - Schau dich im Raum um, an was erinnert dich das?',2,'[]',13,1),(46,'2019-07-17 14:41:25.531000','1','Gefangen in Hogwarts',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',14,1),(47,'2019-07-17 14:43:04.491000','1','Gefangen in Hogwarts',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',14,1),(48,'2019-07-17 14:46:53.029000','1','Gefangen in Hogwarts',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',14,1),(49,'2019-07-17 14:47:04.131000','4','Riddle 4 - <s>Schau dich im Raum um, an was erinnert dich das?</s>',2,'[{\"changed\": {\"fields\": [\"task\"]}}]',13,1),(50,'2019-07-17 14:50:53.202000','1','Gefangen in Hogwarts',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',14,1),(51,'2019-07-17 14:53:40.247000','1','Gefangen in Hogwarts',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',14,1),(52,'2019-07-17 14:56:10.353000','1','Gefangen in Hogwarts',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',14,1),(53,'2019-07-17 15:00:55.609000','2','ActiveScenario object (2)',2,'[{\"changed\": {\"fields\": [\"box\"]}}]',8,1),(54,'2019-07-17 15:00:59.687000','2','ActiveScenario object (2)',2,'[{\"changed\": {\"fields\": [\"box\"]}}]',8,1),(55,'2019-07-17 15:09:34.237000','1','Gefangen in Hogwarts',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',14,1),(56,'2019-07-17 15:09:41.392000','1','Gefangen in Hogwarts',2,'[]',14,1),(57,'2019-07-17 15:26:02.585000','1','Gefangen in Hogwarts',2,'[]',14,1),(58,'2019-07-17 15:26:20.532000','2','ActiveScenario object (2)',2,'[{\"changed\": {\"fields\": [\"riddle\"]}}]',8,1),(59,'2019-07-17 15:27:40.932000','5','Riddle 5 - <p>Der Raum scheint wirklich verhext zu sein. Was könnte das bedeuten?</p>',2,'[{\"changed\": {\"fields\": [\"hints\"]}}]',13,1),(60,'2019-07-17 21:53:06.335000','3','ActiveScenario object (3)',3,'',8,1),(61,'2019-07-18 08:04:45.920000','Lampe aus','Action Lampe aus',2,'[{\"changed\": {\"fields\": [\"parameters\"]}}]',7,1),(62,'2019-07-18 08:04:50.733000','Lampe an','Action Lampe an',2,'[{\"changed\": {\"fields\": [\"parameters\"]}}]',7,1),(63,'2019-07-18 08:05:58.009000','Farbe Gelb','Action Farbe Gelb',2,'[]',7,1),(64,'2019-07-18 08:06:27.664000','Farbe dunkel rot','Action Farbe dunkel rot',1,'[{\"added\": {}}]',7,1),(65,'2019-07-18 08:06:53.265000','Farbe hellrot','Action Farbe hellrot',1,'[{\"added\": {}}]',7,1),(66,'2019-07-18 08:07:07.088000','1','Command Riddle1: Gryffindor Farbwechsel 1',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',9,1),(67,'2019-07-18 08:08:29.308000','10','Command Riddle 1: Gryffindor Farbwechsel 2',1,'[{\"added\": {}}, {\"added\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (21)\"}}, {\"added\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (22)\"}}, {\"added\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (23)\"}}, {\"added\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (24)\"}}, {\"added\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (25)\"}}, {\"added\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (26)\"}}, {\"added\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (27)\"}}, {\"added\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (28)\"}}]',9,1),(68,'2019-07-18 08:08:40.599000','4','Riddle 4 - <s>Schau dich im Raum um, an was erinnert dich das?</s>',2,'[{\"changed\": {\"fields\": [\"commands\"]}}]',13,1),(69,'2019-07-18 08:11:20.816000','blinken rot','Action blinken rot',1,'[{\"added\": {}}]',7,1),(70,'2019-07-18 08:11:49.895000','10','Command Riddle 1: Gryffindor Farbwechsel 2',2,'[{\"changed\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (22)\", \"fields\": [\"action\"]}}]',9,1),(71,'2019-07-18 08:13:26.404000','blinken dunkelrot 2x','Action blinken dunkelrot 2x',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',7,1),(72,'2019-07-18 08:13:48.649000','blinken hellrot 2x','Action blinken hellrot 2x',1,'[{\"added\": {}}]',7,1),(73,'2019-07-18 08:14:01.992000','blinken hellrot 2x','Action blinken hellrot 2x',2,'[]',7,1),(74,'2019-07-18 08:14:16.242000','blinken dunkelgelb 2x','Action blinken dunkelgelb 2x',1,'[{\"added\": {}}]',7,1),(75,'2019-07-18 08:14:20.229000','blinken dunkelgelb 2x','Action blinken dunkelgelb 2x',2,'[]',7,1),(76,'2019-07-18 08:14:47.413000','blinken hellgelb 2x','Action blinken hellgelb 2x',1,'[{\"added\": {}}]',7,1),(77,'2019-07-18 08:15:34.729000','10','Command Riddle 1: Gryffindor Farbwechsel 2',2,'[{\"changed\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (22)\", \"fields\": [\"action\"]}}, {\"changed\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (25)\", \"fields\": [\"action\"]}}, {\"changed\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (26)\", \"fields\": [\"action\"]}}]',9,1),(78,'2019-07-18 08:16:16.776000','1','Command Riddle1: Gryffindor Farbwechsel 1',2,'[{\"changed\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (2)\", \"fields\": [\"action\"]}}, {\"changed\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (4)\", \"fields\": [\"action\"]}}, {\"deleted\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (None)\"}}, {\"deleted\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (None)\"}}, {\"deleted\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (None)\"}}, {\"deleted\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (None)\"}}]',9,1),(79,'2019-07-18 08:16:26.028000','1','Command Riddle1: Gryffindor Farbwechsel 1',2,'[{\"deleted\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (None)\"}}]',9,1),(80,'2019-07-18 08:16:44.570000','10','Command Riddle 1: Gryffindor Farbwechsel 2',2,'[{\"changed\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (23)\", \"fields\": [\"action\"]}}, {\"changed\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (27)\", \"fields\": [\"action\"]}}]',9,1),(81,'2019-07-18 08:17:22.676000','1','Command Riddle1: Gryffindor Farbwechsel 1',2,'[{\"deleted\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (None)\"}}, {\"deleted\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (None)\"}}, {\"deleted\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (None)\"}}]',9,1),(82,'2019-07-18 08:17:44.556000','10','Command Riddle 1: Gryffindor Farbwechsel 2',2,'[{\"deleted\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (None)\"}}, {\"deleted\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (None)\"}}, {\"deleted\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (None)\"}}, {\"deleted\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (None)\"}}]',9,1),(83,'2019-07-18 10:05:25.602000','1','Gefangen in Hogwarts',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',14,1),(84,'2019-07-18 10:07:13.937000','1','Gefangen in Hogwarts',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',14,1),(85,'2019-07-18 10:42:13.957000','4','ActiveScenario object (4)',3,'',8,1),(86,'2019-07-18 10:55:58.237000','4','Riddle 4 - <s>Schau dich im Raum um, an was erinnert dich das?</s>',2,'[{\"changed\": {\"fields\": [\"correct\", \"incorrect\"]}}]',13,1),(87,'2019-07-18 10:56:56.754000','5','ActiveScenario object (5)',2,'[{\"changed\": {\"fields\": [\"riddle\"]}}]',8,1),(88,'2019-07-18 10:58:47.731000','4','Riddle 4 - <s>Schau dich im Raum um, an was erinnert dich das?</s>',2,'[{\"changed\": {\"fields\": [\"correct\"]}}]',13,1),(89,'2019-07-18 11:00:01.752000','5','ActiveScenario object (5)',2,'[]',8,1),(90,'2019-07-18 11:11:13.094000','5','ActiveScenario object (5)',2,'[]',8,1),(91,'2019-07-18 11:16:16.167000','5','Riddle 5 - <p>Der Raum scheint wirklich verhext zu sein. Was könnte das bedeuten?</p>',2,'[{\"changed\": {\"fields\": [\"hints\"]}}]',13,1),(92,'2019-07-18 11:17:23.507000','5','ActiveScenario object (5)',3,'',8,1),(93,'2019-07-18 11:33:41.689000','7','ActiveScenario object (7)',3,'',8,1),(94,'2019-07-18 12:43:02.871000','4','Riddle 4 - <s>Schau dich im Raum um, an was erinnert dich das?</s>',2,'[{\"changed\": {\"fields\": [\"hints\"]}}]',13,1),(95,'2019-07-18 12:46:47.589000','5','Riddle 5 - <p>Der Raum scheint wirklich verhext zu sein. Was könnte das bedeuten?</p>',2,'[{\"changed\": {\"fields\": [\"hints\"]}}]',13,1),(96,'2019-07-18 12:47:08.310000','4','Riddle 4 - <s>Schau dich im Raum um, an was erinnert dich das?</s>',2,'[{\"changed\": {\"fields\": [\"hints\"]}}]',13,1),(97,'2019-07-18 12:50:31.607000','7','Riddle 7 - Vor uns liegen dunkle, schwere Zeiten. Schon bald müssen wir uns entscheiden zwischen dem richtigen Weg und dem leichten. Was würde ein wahrer Zauberer tun um aus dem Raum zu entkommen?',2,'[{\"changed\": {\"fields\": [\"hints\"]}}]',13,1),(98,'2019-07-18 12:51:58.577000','6','Riddle 6 - <p>Na endlich, das blinken hat aufgehört.</p>\r\n\r\n<p>Aber nun ist es so stockfinster, dass du nun garnichts mehr sehen kannst.</p>\r\n<p>Wie gehen die Lichter an?</p>',2,'[{\"changed\": {\"fields\": [\"hints\"]}}]',13,1),(99,'2019-07-18 12:52:28.133000','6','Riddle 6 - <p>Na endlich, das blinken hat aufgehört.</p>\r\n\r\n<p>Aber nun ist es so stockfinster, dass du nun garnichts mehr sehen kannst.</p>\r\n<p>Wie gehen die Lichter an?</p>',2,'[]',13,1),(100,'2019-07-18 12:53:31.729000','7','Riddle 7 - Vor uns liegen dunkle, schwere Zeiten. Schon bald müssen wir uns entscheiden zwischen dem richtigen Weg und dem leichten. Was würde ein wahrer Zauberer tun um aus dem Raum zu entkommen?',2,'[{\"changed\": {\"fields\": [\"correct\"]}}]',13,1),(101,'2019-07-18 12:57:36.667000','7','Riddle 7 - Vor uns liegen dunkle, schwere Zeiten. Schon bald müssen wir uns entscheiden zwischen dem richtigen Weg und dem leichten. Was würde ein wahrer Zauberer tun um aus dem Raum zu entkommen?',2,'[{\"changed\": {\"fields\": [\"correct\"]}}]',13,1),(102,'2019-07-18 13:01:43.458000','2','Scherz Fragen',1,'[{\"added\": {}}]',14,1),(103,'2019-07-18 13:04:37.843000','8','Riddle 8 - Wie heißt ein Bumerang der nicht zurück kommt?',1,'[{\"added\": {}}]',13,1),(104,'2019-07-18 13:07:06.305000','9','Riddle 9 - Was ist der Unterschied zwischen <s>dir</s> und <s>mir</s>?',1,'[{\"added\": {}}]',13,1),(105,'2019-07-18 13:09:30.631000','10','Riddle 10 - Wer hat Federn aber keine Flügel?',1,'[{\"added\": {}}]',13,1),(106,'2019-07-18 13:11:01.566000','11','Riddle 11 - Was machen zwei wütende Schafe?',1,'[{\"added\": {}}]',13,1),(107,'2019-07-18 13:11:43.871000','2','Scherz Fragen',2,'[{\"added\": {\"name\": \"ordered riddle\", \"object\": \"OrderedRiddle object (5)\"}}, {\"added\": {\"name\": \"ordered riddle\", \"object\": \"OrderedRiddle object (6)\"}}, {\"added\": {\"name\": \"ordered riddle\", \"object\": \"OrderedRiddle object (7)\"}}, {\"added\": {\"name\": \"ordered riddle\", \"object\": \"OrderedRiddle object (8)\"}}]',14,1),(108,'2019-07-18 13:12:13.002000','11','Riddle 11 - Was machen zwei wütende Schafe?',2,'[{\"changed\": {\"fields\": [\"solution\"]}}]',13,1),(109,'2019-07-18 13:12:25.665000','10','Riddle 10 - Wer hat Federn aber keine Flügel?',2,'[{\"changed\": {\"fields\": [\"solution\"]}}]',13,1),(110,'2019-07-18 13:12:40.958000','8','Riddle 8 - Wie heißt ein Bumerang der nicht zurück kommt?',2,'[{\"changed\": {\"fields\": [\"correct\"]}}]',13,1),(111,'2019-07-18 13:14:12.018000','1','Gefangen in Hogwarts',2,'[{\"changed\": {\"fields\": [\"other_names\"]}}]',14,1),(112,'2019-07-18 13:17:01.772000','9','Riddle 9 - Was ist der Unterschied zwischen dir und mir?',2,'[{\"changed\": {\"fields\": [\"task\", \"solution\"]}}]',13,1),(113,'2019-07-18 13:18:30.611000','9','Riddle 9 - Was ist der Unterschied zwischen dir und mir?',2,'[{\"changed\": {\"fields\": [\"solution\"]}}]',13,1),(114,'2019-07-18 13:31:25.522000','9','Riddle 9 - Was ist der Unterschied zwischen dir und mir?',2,'[{\"changed\": {\"fields\": [\"solution\"]}}]',13,1),(115,'2019-07-18 14:03:15.548000','11','ActiveScenario object (11)',2,'[{\"changed\": {\"fields\": [\"duration\"]}}]',8,1),(116,'2019-07-18 16:08:50.567000','8','Riddle 8 - Wie heißt ein Bumerang der nicht zurück kommt?',2,'[{\"changed\": {\"fields\": [\"hints\"]}}]',13,1),(117,'2019-07-18 16:09:43.964000','8','Riddle 8 - Wie heißt ein Bumerang der nicht zurück kommt?',2,'[{\"changed\": {\"fields\": [\"hints\"]}}]',13,1),(118,'2019-07-18 18:56:49.669000','11','Riddle 11 - Was machen zwei wütende Schafe?',2,'[{\"changed\": {\"fields\": [\"solution\"]}}]',13,1),(119,'2019-07-18 18:57:18.035000','10','Riddle 10 - Wer hat Federn aber keine Flügel?',2,'[{\"changed\": {\"fields\": [\"solution\"]}}]',13,1),(120,'2019-07-18 18:57:57.404000','8','Riddle 8 - Wie heißt ein Bumerang der nicht zurück kommt?',2,'[{\"changed\": {\"fields\": [\"incorrect\"]}}]',13,1),(121,'2019-07-19 09:32:15.074000','14','ActiveScenario object (14)',3,'',8,1),(122,'2019-07-19 12:26:38.943179','20','KNXLamp knxboardlampe',1,'[{\"added\": {}}]',17,2),(123,'2019-07-19 12:27:49.602293','11','Command knx board lampe an',1,'[{\"added\": {}}, {\"added\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (27)\"}}]',9,2),(124,'2019-07-19 12:30:33.260714','KNX lampe aus','Action KNX lampe aus',1,'[{\"added\": {}}]',7,2),(125,'2019-07-19 12:30:43.001077','KNX Lampe an','Action KNX Lampe an',2,'[{\"changed\": {\"fields\": [\"function\"]}}]',7,2),(126,'2019-07-19 12:31:50.746938','Jalousie runter','Action Jalousie runter',2,'[{\"changed\": {\"fields\": [\"function\"]}}]',7,2),(127,'2019-07-19 12:32:05.191202','Jalousie dreiviertel','Action Jalousie dreiviertel',2,'[{\"changed\": {\"fields\": [\"function\"]}}]',7,2),(128,'2019-07-19 12:32:43.510363','12','Command knx board lampe aus',1,'[{\"added\": {}}, {\"added\": {\"name\": \"ordered action\", \"object\": \"OrderedAction object (28)\"}}]',9,2),(129,'2019-07-19 12:33:06.761121','7','Riddle 7 - Vor uns liegen dunkle, schwere Zeiten. Schon bald müssen wir uns entscheiden zwischen dem richtigen Weg und dem leichten. Was würde ein wahrer Zauberer tun um aus dem Raum zu entkommen?',2,'[{\"changed\": {\"fields\": [\"commands\"]}}]',13,2),(130,'2019-07-19 12:33:24.115558','6','Riddle 6 - <p>Na endlich, das blinken hat aufgehört.</p>\r\n\r\n<p>Aber nun ist es so stockfinster, dass du nun garnichts mehr sehen kannst.</p>\r\n<p>Wie gehen die Lichter an?</p>',2,'[{\"changed\": {\"fields\": [\"commands\"]}}]',13,2),(131,'2019-07-19 15:15:34.860031','6','ActiveScenario object (6)',3,'',8,2),(132,'2019-07-19 15:18:34.366034','7','ActiveScenario object (7)',3,'',8,2);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'core','action'),(8,'core','activescenario'),(9,'core','command'),(10,'core','device'),(15,'core','huelamp'),(16,'core','hueremotecontrol'),(17,'core','knxlamp'),(18,'core','knxshutter'),(19,'core','modbusmotor'),(11,'core','orderedaction'),(12,'core','orderedriddle'),(13,'core','riddle'),(14,'core','scenario'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-07-17 12:36:32.082216'),(2,'auth','0001_initial','2019-07-17 12:39:47.633967'),(3,'admin','0001_initial','2019-07-17 12:40:34.525683'),(4,'admin','0002_logentry_remove_auto_add','2019-07-17 12:40:35.124480'),(5,'admin','0003_logentry_add_action_flag_choices','2019-07-17 12:40:35.924475'),(6,'contenttypes','0002_remove_content_type_name','2019-07-17 12:40:37.474376'),(7,'auth','0002_alter_permission_name_max_length','2019-07-17 12:40:38.024414'),(8,'auth','0003_alter_user_email_max_length','2019-07-17 12:40:38.653695'),(9,'auth','0004_alter_user_username_opts','2019-07-17 12:40:39.331026'),(10,'auth','0005_alter_user_last_login_null','2019-07-17 12:40:40.124395'),(11,'auth','0006_require_contenttypes_0002','2019-07-17 12:40:40.146646'),(12,'auth','0007_alter_validators_add_error_messages','2019-07-17 12:40:40.624491'),(13,'auth','0008_alter_user_username_max_length','2019-07-17 12:40:41.518767'),(14,'auth','0009_alter_user_last_name_max_length','2019-07-17 12:40:42.024397'),(15,'core','0001_initial','2019-07-17 12:47:10.744175'),(16,'sessions','0001_initial','2019-07-17 12:47:31.027693');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('cbt8u0eb2aii06a94rgm0syzayr759yx','ZTQwOGE0YjJjZGVjM2EyNTQ1YzBlOGY0ZjQ1NmQzODMzMmRjMmQ3Yzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4OTUzOGQ0YTllOWUzNjdhZDgxZDZmZjQ4M2ZjZWY5NDExZTlhNTZhIn0=','2019-07-31 21:31:29.106253'),('j2z95od9995svxm0ofyjqu2asg2zh4y0','ZTQwOGE0YjJjZGVjM2EyNTQ1YzBlOGY0ZjQ1NmQzODMzMmRjMmQ3Yzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4OTUzOGQ0YTllOWUzNjdhZDgxZDZmZjQ4M2ZjZWY5NDExZTlhNTZhIn0=','2019-07-31 11:56:49.421000'),('kfrqevg1rftax6ddd8a4fpy0vgmqvzme','N2NkOGRjYTgyMTVlOTI3ZTI1NjU0YmM1MzIwOGZkNTYwNjFiYmEwNjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NDVjOTk3M2RmODAzODY1NzkxMWZkODdlOGJhOTk2MjY4NjYzMDlmIn0=','2019-08-02 12:24:24.399423'),('tsxcz0ijnh83o4eovp5f7hfiphjhlb1y','ZTQwOGE0YjJjZGVjM2EyNTQ1YzBlOGY0ZjQ1NmQzODMzMmRjMmQ3Yzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4OTUzOGQ0YTllOWUzNjdhZDgxZDZmZjQ4M2ZjZWY5NDExZTlhNTZhIn0=','2019-07-31 14:04:06.920000'),('we9z5olx74gwn3zq7zvdvocwb0ler0wc','N2NkOGRjYTgyMTVlOTI3ZTI1NjU0YmM1MzIwOGZkNTYwNjFiYmEwNjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NDVjOTk3M2RmODAzODY1NzkxMWZkODdlOGJhOTk2MjY4NjYzMDlmIn0=','2019-08-02 12:21:06.375867');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-29 10:24:14
