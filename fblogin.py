from time import sleep
from selenium import webdriver
browser = webdriver.Chrome(executable_path="./chromedriver")
browser.get("https://www.facebook.com/hashtag/vtm8682103529")
sleep(2)
# listPost = browser.find_elements_by_xpath(
#     "//div[@class='kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql']")
# for post in listPost:
#     link = post.find_element_by_xpath("//a[@role='link']").get_attribute("href")
#     if post.text != "":
#         print(
#             "__________________________________________________________________________________")
#         print(post.text)
#         print(link)
#         print(
#             "__________________________________________________________________________________")

i = 1
while True:
    i += 1
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(5)
    listPost = browser.find_elements_by_xpath("//div[@role='article']")
    for post in listPost:
        if post.text != "":
            print(
                "###")
            print(post.text)
            print(
                "###")
    if i == 2:
        break
