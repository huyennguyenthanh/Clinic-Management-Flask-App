import psycopg2


def connect():
    # c = psycopg2.connect("dbname=a_1 user=postgres password=17071608")
    c = psycopg2.connect(
        host="localhost",
        port="5433",
        database="a",
        user="postgres",
        password="17071608")
    return c


conn = connect()
cur = conn.cursor()

# let's create a table:
cur.execute("CREATE TABLE IF NOT EXISTS managers (manage_id serial PRIMARY KEY, "
            "username VARCHAR(64), email VARCHAR(64), password VARCHAR(255));")
conn.commit()

cur.execute("CREATE TABLE IF NOT EXISTS medicines (medicine_id serial PRIMARY KEY, "
            "medicine_name VARCHAR(255), unit_price INTEGER, stock_quantity INTEGER);")
conn.commit()

cur.execute("CREATE TABLE IF NOT EXISTS services ("
            "service_id serial , service_name varchar(50) ,"
            "price integer ,"
            "CONSTRAINT services_pk PRIMARY KEY (service_id));")
conn.commit()

cur.execute("CREATE TABLE IF NOT EXISTS patients (patient_id serial,"
            "patient_name varchar(50) ,birthday date ,"
            "gender varchar(1) ,"
            "phone_number varchar(15) ,"
            "CONSTRAINT patients_pk PRIMARY KEY (patient_id),"
            "CONSTRAINT patients_chk CHECK(gender in ('M','F'))"
            ");")
conn.commit()

cur.execute("CREATE TABLE IF NOT EXISTS doctors (doctor_id serial,"
            "doctor_name varchar(64) ,phone_number varchar(16) ,"
            "day_off varchar(8) ,password varchar(255) ,description varchar(255) ,"
            "is_manager BOOLEAN ,"
            "is_work BOOLEAN , "
            "CONSTRAINT doctors_pk PRIMARY KEY (doctor_id));")
conn.commit()


cur.execute("CREATE TABLE IF NOT EXISTS histories ("
            "id serial ,"
            "patient_id integer ,"
            "doctor_id integer ,"
            "disease_name varchar(255) ,"
            "date_time DATE ,"
            "is_done BOOLEAN ,"
            ""
            "treatment_fee integer ,"
            "medicine_fee integer ,"
            "total_price integer ,"
            "is_paid BOOLEAN ,"
            "CONSTRAINT histories_pk PRIMARY KEY (id));")
conn.commit()

cur.execute("CREATE TABLE IF NOT EXISTS pre_medicines ( "
            "prescription_id integer ,"
            "medicine_id integer ,"
            "quantity integer ,"
            "CONSTRAINT pre_medicines_pk PRIMARY KEY (prescription_id, medicine_id));")
conn.commit()

cur.execute("CREATE TABLE IF NOT EXISTS pre_services ("
            "prescription_id integer ,"
            "service_id integer ,"
            "quantity integer ,"
            "CONSTRAINT pre_services_pk PRIMARY KEY (prescription_id, service_id));")
conn.commit()


cur.execute("CREATE TABLE IF NOT EXISTS salary_table (doctor_id integer ,"
            "which_month integer ,"
            "which_year integer ,"
            "num_patient integer, "
            "salary integer );")
conn.commit()






