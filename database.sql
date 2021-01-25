
All create table sql commands are in file project_1/app/db.py



-------------------------DATA-----------------------------------

----Table doctors------

1,Nguyen Van An,0912.345.678,4,an1234,Tốt nghiệp chuyên ngành nha khoa Đại học Y Hà Nội. Tu nghiệp tại Nhật Bản 10 năm,t,f
2,Tran Thi Binh,0912.456.789,4,binh2345,Tốt nghiệp chuyên ngành nha khoa Đại học Y Hải Phòng. 12 năm kinh nghiệm,t,t
3,Ngo Thi Cuc,0923.113.114,5,cuc3456,Tốt nghiệp chuyên ngành nha khoa Đại học Y Hà Nội. Công tác tại Bệnh viện Việt Pháp,f,t
4,Nguyen Binh Duong,0923.225.678,2,duong4567,Tốt nghiệp chuyên ngành nha khoa Đại học Y Thái Bình. Từng công tác 7 năm tại Học Viện Quân Y,f,f
5,Vu Ngoc Anh,0945.987.678,5,anh1234,Tốt nghiệp chuyên ngành nha khoa Đại học Y Tokyo. Công tác tại Bệnh viện Bạch Mai,t,t
7,Le Manh Cuong,0989.345.980,2,cuong3456,Tốt nghiệp chuyên ngành nha khoa Đại học Y Hà Nội. Công tác tại Bệnh viện Quân Y 108,f,t
8,Tran Thi Dao,0904.980.678,2,dao4567,Tốt nghiệp chuyên ngành nha khoa Đại học Y Hải Phòng. Tu nghiệp tại Hàn Quốc 9 năm và được giấy khen của Hiệp hội Nha khoa Hàn Quốc,f,t
6,Truong Thanh Bao,0989.345.987,6,bao2345,Tốt nghiệp chuyên ngành nha khoa Đại học Y Hà Nội. Du học Pháp và làm việc tại bệnh viện Trung ương Paris 18 năm,t,t
9,Cao Minh Hieu,0915.422.231,3,hieucao,"Mới ra trường, chưa có kinh nghiệm.",f,t
10,Nguyen Viet Huy,0915.233.242,48,huynguyen,Có học bổng sinh viên nội trú,f,t




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
15,"Cắt lợi(nướu) thẩm mỹ, khắc phục cười hở lợi",9000000



----Table patients------------------

1,Le Thi Van Anh,1991-01-07,F,0712.123.123
2,Nguyen Thi Van Anh,1997-12-18,F,0712.124.124
3,Le Viet Anh,1995-12-11,M,0712.125.125
4,Le Van Bach,1991-09-04,M,0712.112.126
5,Dao Thi Binh,1996-09-04,F,0712.127.127
6,Nguyen Hoa Binh,1997-10-03,F,0712.128.128
7,Pham Ngoc Bich,1998-08-01,F,0712.129.129
8,Nguyen Thanh Binh,1998-01-08,M,0712.130.130
9,Nguyen Linh Chi,1996-10-30,F,0712.131.131
10,Nguyen Thi Chanh,1995-05-25,F,0712.132.132
11,Pham Ngoc Chien,1990-07-31,M,0712.133.133
12,Vu Manh Chinh,1997-10-30,M,0712.134.134
13,Dinh Van Cuong,1991-01-21,M,0712.135.135
14,Nguyen Ngoc Hai Dang,1984-12-29,M,0712.136.136
15,Hoang Thi Diem,1999-10-29,F,0712.139.148
16,Tran Tien Dat,2003-05-30,M,0713.457.458
17,Pham Van Dong,2010-06-12,M,0713.458.459
18,Cao Thi Van Dung,1975-02-09,F,0713.460.461
19,Nguyen Anh Dung,2012-07-22,M,0713.489.789
20,Vu Thi Thuy Dung,2000-09-09,F,0713.060.082
21,Bui Huy Giang,1984-11-22,M,0714.456.456
22,Le Thi Ky Duyen,1995-07-28,F,0714.457.457
23,Dang Thi Thu Ha,1966-03-31,F,0714.237.238
24,Kieu Thi Hai,1977-04-04,F,0714.777.888
25,Dang Kieu Han,1987-07-09,F,0714.888.145
26,Ngo Thi Thu Hang,1989-07-29,F,0714.889.146
27,Vuong Thi My Hanh,1992-12-08,F,0714.890.167
28,Pham Trung Hieu,1993-02-12,M,0714.891.575
29,Nguyen Ba Hung,2009-09-10,M,0714.892.569
30,Nguyen Quoc Huy,1987-03-01,M,0714.893.123
31,Hoang Van Khanh,1995-05-08,M,0714.894.187
32,Vuong Ngoc Lan,2011-12-12,F,0714.897.972
33,Nguyen Quoc Hai,2008-09-09,M,0714.895.345
34,Cao My Linh,1996-12-29,F,0714.898.098
35,Le Trung Kien,1993-11-11,M,0714.896.214
36,Ho Thi Lien,2006-01-12,F,0714.950.950
37,Nguyen Thi Mai,2007-04-05,F,0714.951.951
38,Ngo Duc Manh,2000-06-13,M,0714.952.896
39,Doan Phuong Nam,2001-09-03,M,0714.953.076
40,Dao Thi Nga,2013-10-06,F,0714.954.146
41,Vu Xuan Nghia,2008-09-10,M,0714.955.189
42,Do Minh Phuc,1990-06-25,M,0714.956.892
43,Luu Thanh Nguyet,1970-04-08,F,0714.957.182
44,Nguyen Bao Phong,2000-09-10,M,0714.958.985
45,Vu Van Quang,2004-02-09,M,0714.959.098
46,Nguyen Diem Quynh,1993-12-03,F,0714.960.742
47,Tran Van Son,1985-12-17,M,0714.961.235
48,Vo Thi My Tam,1964-09-12,F,0714.962.542
49,Hoang Gia Tai,1969-06-06,M,0714.963.673
50,Phung Van Tuan,1971-07-09,M,0714.964.123



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




