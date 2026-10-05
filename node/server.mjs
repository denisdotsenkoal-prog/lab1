import { createServer } from 'node:http';
import { readFileSync } from 'node:fs';

const PORT = 3001;
const files = {
  '/': ['index.html', 'text/html; charset=utf-8', 200],
  '/about': ['about.html', 'text/html; charset=utf-8', 200],
  '/styles.css': ['styles.css', 'text/css; charset=utf-8', 200],
};

const server = createServer((req, res) => {
  const path = new URL(req.url, `http://${req.headers.host || 'localhost'}`).pathname;
  const route = files[path] ?? ['404.html', 'text/html; charset=utf-8', 404];
  const fileUrl = new URL(`./public/${route[0]}`, import.meta.url);
  const body = readFileSync(fileUrl);
  res.writeHead(route[2], { 'Content-Type': route[1] });
  res.end(body);
});

server.listen(PORT, () => console.log(`Node.js server: http://localhost:${PORT}`));
