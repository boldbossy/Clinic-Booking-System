
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;


CREATE DATABASE IF NOT EXISTS `clinic` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `clinic`;

-- --------------------------------------------------------

--
-- Table structure for table `clinic`
--

DROP TABLE IF EXISTS `clinic`;
CREATE TABLE IF NOT EXISTS `clinic` (
  `clinicID`int(11) NOT NULL,
  `clinicName` varchar(64) NOT NULL,
  `clinicLoc` varchar(64) NOT NULL,
  `waitTime` time(6) DEFAULT NULL,
  PRIMARY KEY (`clinicName`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `clinic` Orchard,Jurong East,Changi Airport,Bedok
--

INSERT INTO `clinic` (`clinicID`, `clinicName`, `clinicLoc`, `waitTime`) VALUES
('1', 'Complete Healthcare International', '350 Orchard Rd, #08-00 Shaw House · In Shaw House', '00:30:30'),
('2', 'Orchard Group Clinic', 'SG, Orchard Rd, 545 · In Far East Shopping Centre', '00:30:30'),
('3', 'Tanglin Medical Clinic', '360 Orchard Rd, #07-04 International Building · In International Bldg', '00:30:30'),
('4', 'Minmed Clinic (Jurong East)', '50 Jurong Gateway Rd, #04-17 Jem · In Jem', '00:30:30'),
('5', 'UNIHEALTH 24-HR CLINIC (JURONG EAST)', '135 Jurong Gateway Rd, #01-317', '00:30:30'),
('6', 'Summit Medical Clinic', '134 Jurong Gateway Rd, #01-307', '00:30:30'),
('7', 'NTUC Health Family Medicine Clinic', '264 Serangoon Central, #01-205 · In Serangoon Central', '00:09:56'),
('8', '326 Avenue 3 Clinic', 'Serangoon Ave 3, Block 326', '00:21:30'),
('9', 'Affinity Medical Clinic', 'Serangoon Central Dr, #01-187 Blk 253', '00:08:30'),
('10', 'AcuMed Medical (Bedok)', '214 Bedok North Street 1, #01-165 · In Bedok Town Centre', '00:15:30'),
('11', 'Health Line Family Clinic and Surgery', '25A Chai Chee Rd, #01-467', '00:27:30'),
('12', 'Minmed Clinic (Bedok)', '311 New Upper Changi Rd, #01-47/48 Bedok Mall · In Bedok Mall', '01:05:00');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
