from flask_restplus import Resource, Api, fields
from flask import Flask, request, jsonify
from datetime import datetime
from configparser import ConfigParser
import socket

### Load in config
parser = ConfigParser()

app = Flask(__name__)
api = Api(
    app,
    title='Wawanesa Security Logging Microservice',
    version='0.1')
log = api.namespace(
    'log',
    description='Used for logging to the SIEM')

params =  {
    'tool_name': fields.String(required=True),
    'event_type': fields.String(required=True),
    'username': fields.String(required=True),
    'source_host': fields.String(required=True),
    'dest_host': fields.String(required=True),
    'other': fields.String(required=True),
    'port': fields.Integer()
    }

log_params = api.model('log_params', params
)

def syslog(message, siem_ip, siem_port):
    """
    Send syslog UDP packet to given host and port.
    """
 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(bytes(message, encoding='utf-8') , (siem_ip, siem_port))
    sock.close()
    

@log.route("/pub",  doc={"description": "sends syslog"})
class PublishLogs(Resource):
    def get(self):
        expected_params = {}
        for index in params.keys():
            expected_params[index] = 'value'
        return jsonify({
            "expected_method": "POST",
            "expected_json_payload": expected_params

        })
    
    
    @api.expect(log_params)
    def post(self):

        time = datetime.utcnow().isoformat()
        tool_name = request.json.get('tool_name')
        event_type = request.json.get('event_type')
        source_host = request.json.get('source_host')
        dest_host = request.json.get('dest_host')
        username = request.json.get('username')


        hdr = f"Custom IS Security Toolset | {tool_name} | {time} | "
        payload = f"event_type='{event_type}' userid='{username}' "
        payload += f"target-hostname='{dest_host}' source_hostname='{source_host}'"
        message = hdr + payload
        parser.read('app.config', encoding='utf-8')
        siem_ip = parser.get('siem', 'ip')
        siem_port = int(parser.get('siem', 'port'))
        try:
            syslog(message, siem_ip, siem_port)
            return jsonify({
                "result": "success",
                "destination": f"{siem_ip}:{siem_port}/UDP",
                "message": {
                    "payload_sent": message
                }
            })
        except Exception as msg:
            return jsonify({
                "result": "failure",
                "destination": f"{siem_ip}:{siem_port}/UDP",
                "message": {
                    "payload_sent": message
                },
                "exception": str(msg)
            })
