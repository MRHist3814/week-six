urls = '';
f=open('urls.txt','w')
for x in range(567, 641):
    urls = 'https://dmr.bsu.edu/digital/api/singleitem/image/pdf/RynTms/%d/default.png\n' % (x)
    f.write(urls)
f.close