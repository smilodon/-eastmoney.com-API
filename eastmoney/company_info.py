import requests
import json

index_repo = {
    'company_info_basic_us': ['证券代码', 'ISIN', '证券类型', '上市场所', '上市日期', '年结日', '每股面值', 'ADS折算比',
                              '公司名称', '公司网址', '中文名称', '电邮地址', '所属行业', '电话号码', '主席', '传真号码',
                              '成立日期', '员工人数', '注册地址', '办公地址', '公司介绍'],
    'company_info_basic_hk': ['证券代码', '证券简称', '上市日期', '证券类型', '交易所', '板块', '最新交易单位(每手股数)',
                              'ISIN', '是否沪港通标的', '是否深港通标的', '公司名称', '英文名称', '注册地', '注册地址',
                              '公司成立日期', '所属行业', '董事长', '公司秘书', '员工人数', '办公地址', '公司网址', 'EMAIL',
                              '年结日', '联系电话', '核数师', '传真', '公司介绍'],
}
chrome1 = {
    "Host": "emweb.eastmoney.com",
    "Proxy-Connection": "keep-alive",
    "Accept": "*/*",
    "DNT": "1",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/88.0.4324.190 Safari/537.36",
    "Referer": None,
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
}
sess = requests.Session()


def us_stock_basic(code: str):
    """
    美国股票基本公司信息
    :param code: 完整证券代码 eg. AT.N
    :return: (格式详见注释)
    """
    url = "http://emweb.eastmoney.com/pc_usf10/CompanyInfo/PageAjax?fullCode=" + code
    chrome1["Referer"] = "http://emweb.eastmoney.com/pc_usf10/CompanyInfo/index?code=" + code
    cir = sess.get(url, headers=chrome1)
    cid = json.loads(cir.content)
    try:
        assert len(cid['data']['zqzl']) >= 1
        assert len(cid['data']['gszl']) < 1
    except Exception as e:
        return [], e
    documents = [
        # 证券资料
        cid['data']['zqzl'][0]['SECURITYCODE'],  # 证券代码
        cid['data']['zqzl'][0]['ISINCODE'],  # ISIN
        cid['data']['zqzl'][0]['SECURITYTYPE'],  # 证券类型
        cid['data']['zqzl'][0]['TRADEMARKET'],  # 上市场所
        cid['data']['zqzl'][0]['LISTEDDATE'],  # 上市日期
        cid['data']['zqzl'][0]['FISCALDATE'],  # 年结日
        cid['data']['zqzl'][0]['PARVALUE'],  # 每股面值
        cid['data']['zqzl'][0]['ADSZS'],  # ADS折算比
        # 公司资料
        cid['data']['gszl'][0]['COMPNAME'],  # 公司名称
        cid['data']['gszl'][0]['WEBSITE'],  # 公司网址
        cid['data']['gszl'][0]['COMPNAMECN'],  # 中文名称
        cid['data']['gszl'][0]['EMAIL'],  # 电邮地址
        cid['data']['gszl'][0]['INDUSTRY'],  # 所属行业
        cid['data']['gszl'][0]['PHONE'],  # 电话号码
        cid['data']['gszl'][0]['CHAIRMAN'],  # 主席
        cid['data']['gszl'][0]['FAX'],  # 传真号码
        cid['data']['gszl'][0]['FOUNDDATE'],  # 成立日期
        cid['data']['gszl'][0]['EMPLOYNUM'],  # 员工人数
        cid['data']['gszl'][0]['ADDRESS'],  # 注册地址
        cid['data']['gszl'][0]['OFFICEADDRESS'],  # 办公地址
        # 公司介绍
        cid['data']['gszl'][0]['COMPPROFILE'].strip(),
    ]
    return documents, 0


def hk_stock_basic(code: str):
    """
    香港股票基本公司信息
    :param code: 证券代码 eg. 08187
    :return: (格式详见注释)
    """
    url = "http://emweb.securities.eastmoney.com/PC_HKF10/CompanyProfile/PageAjax?code=" + code
    chrome1['Referer'] = "http://emweb.securities.eastmoney.com/PC_HKF10/CompanyProfile/index?code=" + code
    cir = sess.get(url, headers=chrome1)
    cid = json.loads(cir.content)
    try:
        assert len(cid['zqzl']) >= 1
        assert len(cid['gszl']) >= 1
    except Exception as e:
        return [], e
    documents = [
        # 证券资料
        cid['zqzl']['zqdm'],  # 证券代码
        cid['zqzl']['zqjc'],  # 证券简称
        cid['zqzl']['ssrq'],  # 上市日期
        cid['zqzl']['zqlx'],  # 证券类型
        cid['zqzl']['jys'],  # 交易所
        cid['zqzl']['bk'],  # 板块
        cid['zqzl']['zxjydw'],  # 最新交易单位
        cid['zqzl']['isin'],  # ISIN
        cid['zqzl']['sfhgtbd'],  # 是否沪港通标的
        cid['zqzl']['sfsgtbd'],  # 是否深港通标的
        # 公司资料
        cid['gszl']['gsmc'],  # 公司名称
        cid['gszl']['ywmc'],  # 英文名称
        cid['gszl']['zcd'],  # 注册地
        cid['gszl']['zcdz'],  # 注册地址
        cid['gszl']['gsclrq'],  # 公司成立日期
        cid['gszl']['sshy'],  # 所属行业
        cid['gszl']['dsz'],  # 董事长
        cid['gszl']['gsms'],  # 公司秘书
        cid['gszl']['ygrs'],  # 员工人数
        cid['gszl']['bgdz'],  # 办公地址
        cid['gszl']['gswz'],  # 公司网址
        cid['gszl']['email'],  # EMAIL
        cid['gszl']['njr'],  # 年结日
        cid['gszl']['lxdh'],  # 联系电话
        cid['gszl']['hss'],  # 核数师
        cid['gszl']['cz'],  # 传真
        cid['gszl']['gsjs'],  # 公司介绍
    ]
    return documents, 0
