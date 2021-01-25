from werkzeug.security import generate_password_hash, check_password_hash


class Manage:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# from app import login
#
# @login.user_loader
# def load_user(id):
#     return Manage.query.get(int(id))


def set_password(password):
    return generate_password_hash(password)


def check_password(password_hash, password):
    return check_password_hash(password_hash, password)


from app.db import connect


def update_data(sql):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql)
    print(sql)
    conn.commit()
    cur.close()
    conn.close()


def query_data(sql):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql)
    print(sql)
    rows = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return rows


def query_list_data(column_name, table_name, condition=None, order=None, group=None, having=None):
    conn = connect()
    cur = conn.cursor()
    sql = "SELECT " + column_name + " FROM " + table_name
    if condition:
        sql = "SELECT " + column_name + " FROM " + table_name + " WHERE " + condition
    elif order:
        sql = "SELECT " + column_name + " FROM " + table_name + \
              " ORDER BY " + order
    elif condition and order:
        sql = "SELECT " + column_name + " FROM " + table_name + \
              " WHERE " + condition + " ORDER BY " + order
    elif group and order:
        sql = "SELECT " + column_name + " FROM " + table_name + \
              " GROUP BY " + group + " ORDER BY " + order
    elif group and having and order:
        sql = "SELECT " + column_name + " FROM " + table_name + \
              " GROUP BY " + group + " HAVING " + having + " ORDER BY " + order
    print(sql)
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return rows


def query_medicines(medicine_id=None, medicine_name=None,
                    from_price=None, to_price=None, stock_quantity=None):
    rows = query_list_data('*', 'medicines', order='medicine_id ASC')
    if medicine_id:
        rows = query_list_data('*', 'medicines', 'medicine_id = ' + str(medicine_id))
    elif medicine_name:
        rows = query_list_data('*', 'medicines', 'medicine_name like \'%' + medicine_name + '%\'' +
                               ' or medicine_name ~ \'' + medicine_name.capitalize() + '\'')
    elif from_price and to_price:
        rows = query_list_data('*', 'medicines', 'unit_price>' + from_price + 'and unit_price<' + to_price)
    elif from_price:
        rows = query_list_data('*', 'medicines', 'unit_price>' + from_price)
    elif to_price:
        rows = query_list_data('*', 'medicines', 'unit_price<' + to_price)
    elif stock_quantity:
        rows = query_list_data('*', 'medicines', 'stock_quantity<=' + stock_quantity)
    return rows


def query_doctors(doctor_id=None, doctor_name=None):
    rows = query_list_data('*', 'doctors', order='doctor_id ASC')
    if doctor_id:
        rows = query_list_data('*', 'doctors', 'doctor_id = ' + str(doctor_id))
    elif doctor_name:
        tmp = doctor_name.title()
        print(tmp)
        rows = query_list_data('doctor_id, doctor_name', 'doctors', 'doctor_name like \'%' + doctor_name + '%\'' +
                               ' or doctor_name ~ \'' + tmp + '\'')
    return rows


def query_patients(patient_id=None, patient_name=None):
    rows = query_list_data('*', 'patients', order='patient_id ASC')
    if patient_id:
        rows = query_list_data('*', 'patients', 'patient_id = ' + str(patient_id))
    elif patient_name:
        rows = query_list_data('*', 'patients', 'patient_name like \'%' + patient_name + '%\'' +
                               ' or patient_name ~ \'' + patient_name.title() + '\'')
    return rows


def query_appointment(id=None, doctor_name=None, patient_name=None):
    rows = query_data("Select h.id, p.patient_name, d.doctor_name, h.date_time, h.disease_name, p.patient_id "
                      "from histories as h, doctors as d, patients as p "
                      "WHERE is_done = False and h.doctor_id = d.doctor_id "
                      "and h.patient_id = p.patient_id")
    if doctor_name:
        rows = query_data('Select h.id, p.patient_name, d.doctor_name, h.date_time, h.disease_name, p.patient_id '
                          'from histories as h, doctors as d, patients as p '
                          'WHERE (d.doctor_name like \'%' + doctor_name + '%\'' +
                          ' or d.doctor_name ~ \'' + doctor_name.title() + '\')' +
                          ' and is_done = False and h.doctor_id = d.doctor_id'
                          ' and h.patient_id = p.patient_id')
    elif patient_name:
        rows = query_data('Select h.id, p.patient_name, d.doctor_name, h.date_time, h.disease_name, p.patient_id  '
                          'from histories as h, doctors as d, patients as p '
                          'WHERE (p.patient_name like \'%' + patient_name + '%\'' +
                          ' or p.patient_name ~ \'' + patient_name.title() + '\')' +
                          ' and is_done = False and h.doctor_id = d.doctor_id'
                          ' and h.patient_id = p.patient_id')
    elif id:
        rows = query_data('Select h.id, p.patient_name, d.doctor_name, h.date_time, h.disease_name, p.patient_id '
                          'from histories as h, doctors as d, patients as p '
                          'where h.doctor_id = d.doctor_id and h.patient_id = p.patient_id and '
                          'is_done = False and h.id = ' + str(id))
    return rows


def query_salary(doctor_id=None, doctor_name=None, which_year=None, which_month=None):

    if doctor_id:
        rows = query_list_data(column_name='slr.doctor_id,d.doctor_name,which_month,which_year,num_patient,salary',
                               table_name='salary_table AS slr NATURAL JOIN doctors AS d',
                               condition='doctor_id = ' + str(doctor_id),
                               order='which_year,which_month,doctor_id ASC')
    elif doctor_name:
        rows = query_list_data(column_name='slr.doctor_id,d.doctor_name,which_month,which_year,num_patient,salary',
                               table_name='salary_table AS slr NATURAL JOIN doctors AS d',
                               condition='doctor_name like \'%' + doctor_name + '%\'',
                               order='which_year,which_month,doctor_id ASC')

    elif which_year and which_month:
        rows = query_list_data(column_name='slr.doctor_id,d.doctor_name,which_month,which_year,num_patient,salary',
                               table_name='salary_table AS slr NATURAL JOIN doctors AS d',
                               condition='which_year = ' + str(which_year) + ' and which_month = ' + str(which_month),
                               order='which_year,which_month,doctor_id ASC')
    elif which_year:
        rows = query_list_data(column_name='slr.doctor_id,d.doctor_name,which_month,which_year,num_patient,salary',
                               table_name='salary_table AS slr NATURAL JOIN doctors AS d',
                               condition='which_year = ' + str(which_year) + '',
                               order='which_year,which_month,doctor_id ASC')
    elif which_month:
        rows = query_list_data(column_name='slr.doctor_id,d.doctor_name,which_month,which_year,num_patient,salary',
                               table_name='salary_table AS slr NATURAL JOIN doctors AS d',
                               condition='which_month = ' + str(which_month) + '',
                               order='which_year,which_month,doctor_id ASC')
    else:
        rows = query_list_data('slr.doctor_id,d.doctor_name,which_month,which_year,num_patient,salary',
                               'salary_table AS slr NATURAL JOIN doctors AS d', None,
                               'which_year,which_month,doctor_id ASC')
    return rows


def query_income(which_month=None, which_year=None):
    rows = query_data('select EXTRACT(year from date_time),EXTRACT(month from date_time),'
                      'SUM(medicine_fee),SUM(treatment_fee),SUM(total_price) '
                      'from histories '
                      'group by EXTRACT(year from date_time), EXTRACT(month from date_time)'
                      ' order by  EXTRACT(year from date_time), EXTRACT(month from date_time) ASC')

    if which_year and which_month:
        rows = query_data('select EXTRACT(year from date_time),EXTRACT(month from date_time),'
                          'SUM(medicine_fee),SUM(treatment_fee),SUM(total_price) '
                          'from histories '
                          'group by EXTRACT(year from date_time), EXTRACT(month from date_time) '
                          'having EXTRACT(year from date_time) = ' + str(which_year) +
                          ' and EXTRACT(month from date_time) = ' + str(which_month))
    elif which_year:
        rows = query_data('select EXTRACT(year from date_time) ,'
                          'SUM(medicine_fee),SUM(treatment_fee),SUM(total_price) '
                          'from histories '
                          'group by EXTRACT(year from date_time)  '
                          'having EXTRACT(year from date_time) = ' + str(which_year))
    return rows


def query_expense(which_month=None, which_year=None):
    rows = query_list_data(column_name='doctor_id,doctor_name,which_year,which_month,salary',
                           table_name='salary_table NATURAL JOIN doctors',
                           order='doctor_id ASC')

    if which_month and which_year:
        rows = query_list_data(column_name='doctor_id,doctor_name,which_year,which_month,salary',
                               table_name='salary_table NATURAL JOIN doctors',
                               condition='which_year = ' + str(which_year) + 'and which_month = ' + str(which_month),
                               order='doctor_id ASC')
    elif which_year:
        rows = query_list_data(column_name='doctor_id,doctor_name,which_year,which_month,salary',
                               table_name='salary_table NATURAL JOIN doctors',
                               condition='which_year = ' + str(which_year),
                               order='doctor_id ASC')
    return rows



