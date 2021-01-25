from app import app
from flask import render_template, Response
from flask import request, flash, redirect, url_for
from app.db import connect
from app.models import query_data
import datetime
from datetime import date
today = date.today()


@app.route('/hhh')
def hello_world():
    return "Hello world"


@app.route("/hello")
def hello_user():
    return render_template('menu.html')


# from flask_login import current_user, login_user

from app.forms import RegistrationForm
@app.route('/register', methods=['GET', 'POST'])
def register():
    # if current_user.is_authenticated:
    #     return redirect(url_for('hello_user'))
    form = RegistrationForm()
    conn = connect()
    cur = conn.cursor()
    if form.validate():
        password_hash = set_password(form.password.data)

        rows = query_list_data('*', 'managers', 'username = \'' + form.username.data + '\'')
        if len(rows) != 0:
            flash("The username is valid.")
            return redirect(url_for('register'))

        cur.execute("INSERT INTO managers (username, email, password) VALUES (%s, %s, %s)",
                    (form.username.data, form.email.data, password_hash))
        conn.commit()
        cur.close()
        conn.close()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('registration.html', title='Add new manage', form=form)

@app.route('/logout')
def logout():
    return render_template('logout.html')

from app.forms import LoginForm
from app.models import set_password, check_password
# from flask_login import current_user, login_user

# from app.models import Manage
@app.route('/', methods=['GET', 'POST'])
def login():
    # is_authenticated to check if a user login successful ?
    # if current_user.is_authenticated:
    #     return redirect(url_for('hello_user'))
    # input username and password to login
    form = LoginForm()
    if form.is_submitted():

        # filter_by :  return objects whose username values match the username we used
        # first() : return unique result. all() : all query matching
        user_name = request.form.get('username')
        flash("Login from user {}".format(form.username.data))
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM managers WHERE username = (%s);", (user_name,))
        rows = cur.fetchone()


        if len(rows) == 0 or not check_password(rows[3], form.password.data):
            flash('Invalid username or password')
            conn.commit()
            cur.close()
            conn.close()
            return redirect(url_for('login'))
        # manage = Manage(rows[0], user_name)
        # login_user(manage, remember=form.remember_me.data)
        # accept information and redirect to next page
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('hello_user'))

    return render_template('login.html', form=form)


from app.models import query_list_data
from app.models import query_medicines


@app.route('/manages/list', methods=['GET'])
def manages_page():
    rows = query_list_data('*', 'manages')
    result = [{"username": row[1], "email": row[2] } for row in rows]
    return {"List manage": result}


@app.route("/medicines", methods=["GET", "POST"])
def medicine_page():
    medicine_id = request.args.get("medicine_id")
    medicine_name = request.args.get("medicine_name")
    from_price = request.args.get("from_price")
    to_price = request.args.get("to_price")
    stock_quantity = request.args.get("stock_quantity")

    rows = query_medicines(medicine_id, medicine_name,
                           from_price, to_price, stock_quantity)
    medicines = [{"medicine_id": row[0],
                  "medicine_name": row[1],
                  "unit_price": row[2],
                  "stock_quantity": row[3]} for row in rows]
    return render_template('medicine.html', medicines=medicines, url=url_for('insert_new_medicine'))


from app.forms import MedicineInsertForm


@app.route("/medicines/add", methods=['GET', 'POST'])
def insert_new_medicine():
    form = MedicineInsertForm()
    if form.is_submitted():
        conn = connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO medicines (medicine_name, unit_price, stock_quantity ) "
                    "VALUES (%s, %s, %s)",
                    (form.medicine_name.data, form.unit_price.data, form.stock_quantity.data))
        conn.commit()
        cur.close()
        conn.close()
        flash("Success.")
        return redirect(url_for('medicine_page'))
    return render_template('medicine_insert.html', form=form)


from app.forms import MedicineUpdateForm


@app.route('/medicines/<int:medicine_id>', methods=['GET', 'POST'])
def medicine_update(medicine_id):
    rows = query_medicines(medicine_id=medicine_id)
    print(rows)
    form = MedicineUpdateForm(request.form)
    form.medicine_name.data = rows[0][1]
    form.unit_price.data = rows[0][2]
    form.stock_quantity.data = rows[0][3]
    if request.method == 'POST' and form.is_submitted():
        conn = connect()
        cur = conn.cursor()
        print(form.medicine_name.data, form.unit_price.data, medicine_id)
        cur.execute("UPDATE medicines SET medicine_name = (%s), unit_price = (%s), stock_quantity = (%s) "
                    "WHERE medicine_id  = (%s)",
                    (request.form['medicine_name'], request.form['unit_price'],
                     request.form['stock_quantity'], medicine_id))
        conn.commit()
        cur.close()
        conn.close()
        flash("Success.")
        return redirect(url_for('medicine_page'))
    return render_template('medicine_update.html', form=form)


@app.route("/services", methods=["GET", "POST"])
def service_page():
    service_name = request.args.get("service_name")
    print(service_name)

    if service_name:
        rows = query_list_data('*', 'services', 'service_name like \'%' + service_name + '%\'')
    else:
        rows = query_list_data('*', 'services')
    services = [{"service_id": row[0],
                 "service_name": row[1],
                 "price": row[2]} for row in rows]
    return render_template('service.html', services=services)


from app.models import query_doctors
@app.route("/doctors", methods=["GET", "POST"])
def doctor_page():
    doctor_name = request.args.get("doctor_name")

    rows = query_doctors(doctor_name=doctor_name)
    doctors = [{"doctor_id": row[0],
                "doctor_name": row[1],
                "is_work": row[7]} for row in rows]
    return render_template('doctor.html', doctors=doctors)


@app.route('/doctors/<int:doctor_id>')
def doctor_detail(doctor_id):
    rows = query_doctors(doctor_id=doctor_id)
    print(len(rows))
    print(rows)
    d = {"doctor_id": rows[0][0],
         "doctor_name": rows[0][1],
         "phone_number": rows[0][2],
         "day_off": rows[0][3],
         "description": rows[0][5]
         }
    print(d)
    return render_template('doctor_detail.html', d=d)


from app.forms import DoctorInsertForm
@app.route("/doctors/add", methods=['GET', 'POST'])
def insert_new_doctor():
    form = DoctorInsertForm()
    if form.is_submitted():
        conn = connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO doctors (doctor_name,phone_number,day_off,password,description,is_manager) "
                    "VALUES (%s, %s, %s, %s, %s, %s)",
                    (form.doctor_name.data, form.phone_number.data, form.day_off.data,
                     form.password.data, form.description.data, form.is_manage.data))
        conn.commit()
        cur.close()
        conn.close()
        flash("Success.")
        return redirect(url_for('doctor_page'))
    return render_template('doctor_insert.html', form=form)


from app.forms import DoctorUpdateForm
@app.route('/doctors/update/<int:doctor_id>', methods=['GET', 'POST'])
def doctor_update(doctor_id):
    rows = query_doctors(doctor_id=doctor_id)
    print(rows)
    form = DoctorUpdateForm(request.form)
    form.doctor_name.data = rows[0][1]
    form.phone_number.data = rows[0][2]
    form.description.data = rows[0][5]
    form.is_work.data = rows[0][7]
    if request.method == 'POST' and form.is_submitted():
        conn = connect()
        cur = conn.cursor()
        cur.execute("UPDATE doctors SET doctor_name = (%s), phone_number = (%s), "
                    "description = (%s), is_work = (%s) "
                    "WHERE doctor_id  = (%s)",
                    (request.form['doctor_name'], request.form['phone_number'],
                     request.form['description'], request.form['is_work'], doctor_id))
        conn.commit()
        cur.close()
        conn.close()
        flash("Success.")
        return redirect(url_for('doctor_detail', doctor_id=doctor_id))
    return render_template('doctor_update.html', form=form)


from app.models import query_salary
@app.route('/doctors/salary', methods=["GET", "POST"])
def doctor_salary():
    doctor_name = request.args.get("doctor_name")
    month = request.args.get("which_month")
    year = request.args.get("which_year")
    print(month == None)
    print(month)
    print(type(month))

    rows = query_salary(doctor_name=doctor_name, which_year=year, which_month=month)
    doctors = [{"doctor_id": row[0],
                "doctor_name": row[1],
                "which_month": row[2],
                "which_year": row[3],
                "num_patient": row[4],
                "salary": row[5]} for row in rows]
    return render_template('doctor_salary.html', doctors=doctors)


from app.models import query_patients
@app.route('/patients')
def patient_page():
    patient_name = request.args.get("patient_name")

    rows = query_patients(patient_name=patient_name)
    patients = [{"patient_id": row[0],
                 "patient_name": row[1],
                 "birthday": row[2],
                 "gender": row[3],
                 "phone_number": row[4]} for row in rows]
    return render_template('patient.html', patients=patients)


@app.route('/patients/<int:patient_id>')
def patient_detail(patient_id):
    rows = query_patients(patient_id=patient_id)
    patients = {"patient_id": rows[0][0],
                "patient_name": rows[0][1]}

    rows = query_data('SELECT d.doctor_name, disease_name, total_price,'
                      ' treatment_fee, medicine_fee, h.id, date_time, is_paid, is_done, h.doctor_id'
                      ' from histories as h, doctors as d '
                      ' where h.patient_id = ' + str(patient_id) +
                      ' and (h.doctor_id = d.doctor_id)')
    pres = [{"doctor_name": row[0],
             "disease_name": row[1],
             "total_price": row[2],
             "treatment_fee": row[3],
             "medicine_fee": row[4],
             "id": row[5],
             "date": row[6],
             "is_paid": row[7],
             "is_done": row[8],
             "doctor_id": row[9]} for row in rows]
    # list medicines
    rows = query_data('SELECT pm.prescription_id, medicine_name, pm.quantity , m.unit_price'
                      ' from medicines as m, histories as h, pre_medicines as pm '
                      ' where h.patient_id = ' + str(patient_id) +
                      ' and (m.medicine_id = pm.medicine_id) '
                      ' and (pm.prescription_id = h.id)')
    # print('rows1 = ', rows)
    for i in range(len(pres)):
        pres[i]['medicine_name'] = []
        for j in range(len(rows)):
            if pres[i]['id'] == rows[j][0]:
                pres[i]['medicine_name'].append((rows[j][1], rows[j][2], rows[j][3]))
        if len(pres[i]['medicine_name']) == 0:
            pres[i]['medicine_name'] = 0
    # list services
    rows = query_data('SELECT ps.prescription_id, service_name, ps.quantity , s.price '
                      ' from services as s, histories as h, pre_services as ps '
                      ' where h.patient_id = ' + str(patient_id) +
                      ' and (s.service_id = ps.service_id) '
                      ' and (ps.prescription_id = h.id)')
    # print('rows2 = ', rows)
    for i in range(len(pres)):
        pres[i]['service_name'] = []
        for j in range(len(rows)):
            if pres[i]['id'] == rows[j][0]:
                pres[i]['service_name'].append((rows[j][1], rows[j][2], rows[j][3]))
        if len(pres[i]['service_name']) == 0:
            pres[i]['service_name'] = 0
    return render_template('patient_detail.html', d=patients, pres=pres)


from app.models import update_data


@app.route('/patients/<int:patient_id>/<int:id>')
def prescription_paid(patient_id, id):
    update_data("Update histories set is_paid = True where id = " + str(id))
    return redirect(url_for('patient_detail', patient_id=patient_id))


from app.forms import NewPatientForm


@app.route("/patients/add", methods=['GET', 'POST'])
def insert_new_patient():
    form = NewPatientForm()
    if form.is_submitted():
        conn = connect()
        cur = conn.cursor()
        if form.gender.data == 'Nam':
            gender = 'F'
        else:
            gender = 'M'
        print(form.birthday.data)
        cur.execute("INSERT INTO patients (patient_name,birthday, gender, phone_number) "
                    "VALUES (%s, %s, %s, %s)",
                    (form.patient_name.data, form.birthday.data,
                     gender, form.phone_number.data))
        conn.commit()
        cur.close()
        conn.close()
        flash("Success.")
        return redirect(url_for('patient_page'))
    return render_template('patient_insert.html', form=form)


import json


@app.route('/_autocomplete', methods=['GET'])
def autocomplete():
    data = [row[0] for row in query_list_data("medicine_name", "medicines", condition="stock_quantity > 0")]
    print(data)
    return Response(json.dumps(data), mimetype='application/json')


def findDay(date):
    dow = datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
    return dow+2


def check_doctor(doctor_id, date_time):
    rows = query_data('Select * from histories '
                      ' where is_done = False and doctor_id = ' + str(doctor_id) + \
                      ' and date_time = \'' + str(date_time) + '\'')
    if len(rows) >= 2:
        return 1
    rows = query_data('Select day_off from doctors where doctor_id = ' + str(doctor_id))[0][0]
    dow = findDay(str(date_time))  # day of week
    print(rows)
    print(dow)
    for i in rows:
        if dow == int(i):
            return 2
    return 0


from app.forms import HistoriesForm
@app.route("/patients/add/<int:patient_id>&&<string:action>", methods=['GET', 'POST'])
def histories_insert(patient_id, action):
    print(action)
    rows = query_patients(patient_id=patient_id)
    form = HistoriesForm()
    form.patient_name.data = rows[0][1]
    form.doctor_name.choices = [""] + [row[0] for row in query_list_data("doctor_name", "doctors",
                                                                         condition="is_work = True")]

    if form.is_submitted():

        doctor_name = form.doctor_name.data
        note = form.note.data
        doctor_id = query_doctors(doctor_name=doctor_name)[0][0]

        print(doctor_id, patient_id, note)
        if action == 'new_pre':
            date_time = today.strftime("%Y-%m-%d")
            is_done = True
        else:
            date_time = request.form['date_time']
            is_done = False
        status = check_doctor(doctor_id=doctor_id, date_time=date_time)
        if status == 1:
            flash('Bác sĩ ' + doctor_name + ' đã có quá số bệnh nhân cho phép vào ngày ' + date_time)
            flash('Mời chọn bác sĩ khác.')
            return redirect(url_for('histories_insert', patient_id=patient_id, action=action))
        elif status == 2:
            flash('Bác sĩ ' + doctor_name + ' không làm việc vào ngày này. ')
            flash('Mời chọn bác sĩ khác.')
            return redirect(url_for('histories_insert', patient_id=patient_id, action=action))

        # insert into table histories
        conn = connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO histories (doctor_id, patient_id, disease_name, "
                    "treatment_fee, medicine_fee, total_price, "
                    "date_time, is_done, is_paid ) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (doctor_id, patient_id, note, 0, 0, 0, date_time, is_done, False))
        conn.commit()
        cur.close()
        conn.close()
        flash("Success.")
        return redirect(url_for('patient_detail', patient_id=patient_id))
    return render_template('histories_insert.html', form=form, flag='insert')


from app.models import query_appointment


@app.route("/appointments", methods=["GET", "POST"])
def appointment_page():
    patient_name = request.args.get("patient_name")
    doctor_name = request.args.get("doctor_name")

    rows = query_appointment(doctor_name=doctor_name, patient_name=patient_name)
    if len(rows) == 0:
        appointments = 0
    else:
        appointments = [{"id": row[0],
                         "patient_name": row[1],
                         "doctor_name": row[2],
                         "date_time": row[3],
                         "note": row[4],
                         "patient_id": row[5]} for row in rows]
    return render_template('appointment.html', appointments=appointments)


@app.route("/patients/update/<int:patient_id>/<int:id>", methods=['GET', 'POST'])
def histories_update(patient_id, id):
    rows = query_appointment(id=id)[0]
    print(rows)
    form = HistoriesForm()
    form.patient_name.data = rows[1]
    form.doctor_name.data = rows[2]
    form.doctor_name.choices = [""] + [row[0] for row in query_list_data("doctor_name", "doctors")]
    # temp = rows[3].strftime('%Y-%m-%d')
    # print(rows[3], type(rows[3]))
    # print(temp, type(temp))
    # temp = datetime.strptime(temp, '%Y-%m-%d')
    # print(temp, type(temp))
    form.date_time.data = rows[3]
    form.note.data = rows[4]

    if form.is_submitted():
        doctor_name = request.form['doctor_name']
        doctor_id = query_doctors(doctor_name=doctor_name)[0][0]
        date_time = request.form['date_time']
        note = request.form['note']
        status = check_doctor(doctor_id=doctor_id, date_time=date_time)
        if status == 1:
            flash('Bác sĩ ' + doctor_name + ' đã có quá số bệnh nhân cho phép vào ngày ' + date_time)
            flash('Mời chọn bác sĩ khác.')
            return redirect(url_for('histories_update', patient_id=patient_id, id=id))
        elif status == 2:
            flash('Bác sĩ ' + doctor_name + ' không làm việc vào ngày này. ')
            flash('Mời chọn bác sĩ khác.')
            return redirect(url_for('histories_update', patient_id=patient_id, id=id))
        update_data('Update histories set doctor_id = ' + str(doctor_id) + ', date_time = \'' + date_time +
                    '\', disease_name = \'' + note + '\' '
                    ' WHERE id = ' + str(id))
        return redirect(url_for('patient_detail', patient_id=patient_id))

    return render_template('histories_insert.html', form=form, flag='update')


from app.forms import NoteForm
@app.route("/patients/update_note/<int:patient_id>&&<int:id>", methods=['GET', 'POST'])
def prescription_note_update(patient_id, id):
    rows = query_data('Select disease_name from histories '
                      'where id = ' + str(id))[0]
    form = NoteForm()
    form.note.data = rows[0]
    if form.is_submitted():
        note = request.form['note']
        update_data('Update histories SET disease_name = \'' + note +
                    '\' WHERE id = ' + str(id))
        return redirect(url_for('patient_detail', patient_id=patient_id))
    return render_template('pres_note_update.html', form=form, id=id)


def cal_total_price(id, medicine_fee=0, treatment_fee=0):
    # total_price = query_data("SELECT total_price from histories WHERE id = " + str(id))[0][0]
    # if total_price is None:
    #     total_price = 0
    # total_price += medicine_fee
    # total_price += treatment_fee
    # update_data("UPDATE histories SET total_price = " + str(total_price) + "WHERE id = " + str(id))
    update_data('UPDATE histories SET total_price = (SELECT (medicine_fee+treatment_fee) '
                'FROM histories WHERE id = ' + str(id) + ') where id = ' + str(id))


@app.route("/patients/confirm/<int:patient_id>&&<int:id>&&<int:doctor_id>", methods=['GET', 'POST'])
def histories_confirm(patient_id, id, doctor_id):
    update_data("UPDATE histories SET is_done = 'True' WHERE id = " + str(id))
    return redirect(url_for('patient_detail', patient_id=patient_id))


from app.forms import PresMedicineUpdateForm


@app.route("/patients/update_me/<int:patient_id>&&<int:id>", methods=['GET', 'POST'])
def prescription_medicine_update(patient_id, id):
    form = PresMedicineUpdateForm(request.form)

    if form.is_submitted():
        conn = connect()
        cur = conn.cursor()
        medicine_name = []
        medicine_quantity = []
        # medicine_fee = 0

        for key in request.form:
            if key.startswith('medicine'):
                id_ = key.partition('.')[-1]
                value = request.form[key]
                medicine_name.append(value)
            if key.startswith('quantity'):
                id_ = key.partition('.')[-1]
                value = request.form[key]
                medicine_quantity.append(value)
        print(medicine_name, medicine_quantity)
        if len(medicine_name) != 0:
            for (m, q) in zip(medicine_name, medicine_quantity):
                if m != '':
                    row = query_medicines(medicine_name=m)[0]
                    medicine_id = row[0]
                    # insert vào table pre_medicines
                    cur.execute("INSERT INTO pre_medicines (prescription_id, medicine_id, quantity)"
                                "VALUES (%s, %s, %s)",
                                (id, medicine_id, q))
                    if len(conn.notices) != 0:
                        flash('Không đủ số lượng thuốc ' + m + ' trong kho')
                        conn.commit()
                        cur.close()
                        conn.close()
                        return redirect(url_for('prescription_medicine_update', patient_id=patient_id, id=id))
                    # row[2] is medicine price, q is quantity
                    # medicine_fee += int(q) * int(row[2])
            # update_data("UPDATE histories SET medicine_fee = " + str(medicine_fee) + 'WHERE id = ' + str(id))
            conn.commit()
            cur.close()
            conn.close()
            update_data('UPDATE histories SET medicine_fee = (SELECT SUM (m.unit_price * pm.quantity) '
                        ' FROM medicines as m, pre_medicines as pm, histories as h '
                        ' WHERE pm.prescription_id = h.id and h.id = ' + str(id) +
                        ' and m.medicine_id = pm.medicine_id ) '
                        ' WHERE id = ' + str(id))
            cal_total_price(id=id)
        return redirect(url_for('patient_detail', patient_id=patient_id))
    return render_template('pres_medicine_update.html', form=form, id=id)


from app.forms import PresServiceUpdateForm


@app.route("/patients/update_se/<int:patient_id>&&<int:id>", methods=['GET', 'POST'])
def prescription_service_update(patient_id, id):
    form = PresServiceUpdateForm(request.form)
    form.service_name.choices = [""] + [row[0] for row in query_list_data("service_name", "services")]
    form.service_name_1.choices = form.service_name.choices
    if form.is_submitted():
        conn = connect()
        cur = conn.cursor()
        service_name = []
        service_quantity = []

        for key in request.form:
            if key.startswith('service'):
                id_ = key.partition('.')[-1]
                value = request.form[key]
                service_name.append(value)
            if key.startswith('quantity'):
                id_ = key.partition('.')[-1]
                value = request.form[key]
                service_quantity.append(value)
        print(service_name, service_quantity)
        for (s, q) in zip(service_name, service_quantity):
            if q != '':
                row = query_list_data('*', 'services', 'service_name = \'' + s + '\'')[0]
                service_id = row[0]
                # insert vào table pre_medicines
                cur.execute("INSERT INTO pre_services (prescription_id, service_id, quantity)"
                            "VALUES (%s, %s, %s)",
                            (id, service_id, q))
                # row[2] là service price q is quantity
                # treatment_fee += int(q) * int(row[2])
        conn.commit()
        cur.close()
        conn.close()
        # update_data("UPDATE histories SET treatment_fee = " + str(treatment_fee) + 'WHERE id = ' + str(id))
        update_data('UPDATE histories SET treatment_fee = (SELECT SUM( s.price * ps.quantity) '
                        ' FROM services as s, pre_services as ps, histories as h '
                        ' WHERE ps.prescription_id = h.id and h.id = ' + str(id) +
                        ' and s.service_id = ps.service_id ) '
                        ' WHERE id = ' + str(id))
        cal_total_price(id=id)

        return redirect(url_for('patient_detail', patient_id=patient_id))
    return render_template('pres_service_update.html', form=form, id=id)


@app.route('/demo', methods=['GET', 'POST'])
def demo():
    form = PresMedicineUpdateForm(request.form)
    id = 12
    if form.is_submitted():
        conn = connect()
        cur = conn.cursor()
        medicine_name = form.medicine_name.data
        medicine_quantity = form.quantity.data

        row = query_medicines(medicine_name=medicine_name)[0]
        medicine_id = row[0]
        print(conn.notices)

        # insert vào table pre_medicines
        cur.execute("INSERT INTO pre_medicines (prescription_id, medicine_id, quantity)"
                    "VALUES (%s, %s, %s)",
                    (id, medicine_id, medicine_quantity))
        print(conn.notices)
        if len(conn.notices) != 0:
            flash('Not enough quantity')
            conn.commit()
            cur.close()
            conn.close()
            return redirect(url_for('demo'))
        medicine_fee = medicine_quantity * int(row[2])
        update_data("UPDATE histories SET medicine_fee = " + str(medicine_fee) + 'WHERE id = ' + str(id))
        cal_total_price(id=id, medicine_fee=medicine_fee)
        conn.commit()
        cur.close()
        conn.close()
        return 'success'
    return render_template('pres_medicine_update.html', form=form, id=id)


from app.models import query_income, query_expense
@app.route('/income_expense',methods = ["GET","POST"])
def income_expense():
    month2 = request.args.get("which_month")
    year2 = request.args.get("which_year")
    rows1 = query_income(which_month=month2, which_year=year2)

    income = []
    try:
        income = [{"Year": row1[0],
                   "Month": row1[1],
                   "SUM(medicine_fee)": row1[2],
                   "SUM(treatment_fee)": row1[3],
                   "SUM(total_price)": row1[4]} for row1 in rows1]
    except IndexError:
        if year2:
            income = [{"Year": row1[0],
                       "SUM(medicine_fee)": row1[1],
                       "SUM(treatment_fee)": row1[2],
                       "SUM(total_price)": row1[3]} for row1 in rows1]

    """
    income is a list of dictionary --> if month2 and year2 != None then return income as a list having ONLY 1 dictionary.
    That is income[0]. To access the data in dictionary. income[0]['SUM(medicine_fee)']
    """
    rows2 = query_expense(which_month=month2, which_year=year2)
    expense = [{"doctor_id": row2[0],
                "doctor_name": row2[1],
                "which_year": row2[2],
                "which_month": row2[3],
                "salary": row2[4]} for row2 in rows2]

    if (month2 == None or year2 == None):
        total_salary = 0
    else:
        total_salary = sum([i['salary'] for i in expense])
    return render_template('income_expense.html', income=income, expense=expense, total_salary=total_salary)