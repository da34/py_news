# coding:utf-8

from colorama import Style, Fore
from getpass import getpass
from service.user_service import UserService
from service.news_service import NewsService
from service.role_service import RoleDao
import os
import sys
import time

__user_service = UserService()
__news_service = NewsService()
__role_service = RoleDao()


def diy_print(style='', text=''):
    print(style, '\n\t' + text)


while True:
    os.system('cls')
    diy_print(Fore.LIGHTBLUE_EX, '-------------------------------------------')
    diy_print(Fore.LIGHTBLUE_EX, '欢迎使用新闻管理系统')
    diy_print(Fore.LIGHTBLUE_EX, '-------------------------------------------')
    diy_print(Fore.LIGHTGREEN_EX, '1.登录系统')
    diy_print(Fore.LIGHTGREEN_EX, '2.退出系统')
    print(Style.RESET_ALL)

    opt = input('\n\t输入操作编号：')

    if opt == '1':
        username = input('\n\t用户名：')
        password = getpass('\n\t密码：')
        result = __user_service.login(username, password)
        # 登录成功
        if result:
            role = __user_service.search_user_role(username)
            if role == '新闻编辑':
                pass
            elif role == '管理员':
                while True:
                    os.system('cls')
                    diy_print(Fore.LIGHTBLUE_EX, '1.新闻管理')
                    diy_print(Fore.LIGHTBLUE_EX, '2.用户管理')
                    diy_print(Fore.LIGHTRED_EX, 'back.退出登录')
                    diy_print(Fore.LIGHTRED_EX, 'exit.退出系统')
                    print(Style.RESET_ALL)
                    opt = input('\n\t输入操作编号：')
                    if opt == '1':
                        while True:
                            os.system('cls')
                            diy_print(Fore.LIGHTBLUE_EX, '1.审批新闻')
                            diy_print(Fore.LIGHTBLUE_EX, '2.删除新闻')
                            diy_print(Fore.LIGHTRED_EX, 'back.返回上一层')
                            print(Style.RESET_ALL)
                            opt = input('\n\t输入操作编号：')
                            if opt == '1':
                                page = 1
                                while True:
                                    os.system('cls')
                                    news_list = __news_service.search_un_review_list(page)
                                    news_count = __news_service.search_un_review_count()
                                    length = len(news_list)

                                    for i in range(length):
                                        new = news_list[i]
                                        diy_print(Fore.LIGHTBLUE_EX, '%d\t%s\t%s\t%s'
                                                  % (i + 1, new[1], new[2], new[3]))
                                    diy_print(Fore.LIGHTBLUE_EX, '%d/%d' % (page, news_count))
                                    diy_print(Fore.LIGHTRED_EX, 'back.返回上一层')
                                    diy_print(Fore.LIGHTRED_EX, 'prev.上一页')
                                    diy_print(Fore.LIGHTRED_EX, 'next.下一页')
                                    print(Style.RESET_ALL)
                                    opt = input('\n\t输入操作编号：')
                                    if opt == 'back':
                                        break
                                    elif opt == 'prev' and page > 1:
                                        page -= 1
                                    elif opt == 'next' and page < news_count:
                                        page += 1
                                    elif 1 <= int(opt) < length:
                                        # 获取新闻id
                                        news_id = news_list[int(opt) - 1][0]
                                        __news_service.update_un_review_new(news_id)

                            elif opt == '2':
                                page = 1
                                while True:
                                    os.system('cls')
                                    news_list = __news_service.search_news_list(page)
                                    news_count = __news_service.search_news_count()
                                    length = len(news_list)

                                    for i in range(length):
                                        new = news_list[i]
                                        diy_print(Fore.LIGHTBLUE_EX, '%d\t%s\t%s\t%s'
                                                  % (i + 1, new[1], new[2], new[3]))
                                    diy_print(Fore.LIGHTBLUE_EX, '%d/%d' % (page, news_count))
                                    diy_print(Fore.LIGHTRED_EX, 'back.返回上一层')
                                    diy_print(Fore.LIGHTRED_EX, 'prev.上一页')
                                    diy_print(Fore.LIGHTRED_EX, 'next.下一页')
                                    print(Style.RESET_ALL)
                                    opt = input('\n\t输入操作编号：')
                                    if opt == 'back':
                                        break
                                    elif opt == 'prev' and page > 1:
                                        page -= 1
                                    elif opt == 'next' and page < news_count:
                                        page += 1
                                    elif 1 <= int(opt) <= length:
                                        # 获取新闻id
                                        news_id = news_list[int(opt) - 1][0]
                                        __news_service.delete_by_id(news_id)
                            elif opt == 'back':
                                break;
                    elif opt == '2':
                        while True:
                            os.system('cls')
                            diy_print(Fore.LIGHTBLUE_EX, '1.添加用户')
                            diy_print(Fore.LIGHTBLUE_EX, '2.修改用户')
                            diy_print(Fore.LIGHTBLUE_EX, '3.删除用户')
                            diy_print(Fore.LIGHTRED_EX, 'back.返回上一层')
                            print(Style.RESET_ALL)
                            opt = input('\n\t输入操作编号：')
                            if opt == '1':
                                os.system('cls')
                                username = input('\n\t用户名：')
                                password = getpass('\n\t密码：')
                                affirm_password = getpass('\n\t确认密码：')
                                if password != affirm_password:
                                    print(Style.RESET_ALL)
                                    print('\n\t两次密码不一致, 3秒后自动返回')
                                    time.sleep(3)
                                    continue
                                email = input('\n\t邮箱：')
                                role_list = __role_service.search_list()
                                for i in range(len(role_list)):
                                    role = role_list[i]
                                    diy_print(Fore.LIGHTBLUE_EX, '%d.%s' % (i+1, role[1]))
                                print(Style.RESET_ALL)
                                while True:
                                    role_id = input('\n\t角色编号：')
                                    if 1 <= int(role_id) <= len(role_list):
                                        role_id = role_list[int(role_id) - 1][0]
                                        break
                                    else:
                                        print(Style.RESET_ALL)
                                        print('\n\t角色编号不存在, 3秒后请重新输入')
                                        time.sleep(3)
                                        continue
                                __user_service.add_user(username, password, email, role_id)
                                print('\n\t保存成功, 3秒后自动返回')
                                time.sleep(3)
                                break
                            elif opt == '2':
                                page = 1
                                while True:
                                    os.system('cls')
                                    user_list = __user_service.search_user_list(page)
                                    user_count = __user_service.search_user_count()
                                    length = len(user_list)

                                    for i in range(length):
                                        new = user_list[i]
                                        diy_print(Fore.LIGHTBLUE_EX, '%d\t%s\t%s'
                                                  % (i + 1, new[1], new[2]))
                                    diy_print(Fore.LIGHTBLUE_EX, '%d/%d' % (page, user_count))
                                    diy_print(Fore.LIGHTRED_EX, 'back.返回上一层')
                                    diy_print(Fore.LIGHTRED_EX, 'prev.上一页')
                                    diy_print(Fore.LIGHTRED_EX, 'next.下一页')
                                    print(Style.RESET_ALL)
                                    opt = input('\n\t输入操作编号：')
                                    if opt == 'back':
                                        break
                                    elif opt == 'prev' and page > 1:
                                        page -= 1
                                    elif opt == 'next' and page < user_count:
                                        page += 1
                                    elif 1 <= int(opt) <= length:
                                        user_id = user_list[int(opt) - 1][0]
                                        os.system('cls')
                                        username = input('\n\t新用户名：')
                                        password = getpass('\n\t新密码：')
                                        affirm_password = getpass('\n\t新确认密码：')
                                        if password != affirm_password:
                                            print(Style.RESET_ALL)
                                            print('\n\t两次密码不一致, 3秒后自动返回')
                                            time.sleep(3)
                                            continue
                                        email = input('\n\t新邮箱：')
                                        role_list = __role_service.search_list()
                                        for i in range(len(role_list)):
                                            role = role_list[i]
                                            diy_print(Fore.LIGHTBLUE_EX, '%d.%s' % (i + 1, role[1]))
                                        print(Style.RESET_ALL)
                                        while True:
                                            role_id = input('\n\t新角色编号：')
                                            if 1 <= int(role_id) <= len(role_list):
                                                role_id = role_list[int(role_id) - 1][0]
                                                break
                                            else:
                                                print(Style.RESET_ALL)
                                                print('\n\t角色编号不存在, 3秒后请重新输入')
                                                time.sleep(3)
                                                continue
                                        opt = input('\n\t是否保存（Y/N）')
                                        if opt.lower() == 'y':
                                            __user_service.update_user(user_id, username, password, email, role_id)
                                            print('\n\t保存成功, 3秒后自动返回')
                                            time.sleep(3)
                                        break
                            elif opt == '3':
                                page = 1
                                while True:
                                    os.system('cls')
                                    user_list = __user_service.search_user_list(page)
                                    user_count = __user_service.search_user_count()
                                    length = len(user_list)

                                    for i in range(length):
                                        new = user_list[i]
                                        diy_print(Fore.LIGHTBLUE_EX, '%d\t%s\t%s'
                                                  % (i + 1, new[1], new[2]))
                                    diy_print(Fore.LIGHTBLUE_EX, '%d/%d' % (page, user_count))
                                    diy_print(Fore.LIGHTRED_EX, 'back.返回上一层')
                                    diy_print(Fore.LIGHTRED_EX, 'prev.上一页')
                                    diy_print(Fore.LIGHTRED_EX, 'next.下一页')
                                    print(Style.RESET_ALL)
                                    opt = input('\n\t输入操作编号：')
                                    if opt == 'back':
                                        break
                                    elif opt == 'prev' and page > 1:
                                        page -= 1
                                    elif opt == 'next' and page < user_count:
                                        page += 1
                                    elif 1 <= int(opt) <= length:
                                        # 获取新闻id
                                        user_id = user_list[int(opt) - 1][0]
                                        __user_service.delete_user(user_id)
                                        print('\n\t删除成功（3秒自动返回）')
                                        time.sleep(3)
                                        break
                            elif opt == 'back':
                                break
                    elif opt == 'back':
                        break
                    elif opt == 'exit':
                        print(Style.RESET_ALL)
                        sys.exit(0)
        # 登录失败
        else:
            diy_print(text='登录失败, (3)秒后自动返回')
            time.sleep(3)
    else:
        # 安全退出
        sys.exit(0)
