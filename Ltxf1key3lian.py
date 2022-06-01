import requests
import re


# 点赞
def praise(news_id, token, session):
    params_get = {"newsId": news_id, "flag": "praise", "token": token}
    headers = {"Accept": "application/json, text/javascript, */*; q=0.01",
               "X-Requested-With": "XMLHttpRequest",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69",
               "Referer": "http://10.236.11.187/page/ltxfHomePage/ltxfDetailPage.html?id=afbab9d2-ace6-4a8b-b607-4b78e761324e",
               "Connection": "close", "DNT": "1", "Accept-Encoding": "gzip, deflate",
               "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5,it;q=0.4"}
    cookies = {"token": token}
    session.get("http://10.236.11.187/api/praiseAndCollect/praise", params=params_get, headers=headers, cookies=cookies)


# 收藏
def collect(news_id, token, session):
    params_get = {"newsId": news_id, "flag": "collect", "token": token}
    headers = {"Accept": "application/json, text/javascript, */*; q=0.01",
               "X-Requested-With": "XMLHttpRequest",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69",
               "Referer": "http://10.236.11.187/page/ltxfHomePage/ltxfDetailPage.html?id=afbab9d2-ace6-4a8b-b607-4b78e761324e",
               "Connection": "close", "DNT": "1", "Accept-Encoding": "gzip, deflate",
               "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5,it;q=0.4"}
    cookies = {"token": token}
    session.get("http://10.236.11.187/api/praiseAndCollect/collect", params=params_get, headers=headers, cookies=cookies)


# 评论
def comment(news_id, token, session):
    params_post = {"newsId": news_id, "commentText": "不忘初心，牢记使命", "token": token}
    headers = {"Origin": "http://10.236.11.187", "Accept": "application/json, text/javascript, */*; q=0.01",
               "X-Requested-With": "XMLHttpRequest",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69",
               "Referer": "http://10.236.11.187/page/ltxfHomePage/ltxfDetailPage.html?id=9116d364-fab3-41d4-abd4-59d05928bdab",
               "Connection": "close", "DNT": "1", "Accept-Encoding": "gzip, deflate",
               "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5,it;q=0.4",
               "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    cookies = {"token": token}
    session.post("http://10.236.11.187/api/commentAndReply/newsComment", data=params_post, headers=headers, cookies=cookies)


# 浏览量
def browse(news_id, token, session):
    params_get = {"param": news_id, "token": token}
    headers = {"Accept": "application/json, text/javascript, */*; q=0.01", "X-Requested-With": "XMLHttpRequest",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62",
               "Referer": "http://10.236.11.187/page/ltxfHomePage/ltxfDetailPage.html?id=d457d440-d83d-45fb-8e31-3a548090325e",
               "Connection": "close", "DNT": "1", "Accept-Encoding": "gzip, deflate",
               "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5,it;q=0.4"}
    cookies = {"token": token}
    session.get("http://10.236.11.187/api/detail/ydlsjl", params=params_get, headers=headers, cookies=cookies)


# 列表
def news_contents(pages, token, session, columnsname):
    params_get = {"curDis": "own", "page": pages, "btnFlag": columnsname,
                 "token": token, "cLevel": "1"}
    headers = {"Accept": "application/json, text/javascript, */*; q=0.01", "X-Requested-With": "XMLHttpRequest",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56",
               "Referer": "http://10.236.11.187/page/ltxfHomePage/ltxfListPage.html?id="+columnsname,
               "Connection": "close", "DNT": "1", "Accept-Encoding": "gzip, deflate",
               "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5,it;q=0.4"}
    cookies = {"token": token}
    response = session.get("http://10.236.11.187/api/homePage/getNewsListByColumn", params=params_get, headers=headers, cookies=cookies)
    urls = re.findall(r'(?<=\"id\":\").[0-9a-z\-]*', response.text)
    return urls


# 选择专栏
def select_columns():
    columns_num = int(input('\n_______________________________________\n1. 集团要闻              | 2. 基层要闻 \n\
3. 贯彻新战略 一起向未来 | 4. 央企担当 \n5. 基层党建              | 6. 先锋典型 \n7. 疫情防控              | 8. 党务公开 \n\
9. 理论研究              | 10.党风廉政\n11.文化园地              |\n_______________________________________\n输入要刷的专栏编号：'))
    columns = ('0', 'xwzl_jituanyaowen', 'xwzl_jicengyaowen', 'xwzl_guancexinzhanlueyiluxiangweilai',
               'xwzl_yangqidandang', 'jcdj', 'xwzl_xianfengrenwu', 'yqfk', 'xwzl_dangwugongkai', 'xwzl_lilunyanjiu',
               'xwzl_dangfenglianzheng', 'whyd')
    return columns[columns_num]


if __name__ == "__main__":
    your_sessions = requests.Session()
    your_token = input('输入你的cookie：')
    columns_you_selected = select_columns()
    start_pages = int(input('输入起始页：'))
    end_pages = int(input('输入结束页：'))
    print('_______________________________________\n程序开始执行\n')
    page = start_pages
    while page <= end_pages:
        news_ids = news_contents(page, your_token, your_sessions, columns_you_selected)
        for news_ids_i in news_ids:
            praise(news_ids_i, your_token, your_sessions)
            collect(news_ids_i, your_token, your_sessions)
            browse(news_ids_i, your_token, your_sessions)
            comment(news_ids_i, your_token, your_sessions)
        print('第'+str(page)+'页完成')
        page = page + 1
    print('_______________________________________\n程序结束\n')
