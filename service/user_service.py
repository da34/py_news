# coding:utf-8

from db.user_dao import UserDao


class UserService:
    __user_dao = UserDao()

    # 验证用户登录
    def login(self, username, password):
        result = self.__user_dao.login(username, password)
        return result

    # 查询用户身份
    def search_user_role(self, username):
        role = self.__user_dao.search_user_role(username)
        return role

    # 添加用户
    def add_user(self, username, password, email, role_id):
        self.__user_dao.add_user(username, password, email, role_id)

    # 查询用户列表
    def search_user_list(self, page):
        user_list = self.__user_dao.search_user_lsit(page)
        return user_list

    # 查询用户总数
    def search_user_count(self):
        count = self.__user_dao.search_user_count()
        return count

    # 修改用户
    def update_user(self, _id, username, password, email, role_id):
        self.__user_dao.update_user(_id, username, password, email, role_id)

    # 删除用户
    def delete_user(self, _id):
        self.__user_dao.delete_user(_id)