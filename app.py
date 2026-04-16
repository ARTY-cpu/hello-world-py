from http.server import BaseHTTPRequestHandler, HTTPServer

from controller.view_controller import GreetingController


def create_handler(controller: GreetingController):
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            body = controller.render_home()
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, format, *args):
            # Keep test output clean.
            return

    return Handler


def create_server(host: str = "0.0.0.0", port: int = 8080) -> HTTPServer:
    controller = GreetingController()
    return HTTPServer((host, port), create_handler(controller))


if __name__ == "__main__":
    create_server().serve_forever()