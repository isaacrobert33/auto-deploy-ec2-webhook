from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/hook/deploy', methods=['POST'])
def handle_webhook():
    if request.headers.get('X-GitHub-Event') == 'push':
        branch = request.json['ref']
        if branch == 'refs/heads/master':  # Check the branch you want to trigger on
            subprocess.run(['cd', '~/HMS-Django &&', 'git', 'pull', 'origin', 'master'])  # Update code from GitHub
            subprocess.run(['~/guni_restart && ~/restart'])  # Replace with your actual deployment command
            return 'Webhook received and redeployment triggered!'
    return 'Ignoring webhook.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  # Listen on all public IPs
