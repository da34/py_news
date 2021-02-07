# coding:utf-8

from .mysql_db import pool


class NewsDao:
    # 查询待审批新闻
    def search_un_review_list(self, page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = 'select n.id, n.title, t.type, u.username ' \
                  'from t_news n join t_type t on n.type_id=t.id ' \
                  'join t_user u on n.editor_id = u.id ' \
                  'where n.state=%s order by n.create_time desc limit %s,%s'
            cursor.execute(sql, ('未审核', (page - 1) * 5, 5))
            news = cursor.fetchall()
            return news
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 查询待审批新闻
    def search_un_review_count(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = 'select ceil(count(*) / 5) from t_news where state = %s'
            cursor.execute(sql, ('未审核',))
            count = cursor.fetchone()[0]
            return count
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 审批新闻
    def update_un_review_new(self, _id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = 'update t_news set state = %s where id = %s'
            cursor.execute(sql, ('已审核', _id))
            con.commit()
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 查询新闻列表
    def search_news_list(self, page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = 'select n.id, n.title, t.type, u.username ' \
                  'from t_news n join t_type t on n.type_id=t.id ' \
                  'join t_user u on n.editor_id = u.id ' \
                  'order by n.create_time desc limit %s,%s'
            cursor.execute(sql, ((page - 1) * 5, 5))
            news = cursor.fetchall()
            return news
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 查询新闻总数
    def search_news_count(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = 'select ceil(count(*) / 5) from t_news'
            cursor.execute(sql)
            count = cursor.fetchone()[0]
            return count
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 删除新闻
    def delete_by_id(self, _id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = 'delete from t_news where id = %s'
            cursor.execute(sql, (_id,))
            con.commit()
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()
