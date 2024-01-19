-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 29, 2021 at 06:38 PM
-- Server version: 10.1.30-MariaDB
-- PHP Version: 7.2.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mbila`
--

-- --------------------------------------------------------

--
-- Table structure for table `bills`
--

CREATE TABLE `bills` (
  `BillNo` varchar(100) NOT NULL,
  `Dispenser` varchar(100) NOT NULL,
  `BigBottle` varchar(100) NOT NULL,
  `SmallBottle` varchar(100) NOT NULL,
  `SachetWater` varchar(100) NOT NULL,
  `CostDispenser` varchar(100) NOT NULL,
  `CostBigBottle` varchar(100) NOT NULL,
  `CostSmallBottle` varchar(100) NOT NULL,
  `CostSachetWater` varchar(100) NOT NULL,
  `Amount` varchar(100) NOT NULL,
  `DateStamp` varchar(100) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Phone` varchar(100) NOT NULL,
  `EnteredBy` varchar(150) NOT NULL,
  `PreviousTotal` varchar(100) NOT NULL,
  `UpdatedBy` varchar(150) NOT NULL,
  `UpdatedDate` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bills`
--

INSERT INTO `bills` (`BillNo`, `Dispenser`, `BigBottle`, `SmallBottle`, `SachetWater`, `CostDispenser`, `CostBigBottle`, `CostSmallBottle`, `CostSachetWater`, `Amount`, `DateStamp`, `Name`, `Phone`, `EnteredBy`, `PreviousTotal`, `UpdatedBy`, `UpdatedDate`) VALUES
('20121810448752605', '3', '3', '3', '3', '250', '150', '90', '60', '1650.00', '18/12/2020 12:29:22.751604', '', '', 'super', '4440.00', 'admin', '28/12/2020 14:24:51.828479'),
('20121814778299639', '5', '5', '5', '5', '250', '150', '90', '60', '2750.00', '18/12/2020 13:16:44.299639', '', '', 'admin', '27750.00', 'super', '26/12/2020 15:39:24.543440'),
('20121818384384060', '6', '6', '6', '6', '250', '150', '95', '60', '3330.00', '18/12/2020 12:23:35.384060', 'Babson Jidda', '08025312632', 'super', '', '', ''),
('20121848473020962', '50', '20', '20', '20', '250', '150', '90', '60', '18500.00', '18/12/2020 11:54:21.020962', '', '', 'super', '180000.00', 'super', '26/12/2020 15:52:23.503407'),
('20121855307829503', '9', '1', '1', '1', '250', '150', '90', '60', '2550.00', '18/12/2020 13:57:49.829503', '', '', 'admin', '3400.00', 'super', '28/12/2020 14:19:43.635394'),
('20121871235573218', '1', '5', '5', '5', '250', '150', '90', '60', '1750.00', '18/12/2020 11:53:45.573218', '', '', 'admin', '2220.00', 'admin', '26/12/2020 19:13:10.323381'),
('20121882641622598', '8', '9', '9', '9', '250', '150', '95', '60', '4745.00', '18/12/2020 12:12:26.622598', '', '', 'admin', '', '', ''),
('20121892434871363', '4', '4', '4', '4', '250', '150', '95', '60', '2220.00', '18/12/2020 12:11:45.871363', '', '', 'admin', '', '', ''),
('20121894790556993', '1', '1', '1', '1', '250', '150', '90', '60', '550.00', '18/12/2020 12:53:41.423692', '', '', 'admin', '250.00', 'admin', '28/12/2020 15:11:27.313186'),
('20121916625788798', '5', '5', '5', '5', '250', '150', '90', '60', '2750.00', '19/12/2020 13:07:35.788798', '', '', 'aliyu', '27500.00', 'super', '28/12/2020 15:16:09.656543'),
('20121956143148516', '4', '4', '4', '4', '250', '150', '90', '60', '2200.00', '19/12/2020 13:06:55.148516', '', '', 'aliyu', '1075.00', 'super', '26/12/2020 15:44:04.040667'),
('20121991134954943', '2', '2', '2', '2', '250', '150', '90', '60', '1100.00', '19/12/2020 13:08:28.954943', '', '', 'admin', '3850.00', 'admin', '26/12/2020 15:50:31.800247'),
('20122632553425462', '5', '5', '5', '5', '250', '150', '90', '60', '2750.00', '26/12/2020 19:23:42.425462', '', '', 'admin', '2450.00', 'admin', '26/12/2020 19:23:55.523706'),
('20122651664280329', '2', '2', '2', '2', '250', '150', '90', '60', '1100.00', '26/12/2020 19:19:04.280329', '', '', 'employee01', '1250.00', 'super', '26/12/2020 19:24:41.762985'),
('20122671955120850', '5', '5', '5', '5', '250', '150', '90', '60', '2750.00', '26/12/2020 19:25:06.120850', '', '', 'super', '3950.00', 'admin', '28/12/2020 14:23:45.661833'),
('20122682774073051', '1', '1', '10', '10', '250', '150', '90', '60', '1900.00', '26/12/2020 19:20:19.073051', '', '', 'admin', '5500.00', 'super', '28/12/2020 16:10:09.963746'),
('20122686318312788', '2', '10', '2', '1', '250', '150', '90', '60', '2240.00', '26/12/2020 19:19:26.312788', '', '', 'employee01', '890.00', 'super', '26/12/2020 19:21:47.259594'),
('20122825453060514', '2', '2', '2', '3', '250', '150', '90', '60', '1160.00', '28/12/2020 15:10:02.060514', '', '', 'employee01', '1040.00', 'super', '28/12/2020 16:22:09.986451'),
('20122825501552134', '1', '1', '1', '1', '250', '150', '90', '60', '550.00', '28/12/2020 15:07:13.552134', '', '', 'employee01', '55000.00', 'super', '28/12/2020 15:45:10.686928'),
('20122847276218374', '3', '3', '3', '3', '250', '150', '90', '60', '1650.00', '28/12/2020 14:26:40.217380', '', '', 'employee01', '14880.00', 'super', '28/12/2020 16:26:23.810096'),
('20122864151544243', '5', '5', '5', '5', '250', '150', '90', '60', '2750.00', '28/12/2020 14:29:38.544243', '', '', 'employee01', '27500.00', 'super', '28/12/2020 15:14:54.719188'),
('20122865010398556', '99', '99', '99', '99', '250', '150', '90', '60', '54450.00', '28/12/2020 15:06:59.398556', '', '', 'employee01', '55550.00', 'super', '28/12/2020 15:26:59.902668'),
('20122880380455206', '18', '18', '18', '18', '250', '150', '90', '60', '9900.00', '28/12/2020 15:09:54.455206', '', '', 'employee01', '99000.00', 'super', '28/12/2020 15:46:07.845839'),
('20123016864796207N', '80', '80', '80', '80', '250', '150', '90', '60', '44000.00', '30/12/2020 16:31:47.796207', '', '', 'super', '3850.00', 'super', '30/12/2020 16:32:50.935419'),
('20123016931468928N', '5', '5', '5', '5', '250', '150', '90', '60', '2750.00', '30/12/2020 17:04:07.468928', '', '', 'super', '', '', ''),
('20123040728444488N', '20', '20', '20', '20', '250', '150', '90', '60', '11000.00', '30/12/2020 17:11:56.444488', '', '', 'admin', '1100.00', 'admin', '30/12/2020 17:12:07.340972'),
('20123044234114155N', '81', '51', '81', '51', '250', '150', '90', '60', '38250.00', '30/12/2020 17:08:47.114155', '', '', 'super', '3770.00', 'super', '30/12/2020 17:09:01.468945'),
('20123045599717611N', '7', '7', '7', '7', '250', '150', '90', '60', '3850.00', '30/12/2020 14:23:33.717611', '', '', 'super', '', '', ''),
('20123082277667514N', '25', '25', '25', '25', '250', '150', '90', '60', '13750.00', '30/12/2020 16:26:24.667514', '', '', 'super', '', '', ''),
('20123084855930815N', '12', '12', '12', '12', '250', '150', '90', '60', '6600.00', '30/12/2020 17:11:12.929837', '', '', 'super', '550.00', 'super', '30/12/2020 17:11:25.148508'),
('21021249073077395N', '50', '50', '50', '250', '250', '150', '90', '60', '39500.00', '12/02/2021 18:30:21.077395', '', '', 'mamadi', '275000.00', 'super', '12/02/2021 18:33:08.365997'),
('21021252447120773N', '10', '10', '10', '10', '250', '150', '90', '60', '5500.00', '12/02/2021 18:26:43.120773', '', '', 'super', '', '', ''),
('21102945661093084N', '150', '150', '10', '100', '250', '150', '90', '60', '66900.00', '29/10/2021 17:27:18.093084', '', '', 'super', '12900.00', 'super', '29/10/2021 17:28:05.831294');

-- --------------------------------------------------------

--
-- Table structure for table `driverbills`
--

CREATE TABLE `driverbills` (
  `BillNo` varchar(100) NOT NULL,
  `Dispenser` varchar(100) NOT NULL,
  `BigBottle` varchar(100) NOT NULL,
  `SmallBottle` varchar(100) NOT NULL,
  `SachetWater` varchar(100) NOT NULL,
  `CostDispenser` varchar(100) NOT NULL,
  `CostBigBottle` varchar(100) NOT NULL,
  `CostSmallBottle` varchar(100) NOT NULL,
  `CostSachetWater` varchar(100) NOT NULL,
  `Amount` varchar(100) NOT NULL,
  `DateStamp` varchar(100) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `PlateNo` varchar(100) NOT NULL,
  `Phone` varchar(100) NOT NULL,
  `NewDateStamp` varchar(100) NOT NULL,
  `RDispenser` varchar(100) NOT NULL,
  `RBigBottle` varchar(100) NOT NULL,
  `RSmallBottle` varchar(100) NOT NULL,
  `RSachetWater` varchar(100) NOT NULL,
  `RAmount` varchar(100) NOT NULL,
  `DDispenser` varchar(100) NOT NULL,
  `DBigBottle` varchar(100) NOT NULL,
  `DSmallBottle` varchar(100) NOT NULL,
  `DSachetWater` varchar(100) NOT NULL,
  `DAmount` varchar(100) NOT NULL,
  `SDispenser` varchar(100) NOT NULL,
  `SBigBottle` varchar(100) NOT NULL,
  `SSmallBottle` varchar(100) NOT NULL,
  `SSachetWater` varchar(100) NOT NULL,
  `SAmount` varchar(100) NOT NULL,
  `EnteredBy` varchar(150) NOT NULL,
  `PreviousTotal` varchar(100) NOT NULL,
  `UpdatedBy` varchar(100) NOT NULL,
  `UpdatedDate` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `driverbills`
--

INSERT INTO `driverbills` (`BillNo`, `Dispenser`, `BigBottle`, `SmallBottle`, `SachetWater`, `CostDispenser`, `CostBigBottle`, `CostSmallBottle`, `CostSachetWater`, `Amount`, `DateStamp`, `Name`, `PlateNo`, `Phone`, `NewDateStamp`, `RDispenser`, `RBigBottle`, `RSmallBottle`, `RSachetWater`, `RAmount`, `DDispenser`, `DBigBottle`, `DSmallBottle`, `DSachetWater`, `DAmount`, `SDispenser`, `SBigBottle`, `SSmallBottle`, `SSachetWater`, `SAmount`, `EnteredBy`, `PreviousTotal`, `UpdatedBy`, `UpdatedDate`) VALUES
('20121814311859208', '50', '5', '5', '5', '240', '140', '85', '55', '13400.00', '18/12/2020 12:13:22.859208', 'Ali Baba', 'XA 101 BIU', '(\'08025632632\',)', '', '0', '0', '0', '0', '0.00', '0', '0', '0', '0', '0.00', '0', '0', '0', '0', '0.00', 'admin', '', '', ''),
('20121832296578950', '7', '6', '6', '6', '240', '140', '85', '55', '3360.00', '18/12/2020 14:03:08.578950', 'Ali Baba', 'XA 101 BIU', '(\'08025632632\',)', '', '0', '0', '0', '0', '0.00', '0', '0', '0', '0', '0.00', '0', '0', '0', '0', '0.00', 'admin', '3150.00', 'super', '29/12/2020 16:58:48.396197'),
('20121849448785571', '52', '26', '2', '2', '240', '140', '90', '55', '16410.00', '18/12/2020 12:07:53.785571', 'Ali Baba', 'XA 101 BIU', '(\'08025632632\',)', '19/12/2020 13:31:02.835832', '0', '0', '0', '1', '55.00', '0', '0', '0', '0', '0.00', '52', '26', '2', '1', '16345.00', 'super', '', '', ''),
('20123020070821836', '6', '6', '6', '6', '240', '140', '85', '55', '3120.00', '30/12/2020 11:41:50.822834', 'Aliyu Baba', 'XA 101 BIU', '(\'8025632632\',)', '', '0', '0', '0', '0', '0.00', '0', '0', '0', '0', '0.00', '0', '0', '0', '0', '0.00', 'admin', '', '', ''),
('20123021535418233D', '50', '50', '50', '50', '240', '140', '85', '55', '26000.00', '30/12/2020 16:27:06.418233', 'Aliyu Baba', 'XA 101 BIU', '(\'8025632632\',)', '12/02/2021 18:27:37.207664', '5', '5', '5', '0', '2325.00', '5', '5', '0', '0', '1900.00', '40', '40', '45', '50', '21775.00', 'super', '', '', ''),
('20123022039817235D', '7', '7', '7', '7', '240', '140', '85', '55', '3640.00', '30/12/2020 14:23:51.817235', 'Aliyu Baba', 'XA 101 BIU', '(\'8025632632\',)', '', '0', '0', '0', '0', '0.00', '0', '0', '0', '0', '0.00', '0', '0', '0', '0', '0.00', 'super', '', '', ''),
('20123028020184618D', '60', '60', '60', '60', '240', '140', '85', '55', '31200.00', '30/12/2020 16:57:20.184618', 'Aliyu Baba', 'XA 101 BIU', '(\'8025632632\',)', '', '0', '0', '0', '0', '0.00', '0', '0', '0', '0', '0.00', '0', '0', '0', '0', '0.00', 'super', '3120.00', 'super', '30/12/2020 16:57:29.681239'),
('20123029389350536', '80', '80', '80', '80', '240', '140', '85', '55', '41600.00', '30/12/2020 10:39:53.350536', 'Aliyu Baba', 'XA 101 BIU', '(\'8025632632\',)', '', '0', '0', '0', '0', '0.00', '0', '0', '0', '0', '0.00', '0', '0', '0', '0', '0.00', 'admin', '4160.00', 'admin', '30/12/2020 11:41:35.701889'),
('20123030338441429', '10', '10', '10', '10', '240', '140', '85', '55', '5200.00', '30/12/2020 10:42:31.441429', 'Aliyu Baba', 'XA 101 BIU', '(\'8025632632\',)', '', '0', '0', '0', '0', '0.00', '0', '0', '0', '0', '0.00', '0', '0', '0', '0', '0.00', 'admin', '20800.00', 'admin', '30/12/2020 10:42:41.919415'),
('20123034635770758', '23', '23', '23', '23', '240', '140', '85', '55', '11960.00', '30/12/2020 09:10:26.770758', 'Aliyu Baba', 'XA 101 BIU', '(\'8025632632\',)', '30/12/2020 09:57:31.393682', '0', '0', '0', '0', '0.00', '0', '0', '0', '0', '0.00', '23', '23', '23', '23', '11960.00', 'admin', '520.00', 'admin', '30/12/2020 09:47:29.824151'),
('20123044845031927D', '40', '40', '40', '40', '240', '140', '85', '55', '20800.00', '30/12/2020 17:03:10.031927', 'Aliyu Baba', 'XA 101 BIU', '(\'8025632632\',)', '29/10/2021 17:31:50.462796', '5', '5', '5', '5', '2600.00', '5', '5', '0', '0', '1900.00', '30', '30', '35', '35', '16300.00', 'super', '2080.00', 'super', '30/12/2020 17:03:24.432282'),
('20123046432671054', '3', '3', '3', '3', '240', '140', '85', '55', '1560.00', '30/12/2020 09:07:25.671054', 'Aliyu Baba', 'XA 101 BIU', '(\'8025632632\',)', '', '0', '0', '0', '0', '0.00', '0', '0', '0', '0', '0.00', '0', '0', '0', '0', '0.00', 'admin', '15600.00', 'admin', '30/12/2020 09:10:08.944284'),
('20123050671688147D', '41', '4', '4', '4', '240', '140', '85', '55', '10960.00', '30/12/2020 17:02:01.688147', 'Aliyu Baba', 'XA 101 BIU', '(\'8025632632\',)', '', '0', '0', '0', '0', '0.00', '0', '0', '0', '0', '0.00', '0', '0', '0', '0', '0.00', 'super', '2080.00', 'super', '30/12/2020 17:02:10.862927'),
('20123065327166578', '1', '1', '1', '1', '240', '140', '85', '55', '520.00', '30/12/2020 11:42:37.166578', 'Aliyu Baba', 'XA 101 BIU', '(\'8025632632\',)', '', '0', '0', '0', '0', '0.00', '0', '0', '0', '0', '0.00', '0', '0', '0', '0', '0.00', 'admin', '', '', ''),
('20123087889657890D', '10', '1', '1', '1', '240', '140', '85', '55', '2680.00', '30/12/2020 16:57:53.657890', 'Aliyu Baba', 'XA 101 BIU', '(\'8025632632\',)', '', '0', '0', '0', '0', '0.00', '0', '0', '0', '0', '0.00', '0', '0', '0', '0', '0.00', 'super', '520.00', 'super', '30/12/2020 16:58:09.766993'),
('20123091340143776D', '1', '1', '1', '1', '240', '140', '85', '55', '520.00', '30/12/2020 16:55:39.143776', 'Aliyu Baba', 'XA 101 BIU', '(\'8025632632\',)', '', '0', '0', '0', '0', '0.00', '0', '0', '0', '0', '0.00', '0', '0', '0', '0', '0.00', 'super', '', '', ''),
('20123098096641663D', '5', '5', '5', '5', '240', '140', '85', '55', '2600.00', '30/12/2020 16:41:46.641663', 'Aliyu Baba', 'XA 101 BIU', '(\'8025632632\',)', '', '0', '0', '0', '0', '0.00', '0', '0', '0', '0', '0.00', '0', '0', '0', '0', '0.00', 'super', '', '', ''),
('20123099305655496', '40', '40', '40', '40', '240', '140', '85', '55', '20800.00', '30/12/2020 10:41:42.655496', 'Aliyu Baba', 'XA 101 BIU', '(\'8025632632\',)', '', '0', '0', '0', '0', '0.00', '0', '0', '0', '0', '0.00', '0', '0', '0', '0', '0.00', 'admin', '2080.00', 'admin', '30/12/2020 10:42:10.208008'),
('21021326541652965D', '500', '500', '500', '100', '240', '140', '85', '55', '238000.00', '13/02/2021 13:01:17.652965', 'Alkali Mohammed', 'XA 555 BIU', '(\'111111\',)', '13/02/2021 13:05:05.614724', '50', '100', '10', '0', '26850.00', '50', '0', '20', '0', '13700.00', '400', '400', '470', '500', '219450.00', 'super', '260000.00', 'super', '13/02/2021 13:06:47.745593'),
('21102925045365524D', '100', '100', '100', '100', '240', '140', '85', '55', '52000.00', '29/10/2021 17:31:01.365524', 'Alkali Mohammed', 'XA 555 BIU', '(\'111111\',)', '', '0', '0', '0', '0', '0.00', '0', '0', '0', '0', '0.00', '0', '0', '0', '0', '0.00', 'super', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `operaterbills`
--

CREATE TABLE `operaterbills` (
  `BillNo` varchar(100) NOT NULL,
  `Dispenser` varchar(100) NOT NULL,
  `BigBottle` varchar(100) NOT NULL,
  `SmallBottle` varchar(100) NOT NULL,
  `SachetWater` varchar(100) NOT NULL,
  `CostDispenser` varchar(100) NOT NULL,
  `CostBigBottle` varchar(100) NOT NULL,
  `CostSmallBottle` varchar(100) NOT NULL,
  `CostSachetWater` varchar(100) NOT NULL,
  `Amount` varchar(100) NOT NULL,
  `PriceType` varchar(100) NOT NULL,
  `DateStamp` varchar(100) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Phone` varchar(100) NOT NULL,
  `EnteredBy` varchar(150) NOT NULL,
  `PreviousTotal` varchar(100) NOT NULL,
  `UpdatedBy` varchar(100) NOT NULL,
  `UpdatedDate` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `operaterbills`
--

INSERT INTO `operaterbills` (`BillNo`, `Dispenser`, `BigBottle`, `SmallBottle`, `SachetWater`, `CostDispenser`, `CostBigBottle`, `CostSmallBottle`, `CostSachetWater`, `Amount`, `PriceType`, `DateStamp`, `Name`, `Address`, `Phone`, `EnteredBy`, `PreviousTotal`, `UpdatedBy`, `UpdatedDate`) VALUES
('20123011515758112', '2', '2', '2', '2', '5', '5', '5', '5', '40.00', 'DAY', '30/12/2020 13:12:13.759109', 'Ali Baba', 'Ajari Ward', '(\'08063256326\',)', 'admin', '20.00', 'super', '30/12/2020 15:56:44.835579'),
('20123013170175662O', '7', '7', '7', '7', '5', '5', '5', '5', '140.00', 'DAY', '30/12/2020 14:24:27.175662', 'Ali Baba', 'Ajari Ward', '(\'08063256326\',)', 'super', '1400.00', 'super', '30/12/2020 16:24:52.249260'),
('20123025939691025O', '56', '56', '56', '56', '5', '5', '5', '5', '1120.00', 'DAY', '30/12/2020 16:22:59.691025', 'Ali Baba', 'Ajari Ward', '(\'08063256326\',)', 'super', '', '', ''),
('20123042516314219O', '80', '80', '80', '80', '5', '5', '5', '5', '1600.00', 'DAY', '30/12/2020 16:29:38.314219', 'Ali Baba', 'Ajari Ward', '(\'08063256326\',)', 'super', '160.00', 'super', '30/12/2020 16:29:49.985288'),
('20123069186354560O', '40', '40', '4', '4', '10', '10', '10', '10', '880.00', 'NIGHT', '30/12/2020 16:58:46.354560', 'Ali Baba', 'Ajari Ward', '(\'08063256326\',)', 'super', '440.00', 'super', '13/02/2021 13:08:25.977485'),
('20123092071323399O', '101', '101', '101', '101', '5', '5', '5', '5', '2020.00', 'DAY', '30/12/2020 15:56:34.323399', 'Ali Baba', 'Ajari Ward', '(\'08063256326\',)', 'super', '200.00', 'super', '30/12/2020 15:56:53.340828'),
('21021339419129421O', '50', '50', '50', '50', '10', '10', '10', '10', '2000.00', 'NIGHT', '13/02/2021 13:08:09.129421', 'Ali Baba', 'Ajari Ward', '(\'08063256326\',)', 'super', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `packagerbills`
--

CREATE TABLE `packagerbills` (
  `BillNo` varchar(100) NOT NULL,
  `Dispenser` varchar(100) NOT NULL,
  `BigBottle` varchar(100) NOT NULL,
  `SmallBottle` varchar(100) NOT NULL,
  `SachetWater` varchar(100) NOT NULL,
  `CostDispenser` varchar(100) NOT NULL,
  `CostBigBottle` varchar(100) NOT NULL,
  `CostSmallBottle` varchar(100) NOT NULL,
  `CostSachetWater` varchar(100) NOT NULL,
  `Amount` varchar(100) NOT NULL,
  `PriceType` varchar(100) NOT NULL,
  `DateStamp` varchar(100) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Phone` varchar(100) NOT NULL,
  `EnteredBy` varchar(150) NOT NULL,
  `PreviousTotal` varchar(100) NOT NULL,
  `UpdatedBy` varchar(100) NOT NULL,
  `UpdatedDate` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `packagerbills`
--

INSERT INTO `packagerbills` (`BillNo`, `Dispenser`, `BigBottle`, `SmallBottle`, `SachetWater`, `CostDispenser`, `CostBigBottle`, `CostSmallBottle`, `CostSachetWater`, `Amount`, `PriceType`, `DateStamp`, `Name`, `Address`, `Phone`, `EnteredBy`, `PreviousTotal`, `UpdatedBy`, `UpdatedDate`) VALUES
('20122867538004314', '5', '6', '6', '6', '1', '1', '1', '1', '23.00', 'DAY', '28/12/2020 18:20:42.004314', 'Vendi Ishaya', 'Bullumkutu Abuja', '(\'08063263532\',)', 'super', '24.00', 'super', '29/12/2020 09:20:54.204869'),
('20122871937707498', '50', '5', '5', '5', '2', '2', '2', '2', '130.00', 'NIGHT', '28/12/2020 18:21:07.707498', 'Vendi Ishaya', 'Bullumkutu Abuja', '(\'08063263532\',)', 'super', '40.00', 'admin', '29/12/2020 09:39:14.115248'),
('20122916718055579', '70', '70', '70', '7', '1', '1', '1', '1', '217.00', 'DAY', '29/12/2020 10:03:40.055579', 'Vendi Ishaya', 'Bullumkutu Abuja', '(\'08063263532\',)', 'admin', '28.00', 'admin', '29/12/2020 10:06:21.201112'),
('20122924260608223', '2', '2', '2', '2', '1', '1', '1', '1', '8.00', 'DAY', '29/12/2020 10:20:09.608223', 'Vendi Ishaya', 'Bullumkutu Abuja', '(\'08063263532\',)', 'admin', '12.00', 'admin', '29/12/2020 10:20:22.080223'),
('20122948153082647', '2', '3', '2', '3', '1', '1', '1', '1', '10.00', 'DAY', '29/12/2020 09:45:06.082647', 'Vendi Ishaya', 'Bullumkutu Abuja', '(\'08063263532\',)', 'admin', '29.00', 'super', '29/12/2020 09:51:51.322417'),
('20122962960646206', '10', '10', '10', '10', '1', '1', '1', '1', '40.00', 'DAY', '29/12/2020 10:38:51.646206', 'Vendi Ishaya', 'Bullumkutu Abuja', '(\'08063263532\',)', 'admin', '4.00', 'admin', '30/12/2020 09:19:55.667837'),
('20123010547001743P', '77', '77', '77', '77', '1', '1', '1', '1', '308.00', 'DAY', '30/12/2020 16:30:20.001743', 'Ucha Ann', 'Custom Area, Maiduguri', '(\'08015216232\',)', 'super', '28.00', 'super', '30/12/2020 16:30:31.130844'),
('20123037747375889', '2', '2', '2', '2', '1', '1', '1', '1', '8.00', 'DAY', '30/12/2020 13:07:35.375889', 'Ucha Ann', 'Custom Area, Maiduguri', '(\'08015216232\',)', 'super', '4.00', 'super', '30/12/2020 16:14:14.808178'),
('20123060220327971', '50', '50', '50', '50', '1', '1', '1', '1', '200.00', 'DAY', '30/12/2020 09:20:08.327971', 'Vendi Ishaya', 'Bullumkutu Abuja', '(\'08063263532\',)', 'admin', '20.00', 'admin', '30/12/2020 11:39:16.093903'),
('20123084979470753', '5', '5', '5', '5', '1', '1', '1', '1', '20.00', 'DAY', '30/12/2020 11:39:34.470753', 'Vendi Ishaya', 'Bullumkutu Abuja', '(\'08063263532\',)', 'admin', '', '', ''),
('20123091346571396P', '8', '8', '8', '8', '1', '1', '1', '1', '32.00', 'DAY', '30/12/2020 16:14:32.571396', 'Ucha Ann', 'Custom Area, Maiduguri', '(\'08015216232\',)', 'super', '', '', ''),
('20123098177271026', '4', '4', '4', '4', '2', '2', '2', '2', '32.00', 'NIGHT', '30/12/2020 11:43:00.271026', 'Vendi Ishaya', 'Bullumkutu Abuja', '(\'08063263532\',)', 'admin', '16.00', 'admin', '30/12/2020 11:43:55.909251');

-- --------------------------------------------------------

--
-- Table structure for table `price`
--

CREATE TABLE `price` (
  `PriceType` varchar(100) NOT NULL,
  `Dispenser` varchar(100) NOT NULL,
  `BigBottle` varchar(100) NOT NULL,
  `SmallBottle` varchar(100) NOT NULL,
  `SachetWater` varchar(100) NOT NULL,
  `PriceDate` varchar(100) NOT NULL,
  `EnteredBy` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `price`
--

INSERT INTO `price` (`PriceType`, `Dispenser`, `BigBottle`, `SmallBottle`, `SachetWater`, `PriceDate`, `EnteredBy`) VALUES
('A. Normal Price', '250', '150', '90', '60', '19/12/2020 13:18:13.602780', 'super'),
('B. Driver Price', '240', '140', '85', '55', '19/12/2020 13:53:39.722912', 'admin'),
('C. Operator Day Price', '5', '5', '5', '5', '28/12/2020 17:46:04.758463', 'super'),
('D. Operator Night Price', '10', '10', '10', '10', '28/12/2020 17:45:58.391263', 'super'),
('E. Packager Day Price', '1', '1', '1', '1', '28/12/2020 17:45:46.677326', 'super'),
('F. Packager Night Price', '2', '2', '2', '2', '28/12/2020 17:45:40.005609', 'super');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `UserID` varchar(100) NOT NULL,
  `Password` varchar(100) NOT NULL,
  `FullName` varchar(100) NOT NULL,
  `MobileNo` varchar(100) NOT NULL,
  `Address` varchar(250) NOT NULL,
  `Category` varchar(100) NOT NULL,
  `VehicleNo` varchar(100) NOT NULL,
  `DateStamp` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`UserID`, `Password`, `FullName`, `MobileNo`, `Address`, `Category`, `VehicleNo`, `DateStamp`) VALUES
('admin', 'kwambal', 'Admin', '+234Kwambal', 'Kwambal', 'Admin', '', '18/12/2020 11:02:47.355451'),
('AliBaba', '', 'Ali Baba', '08063256326', 'Ajari Ward', 'Operator', '', '30/12/2020 13:03:20.776452'),
('aliyu', 'aliyu', 'Aliyu Hassan', '08065326532', 'Jiddari Polo', 'Employee', '', '19/12/2020 12:59:58.087157'),
('alkali', '', 'Alkali Mohammed', '111111', 'Bulumkutu', 'Driver', 'XA 555 BIU', '13/02/2021 13:00:52.823496'),
('DRI001', '', 'Aliyu Baba', '8025632632', 'lkklklklklklkl', 'Driver', 'XA 101 BIU', '18/12/2020 12:07:33.361311'),
('employee01', '123', 'Isa Manga', '08065326325', 'Amaksks akskaskska', 'Employee', '', '26/12/2020 19:10:06.607766'),
('mamadi', '321', 'Mamadi Ali', '080', 'ababab', 'Employee', '', '12/02/2021 18:29:17.277768'),
('super', 'encrypt', 'Super Admin', 'Super', 'Super', 'Super-Admin', 'Super', 'Super-Admin'),
('UcheAnn', '', 'Ucha Ann', '08015216232', 'Custom Area, Maiduguri', 'Packager', '', '30/12/2020 13:04:02.040465'),
('WOR001', '', 'Vendi Ishaya', '08063263532', 'Bullumkutu Abuja', 'Workers', '', '18/12/2020 12:19:43.746717');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bills`
--
ALTER TABLE `bills`
  ADD PRIMARY KEY (`BillNo`);

--
-- Indexes for table `driverbills`
--
ALTER TABLE `driverbills`
  ADD PRIMARY KEY (`BillNo`);

--
-- Indexes for table `operaterbills`
--
ALTER TABLE `operaterbills`
  ADD PRIMARY KEY (`BillNo`);

--
-- Indexes for table `packagerbills`
--
ALTER TABLE `packagerbills`
  ADD PRIMARY KEY (`BillNo`);

--
-- Indexes for table `price`
--
ALTER TABLE `price`
  ADD PRIMARY KEY (`PriceType`);

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`UserID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
