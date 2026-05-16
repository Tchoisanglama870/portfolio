import http.server
import socketserver
import os

# Many cloud platforms (like Replit) assign a specific port. We try to use that, or default to 8080.
PORT = int(os.environ.get("PORT", 8080))
Handler = http.server.SimpleHTTPRequestHandler

# Start the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving website at port {PORT}")
    print("Your website is now running!")
    httpd.serve_forever()
