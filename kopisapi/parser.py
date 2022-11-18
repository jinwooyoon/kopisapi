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

    if data_parse[xml_keys][xml_key] is None:

        logging.warning("The data is empty. Please check the parameter again.")
        raise

    for data in data_parse[xml_keys][xml_key]:
        yield data, len(data_parse[xml_keys][xml_key])
