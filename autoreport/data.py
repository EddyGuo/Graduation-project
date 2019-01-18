from selenium import webdriver
import xlrd
import time
import datetime
from xlutils.copy import copy
from pyecharts import Line

BugClosed = 0           # 已关闭Bug数
BugNotClosed = 0        # 未关闭Bug数
BugActivated = 0        # 已激活Bug数
BugActivatedP1 = 0      # 已激活P1Bug数
BugActivatedP2 = 0   # 已激活P2Bug数

BugType = ['Closed', 'Not Closed', 'Activated', 'P1(Activated)', 'P2(Activated)']
BugData = []
BugReport = {}
BugDateList = []
BugClosedList = []
BugNotClosedList = []
BugActivatedList = []
BugActivatedP1List = []
BugActivatedP2List = []

driver = webdriver.Chrome()
driver.get('http://192.168.0.90/zentaopms/www')
driver.find_element_by_name('account').send_keys('cunnian.guo')
driver.find_element_by_name('password').send_keys('nianKJ0409')
driver.find_element_by_id('submit').click()
driver.find_element_by_xpath('//*[@id="mainmenu"]/ul/li[4]/a').click()
driver.find_element_by_id('currentItem').click()
time.sleep(1)
driver.find_element_by_link_text('P系列/P1pro').click()
time.sleep(1)

# BugNotClosed
driver.find_element_by_xpath('//*[@id="module1112"]').click()
time.sleep(1)
BugNotClosed = driver.find_element_by_xpath('//*[@id="bugList"]/tfoot/tr/td/div[2]/div/strong[1]').get_attribute('innerHTML')

# BugClosed
driver.find_element_by_xpath('//*[@id="bysearchTab"]/a').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="searchmore"]/i').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="field1"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="field1"]/option[11]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="value1_chosen"]/a/div/b').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="value1_chosen"]/div/ul/li[2]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="field2"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="field2"]/option[7]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="value2_chosen"]/a/div/b').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="value2_chosen"]/div/ul/li[3]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="submit"]').click()
time.sleep(1)
BugClosed = driver.find_element_by_xpath('//*[@id="bugList"]/tfoot/tr/td/div[2]/div/strong[1]').get_attribute('innerHTML')
time.sleep(1)

# BugActivated
driver.find_element_by_xpath('//*[@id="value2_chosen"]/a/div/b').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="value2_chosen"]/div/ul/li[1]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="submit"]').click()
time.sleep(1)
BugActivated = driver.find_element_by_xpath('//*[@id="bugList"]/tfoot/tr/td/div[2]/div/strong[1]').get_attribute('innerHTML')
time.sleep(1)

# BugActivatedP1
driver.find_element_by_xpath('//*[@id="field3"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="field3"]/option[13]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="value3_chosen"]/a/div/b').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="value3_chosen"]/div/ul/li[2]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="submit"]').click()
time.sleep(1)
BugActivatedP1 = driver.find_element_by_xpath('//*[@id="bugList"]/tfoot/tr/td/div[2]/div/strong[1]').get_attribute('innerHTML')
time.sleep(1)

# BugActivatedP2
driver.find_element_by_xpath('//*[@id="value3_chosen"]/a/div/b').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="value3_chosen"]/div/ul/li[3]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="submit"]').click()
time.sleep(1)
BugActivatedP2 = driver.find_element_by_xpath('//*[@id="bugList"]/tfoot/tr/td/div[2]/div/strong[1]').get_attribute('innerHTML')
time.sleep(1)

BugData.append(BugClosed)
BugData.append(BugNotClosed)
BugData.append(BugActivated)
BugData.append(BugActivatedP1)
BugData.append(BugActivatedP2)

driver.close()


for i in range(len(BugType)):
    print(BugType[i]+':'+BugData[i])

TimeNow = datetime.datetime.now().strftime('%Y/%m/%d/%H%T')

rb = xlrd.open_workbook("report.xls")
wb = copy(rb)
ws = wb.get_sheet(0)
rs = rb.sheet_by_name('Sheet1')
for j in range(len(BugType)):

    ws.write(0, j+1, BugType[j])

if rs.cell_value(-1, 0) != TimeNow:
    ws.write(rs.nrows, 0, TimeNow)
    for j in range(len(BugType)):
        ws.write(rs.nrows, j+1, BugData[j])
wb .save('report.xls')


rb = xlrd.open_workbook("report.xls")
rs = rb.sheet_by_name('Sheet1')
for i in range(1, rs.nrows):
    BugReport['Time'] = BugDateList
    BugDateList.append(rs.cell_value(i, 0))
for i in range(1, rs.nrows):
    BugReport['Closed'] = BugClosedList
    BugClosedList.append(rs.cell_value(i, 1))
    iList1 = [int(x) for x in BugClosedList]
for i in range(1, rs.nrows):
    BugReport['Not Closed'] = BugNotClosedList
    BugNotClosedList.append(rs.cell_value(i, 2))
    iList2 = [int(x) for x in BugNotClosedList]
for i in range(1, rs.nrows):
    BugReport['Activated'] = BugActivatedList
    BugActivatedList.append(rs.cell_value(i, 3))
    iList3 = [int(x) for x in BugActivatedList]
for i in range(1, rs.nrows):
    BugReport['P1(Activated)'] = BugActivatedP1List
    BugActivatedP1List.append(rs.cell_value(i, 4))
    iList4 = [int(x) for x in BugActivatedP1List]
for i in range(1, rs.nrows):
    BugReport['P2(Activated)'] = BugActivatedP2List
    BugActivatedP2List.append(rs.cell_value(i, 5))
    iList5 = [int(x) for x in BugActivatedP2List]
print(BugReport)

BugLine = Line("Bug折线图")
BugLine.add("Closed", BugDateList, iList1)
BugLine.add("Not Closed", BugDateList, iList2)
BugLine.add("Activated", BugDateList, iList3)
BugLine.add("P1(Activated)", BugDateList, iList4)
BugLine.add("P2(Activated)", BugDateList, iList5)
BugLine.render()
BugLine.render(path='snapshot.png')


