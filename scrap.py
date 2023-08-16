import json
from pprint import pprint
from time import sleep
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
#import chromedriver_autoinstaller as chromedriver
#chromedriver.install()

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = Chrome(service=Service(ChromeDriverManager().install()))
url = 'https://www.avito.ru/sankt-peterburg/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?cd=1&q=%D0%B0%D1%80%D0%B5%D0%BD%D0%B4%D0%B0+%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80'
driver.get(url)
data = {}



def avito_parser():
    flats = driver.find_elements(By.CSS_SELECTOR, "[data-marker='item']")
    for flat in flats:
        title = flat.find_element(By.CSS_SELECTOR, "[itemprop='name']").text
        address = flat.find_element(By.CLASS_NAME, 'geo-root-zPwRk').text
        sub = address[address.find('\n') + 1:]
        underground = "".join((x for x in sub if not x.isdigit())).replace("мин", '').replace("–", '').replace(".", '').replace("до", "").replace("от", "").strip()
        link = flat.find_element(By.CSS_SELECTOR, "[data-marker='item-title']").get_attribute('href')
        price = flat.find_element(By.CSS_SELECTOR, "[itemprop='price']").get_attribute('content')

        post_id = link.split("/")[-1]

        data[post_id] = {'наименование': title,
                        'метро': underground,
                        'ссылка': link,
                        'цена': price,
                        }


        with open("items.json", "w", encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)







def paginator(count):
    while driver.find_elements(By.CSS_SELECTOR, "[data-marker='pagination-button/nextPage']") and count > 0:
        avito_parser()
        driver.find_element(By.CSS_SELECTOR, "[data-marker='pagination-button/nextPage']").click()
        count -= 1





"""Парсинг однокомнатынх квартир и их запись в отдельный словарь"""
def one_room_flats():
    with open('items.json', encoding='utf-8') as f:
        data = json.load(f)

        one_room = {}

        flats = driver.find_elements(By.CSS_SELECTOR, "[data-marker='item']")
        for flat in flats:
            link = flat.find_element(By.CSS_SELECTOR, "[data-marker='item-title']").get_attribute('href')
            post_id = link.split("/")[-1]

            if post_id in data:
                continue



            elif post_id.startswith("1-k."):
                title = flat.find_element(By.CSS_SELECTOR, "[itemprop='name']").text
                price = flat.find_element(By.CSS_SELECTOR, "[itemprop='price']").get_attribute('content')

                address = flat.find_element(By.CLASS_NAME, 'geo-root-zPwRk').text
                sub = address[address.find('\n') + 1:]
                underground = "".join((x for x in sub if not x.isdigit())).replace("мин", '').replace("–", '').replace(".", '').replace("от", "").replace("до", "")

                link = flat.find_element(By.CSS_SELECTOR, "[data-marker='item-title']").get_attribute('href')
                post_id = link.split("/")[-1]

                data[post_id] = {'наименование': title,
                                 'метро': underground,
                                 'ссылка': link,
                                 'цена': price,
                                 }

                one_room[post_id] = {'наименование': title,
                                        'ссылка': link,
                                        'метро': underground,
                                        'цена': price,
                                        }

    with open("items.json", "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)



    return one_room

"""Парсинг двухкомнатных квартир и их запись в отдельный словарь"""
def two_room_flats():
    with open('items.json', encoding='utf-8') as f:
        data = json.load(f)

        two_room = {}

        flats = driver.find_elements(By.CSS_SELECTOR, "[data-marker='item']")
        for flat in flats:
            link = flat.find_element(By.CSS_SELECTOR, "[data-marker='item-title']").get_attribute('href')
            post_id = link.split("/")[-1]

            if post_id in data:
                continue



            elif post_id.startswith("2-k."):
                title = flat.find_element(By.CSS_SELECTOR, "[itemprop='name']").text
                price = flat.find_element(By.CSS_SELECTOR, "[itemprop='price']").get_attribute('content')

                address = flat.find_element(By.CLASS_NAME, 'geo-root-zPwRk').text
                sub = address[address.find('\n') + 1:]
                underground = "".join((x for x in sub if not x.isdigit())).replace("мин", '').replace("–", '').replace(".", '').replace("от", '').replace("до", "")

                link = flat.find_element(By.CSS_SELECTOR, "[data-marker='item-title']").get_attribute('href')
                post_id = link.split("/")[-1]


                data[post_id] = {'наименование': title,
                                 'метро': underground,
                                 'ссылка': link,
                                 'цена': price,
                                 }

                two_room[post_id] = {'наименование': title,
                                     'метро': underground,
                                     'ссылка': link,
                                     'цена': price,

                                        }

    with open("items.json", "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return two_room


"""Парсинг трехкомнатынх квартир и их запись в отдельный словарь"""
def three_room_flats():
    with open('items.json', encoding='utf-8') as f:
        data = json.load(f)

        three_room = {}

        flats = driver.find_elements(By.CSS_SELECTOR, "[data-marker='item']")
        for flat in flats:
            link = flat.find_element(By.CSS_SELECTOR, "[data-marker='item-title']").get_attribute('href')
            post_id = link.split("/")[-1]

            if post_id in data:
                continue



            elif post_id.startswith("3-k."):
                title = flat.find_element(By.CSS_SELECTOR, "[itemprop='name']").text
                address = flat.find_element(By.CLASS_NAME, 'geo-root-zPwRk').text
                sub = address[address.find('\n') + 1:]
                underground = "".join((x for x in sub if not x.isdigit())).replace("мин", '').replace("–", '').replace(".", '').replace("от", "").replace("до", "")
                link = flat.find_element(By.CSS_SELECTOR, "[data-marker='item-title']").get_attribute('href')
                price = flat.find_element(By.CSS_SELECTOR, "[itemprop='price']").get_attribute('content')

                post_id = link.split("/")[-1]

                data[post_id] = {'наименование': title,
                                 'метро': underground,
                                 'ссылка': link,
                                 'цена': price,
                                 }

                three_room[post_id] = {'наименование': title,
                                       'метро': underground,
                                        'ссылка': link,
                                        'цена': price,
                                        }

    with open("items.json", "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return three_room

"""Парсинг квартир-студий и их запись в отдельный словарь"""
def appartment_room_flats():
    with open('items.json', encoding='utf-8') as f:
        data = json.load(f)

        appart_room = {}

        flats = driver.find_elements(By.CSS_SELECTOR, "[data-marker='item']")
        for flat in flats:
            link = flat.find_element(By.CSS_SELECTOR, "[data-marker='item-title']").get_attribute('href')
            post_id = link.split("/")[-1]

            if post_id in data:
                continue


            elif post_id.startswith("kvartira-studiya"):
                title = flat.find_element(By.CSS_SELECTOR, "[itemprop='name']").text
                address = flat.find_element(By.CLASS_NAME, 'geo-root-zPwRk').text
                sub = address[address.find('\n') + 1:]
                underground = "".join((x for x in sub if not x.isdigit())).replace("мин", '').replace("–", '').replace(".", '').replace("от", "").replace("до", "")
                link = flat.find_element(By.CSS_SELECTOR, "[data-marker='item-title']").get_attribute('href')
                price = flat.find_element(By.CSS_SELECTOR, "[itemprop='price']").get_attribute('content')

                post_id = link.split("/")[-1]

                data[post_id] = {'наименование': title,
                                 'метро': underground,
                                 'ссылка': link,
                                 'цена': price,
                                 }

                appart_room[post_id] = {'наименование': title,
                                        'метро': underground,
                                        'ссылка': link,
                                        'цена': price,
                                        }

    with open("items.json", "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return appart_room

