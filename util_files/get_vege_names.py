import re

def get_vegetables(path_to_html_source):
    f = open(path_to_html_source)

    vegetables = []

    pattern = '=0">.*?</a>'
    pattern2 = 'US">.*?</a>'
    patFinder = re.compile(pattern)
    patFinder2 = re.compile(pattern2)

    with open('page.txt') as fp:
        line = fp.readline()
        cnt = 1
        while line:
                findPattern = re.findall(patFinder, line)
                findPattern2 = re.findall(patFinder2, line)
                line = fp.readline()
                cnt += 1
                for _ in findPattern:
                    # print(_[4:-4])
                    vegetables.append(_[4:-4])
                for _ in findPattern2:
                    # print(_[4:-4])
                    vegetables.append(_[4:-4])
    
    return vegetables