my_dict = []


def get_search(query):
    result_set = []
    query_list = query.split()
    print query_list
    for query_item in query_list:
        for dict_item in my_dict:
            if query_item in dict_item["data"]:
                result_set.append(dict_item)
    return list({v['id']: v for v in result_set}.values())


def get_double_search(title, data):
    result_set = []
    for dict_item in my_dict:
        if title in dict_item["title"]:
            result_set.append(dict_item)
        if data is not None and  data in dict_item["data"]:
            result_set.append(dict_item)
    return list({v['id']: v for v in result_set}.values())
