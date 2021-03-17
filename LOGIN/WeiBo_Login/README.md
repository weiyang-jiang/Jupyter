----姜维洋制作-----

这个cookie池是基于selenium自动化爬取cookie
总共分为以下几个模块：
Cookies_Get: 主要的爬取cookies的模块
driver_settings: 这里设置了chrome为selenium的引擎
genenrate: 系统调度文件，负责关联调度其他文件
parse_captcha: 这个是验证码处理文件，由于验证码形式多样，所以暂时运用手动输入的方法
save_cookie: 这个是保存cookies的文件，暂时保存在json文件中，后面可以保存到数据库
settings: 这个系统配置文件，可以在里面更新微博账号
read_cookie: 这个是读取cookie的文件
verify_cookies: 这个是验证cookie能不能访问到指定页面的程序
run: 这个是总运行文件

templates：里面存放着cookies信息

升级版：
1.可以采用redis或MySQL存储cookies
2.可以给cookies用flask框架写一个api方便调用
