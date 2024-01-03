import os
import unittest

from BeautifulReport import BeautifulReport

ENV = 'Online'  # Online->线上环境   Offline->测试环境
DIR = os.path.dirname(os.path.abspath(__file__))  # 获取当前模块的路径


def run(test_suite):
    # 定义输出的文件位置和名字
    filename = "report.html"
    result = BeautifulReport(test_suite)
    result.report(filename=filename, description='测试报告', report_dir='./')


if __name__ == '__main__':
    print(DIR)
    run_case = 'all'  # all全景测试用例，smoking 冒烟测试用例
    if run_case == 'all':
        suite = unittest.TestLoader().discover('./testCase', 'test_*.py')
    elif run_case == 'smoking':
        suite = unittest.TestLoader().discover('./testCase', 'test_*.py')
    else:
        raise ValueError('枚举值错误')

    run(suite)
