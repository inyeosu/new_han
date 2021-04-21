from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class QuestionForm(FlaskForm):
    subject = StringField('입력오류', validators=[DataRequired('제목을 입력해 주세요')])
    content = TextAreaField('입력오류', validators=[DataRequired('질문내용을 입력해 주세요')])


class AnswerForm(FlaskForm):
    content = TextAreaField('입력오류', validators=[DataRequired('답변내용을 입력해 주세요')])
