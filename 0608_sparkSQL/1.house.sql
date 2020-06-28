/*
 Navicat Premium Data Transfer

 Source Server         : zcx
 Source Server Type    : MySQL
 Source Server Version : 80015
 Source Host           : localhost:3306
 Source Schema         : house

 Target Server Type    : MySQL
 Target Server Version : 80015
 File Encoding         : 65001

 Date: 18/05/2019 20:57:28
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for bank_trend
-- ----------------------------
DROP TABLE IF EXISTS `bank_trend`;
CREATE TABLE `bank_trend`  (
  `amount` double DEFAULT NULL,
  `year` text CHARACTER SET utf8 COLLATE utf8_bin,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;


-- ----------------------------
-- Table structure for city_count
-- ----------------------------
DROP TABLE IF EXISTS `city_count`;
CREATE TABLE `city_count`  (
  `city` text CHARACTER SET utf8 COLLATE utf8_bin,
  `count` bigint(20) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;



-- ----------------------------
-- Table structure for company_amont
-- ----------------------------
DROP TABLE IF EXISTS `company_amont`;
CREATE TABLE `company_amont`  (
  `amount` double DEFAULT NULL,
  `company_name` text CHARACTER SET utf8 COLLATE utf8_bin,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;



-- ----------------------------
-- Table structure for company_sorted
-- ----------------------------
DROP TABLE IF EXISTS `company_sorted`;
CREATE TABLE `company_sorted`  (
  `city` text CHARACTER SET utf8 COLLATE utf8_bin,
  `score` double DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;



-- ----------------------------
-- Table structure for economic_active
-- ----------------------------
DROP TABLE IF EXISTS `economic_active`;
CREATE TABLE `economic_active`  (
  `city` text CHARACTER SET utf8 COLLATE utf8_bin,
  `count` bigint(20) DEFAULT NULL,
  `price` double DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;



-- ----------------------------
-- Table structure for every_regions_ershoufang_count
-- ----------------------------
DROP TABLE IF EXISTS `every_regions_ershoufang_count`;
CREATE TABLE `every_regions_ershoufang_count`  (
  `city` text CHARACTER SET utf8 COLLATE utf8_bin,
  `count` bigint(20) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;



-- ----------------------------
-- Table structure for every_regions_zufang_count
-- ----------------------------
DROP TABLE IF EXISTS `every_regions_zufang_count`;
CREATE TABLE `every_regions_zufang_count`  (
  `city` text CHARACTER SET utf8 COLLATE utf8_bin,
  `count` bigint(20) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;



-- ----------------------------
-- Table structure for fang_wu_zheng_shou
-- ----------------------------
DROP TABLE IF EXISTS `fang_wu_zheng_shou`;
CREATE TABLE `fang_wu_zheng_shou`  (
  `area` text CHARACTER SET utf8 COLLATE utf8_bin,
  `counter` bigint(20) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;



-- ----------------------------
-- Table structure for gong_zu_fang
-- ----------------------------
DROP TABLE IF EXISTS `gong_zu_fang`;
CREATE TABLE `gong_zu_fang`  (
  `area` double DEFAULT NULL,
  `counter` bigint(20) DEFAULT NULL,
  `location` text CHARACTER SET utf8 COLLATE utf8_bin,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;


-- ----------------------------
-- Table structure for serven_area
-- ----------------------------
DROP TABLE IF EXISTS `serven_area`;
CREATE TABLE `serven_area`  (
  `city` text CHARACTER SET utf8 COLLATE utf8_bin,
  `price` double DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;


-- ----------------------------
-- Table structure for yu_shou_trend
-- ----------------------------
DROP TABLE IF EXISTS `yu_shou_trend`;
CREATE TABLE `yu_shou_trend`  (
  `area` double DEFAULT NULL,
  `year` text CHARACTER SET utf8 COLLATE utf8_bin,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;



-- ----------------------------
-- Table structure for zufang_shoufang_price_compare
-- ----------------------------
DROP TABLE IF EXISTS `zufang_shoufang_price_compare`;
CREATE TABLE `zufang_shoufang_price_compare`  (
  `city` text CHARACTER SET utf8 COLLATE utf8_bin,
  `data_type` text CHARACTER SET utf8 COLLATE utf8_bin,
  `price` double DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;



SET FOREIGN_KEY_CHECKS = 1;
