# coding:utf-8

from .mysql_db import pool


class UserDao:
    # 验证用户登录
    def login(self, username, password):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            # print(username, password)
            # sql = 'select count(*) from t_user where username = %s and password = %s'
            sql = 'select count(*) from t_user where username = %s and AES_DECRYPT(UNHEX(password),"我是你爹") = %s'
            cursor.execute(sql, (username, password))
            count = cursor.fetchone()[0]
            return True if count == 1 else False
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 查询用户身份
    def search_user_role(self, username):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = 'select r.role from t_user u join t_role r on u.role_id = r.id where u.username = %s'
            cursor.execute(sql, (username,))
            role = cursor.fetchone()[0]
            return role
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 添加用户
    def add_user(self, username, password, email, role_id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = 'insert into t_user(username, password, email, role_id) values (%s,HEX(AES_ENCRYPT(%s, "我是你爹")),%s,%s)'
            cursor.execute(sql, (username, password, email, role_id))
            con.commit()
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 查询用户列表
    def search_user_lsit(self, page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = 'select u.id, u.username, r.role from t_user u join t_role r on u.role_id = r.id order by u.id limit %s, %s'
            cursor.execute(sql, ((page - 1) * 5, 5))
            user_list = cursor.fetchall()
            return user_list
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 修改用户
    def update_user(self, _id, username, password, email, role_id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = 'update t_user set username = %s,password=HEX(AES_ENCRYPT(%s, "我是你爹")),email=%s,role_id=%s  where id = %s'
            cursor.execute(sql, (username, password, email, role_id, _id))
            con.commit()
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 删除用户
    def delete_user(self, _id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = 'delete from t_user where id = %s'
            cursor.execute(sql, (_id,))
            con.commit()
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 查询用户总数
    def search_user_count(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = 'select ceil(count(*) / 5) from t_user'
            cursor.execute(sql)
            count = cursor.fetchone()[0]
            return count
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()
