import requests
url_list = ['http://dz.yteu.biz/thread0806.php?fid=22&search=&page='+str(i)  for i in range(2,100)]
# url_list = ['http://dz.yteu.biz/thread0806.php?fid=21&search=&page='+str(i)  for i in range(2,100)]
url_list.insert(0, 'http://dz.yteu.biz/thread0806.php?fid=22')

# print(url_list)
for url in url_list:
    r = requests.get(url)
    print(r.encoding)
    # print(r.content.decode('gbk'))
    text = r.content.decode('gbk', 'ignore')
    with open('test_request.txt', 'a',encoding='utf-8') as f:
        f.write(text)

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