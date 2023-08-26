import http.server
import socketserver
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Specify the directory containing your static files
DIRECTORY = "."

# Set up the HTTP server
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

print(f"Serving at port {PORT}")

# Set up the watchdog to watch for file changes
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".html") or event.src_path.endswith(".css") or event.src_path.endswith(".js"):
            print("File change detected. Reloading...")
            httpd.shutdown()  # Shut down the server
        
observer = Observer()
observer.schedule(MyHandler(), path=DIRECTORY, recursive=True)
observer.start()

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    observer.stop()

observer.join()
