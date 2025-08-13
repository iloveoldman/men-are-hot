from flask import Flask, jsonify, request, render_template
import requests
import threading
import time

app = Flask(__name__)

# To store the most recent log
latest_log = ""

def print_colored_info(data_dict):
    PINK = '\033[95m'    # ANSI bright pink
    RESET = '\033[0m'    # reset color
    global latest_log
    log_str = ""
    for key, value in data_dict.items():
        line = f"{PINK}{key}:{RESET} {value}"
        print(line)
        log_str += f"{key}: {value}\n"
    latest_log = log_str  # store latest log for saving

def ask_to_save():
    global latest_log
    choice = input("Want to save this one? \n[y/n]: ").strip().lower()
    if choice == 'y':
        with open("saved.txt", "a", encoding="utf-8") as f:
            f.write(latest_log + "\n" + "="*40 + "\n")
        print("✅ Saved to saved.txt")
    else:
        print("❌ Not saved.")

@app.route("/")
def index1():
    return render_template("index.html")

@app.route("/ekrithjerbjtjejebtjriekthifiguufifiro39r884ifjf8939374758idjfud83ijrif8ei3jo3928rutieoejfufurhfiehiehrhrurhrbrheieihrururhrudhkehebrudiebrhtiurhrjeoeiduhfjfbrhr")
def info():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = {'ip': request.environ['REMOTE_ADDR']}
    else:
        ip = {'ip': request.environ['HTTP_X_FORWARDED_FOR']}
    user_agent = request.user_agent
    platform = user_agent.platform
    browser = user_agent.browser
    version = user_agent.version
    usr_agnt = user_agent.string

    try:
        family = usr_agnt.split("(")[1].split(")")[0].split(";")[0].strip()
        os_ = usr_agnt.split("(")[1].split(")")[0].split(";")[1].strip()
        device = usr_agnt.split("(")[1].split(")")[0].split(";")[2].strip()
    except IndexError:
        family = os_ = device = "Unknown"

    ip_url = "http://ip-api.com/json/" + ip['ip'].split(",")[0]
    ip_info = requests.get(ip_url).json()

    # Prepare dict for printing
    info_to_print = {
        "ip": ip["ip"],
        "status": ip_info.get("status", ""),
        "country": ip_info.get("country", ""),
        "region": ip_info.get("regionName", ""),
        "city": ip_info.get("city", ""),
        "zip": ip_info.get("zip", ""),
        "latitude": ip_info.get("lat", ""),
        "longitude": ip_info.get("lon", ""),
        "timezone": ip_info.get("timezone", ""),
        "isp": ip_info.get("isp", ""),
        "org": ip_info.get("org", ""),
        "platform": platform,
        "browser": browser,
        "version": version,
        "family": family,
        "os": os_,
        "device": device,
        "user_agent": str(user_agent)
    }

    print("\n[User info]")
    print_colored_info(info_to_print)

    # Ask to save ONLY when visiting /info
    threading.Thread(target=ask_to_save, daemon=True).start()

    return render_template(
        "info.html",
        ip=ip["ip"],
        status=ip_info["status"],
        country=ip_info["country"],
        countrycode=ip_info["countryCode"],
        region=ip_info["region"],
        regionname=ip_info["regionName"],
        city=ip_info["city"],
        zip=ip_info["zip"],
        latitude=ip_info["lat"],
        longitude=ip_info["lon"],
        timezone=ip_info["timezone"],
        isp=ip_info["isp"],
        org=ip_info["org"],
        asa=ip_info["as"],
        query=ip_info["query"],
        family=family,
        device=device,
        os=os_,
        platform=platform,
        browser=browser,
        chromeversion=version,
        user_agent=user_agent,
    )

@app.route('/button-press', methods=['POST'])
def button_press():
    data = request.get_json()
    print("\n[Button pressed]")
    print_colored_info(data)
    # No save question here
    return jsonify({"status": "received"}), 200

@app.route('/log-page', methods=['POST'])
def log_page():
    return '', 204

if __name__ == '__main__':
    preferred_ports = [3001, 3000, 3020, 8080]

    for port in preferred_ports:
        try:
            print(f"Trying port {port}...")
            app.run(host='0.0.0.0', debug=True, port=port, threaded=True)
            break  # exit loop if Flask starts successfully
        except OSError as e:
            print(f"Port {port} failed: {e}")
            time.sleep(0.5)