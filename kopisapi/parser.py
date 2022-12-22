import json
import logging
import xmltodict

logging.basicConfig(level=logging.WARNING)


def parse(param_type, data_parse):

    response = data_parse.encode('utf-8')
    data_parse = xmltodict.parse(response)
    if param_type == "pblprfr" or param_type == "prffest" or param_type == "prfawad" or param_type == "prfper" or param_type == "prfplc" or param_type == "mnfct":

        xml_keys = "dbs"
        xml_key = "db"

    elif param_type == "boxoffice":
        xml_keys = "boxofs"
        xml_key = "boxof"

    elif param_type == "prfstsTotal" or param_type == "prfstsCreate" or param_type == "prfstsPrfByFct" or param_type == "prfstsArea" or param_type == "prfstsCate" or param_type == "prfstsPrfBy":
        xml_keys = "prfsts"
        xml_key = "prfst"

    check_data_list = data_parse[xml_keys][xml_key]

    if type(check_data_list) == type({}):
        check_data_list = []
        check_data_list.append(data_parse[xml_keys][xml_key])

    try:
        for data in check_data_list:

            yield data, len(data_parse[xml_keys][xml_key])

    except TypeError:

        logging.warning("API has no data or is a parameter problem.")
        raise
