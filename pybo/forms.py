from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class QuestionForm(FlaskForm):
    subject = StringField('입력오류', validators=[DataRequired('제목을 입력해 주세요')])
    content = TextAreaField('입력오류', validators=[DataRequired('질문내용을 입력해 주세요')])


class AnswerForm(FlaskForm):
    content = TextAreaField('입력오류', validators=[DataRequired('답변내용을 입력해 주세요')])


class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[
        DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField(
        '비밀번호', validators=[DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다.')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])


class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[
        DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])


class CommentForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired()])
