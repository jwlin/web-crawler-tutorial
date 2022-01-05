from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


if __name__ == '__main__':
    url = 'https://www2.bot.com.tw/house/default.aspx'
    try:
        driver = webdriver.Chrome(executable_path='chromedriver.exe')
        # Webdriver 的執行檔也可以使用 PhantomJS
        # driver = webdriver.PhantomJS('phantomjs.exe')
        driver.maximize_window()
        driver.set_page_load_timeout(60)
        driver.get(url)

        # 定位日期輸入欄位, 並輸入日期
        element = driver.find_element_by_id('fromdate_TextBox')
        element.send_keys('1010101')
        element = driver.find_element_by_id('todate_TextBox')
        element.send_keys('1060101')

        # 定位選單所在欄位並點擊
        element = driver.find_element_by_id('purpose_DDL')
        element.click()

        # 巡覽選單, 點擊對應選項
        for option in element.find_elements_by_tag_name('option'):
            if option.text == '其他':
                option.click()

        # 點擊送出按鈕
        element = driver.find_element_by_id('Submit_Button').click()

        # 等待目標表格出現
        element = WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((By.ID, 'House_GridView'))
        )

        # page_source 可以回傳目前瀏覽器所看到的網頁文件
        soup = BeautifulSoup(driver.page_source, 'html5lib')
        table = soup.find(id='House_GridView')
        for row in table.find_all('tr'):
            print([s for s in row.stripped_strings])
    finally:
        driver.quit()  # 關閉瀏覽器, 結束 webdriver process
