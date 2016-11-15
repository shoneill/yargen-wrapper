# Our AWS Lamba function defined here
# Call yarGen.py

from subprocess import Popen, PIPE
import json

def lambda_handler(event, context):
    process = Popen(["yargen", event['args']], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    payload = {'output': output, 'err': err, 'exit_code': exist_code}
    return json.dumps(payload)
