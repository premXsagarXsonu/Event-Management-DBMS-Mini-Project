-- MINI PROJECT: EVENT MANAGEMENT COMPANY DATABASE
--SRN: PES1UG20CS825
--NAME: PREM SAGAR J S
--SRN: PES1UG20CS808
--NAME: BHAVANA N G

-- THIS .SQL FILE CONTAINS CREATION OF DB,TABLES,VIEWS,TRIGGERS,FUNCTIONS,CURSORS AND PROCEDUCERS.
-- YOU CAN USE THIS .SQL FILE TO IMPORT MY EVENT MANAGEMENT DB


-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 28, 2022 at 04:18 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ems`
--
CREATE DATABASE IF NOT EXISTS `ems` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `ems`;

DELIMITER $$
--
-- Procedures
--
DROP PROCEDURE IF EXISTS `WorkerEmailList`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `WorkerEmailList` (INOUT `emailList` VARCHAR(4000))  BEGIN
DECLARE finished INTEGER DEFAULT 0;
DECLARE Worker_Email varchar(100) DEFAULT "";
DEClARE curEmail CURSOR FOR SELECT w_email FROM worker;
DECLARE CONTINUE HANDLER FOR NOT FOUND SET finished = 1;
OPEN curEmail;
getEmail: LOOP
FETCH curEmail INTO Worker_Email;
IF finished = 1 THEN
LEAVE getEmail;
END IF;
SET emailList = CONCAT(Worker_Email,";",emailList);
END LOOP getEmail;
CLOSE curEmail;
END$$

--
-- Functions
--
DROP FUNCTION IF EXISTS `no_of_days_remaining_for_e`$$
CREATE DEFINER=`root`@`localhost` FUNCTION `no_of_days_remaining_for_e` (`event_date` DATE) RETURNS INT(11) BEGIN
DECLARE cur_date DATE;
Select current_date()into cur_date;
RETURN (event_date)-(cur_date);
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--
-- Creation: Nov 17, 2022 at 07:13 AM
--

DROP TABLE IF EXISTS `admin`;
CREATE TABLE IF NOT EXISTS `admin` (
  `A_Id` int(11) NOT NULL,
  `A_Name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`A_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELATIONSHIPS FOR TABLE `admin`:
--

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`A_Id`, `A_Name`) VALUES
(1, 'ANU'),
(2, 'Bhavana'),
(825, 'Prem Sagar');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--
-- Creation: Nov 17, 2022 at 07:14 AM
--

DROP TABLE IF EXISTS `customer`;
CREATE TABLE IF NOT EXISTS `customer` (
  `C_ID` int(11) NOT NULL,
  `C_Name` varchar(20) DEFAULT NULL,
  `C_Place` varchar(20) DEFAULT NULL,
  `C_Phone` varchar(10) NOT NULL,
  PRIMARY KEY (`C_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELATIONSHIPS FOR TABLE `customer`:
--

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`C_ID`, `C_Name`, `C_Place`, `C_Phone`) VALUES
(441, 'PRATHIBHA', 'MYSURU', '7001931823'),
(442, 'ARPITH', 'UDUPI', '6633662728'),
(443, 'SNEHA', 'SULLIA', '7332211100'),
(444, 'PREM', 'KOLAR', '6112881826'),
(445, 'SAMPREETH', 'BENGALURU', '7117289117');

-- --------------------------------------------------------

--
-- Table structure for table `event`
--
-- Creation: Nov 17, 2022 at 07:14 AM
--

DROP TABLE IF EXISTS `event`;
CREATE TABLE IF NOT EXISTS `event` (
  `E_Id` int(11) NOT NULL,
  `E_Date` date DEFAULT NULL,
  `E_Place` varchar(20) DEFAULT NULL,
  `E_Type` varchar(20) DEFAULT NULL,
  `E_Fee` int(11) NOT NULL,
  `W_Id` int(11) NOT NULL,
  `A_Id` int(11) NOT NULL,
  `C_ID` int(11) NOT NULL,
  PRIMARY KEY (`E_Id`),
  KEY `W_Id` (`W_Id`),
  KEY `A_Id` (`A_Id`),
  KEY `C_ID` (`C_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELATIONSHIPS FOR TABLE `event`:
--   `W_Id`
--       `worker` -> `W_Id`
--   `A_Id`
--       `admin` -> `A_Id`
--   `C_ID`
--       `customer` -> `C_ID`
--

--
-- Dumping data for table `event`
--

INSERT INTO `event` (`E_Id`, `E_Date`, `E_Place`, `E_Type`, `E_Fee`, `W_Id`, `A_Id`, `C_ID`) VALUES
(11, '2022-11-30', 'SULLIA', 'Marriage', 300000, 1001, 1, 441),
(22, '2022-11-25', 'MYSURU', 'Engagment', 50000, 1001, 2, 443),
(33, '2022-11-27', 'OOTY', 'Mehendi', 100000, 1004, 1, 445),
(44, '2022-11-28', 'LEH', 'Engagment', 60000, 1003, 1, 442),
(55, '2022-11-30', 'DHARWAD', 'Birthday', 25000, 1003, 2, 444),
(66, '2022-11-29', 'MYSURU', 'Anniversary', 40000, 1005, 2, 441);

--
-- Triggers `event`
--
DROP TRIGGER IF EXISTS `Check_date`;
DELIMITER $$
CREATE TRIGGER `Check_date` BEFORE INSERT ON `event` FOR EACH ROW BEGIN
DECLARE cur_date DATE;
Select current_date()into cur_date;
IF NEW.e_date < cur_date THEN
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = 'ERROR: Event Date Is Not Available';
END IF;
END
$$
DELIMITER ;
DROP TRIGGER IF EXISTS `backup`;
DELIMITER $$
CREATE TRIGGER `backup` BEFORE DELETE ON `event` FOR EACH ROW Begin
Insert into event_backup
Values (old.e_id,old.e_date,old.e_place,old.e_type,old.e_fee,old.w_id,old.a_id,old.c_id);
End
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `event_backup`
--
-- Creation: Nov 24, 2022 at 04:01 AM
--

DROP TABLE IF EXISTS `event_backup`;
CREATE TABLE IF NOT EXISTS `event_backup` (
  `E_id` int(11) NOT NULL,
  `E_date` date DEFAULT NULL,
  `E_place` varchar(20) DEFAULT NULL,
  `E_type` varchar(20) DEFAULT NULL,
  `E_fee` int(11) NOT NULL,
  `W_id` int(11) NOT NULL,
  `A_id` int(11) NOT NULL,
  `C_id` int(11) NOT NULL,
  PRIMARY KEY (`E_id`),
  KEY `W_id` (`W_id`),
  KEY `A_id` (`A_id`),
  KEY `C_id` (`C_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELATIONSHIPS FOR TABLE `event_backup`:
--   `W_id`
--       `worker` -> `W_Id`
--   `A_id`
--       `admin` -> `A_Id`
--   `C_id`
--       `customer` -> `C_ID`
--

--
-- Dumping data for table `event_backup`
--

INSERT INTO `event_backup` (`E_id`, `E_date`, `E_place`, `E_type`, `E_fee`, `W_id`, `A_id`, `C_id`) VALUES
(78, '2022-11-24', 'Kolar', 'Fest', 60000, 1001, 825, 441);

-- --------------------------------------------------------

--
-- Table structure for table `worker`
--
-- Creation: Nov 17, 2022 at 07:13 AM
--

DROP TABLE IF EXISTS `worker`;
CREATE TABLE IF NOT EXISTS `worker` (
  `W_Id` int(11) NOT NULL,
  `W_Name` varchar(20) DEFAULT NULL,
  `W_Type` varchar(20) DEFAULT NULL,
  `W_Email` varchar(20) DEFAULT NULL,
  `W_City` varchar(20) DEFAULT NULL,
  `W_Phone` varchar(10) NOT NULL,
  PRIMARY KEY (`W_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELATIONSHIPS FOR TABLE `worker`:
--

--
-- Dumping data for table `worker`
--

INSERT INTO `worker` (`W_Id`, `W_Name`, `W_Type`, `W_Email`, `W_City`, `W_Phone`) VALUES
(1001, 'Venkatesh', 'Manager', 'Venku@ems', 'MYSURU', '9008593113'),
(1002, 'Arvind', 'Caterier', 'Arviu@ems', 'SULLIA', '7349150055'),
(1003, 'Lokesh', 'Flowermen', 'Lokeu@ems', 'PUTTUR', '7892051935'),
(1004, 'Vishvesh', 'Cleaner', 'Vishu@ems', 'SAGARA', '9480155585'),
(1005, 'Ramesh', 'Accountant', 'Rameu@ems', 'SRINGERI', '9423422342'),
(1006, 'Suresh', 'Cleaner', 'Sureu@ems', 'BENGALURU', '9878927304'),
(1007, 'Vishnu', 'Decoter', 'Vishnu@ems', 'PUTTUR', '8887382826');

-- --------------------------------------------------------

--
-- Stand-in structure for view `workerevent`
-- (See below for the actual view)
--
DROP VIEW IF EXISTS `workerevent`;
CREATE TABLE IF NOT EXISTS `workerevent` (
`Worker` varchar(20)
,`Event` varchar(20)
);

-- --------------------------------------------------------

--
-- Structure for view `workerevent` exported as a table
--
DROP TABLE IF EXISTS `workerevent`;
CREATE TABLE IF NOT EXISTS `workerevent`(
    `Worker` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
    `Event` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL
);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `event`
--
ALTER TABLE `event`
  ADD CONSTRAINT `event_ibfk_1` FOREIGN KEY (`W_Id`) REFERENCES `worker` (`W_Id`),
  ADD CONSTRAINT `event_ibfk_2` FOREIGN KEY (`A_Id`) REFERENCES `admin` (`A_Id`),
  ADD CONSTRAINT `event_ibfk_3` FOREIGN KEY (`C_ID`) REFERENCES `customer` (`C_ID`);

--
-- Constraints for table `event_backup`
--
ALTER TABLE `event_backup`
  ADD CONSTRAINT `event_backup_ibfk_1` FOREIGN KEY (`W_id`) REFERENCES `worker` (`W_Id`),
  ADD CONSTRAINT `event_backup_ibfk_2` FOREIGN KEY (`A_id`) REFERENCES `admin` (`A_Id`),
  ADD CONSTRAINT `event_backup_ibfk_3` FOREIGN KEY (`C_id`) REFERENCES `customer` (`C_ID`);


--
-- Metadata
--
USE `phpmyadmin`;

--
-- Metadata for table admin
--

--
-- Metadata for table customer
--

--
-- Metadata for table event
--

--
-- Metadata for table event_backup
--

--
-- Metadata for table worker
--

--
-- Metadata for table workerevent
--

--
-- Metadata for database ems
--
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
