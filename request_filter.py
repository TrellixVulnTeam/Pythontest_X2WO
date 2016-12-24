filter_result = []
with open('test_request.txt', 'r', encoding='utf-8') as f:
    for i in f:
        if '</a></h3>' in i:
            i = i.replace('href="','href="http://dz.yteu.biz/')
            filter_result.append(i)
# print(len(filter_result))
with open('filter_request.txt','w', encoding='utf-8') as write_line:
    for url in filter_result:
        write_line.write(url)