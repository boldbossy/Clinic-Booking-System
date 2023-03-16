-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jan 14, 2019 at 06:42 AM
-- Server version: 5.7.19
-- PHP Version: 7.1.9


SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `appointment`
--
CREATE DATABASE IF NOT EXISTS `appointment` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `appointment`;

-- --------------------------------------------------------

--
-- Table structure for table `appointment`
--

DROP TABLE IF EXISTS `appointment`;
CREATE TABLE IF NOT EXISTS `appointment` (
    `appointmentID` INT NOT NULL AUTO_INCREMENT,
    `clinicName` VARCHAR(200) NOT NULL,
    `nric` VARCHAR(9) NOT NULL,
    `email` VARCHAR(64) NOT NULL,
    `name` VARCHAR(64) NOT NULL,
    `address` VARCHAR(200) NOT NULL,
    `dob` DATE NOT NULL,
    `datetime` DATETIME NOT NULL,

    PRIMARY KEY (`appointmentID`, `clinicName`)

) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `appointment`
--
INSERT INTO `appointment` (`clinicName`, `nric`, `email`, `name`, `address`, `dob`, `datetime`) VALUES
('Complete Healthcare International', 'T0123456A', 'doctorasap2023@gmail.com', 'John Tan', 'BUKIT BATOK STREET 25', '1994-04-12', '2023-01-04 09:18:44'),
('Orchard Group Clinic', 'T0122222A', 'doctorasap2023@gmail.com', 'Joe Lee', '10 BRADDELL HILL', '2000-01-30', '2023-02-18 10:02:35'),
('Tanglin Medical Clinic', 'T0333333A', 'doctorasap2023@gmail.com', 'Mary Goh', '148 GANGSA ROAD', '1990-08-09', '2023-03-04 13:02:45'),
('Complete Healthcare International', 'T0109111G', 'doctorasap2023@gmail.com', 'Matilda Lim', 'JURONG EAST STREET 21', '1987-07-17', '2022-12-23 16:02:34'),
('UNIHEALTH 24-HR CLINIC (JURONG EAST)', 'T0213921S', 'doctorasap2023@gmail.com', 'William Tan', 'TELOK BLANGAH STREET 31', '1995-09-23', '2023-01-11 11:02:13');
COMMIT;