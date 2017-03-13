from selenium import webdriver
import csv
from datetime import *

browser = webdriver.Firefox()




browser.get("http://www.sse.com.cn/market/stockdata/overview/day/")
browser.implicitly_wait(5)
js = "document.getElementById('start_date2').removeAttribute('readOnly');"
browser.execute_script(js)

csvFile = open("./shanghaiData.csv", 'w')
writer = csv.writer(csvFile)
writer.writerow(('marketA', 'marketB'))

dateS = date(1999,1,1)
for i in range(0,10000):
	#print('%s-%s-%s' % (year, month, day))
	dateD = dateS + timedelta(days=i)		

	if dateD == date.today():
		break
	
	browser.find_element_by_id('start_date2').clear()
	browser.find_element_by_id('start_date2').send_keys(dateD.strftime('%Y-%m-%d'))
	browser.find_element_by_id('btnQuery').click()
			
	browser.implicitly_wait(10)
	table_data = browser.find_element_by_id('tableData_934').text
	table_data = table_data.split('\n')
	#print(table_data)
	if len(table_data) < 31: # no data record.
		continue
	else: # handle and save the record.
		market_A_dRatio = table_data[27]
		market_A_eXchangeRatio = table_data[31]		
		print(dateD.strftime('%Y-%m-%d') + ': ' + market_A_dRatio + ' ' + market_A_eXchangeRatio)
		writer.writerow((date, market_A_dRatio,market_A_eXchangeRatio))
	
 
