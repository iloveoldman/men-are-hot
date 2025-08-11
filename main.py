from flask import Flask, jsonify, request, redirect, url_for, _request_ctx_stack, render_template 
import requests
import random
import string
import os

app = Flask(__name__)
@app.route("/")
def index1():
  return render_template("index.html")

@app.route("/info")
def info():
  if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
      ip = {'ip': request.environ['REMOTE_ADDR']}, 200
  else:
      ip = {'ip': request.environ['HTTP_X_FORWARDED_FOR']}, 200
  user_agent = request.user_agent
  platform = user_agent.platform
  browser = user_agent.browser
  version = user_agent.version
  usr_agnt = user_agent.string
  family = usr_agnt.split("(")[1].split(")")[0].split(";")[0]
  os = usr_agnt.split("(")[1].split(")")[0].split(";")[1]
  device = usr_agnt.split("(")[1].split(")")[0].split(";")[2]
  ip_url = "http://ip-api.com/json/"+ ip[0]['ip'].split(",")[0]
  ip_info = requests.get(ip_url).json()
  return render_template("info.html", ip=ip[0]["ip"], status=ip_info["status"], country=ip_info["country"], countrycode=ip_info["countryCode"], region=ip_info["region"], regionname=ip_info["regionName"], city=ip_info["city"], zip=ip_info["zip"], latitude=ip_info["lat"], longitude=ip_info["lon"], timezone=ip_info["timezone"], isp=ip_info["isp"], org=ip_info["org"], asa=ip_info["as"], query=ip_info["query"], family=family, device=device, os=os, platform=platform, browser=browser, chromeversion=version, user_agent=user_agent)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=5000,use_reloader=True,threaded=True)