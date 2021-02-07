# coding:utf-8

from db.role_dao import RoleDao


class NewsService:
    __role_dao = RoleDao()

    # 查询角色列表
    def search_list(self):
        roles = self.__role_dao.search_list()
        return roles

