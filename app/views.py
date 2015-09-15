from flask import render_template, flash, redirect
from app import config
from app import app
from .forms import AddFlowForm
import requests
import pprint

@app.route('/')
@app.route('/index')
def index():
    headers = {
        'accept': 'application/json',
        'content-type': 'application/xml'
    }

    r = requests.get('http://192.168.229.133:8181/restconf/config/opendaylight-inventory:nodes/', headers=headers, auth=('admin', 'admin'))

    return render_template('index.html', page_title='Dashboard', panel_title='Flows', flows_data=r.json())


@app.route('/add_flow', methods=['GET'])
def add_flow():
    form = AddFlowForm()

    return render_template('add_flow.html', page_title='Add Flow', panel_title='Form', form=form)


@app.route('/api/add_flow', methods=['POST'])
def api_add_flow():
    form = AddFlowForm()

    if form.validate_on_submit():
        xml = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
                <flow xmlns="urn:opendaylight:flow:inventory">
                    <priority>%s</priority>
                    <match>
                        <ethernet-match>
                            <ethernet-type>
                                <type>2048</type>
                            </ethernet-type>
                        </ethernet-match>
                        <ipv4-destination>%s</ipv4-destination>
                    </match>
                    <id>%s</id>
                    <table_id>%s</table_id>
                    <instructions>
                        <instruction>
                            <order>0</order>
                            <apply-actions>
                                <action>
                                   <order>0</order>
                                   <dec-nw-ttl/>
                                </action>
                            </apply-actions>
                        </instruction>
                    </instructions>
                </flow>""" % (form.flow_priority.data, form.flow_destination_prefix.data, form.flow_id.data, form.flow_table_id.data)


        headers = {
            'accept': 'application/json',
            'content-type': 'application/xml'
        }

        r = requests.put('http://192.168.229.133:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/table/%s/flow/%s' % (form.flow_table_id.data, form.flow_id.data), data=xml, headers=headers, auth=('admin', 'admin'))



        return r.text

@app.route('/remove_flow')
def remove_flow():
    headers = {
        'accept': 'application/json',
        'content-type': 'application/xml'
    }

    r = requests.get('http://192.168.229.133:8181/restconf/config/opendaylight-inventory:nodes/', headers=headers, auth=('admin', 'admin'))

    return render_template('remove_flow.html', page_title='Remove Flow', panel_title='Form', flows_data=r.json())


@app.route('/read_config')
def read_config():

    return config.get_basic_auth()