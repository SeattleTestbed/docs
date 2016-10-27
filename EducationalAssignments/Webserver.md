# Seattle Web Server
----

----



## Overview
----

In this part of the project you will create a minimal web server to serve text and html files. Your webserver will have a single dynamic component for listing files in a directory, it will need to read and send file contents to clients as well as accept incoming data. 



## How does HTTP work?
----

HTTP is a client-server request-response protocol. All communication happens over a TCP connection. The server listens on a TCP port, and accepts new connections. The client connects to the server and sends an HTTP Request. The server responds with an HTTP Response. For this class, your webserver should service a single HTTP Request per connection (the full HTTP protocol supports multiple requests per connection). HTTP Requests and Responses are in ascii. Here is an example of an HTTP Request that a server may receive (line numbers do not appear in the actual transmission):
```
1. GET / HTTP/1.1
2. User-Agent: curl/7.18.0 (i486-pc-linux-gnu) libcurl/7.18.0 OpenSSL/0.9.8g zlib/1.2.3.3 libidn/1.1
3. Host: google.com
4. Accept: */*
5.  
```
Line 1 of this request contains the HTTP Method (GET), the request URI (/), and the HTTP version (HTTP/1.1). For this project, your web-server can ignore all other request header fields. Note that the request is terminated by a single blank line (line 5). This is used to indicate to the server that the client has finished sending the HTTP header.

The server's response to this request might look like the following:
```
1. HTTP/1.1 200 OK
2. Date: Wed, 29 Oct 2008 03:24:19 GMT
3. Server: Apache/2.2.8 (Fedora) DAV/2 mod_pubcookie/3.3.3 mod_ssl/2.2.8 OpenSSL/0.9.8g
4. Accept-Ranges: bytes
5. Transfer-Encoding: chunked
6. Content-Type: text/html
7. Content-Language: en
8. 
9. ... HTTP CONTENT ...
...
```
Line 1 of this response contains the HTTP version (HTTP/1.1), the status code (200), and the reason phrase (OK). This is then followed by some number of response headers. For this project, your web-server does not need to generate any other response header fields. Note that like the HTTP request, the response is also terminated with a blank line (line 8). The lines immediately following the blank line (line 9+) contain HTTP content.

Your server can assume that the client sends a single HTTP request, and can close the TCP connection after sending the HTTP response to the client.



## Project requirements
----

A web-server that..

    * Takes a single server port argument on the command line
    * Works with firefox
    * Support HTTP versions 1.0 and 1.1
    * Serves files out of the current directory
    * Shows a page listing available files for URI '/'
    * Handles multiple clients

By "works with firefox," we mean that if your server is run on port X, and there is a file where the server was run called F.txt, then typing "http://server:X/F.txt" in the firefox location bar should bring up the contents of the file F.txt in firefox window. Your web-server is required to generate only three status codes and respective reason phrases:

    * 200 OK

    * 400 Bad Request

    * 404 Not Found

A minimal web-server will (1) read the request line: request method, request URI, HTTP version, (2) wait for a blank line (3) respond with a Bad Request error message if an invalid/incomplete request is received; close the connection if the client times out (after 5 seconds) (5) respond with content of request file (or list current directory contents) using a valid HTTP 1.0 response message and (6) returns a status code of 200, 400, or 404.



## Serving Files
----

Your web-server should serve files from its current directory. That is, when you run the web-server program, the program's current directory will be some directory (e.g., a subdirectory of your home directory). HTTP GET requests for files in only that directory should be satisified. In other words, if you get a request like "GET /hello.html HTTP/1.0", you should return the file "hello.html" that is located in the current working directory of the web server. For this project it is assumed that the web-server serves HTML and plain text files only.



## Listing Files
----

For listing available files for URI '/', you will need to be able to read the contents of the directory using listdir().

You may return the listing of files in plain text, with one entry per line, or as formatted HTML, either of these is acceptable.



## GET Request With Arguments
----

One way that webservers commonly accept incoming information is in arguments to GET requests.   Instead of saying ```GET /hello.html HTTP/1.1```, the client might say ```GET /hello.html?arg1=value1&arg2=value2&arg3=value3&... HTTP/1.1```.   The webserver interprets this as saying on page "hello.html", the client is submitting the information arg1=value1, arg2=value2, arg3=value3, etc.   

You should have a page [raw-attachment:thewall.html thewall.html] that allows a user to post comments on it via a form.   To post a comment there must be two specific arguments (any others are ignored).   The first argument is "name" and represents the name of the person posting the comment.   The second argument is "comment" and is the comment text itself.   Names and comments may only contain letters and numbers.   You will see funny characters like '%20' or '+' being sent to the web server if the user types incorrect data.

For any request to "thewall.html" that has no arguments, display the current page with all of the posts.    If you get a request with "name" and "comment" arguments, add those to "thewall.html" so the new user will see them.   If you get invalid arguments, display a valid webpage (i.e. return 200 status) that informs the user that they have incorrect arguments.

