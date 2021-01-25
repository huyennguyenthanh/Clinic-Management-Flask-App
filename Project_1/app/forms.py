from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms import SelectField, DateField, TextAreaField, DateTimeField, FieldList, FormField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Email


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


class MedicineInsertForm(FlaskForm):
    medicine_name = StringField('Input medicine_name', validators=[DataRequired()])
    unit_price = IntegerField('Input unit_price', validators=[DataRequired()])
    stock_quantity = IntegerField('Input quantity', validators=[DataRequired()])
    submit = SubmitField('Confirm')


class MedicineSearch(FlaskForm):
    medicine_name = StringField('Input medicine_name', validators=[DataRequired()])
    submit = SubmitField('search')


class MedicineUpdateForm(FlaskForm):
    medicine_name = StringField('Cập nhật thông tin thuốc', validators=[DataRequired()])
    unit_price = IntegerField('Cập nhật giá thuốc', validators=[DataRequired()])
    stock_quantity = IntegerField('Cập nhật số lượng tồn kho', validators=[DataRequired()])
    submit = SubmitField('Confirm')


class DoctorInsertForm(FlaskForm):
    doctor_name = StringField('Tên bác sĩ', validators=[DataRequired()])
    phone_number = StringField('Số điện thoại ', validators=[DataRequired()])
    description = TextAreaField('Tiểu sử bác sĩ ', validators=[])
    day_off = StringField('Ngày nghỉ cố định ', validators=[DataRequired()])
    password = StringField('Đặt mật khẩu cho tài khoản ', validators=[DataRequired()])
    is_manage = BooleanField('Có phải là quản lí không ? ')
    submit = SubmitField('Confirm')


class DoctorUpdateForm(FlaskForm):
    doctor_name = StringField('Tên bác sĩ', validators=[DataRequired()])
    phone_number = StringField('Số điện thoại ', validators=[DataRequired()])
    day_off = StringField('Cập nhật ngày nghỉ cố định ', validators=[DataRequired()])
    description = TextAreaField('Cập nhật tiểu sử bác sĩ ', validators=[DataRequired()])
    is_work = BooleanField('Tình trạng làm việc ', validators=[DataRequired()])
    submit = SubmitField('Confirm')


class NewPatientForm(FlaskForm):
    patient_name = StringField('Tên bệnh nhân', validators=[DataRequired()])
    birthday = DateField("Ngày sinh", validators=[DataRequired()], format="%Y-%m-%d")
    gender = SelectField('Giới tính ', choices=['Nam', 'Nữ'])
    phone_number = StringField("Số điện thoại ",  validators=[DataRequired()])
    submit = SubmitField('Confirm')


class HistoriesForm(FlaskForm):
    patient_name = StringField('Nhập tên bênh nhân ', validators=[DataRequired()])
    doctor_name = SelectField('Bác sĩ kê đơn ', validators=[DataRequired()])
    note = TextAreaField('Nhập ghi chú/chẩn đoán ', validators=[DataRequired()])
    date_time = DateTimeField("Chọn ngày giờ", validators=[DataRequired()], format='%Y-%m-%d%H:%M:%S')
    submit = SubmitField('Confirm')


class NoteForm(FlaskForm):
    note = TextAreaField('Cập nhật ghi chú và chẩn đoán', validators=[DataRequired()])
    submit = SubmitField('Confirm')


class PresMedicineUpdateForm(FlaskForm):
    medicine_name = StringField('Thuốc được kê', id='medicine_autocomplete')
    quantity = IntegerField('Số lượng ', validators=[DataRequired()])
    medicine_name_1 = StringField('Thuốc được kê', id='medicine1_autocomplete')
    quantity_1 = IntegerField('Số lượng ', validators=[DataRequired()])
    medicine_name_2 = StringField('Thuốc được kê', id='medicine2_autocomplete')
    quantity_2 = IntegerField('Số lượng ', validators=[DataRequired()])
    medicine_name_3 = StringField('Thuốc được kê', id='medicine3_autocomplete')
    quantity_3 = IntegerField('Số lượng ', validators=[DataRequired()])

    submit = SubmitField('Confirm')


class PresServiceUpdateForm(FlaskForm):
    service_name = SelectField('Dịch vụ đã sử dụng ', validators=[DataRequired()])
    quantity = IntegerField('Số lượng ', validators=[DataRequired()])
    service_name_1 = SelectField('Dịch vụ đã sử dụng ', validators=[DataRequired()])
    quantity_1 = IntegerField('Số lượng ', validators=[DataRequired()])
    submit = SubmitField('Confirm')



