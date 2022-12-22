-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Dec 22, 2022 at 10:57 PM
-- Server version: 5.7.31
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `point_of_sale_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `clerk`
--

DROP TABLE IF EXISTS `clerk`;
CREATE TABLE IF NOT EXISTS `clerk` (
  `id_clerk` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_clerk`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `clerk`
--

INSERT INTO `clerk` (`id_clerk`, `username`, `password`) VALUES
(1, 'Victor', '12345678'),
(2, 'Jacob', '87654321'),
(3, 'Filbert', 'qwerasdf');

-- --------------------------------------------------------

--
-- Table structure for table `invoice`
--

DROP TABLE IF EXISTS `invoice`;
CREATE TABLE IF NOT EXISTS `invoice` (
  `id_invoice` int(11) NOT NULL AUTO_INCREMENT,
  `id_clerk` int(11) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`id_invoice`),
  KEY `id_clerk` (`id_clerk`)
) ENGINE=MyISAM AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `invoice`
--

INSERT INTO `invoice` (`id_invoice`, `id_clerk`, `date`) VALUES
(1, 2, '2022-12-23 04:05:47'),
(2, 2, '2022-12-23 04:06:32'),
(3, 1, '2022-12-23 05:18:20'),
(4, 3, '2022-12-23 05:18:42'),
(5, 3, '2022-12-23 05:18:46'),
(6, 3, '2022-12-23 05:18:50'),
(7, 3, '2022-12-23 05:18:53'),
(8, 3, '2022-12-23 05:19:06'),
(9, 3, '2022-12-23 05:28:34'),
(10, 3, '2022-12-23 05:32:14'),
(11, 3, '2022-12-23 05:32:22'),
(12, 1, '2022-12-23 05:32:33'),
(13, 1, '2022-12-23 05:32:44'),
(14, 1, '2022-12-23 05:32:48'),
(15, 1, '2022-12-23 05:32:51'),
(16, 1, '2022-12-23 05:32:54'),
(17, 1, '2022-12-23 05:32:57'),
(18, 1, '2022-12-23 05:33:02'),
(19, 1, '2022-12-23 05:33:08'),
(20, 1, '2022-12-23 05:33:14'),
(21, 2, '2022-12-23 05:51:50'),
(22, 2, '2022-12-23 05:54:01'),
(23, 2, '2022-12-23 05:54:13'),
(24, 2, '2022-12-23 05:54:42'),
(25, 2, '2022-12-23 05:54:54');

-- --------------------------------------------------------

--
-- Table structure for table `invoice_detail`
--

DROP TABLE IF EXISTS `invoice_detail`;
CREATE TABLE IF NOT EXISTS `invoice_detail` (
  `id_idetail` int(11) NOT NULL AUTO_INCREMENT,
  `id_invoice` int(11) DEFAULT NULL,
  `id_product` int(11) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `sub_total` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_idetail`),
  KEY `id_invoice` (`id_invoice`),
  KEY `id_product` (`id_product`)
) ENGINE=MyISAM AUTO_INCREMENT=65 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `invoice_detail`
--

INSERT INTO `invoice_detail` (`id_idetail`, `id_invoice`, `id_product`, `quantity`, `sub_total`) VALUES
(1, 1, 1, 1, 15000),
(2, 1, 5, 3, 51000),
(3, 1, 4, 2, 36000),
(4, 1, 6, 2, 28000),
(5, 2, 1, 13, 195000),
(6, 3, 1, 1, 15000),
(7, 3, 2, 1, 20000),
(8, 3, 3, 1, 17000),
(9, 3, 4, 1, 18000),
(10, 3, 5, 1, 17000),
(11, 3, 6, 1, 14000),
(12, 3, 7, 1, 10000),
(13, 3, 8, 1, 8000),
(14, 3, 9, 1, 12000),
(15, 4, 1, 1, 15000),
(16, 4, 2, 1, 20000),
(17, 5, 3, 1, 17000),
(18, 5, 2, 1, 20000),
(19, 5, 5, 1, 17000),
(20, 5, 6, 1, 14000),
(21, 6, 9, 1, 12000),
(22, 6, 8, 1, 8000),
(23, 6, 7, 1, 10000),
(24, 7, 3, 1, 17000),
(25, 7, 9, 1, 12000),
(26, 8, 2, 9, 180000),
(27, 8, 6, 7, 98000),
(28, 8, 8, 4, 32000),
(29, 8, 7, 3, 30000),
(30, 9, 7, 1, 10000),
(31, 9, 8, 1, 8000),
(32, 10, 2, 1, 20000),
(33, 11, 9, 1, 12000),
(34, 11, 8, 1, 8000),
(35, 11, 7, 1, 10000),
(36, 12, 1, 1, 15000),
(37, 12, 2, 1, 20000),
(38, 13, 8, 1, 8000),
(39, 13, 7, 1, 10000),
(40, 13, 9, 1, 12000),
(41, 13, 5, 1, 17000),
(42, 14, 9, 1, 12000),
(43, 14, 8, 1, 8000),
(44, 15, 2, 1, 20000),
(45, 15, 3, 1, 17000),
(46, 16, 3, 1, 17000),
(47, 17, 1, 9, 135000),
(48, 18, 5, 4, 68000),
(49, 18, 4, 4, 72000),
(50, 19, 9, 4, 48000),
(51, 19, 7, 4, 40000),
(52, 20, 8, 2, 16000),
(53, 20, 7, 2, 20000),
(54, 21, 1, 1, 15000),
(55, 21, 5, 1, 17000),
(56, 21, 6, 5, 70000),
(57, 22, 5, 4, 68000),
(58, 22, 6, 3, 42000),
(59, 23, 8, 2, 16000),
(60, 23, 7, 3, 30000),
(61, 24, 2, 20, 400000),
(62, 25, 6, 7, 98000),
(63, 25, 8, 7, 56000),
(64, 25, 7, 13, 130000);

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
CREATE TABLE IF NOT EXISTS `product` (
  `id_product` int(11) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(255) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `img_path` text,
  PRIMARY KEY (`id_product`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`id_product`, `product_name`, `price`, `category`, `img_path`) VALUES
(1, 'Pisang Goreng', 15000, 'Goreng', 'http://127.0.0.1:5000/static/images/gorengan/pisanggoreng.jpg'),
(2, 'Nasi Goreng', 20000, 'Goreng', 'http://127.0.0.1:5000/static/images/gorengan/nasigoreng.jpg'),
(3, 'Ayam Goreng', 17000, 'Goreng', 'http://127.0.0.1:5000/static/images/gorengan/ayamgoreng.jpg'),
(4, 'Sop Ayam', 18000, 'Soup', 'http://127.0.0.1:5000/static/images/gorengan/sopayam.jpg'),
(5, 'Soto Ayam', 17000, 'Soup', 'http://127.0.0.1:5000/static/images/gorengan/sotoayam.jpg'),
(6, 'Bakso', 14000, 'Soup', 'http://127.0.0.1:5000/static/images/gorengan/bakso.jpg'),
(7, 'Coca-cola', 10000, 'Minuman', 'http://127.0.0.1:5000/static/images/gorengan/cocacola.jpg'),
(8, 'Es Teh Manis', 8000, 'Minuman', 'http://127.0.0.1:5000/static/images/gorengan/estehmanis.jpg'),
(9, 'Es Jeruk', 12000, 'Minuman', 'http://127.0.0.1:5000/static/images/gorengan/esjeruk.jpg');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
