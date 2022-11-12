def bool_to_text(var):
    if isinstance(var, bool):
        if var:
            return 'true'
        else:
            return 'false'
    return var


def diff_report_create(dict_1, dict_2):
    dict_to_str = '{' + '\n'
    key1_lst = []
    key2_lst = []

    key1_lst = list(dict_1.keys())
    key2_lst = list(dict_2.keys())

    key1_lst = key1_lst + key2_lst
    key1_lst = list(set(key1_lst))
    key1_lst.sort()
    for key in key1_lst:
        if dict_2.get(key, '-') != '-':
            if dict_2.get(key) == dict_1.get(key):
                dict_to_str = dict_to_str \
                    + '   ' + key + ': ' + \
                    str(bool_to_text(dict_1.get(key))) + '\n'
            else:
                if dict_1.get(key, 'none') != 'none':
                    dict_to_str = dict_to_str \
                        + ' - ' + key + ': ' \
                        + str(bool_to_text(dict_1.get(key))) + '\n' + \
                        ' + ' + key + ': ' + \
                        str(bool_to_text(dict_2.get(key))) + '\n'
                else:
                    dict_to_str = dict_to_str + ' + ' \
                        + key + ': ' + str(bool_to_text(dict_2.get(key))) + '\n'
        else:
            dict_to_str = dict_to_str + ' - ' + key + ': ' \
                + str(bool_to_text(dict_1.get(key))) + '\n'

    dict_to_str = dict_to_str + '}'
    return dict_to_str
