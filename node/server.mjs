import http from 'node:http';
import fs from 'node:fs';

const PORT = 3001;

const files = {
    index: fs.readFileSync(new URL('./public/index.html', import.meta.url)),
    about: fs.readFileSync(new URL('./public/about.html', import.meta.url)),
    notFound: fs.readFileSync(new URL('./public/404.html', import.meta.url)),
    css: fs.readFileSync(new URL('./public/styles.css', import.meta.url))
};

const server = http.createServer((req, res) => {
    const parsedUrl = new URL(req.url, `http://${req.headers.host}`);
    const pathname = parsedUrl.pathname;

    let statusCode = 200;
    let contentType = 'text/html; charset=utf-8';
    let content = '';

    switch (pathname) {
        case '/':
            content = files.index;
            break;
        case '/about':
            content = files.about;
            break;
        case '/styles.css':
            contentType = 'text/css; charset=utf-8';
            content = files.css;
            break;
        default:
            statusCode = 404;
            content = files.notFound;
            break;
    }

    res.writeHead(statusCode, { 'Content-Type': contentType });
    res.end(content);
});

server.listen(PORT, () => {
    console.log(`Node.js сервер запущено на http://localhost:${PORT}`);
});