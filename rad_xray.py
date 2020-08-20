import  subprocess
from multiprocessing import Pool

def run_rad(target):
	cmd = ["rad.exe", "-t", target,'--disable-headless','-http-proxy','127.0.0.1:7777']
	ret = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,encoding='utf-8')
	output = ret.communicate()
	with open('crawl.txt','a+',encoding='utf-8') as f:
		for display in output:
			value = display.split('\n')
			for i in value:
				if ('GET' in i)  or ('POST' in i):
					f.write(i + '\n')
					print(i)
	if ret.returncode == 0:
		print("success:", ret)
	else:
		print("error:", ret)
if __name__ == '__main__':
	target_queue = []
	po = Pool(3)#使用进程池，这里是设置最大进程数量，也就是同时开启多少个chrom进行爬取
	file = open('rad.txt',encoding='utf-8')
	for text in file.readlines():
		target_queue.append(text.strip('\n'))
	target_queue = list(filter(None, target_queue))
	while len(target_queue) > 0:
		crawling = target_queue.pop(0)
		po.apply_async(run_rad,(crawling,))
		# print(target_queue)
		# print(crawling)
	print("----start----")
	po.close()  # 关闭进程池，关闭后po不再接收新的请求
	po.join()  # 等待po中所有子进程执行完成，再执行下面的代码,可以设置超时时间join(timeout=)
	print("-----end-----")