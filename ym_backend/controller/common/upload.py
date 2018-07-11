import json
from flask import request

def upload_file():
  if request.method == 'POST':
    f = request.files['files']
    f.save('./img_card.jpg')
    data = '{"result":"sucess"}'
    result = json.loads(data)
    return json.dumps(result)
  else:
    return "error"
