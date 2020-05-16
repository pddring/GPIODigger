import RPi.GPIO as GPIO
import os
from digger import Digger
from http.server import BaseHTTPRequestHandler, HTTPServer

host_name = ''  # Host on all available IP addresses
host_port = 8000
d = Digger()

class DiggerServer(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _redirect(self, path):
        self.send_response(303)
        self.send_header('Content-type', 'text/html')
        self.send_header('Location', path)
        self.end_headers()

    def do_GET(self):
        with open("server.html") as file:
            html = file.read()
        
        temp = os.popen("/opt/vc/bin/vcgencmd measure_temp").read()
        self.do_HEAD()
        self.wfile.write(html.format(temp[5:]).encode("utf-8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode("utf-8")
        post_data = post_data.split("=")[1]
        
        if post_data == 'Stop':
            d.stop()
        if post_data == "Forwards":
            d.left_track.forward()
            d.right_track.forward()
        self._redirect('/')
        
if __name__ == '__main__':
    http_server = HTTPServer((host_name, host_port), DiggerServer)
    print("Server Starts - %s:%s" % (host_name, host_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()