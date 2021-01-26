/* Các câu lệnh tạo bảng */
--medicines TABLE
DROP TABLE IF EXISTS medicines CASCADE;
CREATE TABLE medicines (
	medicine_id serial ,
	medicine_name varchar(255) ,
	unit_price integer ,
	stock_quantity integer ,
	CONSTRAINT medicines_pk PRIMARY KEY (medicine_id)
) ;
--services TABLE
DROP TABLE IF EXISTS services CASCADE;
CREATE TABLE services (
	service_id serial ,
	service_name varchar(255) ,
	price integer ,
	CONSTRAINT services_pk PRIMARY KEY (service_id)
);

--patients TABLE 
CREATE TABLE IF NOT EXISTS patients (
	patient_id serial,
	patient_name varchar(50) ,
	patient_dob date , 
	gender varchar(1) , --> M or F ("Male": nam & "Female": nu)
	phone_number varchar(15) ,
	CONSTRAINT patients_pk PRIMARY KEY (patient_id),
	CONSTRAINT patients_chk CHECK(gender in ('M','F'))
);

--doctors TABLE
DROP TABLE IF EXISTS doctors CASCADE;
CREATE TABLE doctors (
	doctor_id serial,
	doctor_name varchar(64) ,
	phone_number varchar(16) ,
	day_off varchar(8) ,
	password varchar(255) ,
	description varchar(255) ,
	is_manager BOOLEAN default False,
	is_work BOOLEAN default True, 
	CONSTRAINT doctors_pk PRIMARY KEY (doctor_id)
);

--histories TABLE
DROP TABLE IF EXISTS histories CASCADE;
CREATE TABLE histories (
	id serial ,
	doctor_id integer , 
	patient_id integer ,
	note varchar(255) ,
	date_time date , 
	is_done BOOLEAN ,

	medicine_fee integer default 0,
	treatment_fee integer default 0,
	total_price integer default 0,
	is_paid BOOLEAN ,

	CONSTRAINT histories_pk PRIMARY KEY (id)
	--CONSTRAINT ... is_paid and is_done 
);


--pre_medicines TABLE
DROP TABLE IF EXISTS pre_medicines CASCADE;
CREATE TABLE pre_medicines (
	prescription_id integer ,
	medicine_id integer ,
	quantity integer 
);

--pre_services TABLE
DROP TABLE IF EXISTS pre_services CASCADE;
CREATE TABLE pre_services (
	prescription_id integer ,
	service_id integer ,
	quantity integer

);

--salary_table TABLE
DROP TABLE IF EXISTS salary_table CASCADE;
CREATE TABLE salary_table (
	doctor_id integer ,
	which_month integer ,
	which_year integer ,
	num_patient integer ,
	salary integer 
);

--managers TABLE
DROP TABLE IF EXISTS managers CASCADE;
CREATE TABLE managers (
	manager_id serial ,
	manager_name varchar(64) ,
	phone_number varchar(16) ,
	password varchar(255) 
);


/* Tạp các khóa ngoài */
/* foreign key of TABLE "histories" */
ALTER TABLE histories ADD CONSTRAINT histories_fk0 FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id) ON UPDATE CASCADE;
ALTER TABLE histories ADD CONSTRAINT histories_fk1 FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON UPDATE CASCADE;


/* foreign key of TABLE "pre_medicines" */
ALTER TABLE pre_medicines ADD CONSTRAINT pre_medicines_fk0 FOREIGN KEY (prescription_id) REFERENCES histories(id) ON UPDATE CASCADE;
ALTER TABLE pre_medicines ADD CONSTRAINT pre_medicines_fk1 FOREIGN KEY (medicine_id) REFERENCES medicines(medicine_id) ON UPDATE CASCADE;

/* foreign key of TABLE "pre_services" */
ALTER TABLE pre_services ADD CONSTRAINT pre_services_fk0 FOREIGN KEY (prescription_id) REFERENCES histories(id) ON UPDATE CASCADE;
ALTER TABLE pre_services ADD CONSTRAINT pre_services_fk1 FOREIGN KEY (service_id) REFERENCES services(service_id) ON UPDATE CASCADE;


/* foreign key of TABLE "salary_table" */
ALTER TABLE salary_table ADD CONSTRAINT salary_table_fk0 FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id) ON UPDATE CASCADE;



/* INSERT TABLE "patients" */
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Le Thi Van Anh','1991-01-07','F','0712.123.123');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Nguyen Thi Van Anh','1997-12-18','F','0712.124.124');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Le Viet Anh','1995-12-11','M','0712.125.125');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Le Van Bach','1991-09-04','M','0712.112.126');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Dao Thi Binh','1996-09-04','F','0712.127.127');

INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Nguyen Hoa Binh','1997-10-3','F','0712.128.128');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Pham Ngoc Bich','1998-08-01','F','0712.129.129');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Nguyen Thanh Binh','1998-01-08','M','0712.130.130');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Nguyen Linh Chi','1996-10-30','F','0712.131.131');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Nguyen Thi Chanh','1995-5-25','F','0712.132.132');

INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Pham Ngoc Chien','1990-7-31','M','0712.133.133');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Vu Manh Chinh','1997-10-30','M','0712.134.134');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Dinh Van Cuong','1991-01-21','M','0712.135.135');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Nguyen Ngoc Hai Dang','1984-12-29','M','0712.136.136');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Hoang Thi Diem','1999-10-29','F','0712.139.148');

INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Tran Tien Dat','2003-5-30','M','0713.457.458');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Pham Van Dong','2010-6-12','M','0713.458.459');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Cao Thi Van Dung','1975-02-09','F','0713.460.461');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Nguyen Anh Dung','2012-7-22','M','0713.489.789');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Vu Thi Thuy Dung','2000-09-09','F','0713.060.082');

INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Bui Huy Giang','1984-11-22','M','0714.456.456');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Le Thi Ky Duyen','1995-07-28','F','0714.457.457');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Dang Thi Thu Ha','1966-03-31','F','0714.237.238');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Kieu Thi Hai','1977-04-04','F','0714.777.888');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Dang Kieu Han','1987-07-09','F','0714.888.145');

INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Ngo Thi Thu Hang','1989-07-29','F','0714.889.146');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Vuong Thi My Hanh','1992-12-08','F','0714.890.167');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Pham Trung Hieu','1993-02-12','M','0714.891.575');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Nguyen Ba Hung','2009-9-10','M','0714.892.569');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Nguyen Quoc Huy','1987-03-01','M','0714.893.123');

INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Hoang Van Khanh','1995-05-08','M','0714.894.187');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Vuong Ngoc Lan','2011-12-12','F','0714.897.972');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Nguyen Quoc Hai','2008-09-09','M','0714.895.345');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Cao My Linh','1996-12-29','F','0714.898.098');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Le Trung Kien','1993-11-11','M','0714.896.214');

INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Ho Thi Lien','2006-1-12','F','0714.950.950');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Nguyen Thi Mai','2007-4-5','F','0714.951.951');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Ngo Duc Manh','2000-6-13','M','0714.952.896');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Doan Phuong Nam','2001-9-3','M','0714.953.076');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Dao Thi Nga','2013-10-6','F','0714.954.146');

INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Vu Xuan Nghia','2008-9-10','M','0714.955.189');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Do Minh Phuc','1990-06-25','M','0714.956.892');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Luu Thanh Nguyet','1970-4-8','F','0714.957.182');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Nguyen Bao Phong','2000-9-10','M','0714.958.985');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Vu Van Quang','2004-02-09','M','0714.959.098');

INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Nguyen Diem Quynh','1993-12-3','F','0714.960.742');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Tran Van Son','1985-12-17','M','0714.961.235');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Vo Thi My Tam','1964-9-12','F','0714.962.542');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Hoang Gia Tai','1969-6-6','M','0714.963.673');
INSERT INTO patients(patient_name,patient_dob,gender,phone_number) VALUES('Phung Van Tuan','1971-7-9','M','0714.964.123');

/* INSERT TABLE "doctors" */
INSERT INTO doctors(doctor_name,phone_number,day_off,password,description,is_manager) VALUES('Nguyen Van An','0912.345.678',4,'an1234','Tốt nghiệp chuyên ngành nha khoa Đại học Y Hà Nội. Tu nghiệp tại Nhật Bản 10 năm',true);
INSERT INTO doctors(doctor_name,phone_number,day_off,password,description,is_manager) VALUES('Tran Thi Binh','0912.456.789',4,'binh2345','Tốt nghiệp chuyên ngành nha khoa Đại học Y Hải Phòng. 12 năm kinh nghiệm',true);
INSERT INTO doctors(doctor_name,phone_number,day_off,password,description,is_manager) VALUES('Ngo Thi Cuc','0923.113.114',5,'cuc3456','Tốt nghiệp chuyên ngành nha khoa Đại học Y Hà Nội. Công tác tại Bệnh viện Việt Pháp',false);
INSERT INTO doctors(doctor_name,phone_number,day_off,password,description,is_manager) VALUES('Nguyen Binh Duong','0923.225.678',2,'duong4567','Tốt nghiệp chuyên ngành nha khoa Đại học Y Thái Bình. Từng công tác 7 năm tại Học Viện Quân Y',false);

INSERT INTO doctors(doctor_name,phone_number,day_off,password,description,is_manager) VALUES('Vu Ngoc Anh','0945.987.678',5,'anh1234','Tốt nghiệp chuyên ngành nha khoa Đại học Y Tokyo. Công tác tại Bệnh viện Bạch Mai',true);
INSERT INTO doctors(doctor_name,phone_number,day_off,password,description,is_manager) VALUES('Truong Thanh Bao','0989.345.987',6,'bao2345','Tốt nghiệp chuyên ngành nha khoa Đại học Y Hà Nội. Du học Pháp và làm việc tại bệnh viện Trung ương Paris 18 năm',true);
INSERT INTO doctors(doctor_name,phone_number,day_off,password,description,is_manager) VALUES('Le Manh Cuong','0989.345.980',2,'cuong3456','Tốt nghiệp chuyên ngành nha khoa Đại học Y Hà Nội. Công tác tại Bệnh viện Quân Y 108',false);
INSERT INTO doctors(doctor_name,phone_number,day_off,password,description,is_manager) VALUES('Tran Thi Dao','0904.980.678',2,'dao4567','Tốt nghiệp chuyên ngành nha khoa Đại học Y Hải Phòng. Tu nghiệp tại Hàn Quốc 9 năm và được giấy khen của Hiệp hội Nha khoa Hàn Quốc',false);



INSERT INTO doctors(doctor_name,phone_number,day_off,password,description,is_manager, is_work) VALUES('Nguyen Van An','0912.345.678',4,'an1234','Tốt nghiệp chuyên ngành nha khoa Đại học Y Hà Nội. Tu nghiệp tại Nhật Bản 10 năm',true, false);
INSERT INTO doctors(doctor_name,phone_number,day_off,password,description,is_manager, is_work) VALUES('Tran Thi Binh','0912.456.789',4,'binh2345','Tốt nghiệp chuyên ngành nha khoa Đại học Y Hải Phòng. 12 năm kinh nghiệm',true, true);
INSERT INTO doctors(doctor_name,phone_number,day_off,password,description,is_manager, is_work) VALUES('Ngo Thi Cuc','0923.113.114',5,'cuc3456','Tốt nghiệp chuyên ngành nha khoa Đại học Y Hà Nội. Công tác tại Bệnh viện Việt Pháp',false, true);
INSERT INTO doctors(doctor_name,phone_number,day_off,password,description,is_manager, is_work) VALUES('Nguyen Binh Duong','0923.225.678',2,'duong4567','Tốt nghiệp chuyên ngành nha khoa Đại học Y Thái Bình. Từng công tác 7 năm tại Học Viện Quân Y',false, flase);

INSERT INTO doctors(doctor_name,phone_number,day_off,password,description,is_manager, is_work) VALUES('Vu Ngoc Anh','0945.987.678',5,'anh1234','Tốt nghiệp chuyên ngành nha khoa Đại học Y Tokyo. Công tác tại Bệnh viện Bạch Mai',true, true);
INSERT INTO doctors(doctor_name,phone_number,day_off,password,description,is_manager, is_work) VALUES('Truong Thanh Bao','0989.345.987',6,'bao2345','Tốt nghiệp chuyên ngành nha khoa Đại học Y Hà Nội. Du học Pháp và làm việc tại bệnh viện Trung ương Paris 18 năm',true, true);
INSERT INTO doctors(doctor_name,phone_number,day_off,password,description,is_manager, is_work) VALUES('Le Manh Cuong','0989.345.980',2,'cuong3456','Tốt nghiệp chuyên ngành nha khoa Đại học Y Hà Nội. Công tác tại Bệnh viện Quân Y 108',false, true);
INSERT INTO doctors(doctor_name,phone_number,day_off,password,description,is_manager, is_work) VALUES('Tran Thi Dao','0904.980.678',2,'dao4567','Tốt nghiệp chuyên ngành nha khoa Đại học Y Hải Phòng. Tu nghiệp tại Hàn Quốc 9 năm và được giấy khen của Hiệp hội Nha khoa Hàn Quốc',false, true);


/* INSERT TABLE "medicines" */ 
INSERT INTO medicines(medicine_name,unit_price,stock_quantity) VALUES('Nước súc miệng bệnh viện Đại học Y Hà Nội',90000,20);
INSERT INTO medicines(medicine_name,unit_price,stock_quantity) VALUES('Gel trị viêm nha chu',100000,25);
INSERT INTO medicines(medicine_name,unit_price,stock_quantity) VALUES('Acyclovir trị nấm khoang miệng',120000,19);
INSERT INTO medicines(medicine_name,unit_price,stock_quantity) VALUES('Alphachoay kháng viêm - Hộp 30 viên',70000,100);
INSERT INTO medicines(medicine_name,unit_price,stock_quantity) VALUES('Paracetamol 500mg giảm đau - Hộp 50 viên',32500,78);

INSERT INTO medicines(medicine_name,unit_price,stock_quantity) VALUES('Gel Foramen trị viêm lợi,viêm nha chu,chảy máchân răng',105000,33);
INSERT INTO medicines(medicine_name,unit_price,stock_quantity) VALUES('Nước muối sinh lý',5000,98);
INSERT INTO medicines(medicine_name,unit_price,stock_quantity) VALUES('Kháng sinh Clindamycin - vỉ 10 viên',21000,214);
INSERT INTO medicines(medicine_name,unit_price,stock_quantity) VALUES('Kháng sinh Clarithromycin 500mg - hôp 28 viên - rất hay dùng',163000,23);
INSERT INTO medicines(medicine_name,unit_price,stock_quantity) VALUES('Prednisolone 5mg kháng viêm - vỉ 20 viên',10000,76);

/* INSERT TABLE "services" */ 
INSERT INTO services(service_name,price) VALUES ('Nhổ răng sữa (trẻ em)',100000); -->100k
INSERT INTO services(service_name,price) VALUES ('Nhổ răng khôn (người lớn)',1200000); -->1.2tr
INSERT INTO services(service_name,price) VALUES ('Niềng răng',20000000); -->20tr
INSERT INTO services(service_name,price) VALUES ('Trồng răng sứ (Implant)',7000000); -->7tr
INSERT INTO services(service_name,price) VALUES ('Trồng răng vàng (Implant)',25000000); -->25tr

INSERT INTO services(service_name,price) VALUES ('Lấy cao răng',200000); -->200k
INSERT INTO services(service_name,price) VALUES ('Điều trị viêm nha chu 1 hàm',6000000); -->6tr
INSERT INTO services(service_name,price) VALUES ('Điều trị viêm nha chu 2 hàm',10000000); -->10tr
INSERT INTO services(service_name,price) VALUES ('Trám răng sâu',300000); -->300k
INSERT INTO services(service_name,price) VALUES ('Chụp X-quang răng 3D',400000); -->400k

INSERT INTO services(service_name,price) VALUES ('Chụp X-quang phim Pano/Cepha',100000); -->100k
INSERT INTO services(service_name,price) VALUES ('Làm trắng răng',2300000); -->2.3tr
INSERT INTO services(service_name,price) VALUES ('Khám và tư vấn',0); --> FREE
INSERT INTO services(service_name,price) VALUES ('Chỉnh răng sớm cho trẻ em',10000000); -->10tr
INSERT INTO services(service_name,price) VALUES ('Cắt lợi(nướu) thẩm mỹ, khắc phục cười hở lợi',9000000); -->9tr


/* INSERT TABLE "managers" */
/* Tài khoản cũng cần phải được mã hóa mật khẩu, nên dữ liệu của một tài khoản được tạo ra trên web*/
/* Không có câu lệnh insert sql*/
/* Muốn đăng nhập vào hệ thống, bạn cần đăng kí trước*/

/* foreign key of TABLE "histories" */
ALTER TABLE histories ADD CONSTRAINT histories_fk0 FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id) ON UPDATE CASCADE;
ALTER TABLE histories ADD CONSTRAINT histories_fk0_a FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id) ON DELETE SET NULL;

ALTER TABLE histories ADD CONSTRAINT histories_fk1 FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON UPDATE CASCADE;
ALTER TABLE histories ADD CONSTRAINT histories_fk1_a FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE SET NULL;

/* foreign key of TABLE "pre_medicines" */
ALTER TABLE pre_medicines ADD CONSTRAINT pre_medicines_fk0 FOREIGN KEY (prescription_id) REFERENCES histories(id) ON UPDATE CASCADE;
ALTER TABLE pre_medicines ADD CONSTRAINT pre_medicines_fk0_a FOREIGN KEY (prescription_id) REFERENCES histories(id) ON DELETE SET NULL;

ALTER TABLE pre_medicines ADD CONSTRAINT pre_medicines_fk1 FOREIGN KEY (medicine_id) REFERENCES medicines(medicine_id) ON UPDATE CASCADE;
ALTER TABLE pre_medicines ADD CONSTRAINT pre_medicines_fk1_a FOREIGN KEY (medicine_id) REFERENCES medicines(medicine_id) ON DELETE SET NULL;

/* foreign key of TABLE "pre_services" */
ALTER TABLE pre_services ADD CONSTRAINT pre_services_fk0 FOREIGN KEY (prescription_id) REFERENCES histories(id) ON UPDATE CASCADE;
ALTER TABLE pre_services ADD CONSTRAINT pre_services_fk0_a FOREIGN KEY (prescription_id) REFERENCES histories(id) ON DELETE SET NULL;

ALTER TABLE pre_services ADD CONSTRAINT pre_services_fk1 FOREIGN KEY (service_id) REFERENCES services(service_id) ON UPDATE CASCADE;
ALTER TABLE pre_services ADD CONSTRAINT pre_services_fk1_a FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE SET NULL;

/* foreign key of TABLE "salary_table" */
ALTER TABLE salary_table ADD CONSTRAINT salary_table_fk0 FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id) ON UPDATE CASCADE;
ALTER TABLE salary_table ADD CONSTRAINT salary_table_fk0_a FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id) ON DELETE SET NULL;



/* GIẢI THÍCH */
/* Bởi vì bắt đầu từ bảng histories, các giá trị nếu nhập tay vào database sẽ dễ gây ra nhiều sai sót */
/* Thế nên, nhóm chúng em đã xây dựng web để nhập thuận tiện hơn (và đúng là thực tế dữ liệu nhập từ web về) */
/* Nên từ đây, bảng histories, pre_medicines, pre_services chỉ có data mà không có câu lệnh sql insert */
/* Đồng thời, bảng salary_table được suy ra từ giá trị các bảng khác nên cũng không có câu lệnh sql insert */





----Table medicines------

2,Gel trị viêm nha chu,100000,25
3,Acyclovir trị nấm khoang miệng,120000,19
4,Alphachoay kháng viêm - Hộp 30 viên,70000,100
5,Paracetamol 500mg giảm đau - Hộp 50 viên,32500,78
10,Prednisolone 5mg kháng viêm - vỉ 20 viên,10000,76
11,Paracetamol 100mg dạng gói uống,20000,50
6,"Gel Foramen trị viêm lợi,viêm nha chu,chảy máu chân răng",105000,33
7,Nước muối sinh lý,5000,96
12,Viên Sủi Bổ Sung Vitamin Myvita Multivitamin Vị Cam 20 Viên,26000,20
14,"Ibuprofen thuốc giảm đau, kháng viêm400mg hộp 100 viên",90000,50
13,Vitamin C 500mg Mekophar 200 viên,95000,9
1,Nước súc miệng bệnh viện Đại học Y Hà Nội,90000,48
8,Kháng sinh Clindamycin - vỉ 10 viên,21000,213
9,Kháng sinh Clarithromycin 500mg - hôp 28 viên - rất hay dùng,163000,21



---Table services----- 

1,Nhổ răng sữa (trẻ em),100000
2,Nhổ răng khôn (người lớn),1200000
3,Niềng răng,20000000
4,Trồng răng sứ (Implant),7000000
5,Trồng răng vàng (Implant),25000000
6,Lấy cao răng,200000
7,Điều trị viêm nha chu 1 hàm,6000000
8,Điều trị viêm nha chu 2 hàm,10000000
9,Trám răng sâu,300000
10,Chụp X-quang răng 3D,400000
11,Chụp X-quang phim Pano/Cepha,100000
12,Làm trắng răng,2300000
13,Khám và tư vấn,0
14,Chỉnh răng sớm cho trẻ em,10000000
15,"Cắt lợi(nướu) thẩm mỹ, khắc phục cười hở lợi",900000



-----Table histories---------------------------

1,1,5,Sâu răng 2 cái. Sau này không được ăn đồ ngọt.,2021-01-06,t,600000,10000,610000,t
2,2,5,"Men răng kém, sau này chú ý không cắn vật cứng
",2020-10-12,t,0,95000,95000,t
3,3,8,"Viêm nha chu, chảy máu",2020-10-14,t,6000000,0,6000000,f
4,3,8,Lịch tái khám điều trị viêm nha chu,2020-11-12,f,0,0,0,f
5,4,6,"Chảy máu viêm lợi
",2020-10-19,t,0,275000,275000,t
6,25,7,"Niềng răng
",2020-10-23,t,20000000,0,20000000,t
7,7,6,"nhổ răng khôn 2 cái
",2020-11-03,t,2400000,21000,2421000,f
8,5,7,"Hẹn trước.
",2020-10-20,t,14000000,326000,14326000,t
9,5,9,tái khám sau trồng răng,2020-11-30,f,0,0,0,f
10,45,8,"Răng hỏng tủy, thay răng",2020-10-25,t,21000000,0,21000000,f
11,33,5,Hẹn chỉnh răng,2020-11-06,f,0,0,0,f
12,48,8,Hẹn khám răng định kì,2020-12-02,f,0,0,0,f
13,14,8,"Răng hỏng tủy, thay răng mới",2020-11-05,t,28000000,0,28000000,f
14,10,7,Trồng răng,2020-10-28,t,25000000,0,25000000,t
15,10,7,Tái khám kiểm tra răng sau trồng răng,2020-11-15,t,0,0,0,f
16,50,6,Hẹn trước,2020-01-08,f,0,0,0,f
17,44,2,Hẹn trước ,2021-01-08,f,0,0,0,f
18,43,2,Hẹn trước kiểm tra răng định kì,2021-01-08,f,0,0,0,f
19,1,6,"",2020-01-08,f,0,0,0,f
20,1,3,"",2021-01-08,t,0,0,0,f

-----Table pre_medicines---------
1,7,2
2,13,1
5,13,1
5,1,2
7,8,1
8,9,2


-----Table pre_services---------------
1,9,2
3,7,1
5,13,1
6,3,1
7,2,2
8,4,2
10,4,3
13,4,4
14,5,1
15,13,1



-----Table salary_table--------------
5,1,2021,1,6122000
5,10,2020,1,6019000
6,10,2020,1,6055000
7,10,2020,3,17865200




