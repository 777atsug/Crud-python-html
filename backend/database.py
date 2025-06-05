import sqlite3

def init_db():
    init_user_table()
    init_produto_table()

def init_user_table():
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        senha TEXT NOT NULL
    )""")
    conn.commit()
    conn.close()

def get_users():
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM usuarios')
    users = cur.fetchall()
    conn.close()
    return [{'id': u[0], 'nome': u[1], 'email': u[2]} for u in users]

def add_user(nome, email, senha):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)', (nome, email, senha))
    conn.commit()
    conn.close()
    return {'success': True}

def update_user(id, nome, email, senha):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute('UPDATE usuarios SET nome=?, email=?, senha=? WHERE id=?', (nome, email, senha, id))
    conn.commit()
    conn.close()
    return {'success': True}

def delete_user(id):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM usuarios WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return {'success': True}

def check_login(email, senha):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM usuarios WHERE email=? AND senha=?', (email, senha))
    user = cur.fetchone()
    conn.close()
    return user is not None

# -------------------
# PRODUTOS
# -------------------

def init_produto_table():
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL
    )""")
    conn.commit()
    conn.close()

def add_produto(nome, preco):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO produtos (nome, preco) VALUES (?, ?)", (nome, preco))
    conn.commit()
    conn.close()
    return {'success': True}

def get_produtos():
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM produtos")
    rows = cur.fetchall()
    conn.close()
    return [{'id': r[0], 'nome': r[1], 'preco': r[2]} for r in rows]

def update_produto(id, nome, preco):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute("UPDATE produtos SET nome=?, preco=? WHERE id=?", (nome, preco, id))
    conn.commit()
    conn.close()
    return {'success': True}

def delete_produto(id):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM produtos WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return {'success': True}
