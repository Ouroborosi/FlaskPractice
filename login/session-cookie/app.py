from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

@app.route('/')
def index():
    # 判断本次请求的session中是否包含有 'username'属性
    if 'username' in session:
        # 如果有，从session中读取该属性
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        ## 将　‘username’属性放入 session中， 在本次request返回 response的时候，服务器发送了将
        ## session放到 cookies的指令，将session存储到客户端浏览器
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
            <form action="" method="post">
                <p><input type=text name=username>
                <p><input type=submit value=Login>
            </form>
        '''

@app.route('/logout')
def logout():
    # 如果会话中有用户名就删除它。
    # 同时从客户端浏览器中删除 session的 name属性
    session.pop('username', None)
    return redirect(url_for('index'))

# 设置密钥，复杂一点：
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run()