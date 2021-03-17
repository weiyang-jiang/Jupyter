/*
Navicat MySQL Data Transfer

Source Server         : test1
Source Server Version : 80017
Source Host           : localhost:3306
Source Database       : data

Target Server Type    : MYSQL
Target Server Version : 80017
File Encoding         : 65001

Date: 2020-07-09 02:24:25
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for cookies
-- ----------------------------
DROP TABLE IF EXISTS `cookies`;
CREATE TABLE `cookies` (
  `username` varchar(255) NOT NULL,
  `cookies` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of cookies
-- ----------------------------
INSERT INTO `cookies` VALUES ('13224675724', '_2A25yAULNDeRhGeFK71AR9y3PwjiIHXVRCm6FrDV6PUJbktANLU7CkW1NQ0q6yYRqwmoyY-9KQ57OyuYmr9_R2Jle;');
INSERT INTO `cookies` VALUES ('13258543154', '_2A25yAnzIDeRhGeFK71AT-SjKwzWIHXVRDQSArDV6PUJbktANLUzVkW1NQ0q5jzy5aGHUfU07LO_O02sqIb5sxgwn;');
INSERT INTO `cookies` VALUES ('13274691941', '_2A25yAnz-DeRhGeFK71AR9y3PzD-IHXVRDQS2rDV6PUJbktAKLU_gkW1NQ0q6NnEwhdyHni6xmoXsictzclZ99DxI;');
INSERT INTO `cookies` VALUES ('15504542040', '_2A25yAnzUDeRhGeFK71AR9yzLwzSIHXVRDQScrDV6PUJbktANLVD8kW1NQ0q5T5tsMVDclSm3HCkvyFhKR7nKTHJG;');
INSERT INTO `cookies` VALUES ('15636486842', '_2A25yAnwjDeRhGeFK71AT-SjEwzmIHXVRDQRrrDV6PUJbktANLRTDkW1NQ0q6fYQquu_0yJ0FaQnzB9h-s6JFgPgV;');
