from django.shortcuts import render


def get_html_content(request):
    import requests
    city = request.GET.get('city')
    city = city.replace(" ", "+")
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f'https://www.google.com/search?q=weather+{city}').text
    html_content_image = session.get(f'https://fr.freepik.com/search?format=search&last_filter=query&last_value=a&query={city}').text
    return [html_content, html_content_image]


def home(request):
    result = None
    if 'city' in request.GET:
        html_content = get_html_content(request)[0]
        html_content_image = get_html_content(request)[1]
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        soup_image = BeautifulSoup(html_content_image, 'html.parser')
        result = dict()
        image_src1 = soup_image.find_all(lambda tag: tag.name == 'img')
        img_list = []
        for c in range(len(image_src1)):
            if "https://img.freepik.com/" in image_src1[c]['src'] and ".jpg" in image_src1[c]['src']:
                img_list.append(image_src1[c]['src'])
        result['image1'] = img_list[2]
        result['image2'] = img_list[3]
        result['image3'] = img_list[4]

        try:
            result['region'] = soup.find("span", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text
            result['temp_now'] = soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"}).text
            result['dayhour'], result['weather_now'] = soup.find("div", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text.split(
                '\n')
        except:
            result['region'] = 'Digite uma Cidade válida'
            result['temp_now'] = ''
            result['dayhour'], result['weather_now'] = '', ''
    return render(request, 'core/home.html', {'result': result})
