基于长亭科技的radium爬虫造了个新轮子
实现功能：
批量爬取链接，可以在cmd中添加radium支持的功能，比如登录后爬取，把流量转发到xray的监听地址中
详细查看radium爬虫的使用方法：
https://github.com/chaitin/rad
使用Pool进程池管理进程，可以设置同时运行几个进程。
使用方法：
1、把需要爬取的域名放入rad.txt中

2、在代码的po = Pool(3)设置进程池的最大数，脚本里写的是最大3个，也就是同时开启3个chrom浏览器进行爬取。

3、爬取完成后会生成crawl.txt，格式为GET http://www.xxx.com/index.php?id=1  POST http://www.xxx.com/index.php

4、--disable-headless参数为前台显示chrom浏览器的操作，不需要可以删除该参数。

5、-http-proxy参数为转发流量到代理地址中，可以无缝对接xray，或考虑做个接口用于处理接收到的流量。

还存在的问题：
1、目前不清楚单个标签页最长的爬取时间是多久，因为没有timeout的参数（这应该是在爬虫内设定的，如果未来也没有会考虑对进程的执行时间做个限制）

2、测试时发现会爬取大量类似的页面，而且对无意义的页面还会爬取，比如遇到伪静态的页面会一直爬取，看到可以在配置文件中通过正则来判断做限制（还要再考虑下怎么写正则的匹配规则）
