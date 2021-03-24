import requests
import json

def monthlyGet(startDate, endDate, time):

    cookies = {
        'JSESSIONID': '7d8fd6fc-b31c-408f-b628-b4cc6d87b79f',
        'JSESSIONID-samesite': '7d8fd6fc-b31c-408f-b628-b4cc6d87b79f',
        'TS0190562b': '0171bb39ba4c0e8f24294ce05bedd9c4b07d02718979b729364a1a5a1cd1ab94afcc19deda45d6424d935d21b5bece9ef0e704b6ad394b084d37603a9318b519fbb173b006aab79d686e155e566adb221dd8cae51e',
        'TS0104273d': '0171bb39bac5ece834c4aff212063447ffc1d4b2c079b729364a1a5a1cd1ab94afcc19dedacbf4698ecab8473a94a724766e909c9f',
        '__utma': '268182301.813209028.1610299794.1610299794.1610299794.1',
        '__utmb': '268182301.20.0.1610299806572',
        '__utmc': '268182301',
        '__utmz': '268182301.1610299794.1.1.utmcsr=secure.bge.com|utmccn=(referral)|utmcmd=referral|utmcct=/Pages/spsso.aspx',
        '__utmt': '1',
        '_sp_id.bff6': '28c1fbf41e2b1d2c.1610299794.1.1610299989.1610299794',
        '_sp_ses.bff6': '*',
        '_ga': 'GA1.2.813209028.1610299794',
        '_gid': 'GA1.2.1371100162.1610299794',
        'ORA_FPC': 'id=0e5f78fe-2228-4434-8623-797ffeb0416b',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US',
        'Referer': 'https://bgec.opower.com/ei/x/e/energy-use-details?fixtures=false&utilityCustomerId=45edd7666710b5245b6eadb8590df233231b655f1abf0e758cc7b7627ff01f6a&ou-data-browser=%2Fusage%2Felectricity%2Fyear%2F2019-12-26%3FaccountUuid%3Da6c126c8-3214-11e7-b13f-de732d5c59eb',
        'opower-selected-entities': '["urn:opower:customer:uuid:31d7280c-3214-11e7-b13f-de732d5c59eb"]',
        'x-requested-with': 'XMLHttpRequest',
        'Connection': 'keep-alive',
    }

    params = (
        ('startDate', startDate),
        ('endDate', endDate),
        ('aggregateType', time),
        ('includeEnhancedBilling', 'false'),
        ('includeMultiRegisterData', 'false'),
    )

    response = requests.get('https://bgec.opower.com/ei/edge/apis/DataBrowser-v1/cws/utilities/bgec/utilityAccounts/a6c126c8-3214-11e7-b13f-de732d5c59eb/reads', headers=headers, params=params, cookies=cookies)

    #NB. Original query string below. It seems impossible to parse and
    #reproduce query strings 100% accurately so the one below is given
    #in case the reproduced version is not "correct".
    # response = requests.get('https://bgec.opower.com/ei/edge/apis/DataBrowser-v1/cws/utilities/bgec/utilityAccounts/a6c126c8-3214-11e7-b13f-de732d5c59eb/reads?startDate=2020-12-28&endDate=2021-02-05&aggregateType=day&includeEnhancedBilling=false&includeMultiRegisterData=false', headers=headers, cookies=cookies)

    resp = response.json()

    reads = resp["reads"]

    value = []
    time = []

    for read in reads:

        value.append(read["consumption"]["value"])
        time.append(read["startTime"])
    # print (value)

    return value, time
