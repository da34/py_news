# codnig:utf-8

from .mysql_db import pool


class RoleDao:
    def search_list(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = 'select * from t_role'
            cursor.execute(sql)
            roles = cursor.fetchall()
            return roles
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()
