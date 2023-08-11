import sqlite3

class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect('web_enumeration.db')
        self.cursor = self.conn.cursor()
        self.create_tables()
    
    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS page_info (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT,
                page_title TEXT,
                meta_desc TEXT,
                body_text TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS links (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url_id INTEGER,
                link TEXT,
                FOREIGN KEY (url_id) REFERENCES page_info (id)
            )
        ''')


        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS dns_subdomains (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url_id INTEGER,
                domain TEXT,
                subdomain TEXT,
                FOREIGN KEY (url_id) REFERENCES urls (id)
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS ports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url_id INTEGER,
                port INTEGER,
                FOREIGN KEY (url_id) REFERENCES urls (id)
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS server_info (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url_id INTEGER,
                server_type TEXT,
                platform TEXT,
                services TEXT,
                version TEXT,
                FOREIGN KEY (url_id) REFERENCES urls (id)
            )
        ''')
        self.conn.commit()

    def insert_page_info(self, url_id, page_title, meta_desc, body_text):
        sql = '''
            INSERT INTO page_info (url, page_title, meta_desc, body_text)
            VALUES (?, ?, ?, ?)
        '''
        values = (url_id, page_title, meta_desc, body_text)
        self.cursor.execute(sql, values)
        self.conn.commit()


    def insert_link(self, url_id, link):
        sql = '''
            INSERT INTO links (url_id, link)
            VALUES (?, ?)
        '''
        values = (url_id, link)
        self.cursor.execute(sql, values)
        self.conn.commit()



    def insert_dns_subdomain(self, url_id, domain, subdomain):
        sql = '''
            INSERT INTO dns_subdomains (url_id, domain, subdomain)
            VALUES (?, ?, ?)
        '''
        values = (url_id, domain, subdomain)
        self.cursor.execute(sql, values)
        self.conn.commit()

    def insert_port(self, url_id, port):
        sql = '''
            INSERT INTO ports (url_id, port)
            VALUES (?, ?)
        '''
        values = (url_id, port)
        self.cursor.execute(sql, values)
        self.conn.commit()

    def insert_server_info(self, url_id, server_type, platform, services, version):
        sql = '''
            INSERT INTO server_info (url_id, server_type, platform, services, version)
            VALUES (?, ?, ?, ?, ?)
        '''
        values = (url_id, server_type, platform, services, version)
        self.cursor.execute(sql, values)
        self.conn.commit()
