from flask import render_template, flash, redirect, jsonify
from app import app
from .forms import AddFlowForm
from .forms import RemoveFlowForm
import requests
import pprint
@app.route('/')
@app.route('/index')
def index():

    r = requests.get(
        'http://'+app.config['ODL_SERVER_IP']+':'+app.config['ODL_SERVER_PORT']+'/restconf/config/opendaylight-inventory:nodes/',
        headers={
            'accept': 'application/json',
            'content-type': 'application/xml'
         },
         auth=(app.config['ODL_USERNAME'], app.config['ODL_PASSWORD'])
    )

    return render_template(
        'index.html',
        page_title='Dashboard',
        panel_title='Flows',
        flows_data=r.json()
    )


@app.route('/add_flow', methods=['GET'])
def add_flow():
    form = AddFlowForm()

    r = requests.get(
        'http://'+app.config['ODL_SERVER_IP']+':'+app.config['ODL_SERVER_PORT']+'/restconf/config/opendaylight-inventory:nodes/',
        headers={
            'accept': 'application/json',
            'content-type': 'application/xml'
         },
         auth=(app.config['ODL_USERNAME'], app.config['ODL_PASSWORD'])
    )

    flows_data = r.json()

    r = requests.get(
        'http://'+app.config['ODL_SERVER_IP']+':'+app.config['ODL_SERVER_PORT']+'/restconf/operational/opendaylight-inventory:nodes/',
        headers={
            'accept': 'application/json',
            'content-type': 'application/xml'
         },
         auth=(app.config['ODL_USERNAME'], app.config['ODL_PASSWORD'])
    )


    flows_output_ports = r.json()
    return render_template(
        'add_flow.html',
        page_title='Add Flow',
        panel_title='Form',
        form=form,
        flows_data=flows_data,
        flows_output_ports = flows_output_ports
    )



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
                                   <output-action>
                                        <output-node-connector>
                                            %s
                                        </output-node-connector>
                                   </output-action>
                                </action>
                            </apply-actions>
                        </instruction>
                    </instructions>
                </flow>""" % (form.flow_priority.data, form.flow_destination_prefix.data, form.flow_id.data, form.flow_table_id.data, form.flow_output_port.data)

        r = requests.put(
                'http://'+app.config['ODL_SERVER_IP']+':'+app.config['ODL_SERVER_PORT']+'/restconf/config/opendaylight-inventory:nodes/node/%s/table/%s/flow/%s' % (form.flow_node.data, form.flow_table_id.data, form.flow_id.data),
                 data=xml,
                 headers = {
                    'accept': 'application/json',
                    'content-type': 'application/xml'
                 },
                 auth=(app.config['ODL_USERNAME'], app.config['ODL_PASSWORD'])
             )

        if r.status_code == 200:
            return jsonify({'error': 0, 'message': 'Flow pushed!'})

        return jsonify({'error': 1, 'message': 'Unable to push flow'})



@app.route('/remove_flow')
def remove_flow():
    form = RemoveFlowForm()

    r = requests.get(
        'http://'+app.config['ODL_SERVER_IP']+':'+app.config['ODL_SERVER_PORT']+'/restconf/config/opendaylight-inventory:nodes/',
         headers={
            'accept': 'application/json',
            'content-type': 'application/xml'
         },
         auth=(app.config['ODL_USERNAME'], app.config['ODL_PASSWORD'])
    )

    return render_template(
        'remove_flow.html',
        page_title='Remove Flow',
        panel_title='Form',
        flows_data=r.json(),
        form=form
    )


@app.route('/api/remove_flow', methods=['POST'])
def api_remove_flow():

    form = RemoveFlowForm()

    flow_info = form.flow_key.data.split('@!@')

    if form.validate_on_submit():
        r = requests.delete(
            'http://'+app.config['ODL_SERVER_IP']+':'+app.config['ODL_SERVER_PORT']+'/restconf/config/opendaylight-inventory:nodes/node/%s/flow-node-inventory:table/%s/flow/%s/' % (flow_info[0], flow_info[1], flow_info[2]),
             headers={
                'accept': 'application/json',
                'content-type': 'application/xml'
             },
             auth=(app.config['ODL_USERNAME'], app.config['ODL_PASSWORD'])
        )

        if r.status_code == 200:
            return jsonify({'error': 0, 'message': 'Flow removed!'})

        return jsonify({'error': 1, 'message': 'Unable to remove flow'})