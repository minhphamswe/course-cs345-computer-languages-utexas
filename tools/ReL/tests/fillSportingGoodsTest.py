# Sporting goods store test script for ReL

# Little function that prints results neatly
def neatPrint(results):
        for ii in range(0, len(results)):
                print(results[ii]);
        print;

# Connect to the database
MAKECONNECT URL jdbc:oracle:thin:@rising-sun.microlab.cs.utexas.edu:1521:orcl UNAME CS345_demo PWORD orcl_demo CONTYPE local;
DROP TABLE RDF_DATA;

# Header from the original file:
#   Sporting_Goods Database
#
# 
#  SCRIPT - FUNCTION
#   Create and populate tables and sequences to support the Sporting Goods business scenario.
#   This database is a modified version of the database used in some of the classes of
#   the ORACLE Corporation.
# 
# NOTES
# 
# MODIFIED
# Originally created:  GDURHAM  Mar 15, 1993  -- ORACLE Corporation
#
# Modified and reprinted with permission from The ORACLE Corporation
# by Drs. Ramon A. Mata-Toledo and Pauline K. Cushman on Dec 15, 1999.
#
# Most recently modified by Andrew Oldag 29 July 2012
# NOTE: As it stands now, ReL can't create sequences, so those will be commented out, 
# perhaps for future use down the line.
# Other changes where made in the original script so that they would be understood by the existing grammar.


# Start of the creation and population of tables. Please wait.

#	************** S_CUSTOMER TABLE *********************************
#	*****************************************************************

DROP TABLE s_customer CASCADE CONSTRAINTS;
CREATE TABLE s_customer (id VARCHAR2(3), name VARCHAR2(20), phone VARCHAR2(20), address VARCHAR2(20), city VARCHAR2(20), state VARCHAR2(15), country VARCHAR2(20), zip_code VARCHAR2(15), credit_rating VARCHAR2(9), sales_rep_id VARCHAR2(3), region_id VARCHAR2(3), comments VARCHAR2(255) );


INSERT INTO s_customer (id, name, phone, address, city, state, country, zip_code, credit_rating, sales_rep_id, region_id, comments) VALUES ('301', 'Sports,Inc', '540-123-4567','72 High St','Harrisonburg', 'VA','US', '22809','EXCELLENT', '12', '1', '');
INSERT INTO s_customer (id, name, phone, address, city, state, country, zip_code, credit_rating, sales_rep_id, region_id, comments) VALUES ('302', 'Toms Sporting Goods', '540-987-6543','6741 Main St','Harrisonburg', 'VA','US', '22809','POOR', '14', '1', '');
INSERT INTO s_customer (id, name, phone, address, city, state, country, zip_code, credit_rating, sales_rep_id, region_id, comments) VALUES ('303', 'Athletic Attire', '540-123-6789','54 Market St','Harrisonburg', 'VA','US', '22808','GOOD', '14', '1', '');
INSERT INTO s_customer (id, name, phone, address, city, state, country, zip_code, credit_rating, sales_rep_id, region_id, comments) VALUES ('304', 'Athletics For All', '540-987-1234','286 Main St', 'Harrisonburg', 'VA','US', '22808','EXCELLENT', '12', '1', '');
INSERT INTO s_customer (id, name, phone, address, city, state, country, zip_code, credit_rating, sales_rep_id, region_id, comments) VALUES ('305', 'Shoes for Sports', '540-123-9876','538 High St','Harrisonburg', 'VA','US', '22809','EXCELLENT', '14', '1', '');
INSERT INTO s_customer (id, name, phone, address, city, state, country, zip_code, credit_rating, sales_rep_id, region_id, comments) VALUES ('306', 'BJ Athletics', '540-987-9999','632 Water St','Harrisonburg', 'VA','US', '22810','POOR', '12', '1', '');

INSERT INTO s_customer (id, name, phone, address, city, state, country, zip_code, credit_rating, sales_rep_id, region_id, comments) VALUES ('403', 'Athletics One', '717-234-6786','912 Columbia Rd','Lancaster', 'PA','US', '17601','GOOD', '14', '1', '');
INSERT INTO s_customer (id, name, phone, address, city, state, country, zip_code, credit_rating, sales_rep_id, region_id, comments) VALUES ('404', 'Great Athletes', '717-987-2341','121 Litiz Pike','Lancaster', 'PA','US', '17602','EXCELLENT', '12', '1', '');
INSERT INTO s_customer (id, name, phone, address, city, state, country, zip_code, credit_rating, sales_rep_id, region_id, comments) VALUES ('405', 'Athletics Two', '717-987-9875','435 High Rd','Lancaster', 'PA','US', '17602','EXCELLENT', '14', '1', '');
INSERT INTO s_customer (id, name, phone, address, city, state, country, zip_code, credit_rating, sales_rep_id, region_id, comments) VALUES ('406', 'Athletes Attic', '717-234-9888','101 Greenfield Rd','Lancaster', 'PA','US', '17601','POOR', '12', '1', '');

INSERT INTO s_customer (id, name, phone, address, city, state, country, zip_code, credit_rating, sales_rep_id, region_id, comments) VALUES ('201', 'One Sport', '55-112066222','82 Via Bahia', 'Sao Paolo','', 'Brazil', '','EXCELLENT', '12', '2', '');
INSERT INTO s_customer (id, name, phone, address, city, state, country, zip_code, credit_rating, sales_rep_id, region_id, comments) VALUES ('202', 'Deportivo Caracas', '58-28066222','31 Sabana Grande','Caracas', '', 'Venezuela', '','EXCELLENT', '12', '2', '');
INSERT INTO s_customer (id, name, phone, address, city, state, country, zip_code, credit_rating, sales_rep_id, region_id, comments) VALUES ('203', 'New Delhi Sports', '91-11903338','11368 Chanakya','New Delhi', '', 'India', '','GOOD', '11', '4', '');
INSERT INTO s_customer (id, name, phone, address, city, state, country, zip_code, credit_rating, sales_rep_id, region_id, comments) VALUES ('204', 'Ladysport', '1-206-104-0111','281 Queen Street','Seattle', 'Washington', 'US', '','EXCELLENT', '11', '1', '');
INSERT INTO s_customer (id, name, phone, address, city, state, country, zip_code, credit_rating, sales_rep_id, region_id, comments) VALUES ('205', 'Kim''s Sporting Goods', '852-3693888','15 Henessey Road','Hong Kong', '', '', '','EXCELLENT', '11', '4', '');
INSERT INTO s_customer (id, name, phone, address, city, state, country, zip_code, credit_rating, sales_rep_id, region_id, comments) VALUES ('206', 'Sportique', '33-93425722253','172 Rue de Place','Cannes', '', 'France', '','EXCELLENT', '13', '5', '');
INSERT INTO s_customer (id, name, phone, address, city, state, country, zip_code, credit_rating, sales_rep_id, region_id, comments) VALUES ('207', 'Tall Rock Sports', '234-16036222','10 Saint Antoine','Lagos', '', 'Nigeria', '','GOOD', '', '3', '');
INSERT INTO s_customer (id, name, phone, address, city, state, country, zip_code, credit_rating, sales_rep_id, region_id, comments) VALUES ('208', 'Muench Sports', '49-895274449','435 Gruenestrasse','Munich', '', 'Germany', '','GOOD', '13', '5', '');

INSERT INTO s_customer (id, name, phone, address, city, state, country, zip_code, credit_rating, sales_rep_id, region_id, comments) VALUES ('209', 'Beisbol Si!', '809-352666','415 Playa Del Mar', 'San Pedro de Macoris', '', 'Dominican Republic', '', 'EXCELLENT', '11', '6', '');
INSERT INTO s_customer (id, name, phone, address, city, state, country, zip_code, credit_rating, sales_rep_id, region_id, comments) VALUES ('210', 'Futbol Sonora', '52-404555','5 Via Saguaro', 'Nogales','', 'Mexico', '','EXCELLENT', '12', '2', '');
INSERT INTO s_customer (id, name, phone, address, city, state, country, zip_code, credit_rating, sales_rep_id, region_id, comments) VALUES ('211', 'Helmut''s Sports', '42-2111222','45 Modrany', 'Prague','', 'Czechoslovakia', '','EXCELLENT', '11', '5', '');
INSERT INTO s_customer (id, name, phone, address, city, state, country, zip_code, credit_rating, sales_rep_id, region_id, comments) VALUES ('212', 'Hamada Sport', '20-31209222','47A Corniche', 'Alexandria', '', 'Egypt', '','EXCELLENT', '13', '3', '');
INSERT INTO s_customer (id, name, phone, address, city, state, country, zip_code, credit_rating, sales_rep_id, region_id, comments) VALUES ('213', 'Sports Emporium', '1-415-555-6281','4783 168th Street','San Francisco', 'CA', 'US', '','EXCELLENT', '11', '1', '');
INSERT INTO s_customer (id, name, phone, address, city, state, country, zip_code, credit_rating, sales_rep_id, region_id, comments) VALUES ('214', 'Sports Retail', '1-716-555-7777','115 Main Street','Buffalo', 'NY', 'US', '', 'POOR', '11', '1', '');
INSERT INTO s_customer (id, name, phone, address, city, state, country, zip_code, credit_rating, sales_rep_id, region_id, comments) VALUES ('215', 'Sports Russia', '7-0953892444','7070 Yekatamina','Saint Petersburg', '', 'Russia', '','POOR', '11', '5', '');

#	************** S_CUSTOMER TABLE ********************************
#	*****************************************************************

DROP TABLE s_dept CASCADE CONSTRAINTS;
CREATE TABLE s_dept (id VARCHAR2(3), name VARCHAR2(20), region_id VARCHAR2(3));

INSERT INTO s_dept (id, name, region_id) VALUES ('10', 'Finance', '1');
INSERT INTO s_dept (id, name, region_id) VALUES ('31', 'Sales', '1');
INSERT INTO s_dept (id, name, region_id) VALUES ('32', 'Sales', '2');
INSERT INTO s_dept (id, name, region_id) VALUES ('33', 'Sales', '3');
INSERT INTO s_dept (id, name, region_id) VALUES ('34', 'Sales', '4');
INSERT INTO s_dept (id, name, region_id) VALUES ('35', 'Sales', '5');
INSERT INTO s_dept (id, name, region_id) VALUES ('41', 'Operations', '1');
INSERT INTO s_dept (id, name, region_id) VALUES ('42', 'Operations', '2');
INSERT INTO s_dept (id, name, region_id) VALUES ('43', 'Operations', '3');
INSERT INTO s_dept (id, name, region_id) VALUES ('44', 'Operations', '4');
INSERT INTO s_dept (id, name, region_id) VALUES ('45', 'Operations', '5');
INSERT INTO s_dept (id, name, region_id) VALUES ('50', 'Administration', '1');

#	************** S_EMP TABLE ********************************
#	*****************************************************************

DROP TABLE s_emp CASCADE CONSTRAINTS;
CREATE TABLE s_emp (id VARCHAR2(3), last_name VARCHAR2(20), first_name VARCHAR2(20), userid VARCHAR2(8), start_date DATE, comments VARCHAR2(255), manager_id VARCHAR2(3), title VARCHAR2(25), dept_id VARCHAR2(3), salary NUMERIC(11,2), commission_pct NUMERIC(4,2) );

INSERT INTO s_emp (id, last_name, first_name, userid, start_date, comments, manager_id, title, dept_id, salary, commission_pct) VALUES ('1', 'Martin','Carmen','martincu','1990-03-03', '','', 'President', '50', 4500, 0);
INSERT INTO s_emp (id, last_name, first_name, userid, start_date, comments, manager_id, title, dept_id, salary, commission_pct) VALUES ('2','Smith','Doris','smithdj', '1990-03-08','','1', 'VP, Operations','41', 2450,0);
INSERT INTO s_emp (id, last_name, first_name, userid, start_date, comments, manager_id, title, dept_id, salary, commission_pct) VALUES ('3', 'Norton','Michael','nortonma','1991-06-17','','1', 'VP, Sales', '31', 2400,0);
INSERT INTO s_emp (id, last_name, first_name, userid, start_date, comments, manager_id, title, dept_id, salary, commission_pct) VALUES ('4', 'Quentin', 'Mark','quentiml','1990-04-07','','1', 'VP, Finance', '10', 2450, 0);
INSERT INTO s_emp (id, last_name, first_name, userid, start_date, comments, manager_id, title, dept_id, salary, commission_pct) VALUES ('5', 'Roper', 'Joseph','roperjm','1990-03-04','','1', 'VP, Administration', '50', 2550, 0);
INSERT INTO s_emp (id, last_name, first_name, userid, start_date, comments, manager_id, title, dept_id, salary, commission_pct) VALUES ('6', 'Brown', 'Molly','brownmr','1991-01-18','','2', 'Warehouse Manager', '41', 1600, 0);
INSERT INTO s_emp (id, last_name, first_name, userid, start_date, comments, manager_id, title, dept_id, salary, commission_pct) VALUES ('7', 'Hawkins', 'Roberta','hawkinrt','1990-05-14','','2', 'Warehouse Manager','42', 1650, 0);
INSERT INTO s_emp (id, last_name, first_name, userid, start_date, comments, manager_id, title, dept_id, salary, commission_pct) VALUES ('8', 'Burns', 'Ben','burnsba','1990-04-07','','2', 'Warehouse Manager','43', 1500, 0);

INSERT INTO s_emp (id, last_name, first_name, userid, start_date, comments, manager_id, title, dept_id, salary, commission_pct) VALUES ('9', 'Catskill', 'Antoinette','catskiaw','1992-02-09','','2', 'Warehouse Manager','44', 1700,0);
INSERT INTO s_emp (id, last_name, first_name, userid, start_date, comments, manager_id, title, dept_id, salary, commission_pct) VALUES ('10', 'Jackson', 'Marta','jacksomt','1991-02-27','','2', 'Warehouse Manager','45', 1507,0);
INSERT INTO s_emp (id, last_name, first_name, userid, start_date, comments, manager_id, title, dept_id, salary, commission_pct) VALUES ('11', 'Henderson', 'Colin','hendercs','1990-05-14','','3', 'Sales Representative', '31', 1400, 10);
INSERT INTO s_emp (id, last_name, first_name, userid, start_date, comments, manager_id, title, dept_id, salary, commission_pct) VALUES ('12', 'Gilson', 'Sam', 'gilsonsj','1992-01-18','','3', 'Sales Representative','32', 1490, 12.5);
INSERT INTO s_emp (id, last_name, first_name, userid, start_date, comments, manager_id, title, dept_id, salary, commission_pct) VALUES ('13', 'Sanders', 'Jason', 'sanderjk','1991-02-18','','3', 'Sales Representative','33', 1515, 10);
INSERT INTO s_emp (id, last_name, first_name, userid, start_date, comments, manager_id, title, dept_id, salary, commission_pct) VALUES ('14', 'Dameron', 'Andre', 'dameroap','1991-10-09','','3', 'Sales Representative','35', 1450, 17.5);
INSERT INTO s_emp (id, last_name, first_name, userid, start_date, comments, manager_id, title, dept_id, salary, commission_pct) VALUES ('15', 'Hardwick', 'Elaine', 'hardwiem','1992-02-07','','6', 'Stock Clerk','41', 1400, 0);
INSERT INTO s_emp (id, last_name, first_name, userid, start_date, comments, manager_id, title, dept_id, salary, commission_pct) VALUES ('16', 'Brown', 'George', 'browngw','1990-03-08','','6', 'Stock Clerk','41', 940, 0);

INSERT INTO s_emp (id, last_name, first_name, userid, start_date, comments, manager_id, title, dept_id, salary, commission_pct) VALUES ('17', 'Washington', 'Thomas', 'washintl','1991-02-09','','7', 'Stock Clerk', '42', 1200, 0);
INSERT INTO s_emp (id, last_name, first_name, userid, start_date, comments, manager_id, title, dept_id, salary, commission_pct) VALUES ('18', 'Patterson', 'Donald', 'patterdv','1991-08-06','','7', 'Stock Clerk','42', 795, 0);
INSERT INTO s_emp (id, last_name, first_name, userid, start_date, comments, manager_id, title, dept_id, salary, commission_pct) VALUES ('19', 'Bell', 'Alexander', 'bellag','1991-05-26','','8', 'Stock Clerk','43', 850, 0);
INSERT INTO s_emp (id, last_name, first_name, userid, start_date, comments, manager_id, title, dept_id, salary, commission_pct) VALUES ('20', 'Gantos', 'Eddie', 'gantosej','1990-11-30','','9', 'Stock Clerk','44', 800, 0);
INSERT INTO s_emp (id, last_name, first_name, userid, start_date, comments, manager_id, title, dept_id, salary, commission_pct) VALUES ('21', 'Stephenson', 'Blaine', 'stephebs','1991-03-17','','10', 'Stock Clerk','45', 860, 0);

INSERT INTO s_emp (id, last_name, first_name, userid, start_date, comments, manager_id, title, dept_id, salary, commission_pct) VALUES ('22', 'Chester', 'Eddie', 'chesteek','1990-11-30', '', '9', 'Stock Clerk','44', 800, 0);
INSERT INTO s_emp (id, last_name, first_name, userid, start_date, comments, manager_id, title, dept_id, salary, commission_pct) VALUES ('23', 'Pearl', 'Roger', 'pearlrg','1990-10-17', '', '9', 'Stock Clerk','34', 795, 0);
INSERT INTO s_emp (id, last_name, first_name, userid, start_date, comments, manager_id, title, dept_id, salary, commission_pct) VALUES ('24', 'Dancer', 'Bonnie', 'dancerbw','1991-03-17', '', '7', 'Stock Clerk','45', 860, 0);
INSERT INTO s_emp (id, last_name, first_name, userid, start_date, comments, manager_id, title, dept_id, salary, commission_pct) VALUES ('25', 'Schmitt', 'Sandra', 'schmitss','1991-05-09', '', '8', 'Stock Clerk','45', 1100, 0);

#	************** S_INVENTORY TABLE ********************************
#	*****************************************************************

DROP TABLE s_inventory CASCADE CONSTRAINTS;
CREATE TABLE s_inventory (product_id VARCHAR2(7), warehouse_id VARCHAR2(7), amount_in_stock NUMERIC(9), reorder_point NUMERIC(9), max_in_stock NUMERIC(9), out_of_stock_explanation VARCHAR2(255), restock_date DATE);

INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('10011', '101', 650, 625, 1100, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('10012', '101', 600, 560, 1000, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('10013', '101', 400, 400, 700, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('10021', '101', 500, 425, 740, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('10022', '101', 300, 200, 350, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('10023', '101', 400, 300, 525, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('20106', '101', 993, 625, 1000, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('20108', '101', 700, 700, 1225, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('20201', '101', 802, 800, 1400, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('20510', '101', 1389, 850, 1400, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('20512', '101', 850, 850, 1450, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('30321', '101', 2000, 1500, 2500, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('30326', '101', 2100, 2000, 3500, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('30421', '101', 1822, 1800, 3150, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('30426', '101', 2250, 2000, 3500, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('30433', '101', 650, 600, 1050, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('32779', '101', 2120, 1250, 2200, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('32861', '101', 505, 500, 875, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('40421', '101', 578, 350, 600, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('40422', '101', 0, 350, 600, 'Phenomenal sales...', '1993-02-08');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('41010', '101', 250, 250, 437, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('41020', '101', 471, 450, 750, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('41050', '101', 501, 450, 750, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('41080', '101', 400, 400, 700, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('41100', '101', 350, 350, 600, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('50169', '101', 2530, 1500, 2600, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('50273', '101', 233, 200, 350, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('50417', '101', 518, 500, 875, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('50418', '101', 244, 100, 275, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('50419', '101', 230, 120, 310, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('50530', '101', 669, 400, 700, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('50532', '101', 0, 100, 175, 'Wait for Spring.', '1993-04-12');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('50536', '101', 173, 100, 175, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('20106', '201', 220, 150, 260, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('20108', '201', 166, 150, 260, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('20201', '201', 320, 200, 350, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('20510', '201', 175, 100, 175, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('20512', '201', 162, 100, 175, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('30321', '201', 96, 80, 140, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('30326', '201', 147, 120, 210, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('30421', '201', 102, 80, 140, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('30426', '201', 200, 120, 210, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('30433', '201', 130, 130, 230, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('32779', '201', 180, 150, 260, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('32861', '201', 132, 80, 140, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('50169', '201', 225, 220, 385, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('50273', '201', 75, 60, 100, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('50417', '201', 82, 60, 100, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('50418', '201', 98, 60, 100, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('50419', '201', 77, 60, 100, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('50530', '201', 62, 60, 100, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('50532', '201', 67, 60, 100, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('50536', '201', 97, 60, 100, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('20510', '301', 69, 40, 100, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('20512', '301', 28, 20, 50, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('30321', '301', 85, 80, 140, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('30421', '301', 102, 80, 140, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('30433', '301', 35, 20, 35, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('32779', '301', 102, 95, 175, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('32861', '301', 57, 50, 100, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('40421', '301', 70, 40, 70, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('40422', '301', 65, 40, 70, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('41010', '301', 59, 40, 70, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('41020', '301', 61, 40, 70, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('41050', '301', 49, 40, 70, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('41080', '301', 50, 40, 70, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('41100', '301', 42, 40, 70, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('20510', '401', 88, 50, 100, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('20512', '401', 75, 75, 140, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('30321', '401', 102, 80, 140, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('30326', '401', 113, 80, 140, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('30421', '401', 85, 80, 140, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('30426', '401', 135, 80, 140, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('30433', '401', 0, 100, 175, '', '' );
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('32779', '401', 135, 100, 175, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('32861', '401', 250, 150, 250, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('40421', '401', 47, 40, 70, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('40422', '401', 50, 40, 70, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('41010', '401', 80, 70, 220, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('41020', '401', 91, 70, 220, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('41050', '401', 169, 70, 220, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('41080', '401', 100, 70, 220, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('41100', '401', 75, 70, 220, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('50169', '401', 240, 200, 350, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('50273', '401', 224, 150, 280, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('50417', '401', 130, 120, 210, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('50418', '401', 156, 100, 175, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('50419', '401', 151, 150, 280, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('50530', '401', 119, 100, 175, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('50532', '401', 233, 200, 350, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('50536', '401', 138, 100, 175, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('10012', '10501', 300, 300, 525, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('10013', '10501', 314, 300, 525, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('10022', '10501', 502, 300, 525, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('10023', '10501', 500, 300, 525, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('20106', '10501', 150, 100, 175, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('20108', '10501', 222, 200, 350, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('20201', '10501', 275, 200, 350, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('20510', '10501', 57, 50, 87, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('20512', '10501', 62, 50, 87, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('30321', '10501', 194, 150, 275, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('30326', '10501', 277, 250, 440, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('30421', '10501', 190, 150, 275, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('30426', '10501', 423, 250, 450, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('30433', '10501', 273, 200, 350, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('32779', '10501', 280, 200, 350, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('32861', '10501', 288, 200, 350, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('40421', '10501', 97, 80, 140, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('40422', '10501', 90, 80, 140, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('41010', '10501', 151, 140, 245, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('41020', '10501', 224, 140, 245, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('41050', '10501', 157, 140, 245, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('41080', '10501', 159, 140, 245, '', '');
INSERT INTO s_inventory (product_id, warehouse_id, amount_in_stock, reorder_point, max_in_stock, out_of_stock_explanation, restock_date) VALUES ('41100', '10501', 141, 140, 245, '', '');

#	************** S_ITEM TABLE ********************************
#	*****************************************************************

DROP TABLE s_item CASCADE CONSTRAINTS;
CREATE TABLE s_item (ord_id VARCHAR2(6), item_id VARCHAR2(7), product_id VARCHAR2(7), price NUMERIC(11,2), quantity NUMERIC(9), quantity_shipped NUMERIC(9));

INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('100', '1', '10011', 135, 500, 500);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('100', '2', '10013', 380, 400, 400);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('100', '3', '10021', 14, 500, 500);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('100', '5', '30326', 582, 600, 600);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('100', '7', '41010', 8, 250, 250);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('100', '6', '30433', 20, 450, 450);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('100', '4', '10023', 36, 400, 400);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('101', '1', '30421', 16, 15, 15);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('101', '3', '41010', 8, 20, 20);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('101', '5', '50169', 4.29, 40, 40);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('101', '6', '50417', 80, 27, 27);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('101', '7', '50530', 45, 50, 50);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('101', '4', '41100', 45, 35, 35);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('101', '2', '40422', 50, 30, 30);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('102', '1', '20108', 28, 100, 100);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('102', '2', '20201', 123, 45, 45);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('103', '1', '30433', 20, 15, 15);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('103', '2', '32779', 7, 11, 11);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('104', '1', '20510', 9, 7, 7);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('104', '4', '30421', 16, 35, 35);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('104', '2', '20512', 8, 12, 12);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('104', '3', '30321', 1669, 19, 19);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('105', '1', '50273', 22.89, 16, 16);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('105', '3', '50532', 47, 28, 28);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('105', '2', '50419', 80, 13, 13);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('106', '1', '20108', 28, 46, 46);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('106', '4', '50273', 22.89, 75, 75);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('106', '5', '50418', 75, 98, 98);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('106', '6', '50419', 80, 27, 27);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('106', '2', '20201', 123, 21, 21);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('106', '3', '50169', 4.29, 125, 125);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('107', '1', '20106', 11, 50, 50);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('107', '3', '20201', 115, 130, 130);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('107', '5', '30421', 16, 55, 55);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('107', '4', '30321', 1669, 75, 75);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('107', '2', '20108', 28, 22, 22);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('108', '1', '20510', 9, 9, 9);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('108', '6', '41080', 35, 50, 50);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('108', '7', '41100', 45, 42, 42);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('108', '5', '32861', 60, 57, 57);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('108', '2', '20512', 8, 18, 18);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('108', '4', '32779', 7, 60, 60);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('108', '3', '30321', 1669, 85, 85);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('109', '1', '10011', 140, 150, 150);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('109', '5', '30426', 18.25, 500, 500);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('109', '7', '50418', 75, 43, 43);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('109', '6', '32861', 60, 50, 50);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('109', '4', '30326', 582, 1500, 1500);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('109', '2', '10012', 175, 600, 600);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('109', '3', '10022', 21.95, 300, 300);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('110', '1', '50273', 22.89, 17, 17);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('110', '2', '50536', 50, 23, 23);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('111', '1', '40421', 65, 27, 27);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('111', '2', '41080', 35, 29, 29);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('97', '1', '20106', 9, 1000, 1000);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('97', '2', '30321', 1500, 50, 50);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('98', '1', '40421', 85, 7, 7);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('99', '1', '20510', 9, 18, 18);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('99', '2', '20512', 8, 25, 25);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('99', '3', '50417', 80, 53, 53);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('99', '4', '50530', 45, 69, 69);
INSERT INTO s_item (ord_id, item_id, product_id, price, quantity, quantity_shipped) VALUES ('112', '1', '20106', 11, 50, 50);

#	************** S_ORD TABLE ********************************
#	*****************************************************************

DROP TABLE s_ord CASCADE CONSTRAINTS;
CREATE TABLE s_ord (id VARCHAR2(3), customer_id VARCHAR2(3), date_ordered DATE, date_shipped DATE, sales_rep_id VARCHAR2(3), total NUMERIC(11,2), payment_type VARCHAR2(6), order_filled VARCHAR2(1));

INSERT INTO s_ord (id, customer_id, date_ordered, date_shipped, sales_rep_id, total, payment_type, order_filled) VALUES ('100', '204', '1992-08-31', '1992-09-10', '11', 601100, 'CREDIT', 'Y');
INSERT INTO s_ord (id, customer_id, date_ordered, date_shipped, sales_rep_id, total, payment_type, order_filled) VALUES ('101', '205', '1992-08-31', '1992-09-15', '14', 8056.6, 'CREDIT', 'Y');
INSERT INTO s_ord (id, customer_id, date_ordered, date_shipped, sales_rep_id, total, payment_type, order_filled) VALUES ('102', '206', '1992-09-01', '1992-09-08', '12', 8335, 'CREDIT', 'Y');
INSERT INTO s_ord (id, customer_id, date_ordered, date_shipped, sales_rep_id, total, payment_type, order_filled) VALUES ('103', '208', '1992-09-02', '1992-09-22', '11', 377, 'CASH', 'Y');
INSERT INTO s_ord (id, customer_id, date_ordered, date_shipped, sales_rep_id, total, payment_type, order_filled) VALUES ('104', '208', '1992-09-03', '1992-09-23', '13', 32430, 'CREDIT', 'Y');
INSERT INTO s_ord (id, customer_id, date_ordered, date_shipped, sales_rep_id, total, payment_type, order_filled) VALUES ('105', '209', '1992-09-04', '1992-09-18', '11', 2722.24, 'CREDIT', 'Y');
INSERT INTO s_ord (id, customer_id, date_ordered, date_shipped, sales_rep_id, total, payment_type, order_filled) VALUES ('106', '210', '1992-09-07', '1992-09-15', '12', 15634, 'CREDIT', 'Y');
INSERT INTO s_ord (id, customer_id, date_ordered, date_shipped, sales_rep_id, total, payment_type, order_filled) VALUES ('107', '211', '1992-09-07', '1992-09-21', '14', 142171, 'CREDIT', 'Y');
INSERT INTO s_ord (id, customer_id, date_ordered, date_shipped, sales_rep_id, total, payment_type, order_filled) VALUES ('108', '212', '1992-09-07', '1992-09-10', '13', 149570, 'CREDIT', 'Y');
INSERT INTO s_ord (id, customer_id, date_ordered, date_shipped, sales_rep_id, total, payment_type, order_filled) VALUES ('109', '213', '1992-09-08', '1992-09-28', '11', 1020935, 'CREDIT', 'Y');
INSERT INTO s_ord (id, customer_id, date_ordered, date_shipped, sales_rep_id, total, payment_type, order_filled) VALUES ('110', '214', '1992-09-09','1992-09-21', '11', 1539.13, 'CASH', 'Y');
INSERT INTO s_ord (id, customer_id, date_ordered, date_shipped, sales_rep_id, total, payment_type, order_filled) VALUES ('111', '204', '1992-09-09', '1992-09-21', '11', 2770, 'CASH', 'Y');
INSERT INTO s_ord (id, customer_id, date_ordered, date_shipped, sales_rep_id, total, payment_type, order_filled) VALUES ('97', '201', '1992-08-28', '1992-09-17', '12', 84000, 'CREDIT', 'Y');
INSERT INTO s_ord (id, customer_id, date_ordered, date_shipped, sales_rep_id, total, payment_type, order_filled) VALUES ('98', '202', '1992-08-31', '1992-09-10', '14', 595, 'CASH', 'Y');
INSERT INTO s_ord (id, customer_id, date_ordered, date_shipped, sales_rep_id, total, payment_type, order_filled) VALUES ('99', '203', '1992-08-31', '1992-09-18', '14', 7707, 'CREDIT', 'Y');
INSERT INTO s_ord (id, customer_id, date_ordered, date_shipped, sales_rep_id, total, payment_type, order_filled) VALUES ('112', '210', '1992-08-31', '1992-09-10', '12', 550, 'CREDIT', 'Y');

#	************** S_PRODUCT TABLE ********************************
#	*****************************************************************

DROP TABLE s_product CASCADE CONSTRAINTS;
CREATE TABLE s_product (id VARCHAR2(7), name VARCHAR2(25), short_desc VARCHAR2(255), suggested_whlsl_price NUMERIC(11,2), whlsl_units VARCHAR2(10));

INSERT INTO s_product (id, name, short_desc, suggested_whlsl_price, whlsl_units) VALUES ('10011', 'Bunny Boot','Beginner''s ski boot',150, '');
INSERT INTO s_product (id, name, short_desc, suggested_whlsl_price, whlsl_units) VALUES ('10012', 'Ace Ski Boot','Intermediate ski boot',200, '');
INSERT INTO s_product (id, name, short_desc, suggested_whlsl_price, whlsl_units) VALUES ('10013', 'Pro Ski Boot','Advanced ski boot',410, '');
INSERT INTO s_product (id, name, short_desc, suggested_whlsl_price, whlsl_units) VALUES ('10021', 'Bunny Ski Pole','Beginner''s ski pole',16.25, '');
INSERT INTO s_product (id, name, short_desc, suggested_whlsl_price, whlsl_units) VALUES ('10022', 'Ace Ski Pole','Intermediate ski pole',21.95, '');
INSERT INTO s_product (id, name, short_desc, suggested_whlsl_price, whlsl_units) VALUES ('10023', 'Pro Ski Pole','Advanced ski pole',40.95, '');
INSERT INTO s_product (id, name, short_desc, suggested_whlsl_price, whlsl_units) VALUES ('20106', 'Junior Soccer Ball','Junior soccer ball',11, '');
INSERT INTO s_product (id, name, short_desc, suggested_whlsl_price, whlsl_units) VALUES ('20108', 'World Cup Soccer Ball','World cup soccer ball',28, '');
INSERT INTO s_product (id, name, short_desc, suggested_whlsl_price, whlsl_units) VALUES ('20201', 'World Cup Net','World cup net',123, '');
INSERT INTO s_product (id, name, short_desc, suggested_whlsl_price, whlsl_units) VALUES ('20510', 'Black Hawk Knee Pads','Knee pads, pair',9, '');
INSERT INTO s_product (id, name, short_desc, suggested_whlsl_price, whlsl_units) VALUES ('20512', 'Black Hawk Elbow Pads','Elbow pads, pair',8, '');
INSERT INTO s_product (id, name, short_desc, suggested_whlsl_price, whlsl_units) VALUES ('30321', 'Grand Prix Bicycle','Road bicycle',1669, '');
INSERT INTO s_product (id, name, short_desc, suggested_whlsl_price, whlsl_units) VALUES ('30326', 'Himalaya Bicycle','Mountain bicycle',582, '');
INSERT INTO s_product (id, name, short_desc, suggested_whlsl_price, whlsl_units) VALUES ('30421', 'Grand Prix Bicycle Tires','Road bicycle tires',16, '');
INSERT INTO s_product (id, name, short_desc, suggested_whlsl_price, whlsl_units) VALUES ('30426', 'Himalaya Tires','Mountain bicycle tires',18.25, '');
INSERT INTO s_product (id, name, short_desc, suggested_whlsl_price, whlsl_units) VALUES ('30433', 'New Air Pump','Tire pump',20, '');
INSERT INTO s_product (id, name, short_desc, suggested_whlsl_price, whlsl_units) VALUES ('32779', 'Slaker Water Bottle','Water bottle',7, '');
INSERT INTO s_product (id, name, short_desc, suggested_whlsl_price, whlsl_units) VALUES ('32861', 'Safe-T Helmet','Bicycle helmet',60, '');
INSERT INTO s_product (id, name, short_desc, suggested_whlsl_price, whlsl_units) VALUES ('40421', 'Alexeyer Pro Lifting Bar','Straight bar',65, '');
INSERT INTO s_product (id, name, short_desc, suggested_whlsl_price, whlsl_units) VALUES ('40422', 'Pro Curling Bar','Curling bar',50, '');
INSERT INTO s_product (id, name, short_desc, suggested_whlsl_price, whlsl_units) VALUES ('41010', 'Prostar 10 Pound Weight','Ten pound weight',8, '');
INSERT INTO s_product (id, name, short_desc, suggested_whlsl_price, whlsl_units) VALUES ('41020', 'Prostar 20 Pound Weight','Twenty pound weight',12, '');
INSERT INTO s_product (id, name, short_desc, suggested_whlsl_price, whlsl_units) VALUES ('41050', 'Prostar 50 Pound Weight','Fifty pound weight',25, '');
INSERT INTO s_product (id, name, short_desc, suggested_whlsl_price, whlsl_units) VALUES ('41080', 'Prostar 80 Pound Weight','Eighty pound weight',35, '');
INSERT INTO s_product (id, name, short_desc, suggested_whlsl_price, whlsl_units) VALUES ('41100', 'Prostar 100 Pound Weight','One hundred pound weight',45, '');
INSERT INTO s_product (id, name, short_desc, suggested_whlsl_price, whlsl_units) VALUES ('50169', 'Major League Baseball','Baseball',4.29, '');
INSERT INTO s_product (id, name, short_desc, suggested_whlsl_price, whlsl_units) VALUES ('50273', 'Chapman Helmet','Batting helmet',22.89, '');
INSERT INTO s_product (id, name, short_desc, suggested_whlsl_price, whlsl_units) VALUES ('50417', 'Griffey Glove','Outfielder''s glove',80, '');
INSERT INTO s_product (id, name, short_desc, suggested_whlsl_price, whlsl_units) VALUES ('50418', 'Alomar Glove','Infielder''s glove',75, '');
INSERT INTO s_product (id, name, short_desc, suggested_whlsl_price, whlsl_units) VALUES ('50419', 'Steinbach Glove','Catcher''s glove',80, '');
INSERT INTO s_product (id, name, short_desc, suggested_whlsl_price, whlsl_units) VALUES ('50530', 'Cabrera Bat','Thirty inch bat',45, '');
INSERT INTO s_product (id, name, short_desc, suggested_whlsl_price, whlsl_units) VALUES ('50532', 'Puckett Bat','Thirty-two inch bat',47, '');
INSERT INTO s_product (id, name, short_desc, suggested_whlsl_price, whlsl_units) VALUES ('50536', 'Winfield Bat','Thirty-six inch bat',50, '');

#	************** S_REGION TABLE ********************************
#	*****************************************************************

DROP TABLE s_region CASCADE CONSTRAINTS;
CREATE TABLE s_region (id VARCHAR2(3), name VARCHAR2(26));

INSERT INTO s_region (id, name) VALUES ('1', 'North America');
INSERT INTO s_region (id, name) VALUES ('2', 'South America');
INSERT INTO s_region (id, name) VALUES ('3', 'Africa / Middle East');
INSERT INTO s_region (id, name) VALUES ('4', 'Asia');
INSERT INTO s_region (id, name) VALUES ('5', 'Europe');
INSERT INTO s_region (id, name) VALUES ('6', 'Central America /Caribbean');

#	************** S_TITLE TABLE ********************************
#	*****************************************************************

DROP TABLE s_title CASCADE CONSTRAINTS;
CREATE TABLE s_title (title VARCHAR2(25));

INSERT INTO s_title (title) VALUES ('President');
INSERT INTO s_title (title) VALUES ('Sales Representative');
INSERT INTO s_title (title) VALUES ('Stock Clerk');
INSERT INTO s_title (title) VALUES ('VP, Administration');
INSERT INTO s_title (title) VALUES ('VP, Finance');
INSERT INTO s_title (title) VALUES ('VP, Operations');
INSERT INTO s_title (title) VALUES ('VP, Sales');
INSERT INTO s_title (title) VALUES ('Warehouse Manager');

#	************** S_WAREHOUSE TABLE ********************************
#	*****************************************************************

DROP TABLE s_warehouse CASCADE CONSTRAINTS;
CREATE TABLE s_warehouse (id VARCHAR2(7), region_id VARCHAR2(3), address VARCHAR2(20), city VARCHAR2(20), state VARCHAR2(15), country VARCHAR2(20), zip_code VARCHAR2(15), phone VARCHAR2(20), manager_id VARCHAR2(3));

INSERT INTO s_warehouse (id, region_id, address, city, state, country, zip_code, phone, manager_id) VALUES ('101', '1', '283 King Street', 'Seattle', 'WA', 'US', '', '', '6');
INSERT INTO s_warehouse (id, region_id, address, city, state, country, zip_code, phone, manager_id) VALUES ('10501', '5', '5 Modrany', 'Bratislava', '', 'Czechozlovakia', '', '', '10');
INSERT INTO s_warehouse (id, region_id, address, city, state, country, zip_code, phone, manager_id) VALUES ('201', '2', '68 Via Centrale', 'Sao Paolo', '', 'Brazil', '', '', '7');
INSERT INTO s_warehouse (id, region_id, address, city, state, country, zip_code, phone, manager_id) VALUES ('301', '3', '6921 King Way', 'Lagos', '', 'Nigeria', '', '', '8');
INSERT INTO s_warehouse (id, region_id, address, city, state, country, zip_code, phone, manager_id) VALUES ('401', '4', '86 Chu Street', 'Hong Kong', '', '', '', '', '9');


