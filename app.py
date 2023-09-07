from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import pytz

app = Flask(__name__)
@app.route('/api', methods=['GET'])

def get_info():

    slack_name = request.args.get('slack_name') 
    track = request.args.get('track')

    if not slack_name or not track:
        return jsonify({"error": "slack_name and track are required parameters"}), 400

    utc_now = datetime.now(timezone.utc)
    allowed_time_difference = timedelta(minutes=2)
    
    utc_now_naive = utc_now.astimezone(pytz.utc).replace(tzinfo=None)
    
    if abs(utc_now_naive - datetime.utcnow()) > allowed_time_difference:
        return jsonify({"error": "UTC time validation failed"}), 400

    current_day = utc_now.strftime('%A')
    github_file_url = "https://github.com/gladysgodwin/HNGx-Stage-one/app.py"
    github_repo_url = "https://github.com/gladysgodwin/HNGx-Stage-one/"

    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_now.strftime('%Y-%m-%dT%H:%M:%SZ'),
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
