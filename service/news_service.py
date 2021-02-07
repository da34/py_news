# coding:utf-8

from db.news_dao import NewsDao


class NewsService:
    __news_dao = NewsDao()

    # 查询待审批新闻
    def search_un_review_list(self, page):
        news = self.__news_dao.search_un_review_list(page)
        return news

    # 查询待审批总数
    def search_un_review_count(self):
        count = self.__news_dao.search_un_review_count()
        return count

    # 审批新闻
    def update_un_review_new(self, _id):
        self.__news_dao.update_un_review_new(_id)

    # 查询新闻
    def search_news_list(self, page):
        news = self.__news_dao.search_news_list(page)
        return news

    # 查询新闻总数
    def search_news_count(self):
        count = self.__news_dao.search_news_count()
        return count

    # 删除新闻
    def delete_by_id(self, _id):
        self.__news_dao.delete_by_id(_id)
