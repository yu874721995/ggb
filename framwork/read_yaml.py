import os,json
import yaml

class read_yaml():

    def read(self):
        item = []
        with open('F:/appium_jskj/config/config.yaml', 'r',encoding="utf-8") as f:
            load_dict = f.read()
            f.close()
        load_dict = yaml.load(load_dict)
        return list(load_dict)