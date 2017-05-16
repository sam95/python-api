import ast
import resources


def update_page(r):
    my_keys = r.keys()
    main_list = []
    for key in my_keys:
        myl = ast.literal_eval(r.get(key))
        for item in myl:
            if 'dict' in str(type(item)):
                for val in resources.items_label:
                    main_list.append(item[val])
    with open("index.html", "a") as myfile:
        myfile.write(resources.html_string.format(*main_list))