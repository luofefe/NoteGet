import yaml
from main import ENV, DIR


def read_env_yaml():
    with open(file=f'{DIR}/envConfig/{ENV}/config.yml', mode='r', encoding='utf-8') as f:
        res = yaml.load(f, Loader=yaml.FullLoader)
        return res


def read_api_yaml():
    with open(file=f'{DIR}/data/apiData.yml', mode='r', encoding='utf-8') as f:
        res = yaml.load(f, Loader=yaml.FullLoader)
        return res


if __name__ == '__main__':
    print(read_env_yaml())
    pass
