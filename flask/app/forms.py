from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, SelectField, SubmitField,
                     BooleanField, DateField, DateTimeField, DecimalField,
                     FieldList )
from wtforms.validators import DataRequired, Length
"""
  Defines the WTForms forms used by the app

"""
#from ..config import my_config

class PolicyForm(FlaskForm):
    """Policy form for creating a new policy."""
    name = StringField(
        'Name',
        [DataRequired()]
    )

    fromzone = SelectField(
        'From Zone', 
        choices=[('cpp', 'C++'), ('py', 'Python'), 
                ('text', 'Plain Text')])  # Dummy values that will be set later to list zones

    tozone = SelectField(
        'To Zone', 
        choices=[('Dummy Zone1', 'Zone1'), ('Dummy Zone 2', 'Zone2'), 
                ('Dummy Zone 3', 'Zone3')])  # Dummy values that will be set later to list zones

    match_source = SelectField(
        'source-address',
        choices=[('src host1', 'host1'), ('src host2', 'host2')]
    )

    match_dest = SelectField(
        'destination-address',
        choices=[('dst host1', 'host1'), ('dst host2', 'host2')]
    )

    srcAddrs = FieldList(StringField("source-address"), min_entries=1, max_entries=5)
    dstAddrs = FieldList(StringField("destination-address"), min_entries=1, max_entries=5)


    submit = SubmitField('Submit')

class NewAppForm(FlaskForm):
    """New Application form."""
    name = StringField(
        'Name',
        [DataRequired()]
    )

    fromzone = SelectField(
        'Programming Language', 
        choices=[('cpp', 'C++'), ('py', 'Python'), 
                ('text', 'Plain Text')])

    email = StringField(
        'Email',
        [
            DataRequired()
        ]
    )
    body = TextAreaField(
        'Message',
        [
            DataRequired(),
            Length(min=4,
            message=('Your message is too short.'))
        ]
    )

    submit = SubmitField('Submit')

class ContactForm(FlaskForm):
    """Contact form."""
    name = StringField(
        'Name',
        [DataRequired()]
    )

    fromzone = SelectField(
        'Programming Language', 
        choices=[('cpp', 'C++'), ('py', 'Python'), 
                ('text', 'Plain Text')])

    email = StringField(
        'Email',
        [
            DataRequired()
        ]
    )
    body = TextAreaField(
        'Message',
        [
            DataRequired(),
            Length(min=4,
            message=('Your message is too short.'))
        ]
    )

    submit = SubmitField('Submit')

class BasicFieldsForm(FlaskForm):
    """
    Form with all the basic fields.
    """
    
    name = StringField(
        'Name',
        [DataRequired()]
    )

    my_boolean = BooleanField(
        'BooleanField'
    )

    my_date = DateField(
        'DateField',
        [DataRequired()]
    )

    my_datetime = DateTimeField(
        'DateTimeField',
        [DataRequired()]
    )

    my_decimal = DecimalField(
        'DecimalField',
        [DataRequired()]
    )

    fromzone = SelectField(
        'Programming Language', 
        choices=[('cpp', 'C++'), ('py', 'Python'), 
                ('text', 'Plain Text')])

    email = StringField(
        'Email',
        [
            DataRequired()
        ]
    )
    body = TextAreaField(
        'Message',
        [
            DataRequired(),
            Length(min=4,
            message=('Your message is too short.'))
        ]
    )

    submit = SubmitField('Submit')
