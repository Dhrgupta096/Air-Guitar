#!/usr/bin/env python3
"""
Simple local HTTP server for Air Guitar Web App.
Runs on http://localhost:8080 by default.
"""
import http.server
import socketserver
import os
import sys
import webbrowser

PORT = 8081

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Enable caching-free development and cross-origin access if needed
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    socketserver.TCPServer.allow_reuse_address = True
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}"
        print("=" * 60)
        print(f"🎸 AIR GUITAR WEB APP SERVER RUNNING")
        print(f"📡 Local URL: {url}")
        print("💡 Open this URL in Google Chrome or any modern browser.")
        print("   Press Ctrl+C to stop the server.")
        print("=" * 60)
        
        # Optionally auto-open browser
        if "--open" in sys.argv:
            webbrowser.open(url)
            
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")

if __name__ == "__main__":
    main()
