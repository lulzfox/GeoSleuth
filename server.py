from http.server import HTTPServer, BaseHTTPRequestHandler

class LocationHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # This method will be called every time the client sends a location update

        # Read the location from the request body
        length = int(self.headers["Content-Length"])
        body = self.rfile.read(length).decode()
        location = eval(body.split("=")[1])

        # Generate a Google Maps URL with the received coordinates
        maps_url = "https://www.google.com/maps?q={},{}".format(location["latitude"], location["longitude"])
        print(maps_url)

        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        self.wfile.write(b"Location received")

# Set up the server
server = HTTPServer(("localhost", 8000), LocationHandler)
server.serve_forever()
