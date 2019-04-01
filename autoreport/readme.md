# 使用说明
## 环境搭建
1. 安装python3
2. 安装nodejs
3. 管理员方式npm install -g phantomjs-prebuilt
4. pip install -r requirments.txt
5. 安装chrome及与其对应版本的chromedriver
6. 将chromedriver配置到环境变量中

## 注意事项
1. 运行时请关闭本地excel
2. excel中的时间类型为字符串，而不是时间类型，excel->数据->分列可以将时间类型变为字符串
3. tinify访问失败可能是网络被拦截，请关闭杀毒软件和防火墙
4. tinify每个月有500次压缩限额，请使用自己的邮箱注册获取key
5. settings.py中文件位置需手动修改,注意修改收发件邮箱
6. 环境搭建完成后最好重启电脑