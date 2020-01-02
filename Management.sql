-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 02, 2020 at 05:57 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Management`
--

-- --------------------------------------------------------

--
-- Table structure for table `Employee`
--

CREATE TABLE `Employee` (
  `ename` varchar(30) NOT NULL,
  `edept` varchar(25) NOT NULL,
  `eid` int(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Employee`
--

INSERT INTO `Employee` (`ename`, `edept`, `eid`) VALUES
('Divyansh', 'Mechanical', 123),
('Divyansh', 'Mechanical', 123);

-- --------------------------------------------------------

--
-- Table structure for table `Student`
--

CREATE TABLE `Student` (
  `RollNo` int(3) NOT NULL,
  `Class` int(2) NOT NULL,
  `Address` varchar(30) NOT NULL,
  `Fees` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Student`
--

INSERT INTO `Student` (`RollNo`, `Class`, `Address`, `Fees`) VALUES
(2, 2, 'bharatpur', 11000),
(2, 2, 'bharatpur', 11000),
(2, 2, 'bharatpur', 11000);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
