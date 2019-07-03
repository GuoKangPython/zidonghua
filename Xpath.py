from selenium import webdriver
#实例化一个浏览器驱动
chrome = webdriver.Chrome()
#访问页面
chrome.get("http://book.zongheng.com/chapter/837093/55277727.html")
#捕获元素
texts =chrome.find_elements_by_xpath("//div[@class='content']/p")
#将内容写到txt文件当中
for t in texts:
    with open("xiaoshuo.txt","a") as f:
        f.write(t.text)
#关闭浏览器
chrome.close()

