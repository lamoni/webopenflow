from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class AddFlowForm(Form):
    flow_node = StringField('flow_node')
    flow_id = StringField('flow_id')
    flow_priority = StringField('flow_priority')
    flow_input_port = StringField('flow_input_port')
    flow_output_port = StringField('flow_output_port')

class RemoveFlowForm(Form):
    flow_key = StringField('flow_key')