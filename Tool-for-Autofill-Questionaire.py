# -*- coding:utf-8 -*-
# by 'hollowman6' from Lanzhou University(兰州大学)

'''
警告：
仅供测试使用，不可用于任何非法用途！
对于使用本代码所造成的一切不良后果，本人将不负任何责任！

Warning:
For TESTING ONLY, not for any ILLIGAL USE!
I will not be responsible for any adverse consequences caused by using this code.

'''

import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def random_major():
    major_list = ["数学", "物理学", "化学", "中文学", "政治学", "经济学", "历史学", "生物学", "生物学", "考古学", "地理学",
                  "计算机科学与技术", "自动化"]
    n = random.randint(0, len(major_list) - 1)
    r_major = major_list[n]
    return r_major


def random_phone_num():
    all_phone_nums = set()
    num_start = ['134', '135', '136', '137', '138', '139', '150', '151', '152', '158', '159', '157', '182', '187', '188',
                 '147', '130', '131', '132', '155', '156', '185', '186', '133', '153', '180', '189']

    start = random.choice(num_start)
    end = ''.join(random.sample(string.digits, 8))
    res = start+end
    return res


def GBK2312():
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xf9)
    val = f'{head:x}{body:x}'
    st = bytes.fromhex(val).decode('gb2312')
    return st


def first_name():
    first_name_list = [
        '赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
        '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
        '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
        '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
        '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹',
        '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
        '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']
    n = random.randint(0, len(first_name_list) - 1)
    f_name = first_name_list[n]
    return f_name


def second_name():
    second_name_list = [GBK2312(), '']
    n = random.randint(0, 1)
    s_name = second_name_list[n]
    return s_name


def last_name():
    return GBK2312()


def create_name():
    name = first_name() + second_name() + last_name()
    return name


driver = webdriver.Chrome()
while True:
    driver.get("http://contest.zhishijingsai.com.cn/jq/90306762.aspx?udsid=892160")
    wait = WebDriverWait(driver, 5)
    NetworkErr = False
    while True:
        if driver.find_element_by_xpath('/html').get_attribute('dir') == "ltr":
            if not NetworkErr:
                print("Network error, please check your network!")
                NetworkErr = True
            driver.get(
                "http://contest.zhishijingsai.com.cn/jq/90306762.aspx?udsid=892160")
            time.sleep(3)
        else:
            NetworkErr = False
            break

    time.sleep(3)

    js = '''document.evaluate("//*[@id='q1']", document).iterateNext().value = "甘肃-兰州市-榆中县"'''
    driver.execute_script(js)

    time.sleep(3)

    js = '''document.evaluate("//*[@id='q2']", document).iterateNext().value = "兰州大学"'''
    driver.execute_script(js)

    time.sleep(3)

    major = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='q3']")))
    major.send_keys(random_major())

    time.sleep(3)

    name = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='q5']")))
    name.send_keys(create_name())

    time.sleep(3)

    phone = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='q6']")))
    phone.send_keys(random_phone_num())

    time.sleep(3)

    mail = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='q7']")))
    mail.send_keys(''.join(random.sample(string.digits, 8))+"@qq.com")

    time.sleep(3)

    rand_year = random.randint(1, 4)

    js = '''document.evaluate("//*[@id='q4_''' + str(rand_year) + \
        '''']", document).iterateNext().click()'''
    driver.execute_script(js)

    time.sleep(3)

    next_page = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='btnNext']")))
    next_page.click()

    time.sleep(3)

    for qnum in range(8, 28):
        choice = random.randint(1, 4)
        js = '''document.evaluate("//*[@id='q''' + str(qnum) + '''_''' + str(
            choice) + '''']", document).iterateNext().click()'''
        driver.execute_script(js)

        time.sleep(3)

    try:
        submit = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='submit_button']")))
        submit.click()
    except Exception:
        next_page = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='btnNext']")))
        next_page.click()

        time.sleep(3)

        submit = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='submit_button']")))
        submit.click()

    time.sleep(3)

    driver.delete_all_cookies()
