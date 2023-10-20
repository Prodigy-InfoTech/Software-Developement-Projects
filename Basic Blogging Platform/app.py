import http.server
import socketserver
from urllib.parse import parse_qs, urlparse

# Store blog posts in a list (in-memory storage, not suitable for production)
posts = []

class BlogHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Welcome to My Blog\n')
            self.wfile.write(b'<ul>\n')
            for post in posts:
                self.wfile.write(b'<li>\n')
                self.wfile.write(f'<h2>{post["title"]}</h2>\n'.encode('utf-8'))
                self.wfile.write(f'<p>{post["content"]}</p>\n'.encode('utf-8'))
                self.wfile.write(b'</li>\n')
            self.wfile.write(b'</ul>\n')
            self.wfile.write(b'<a href="/create">Create a new post</a>\n')
        elif self.path == '/create':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Create a New Blog Post\n')
            self.wfile.write(b'<form method="POST">\n')
            self.wfile.write(b'<label for="title">Title</label>\n')
            self.wfile.write(b'<input type="text" name="title" required><br>\n')
            self.wfile.write(b'<label for="content">Content</label>\n')
            self.wfile.write(b'<textarea name="content" rows="4" required></textarea><br>\n')
            self.wfile.write(b'<button type="submit">Create Post</button>\n')
            self.wfile.write(b'</form>\n')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        post_params = parse_qs(post_data)
        title = post_params['title'][0]
        content = post_params['content'][0]
        posts.append({'title': title, 'content': content})
        self.send_response(303)
        self.send_header('Location', '/')
        self.end_headers()

if __name__ == '__main__':
    PORT = 8080

    with socketserver.TCPServer(("", PORT), BlogHandler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
