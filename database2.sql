-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 29, 2021 at 01:00 AM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `database2`
--

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `corecatalogid` int(11) NOT NULL,
  `wasanalysed` varchar(50) DEFAULT NULL,
  `coretype` varchar(100) NOT NULL,
  `storeidentifier` varchar(100) NOT NULL,
  `catalogcorefromdepth` float NOT NULL,
  `catalogcoretodepth` float NOT NULL,
  `coresecurityflag` varchar(200) NOT NULL,
  `catalogcorelength` float DEFAULT NULL,
  `hascorephotos` varchar(20) DEFAULT NULL,
  `wellborecorename` varchar(100) DEFAULT NULL,
  `topcoreformation` varchar(20) DEFAULT NULL,
  `bottomcoreformation` varchar(100) DEFAULT NULL,
  `cataloguepicturename` varchar(20) DEFAULT NULL,
  `cataloguepicturesoftcopypath` varchar(100) DEFAULT NULL,
  `cataloguepicturehyperlink` varchar(200) DEFAULT NULL,
  `cataloguereportsoftcopypath` varchar(100) DEFAULT NULL,
  `cataloguereporthyperlink` varchar(200) DEFAULT NULL,
  `documentformat` varchar(100) DEFAULT NULL,
  `filesize` varchar(20) DEFAULT NULL,
  `securitygrade` varchar(100) DEFAULT NULL,
  `openduedate` varchar(20) DEFAULT NULL,
  `comments` varchar(100) DEFAULT NULL,
  `corecatalogname` varchar(200) DEFAULT NULL,
  `welloperator` varchar(100) DEFAULT NULL,
  `wellbore` varchar(200) DEFAULT NULL,
  `spuddate` varchar(100) DEFAULT NULL,
  `corename` varchar(200) DEFAULT NULL,
  `coredate` varchar(100) DEFAULT NULL,
  `comment` varchar(200) DEFAULT NULL,
  `createdby` varchar(100) DEFAULT NULL,
  `datecreated` varchar(20) DEFAULT NULL,
  `modifiedon` varchar(100) DEFAULT NULL,
  `modifiedby` varchar(200) DEFAULT NULL,
  `pictureuploaddate` varchar(100) DEFAULT NULL,
  `reportuploaddate` varchar(200) DEFAULT NULL,
  `recorddate` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=hp8;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `email` varchar(150) NOT NULL,
  `password` varchar(100) NOT NULL,
  `role` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=hp8;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `email`, `password`, `role`) VALUES
(1, 'authority@pau.go.ug', '$2b$12$T5A.IqsvWZhFaPnEN81S3u1eqEKLLbBbEVqF2nRuGZxBAE/GeAMVe', 'admin'),
(2, 'edward@gmail.com', '$2b$12$wRSjUcCnNEOSvOpHoucIX.yNQIPnd.KuqTsPC.dw84I/HVOYR/16O', 'user');

-- --------------------------------------------------------

--
-- Table structure for table `wellbore`
--

CREATE TABLE `wellbore` (
  `wellboreid` int(11) NOT NULL,
  `wellboreofficialname` varchar(150) NOT NULL,
  `wellborelocalname` varchar(100) NOT NULL,
  `wellborealiasname` varchar(100) NOT NULL,
  `spudyear` varchar(100) NOT NULL,
  `wellboretypeid` float NOT NULL,
  `initialwellborepurposeid` float NOT NULL,
  `wellborespuddate` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=hp8;

-- --------------------------------------------------------

--
-- Table structure for table `wellborecore`
--

CREATE TABLE `wellborecore` (
  `wellborecoreid` int(11) NOT NULL,
  `corenumber` float NOT NULL,
  `coredate` varchar(100) NOT NULL,
  `wellborename` varchar(200) NOT NULL,
  `coringcontractor` varchar(200) NOT NULL,
  `coretopmdrt` float NOT NULL,
  `corebottommdrt` float NOT NULL,
  `coretoptvd` float NOT NULL,
  `corebottomtvd` float NOT NULL,
  `cutlength` float NOT NULL,
  `cutlengthtvd` float DEFAULT NULL,
  `recoveredlength` float DEFAULT NULL,
  `corerecovery` float DEFAULT NULL,
  `topformation` varchar(200) NOT NULL,
  `bottomformation` varchar(100) DEFAULT NULL,
  `wellborecorename` varchar(100) DEFAULT NULL,
  `corepicturesoftcopypath` varchar(100) DEFAULT NULL,
  `corepicturehyperlink` varchar(200) DEFAULT NULL,
  `corereportsoftcopypath` varchar(100) DEFAULT NULL,
  `corereporthyperlink` varchar(200) DEFAULT NULL,
  `documentformat` varchar(100) DEFAULT NULL,
  `filesize` varchar(20) DEFAULT NULL,
  `securitygrade` varchar(100) DEFAULT NULL,
  `openduedate` varchar(20) DEFAULT NULL,
  `comments` varchar(100) DEFAULT NULL,
  `documenttitle` varchar(200) DEFAULT NULL,
  `receivedate` varchar(100) DEFAULT NULL,
  `documentdate` varchar(100) DEFAULT NULL,
  `documentname` varchar(200) DEFAULT NULL,
  `cored` varchar(100) DEFAULT NULL,
  `createdby` varchar(100) DEFAULT NULL,
  `datecreated` varchar(20) DEFAULT NULL,
  `modifiedon` varchar(100) DEFAULT NULL,
  `modifiedby` varchar(200) DEFAULT NULL,
  `pictureuploaddate` varchar(100) DEFAULT NULL,
  `reportuploaddate` varchar(200) DEFAULT NULL,
  `recorddate` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=hp8;

-- --------------------------------------------------------

--
-- Table structure for table `wells`
--

CREATE TABLE `wells` (
  `id` int(11) NOT NULL,
  `sampletype` varchar(150) NOT NULL,
  `wellname` varchar(100) NOT NULL,
  `layer` varchar(150) NOT NULL,
  `initialdepth` float NOT NULL,
  `terminationdepth` float NOT NULL,
  `samplebucket` varchar(100) NOT NULL,
  `uploaddate` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=hp8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`corecatalogid`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `wellbore`
--
ALTER TABLE `wellbore`
  ADD PRIMARY KEY (`wellboreid`);

--
-- Indexes for table `wellborecore`
--
ALTER TABLE `wellborecore`
  ADD PRIMARY KEY (`wellborecoreid`);

--
-- Indexes for table `wells`
--
ALTER TABLE `wells`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `corecatalogid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `wellbore`
--
ALTER TABLE `wellbore`
  MODIFY `wellboreid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `wellborecore`
--
ALTER TABLE `wellborecore`
  MODIFY `wellborecoreid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `wells`
--
ALTER TABLE `wells`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
