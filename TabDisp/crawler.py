from bs4 import BeautifulSoup
import updater
import resources


def table_obtain(r, driver):
    driver.get("https://www.nseindia.com/live_market/dynaContent/live_analysis/top_gainers_losers.htm?cat=G")
    soup_obj = BeautifulSoup(driver.page_source, "html.parser")
    table_var = soup_obj.find('table', {'id': 'topGainers'})
    items = table_var.findAll('tr')
    my_list = []
    for item in items:
        items_dict = {}
        numbers = item.findAll('td')
        index = 0
        for val in numbers[:-1]:
            items_dict.update({resources.items_label[index]: val.text})
            index += 1
        my_list.append(items_dict)
    r.set(resources.prod_index, my_list[1:])
    resources.prod_index += 1
    updater.update_page(r)
