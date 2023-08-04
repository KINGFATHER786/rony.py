import requests,random
password = 'Farazking'
for i in range(10):
    session = requests.Session()
    email = f"farazh{str(random.choice(password))}{str(random.choice(password))}{str(random.randint(1,22))}@gmail.com"
    cookies = {'fr': '0JB1mJGXzpJ7eT8qE.AWWDSSh-0Ak05strIf1CQEcCNz0.BknjJo.ud.AAA.0.0.Bko8aC.AWXrh9wdCT8','sb': 'Uc90ZKU5M4n0Ax0SWaxK2Ble','datr': 'Uc90ZDPVIcsxsl17uaK1XgdT','wd': '1024x620'}
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://free.facebook.com/reg/?cid=103&refsrc=deprecated&_rdr',
        'Origin': 'https://free.facebook.com',
        'Alt-Used': 'free.facebook.com',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1'}
    params = {'cid': '103'}
    data = {
        'lsd': 'AVogiANhqkI',
        'jazoest': '21010',
        'ccp': '2',
        'reg_instance': 'Uc90ZDPVIcsxsl17uaK1XgdT',
        'submission_request': 'true',
        'helper': '',
        'reg_impression_id': '242nf345-4ak4-vft3-4d43-1368a9958deb',
        'ns': '0',
        'zero_header_af_client': '',
        'app_id': '',
        'logger_id': '',
        'field_names[]': [
            'firstname',
            'reg_email__',
            'sex',
            'birthday_wrapper',
            'reg_passwd__',
        ],
        'firstname': 'Viqi',
        'lastname': 'ali id',
        'reg_email__': email,
        'sex': '2',
        'custom_gender': '',
        'did_use_age': 'false',
        'birthday_day': str(random.randint(1,28)),
        'birthday_month': '11',
        'birthday_year': '2002',
        'age_step_input': '',
        'reg_passwd__': password,
        'submit': 'Sign Up',
    }

    response = session.post('https://free.facebook.com/reg/submit/', params=params, cookies=cookies, headers=headers, data=data)
    cookie = str(response.cookies)
    uid = str(response.cookies)[40:55]
    print(email,password,cookie)
    # print(response.text)