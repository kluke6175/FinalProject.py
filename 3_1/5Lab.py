import wsgiref.simple_server
import urllib.parse
import sqlite3
import http.cookies
import random

connection = sqlite3.connect('users.db')
stmt = "SELECT name FROM sqlite_master WHERE type='table' AND name='users'"
cursor = connection.cursor()
result = cursor.execute(stmt)
r = result.fetchall()
if (r == []):
    exp = 'CREATE TABLE users (username,password)'
    connection.execute(exp)


def application(environ, start_response):
    headers = [('Content-Type', 'text/html; charset=utf-8')]

    path = environ['PATH_INFO']
    params = urllib.parse.parse_qs(environ['QUERY_STRING'])
    un = params['username'][0] if 'username' in params else None
    pw = params['password'][0] if 'password' in params else None

    if path == '/register' and un and pw:
        user = cursor.execute('SELECT * FROM users WHERE username = ?', [un]).fetchall()
        if user:
            start_response('200 OK', headers)
            return ['Sorry, username {} is taken'.format(un).encode()]
        else:
            connection.execute('INSERT INTO users VALUES (?, ?)', [un, pw])
            connection.commit()
            headers.append(('Set-Cookie', 'session={}:{}'.format(un, pw)))
            start_response('200 OK', headers)
            return ['Username {} been successfully registered'.format(un).encode()]

    elif path == '/login' and un and pw or '/' and un and pw:
        user = cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', [un, pw]).fetchall()
        if user:
            headers.append(('Set-Cookie', 'session={}:{}'.format(un, pw)))
            start_response('200 OK', headers)
            return ['User {} successfully logged in. <a href="/account?{}&{}">Account</a>'.format(un, un, pw).encode()]
        else:
            start_response('200 OK', headers)
            return ['Incorrect username or password'.encode()]

    elif path == '/logout':
        headers.append(('Set-Cookie', 'session=0; expires=Thu, 01 Jan 1970 00:00:00 GMT'))
        start_response('200 OK', headers)
        return ['Logged out. <a href="/">Login</a>'.encode()]

    elif path == '/account':
        start_response('200 OK', headers)

        if 'HTTP_COOKIE' not in environ:
            return ['Not logged in <a href="/">Login</a>'.encode()]

        cookies = http.cookies.SimpleCookie()
        cookies.load(environ['HTTP_COOKIE'])
        if 'session' not in cookies:
            return ['Not logged in <a href="/">Login</a>'.encode()]

        [un, pw] = cookies['session'].value.split(':')
        user = cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', [un, pw]).fetchall()

        #This is where the game begins. This section of is code only executed if the login form works, and if the user is successfully logged in
        if user:
            correct = 0
            wrong = 0

            cookies = http.cookies.SimpleCookie()
            if 'HTTP_COOKIE' in environ:
                cookies = http.cookies.SimpleCookie()
                cookies.load(environ['HTTP_COOKIE'])
                correct = int(cookies['score'].value.split(':')[0])
                wrong = int(cookies['score'].value.split(':')[1])
                if 'an1' in params:
                    correct += 1
                else:
                    wrong += 1
            else:
                correct = 0

            headers = [
                ('Content-Type', 'text/plain; charset=utf-8'),
                ('Set-Cookie', 'correct={}'.format(correct))
            ]


            page = '<!DOCTYPE html><html><head><title>Multiply with Score</title></head><body>'
            if 'f1' in params and 'f2' in params and 'an1' in params:
                page += '''<!DOCTYPE html>
                                    <html>
                                    <head><title>Simple Form</title></head>
                                    <h2 style="background-color: green">Correct</h2>                  
                                    </body>
                                    </html>'''

            elif 'reset' in params:
                correct = 0
                wrong = 0
            else:
                page += '''<!DOCTYPE html>
                                    <html>
                                    <head><title>Simple Form</title></head>
                                    <h2 style="background-color: red">Wrong</h2>
                                    </body>
                                    </html>'''

            headers.append(('Set-Cookie', 'score={}:{}'.format(correct, wrong)))

            f1 = random.randrange(10) + 1
            f2 = random.randrange(10) + 1
            f3 = random.randrange(10) + 1
            f4 = random.randrange(10) + 1
            f5 = random.randrange(10) + 1

            page = page + '<h1>What is {} x {}</h1>'.format(f1, f2)

            a1 = int(f1) * int(f2)
            a2 = int(f5) * int(f3)
            a3 = int(f3) * int(f4)
            a4 = int(f4) * int(f5)
            answer = [a1, a2, a3, a4]
            an1 = answer[0]
            an2 = answer[1]
            an3 = answer[2]
            an4 = answer[3]

            hyperlink = ['<a href="/account?username={}&amp;password={}&amp;f1={}&amp;f2={}&amp;an1={}">{}</a><br>'.format(un, pw, f1, f2, a1, an1), '<a href="/account?username={}&amp;password={}&amp;f1={}&amp;f2={}&amp;an2={}">{}</a><br>'.format(un, pw, f1, f2, a1, an2), '<a href="/account?username={}&amp;password={}&amp;f1={}&amp;f2={}&amp;an3={}">{}</a><br>'.format(un, pw, f1, f2, a1, an3), '<a href="/account?username={}&amp;password={}&amp;f1={}&amp;f2={}&amp;an4={}">{}</a><br>'.format(un, pw, f1, f2, a1, an4)]

            page += '''<!DOCTYPE html>
                                <html><head><title>Page Title</title></head>
                                <body>

                                <p> </p>
                                <p>A: {}</p>
                                <p>B: {}</p>
                                <p>C: {}</p>
                                <p>D: {}</p>
                                </body>
                                </html>'''.format(hyperlink[0], hyperlink[1], hyperlink[2], hyperlink[3])

            page += '''<h2>Score</h2>
            Correct: {}<br>
            Wrong: {}<br>
            <a href="/account?reset=true">Reset</a><br>
            <a href="/logout">Logout</a>
            </body></html>'''.format(correct, wrong)

            return [page.encode()]
        else:
            return ['Not logged in. <a href="/">Login</a>'.encode()]

    elif path == '/' or '/login' or '/register':
        headers = [('Content-Type', 'text/html; charset=utf-8')]
        start_response('200 OK', headers)
        if path == '/' or path == '/login':

            page = '''<!DOCTYPE html>
                    <html>
                    <head><title>Simple Form</title></head>
                    <body>
                    <h1>Login</h1>
                    <form>
                        Username <input type="text" name="username" placeholder="Username"><br>
                        Password <input type="password" name="password"placeholder="Password"><br>
                        <input type="submit">

                    </form>
                    <p> <a href="/register">Register</a></p>'''

        elif path == '/register':
            page = '''<!DOCTYPE html>
                    <html>
                    <head><title>Simple Form</title></head>
                    <body>
                    <h1>Register</h1>
                    <form>
                        Username <input type="text" name="username" placeholder="Username"><br>
                        Password <input type="password" name="password" placeholder="Password"><br>

                        <input type="submit">

                    </form>
                    <p><a href="/login">Login</a></p>
                    </body>
                    </html>'''

        return [page.encode()]

    else:
        start_response('404 Not Found', headers)
        return ['Status 404: Resource not found'.encode()]


httpd = wsgiref.simple_server.make_server('', 8000, application)
httpd.serve_forever()