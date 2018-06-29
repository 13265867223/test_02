import yaml
if __name__ == '__main__':
    with open("./data.yml", 'r')as f:
        data = yaml.load(f)
        print(data)