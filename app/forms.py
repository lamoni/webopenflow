from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class AddFlowForm(Form):
    flow_name = StringField('flow_name') #, validators=[DataRequired()])
    flow_id = StringField('flow_id')
    flow_priority = StringField('flow_priority')
    flow_destination_prefix = StringField('flow_destination_prefix')
    flow_table_id = StringField('flow_table_id')
