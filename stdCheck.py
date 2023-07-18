from selenium import webdriver
from selenium.webdriver.common.by import By
import time

web = webdriver.Chrome()
web.get('http://202.28.17.14/stdcheck/')

time.sleep(2)

stdKey = "รหัสบัตรประชาชน"
last = web.find_element(by=By.XPATH, value='/html/body/div/div[2]/div[1]/form/table/tbody/tr[3]/td/input')
last.send_keys(stdKey)

# อ่านค่าตัวเลขสุ่มจากเว็บ
question_element = web.find_element(by=By.XPATH, value='/html/body/div/div[2]/div[1]/form/table/tbody/tr[4]/td[1]')
question_text = question_element.get_attribute('innerHTML')

# แยกข้อความในแท็ก <td> เป็นส่วนย่อย
parts = question_text.split(' + ')
num1 = int(parts[0].strip())  # ตัวเลขที่ 1
num2 = int(parts[1].split('=')[0].strip())  # ตัวเลขที่ 2

# คำนวณคำตอบ
answer = num1 + num2

# กรอกคำตอบในฟอร์ม
answer_input = web.find_element(by=By.XPATH, value='/html/body/div/div[2]/div[1]/form/table/tbody/tr[4]/td[2]/input')
answer_input.send_keys(str(answer))

# กดปุ่มส่งคำตอบ
submit_button = web.find_element(by=By.XPATH, value='/html/body/div/div[2]/div[1]/form/table/tbody/tr[5]/td/input')
submit_button.click()

time.sleep(2)

# Set the desired directory path
directory_path = r'DirectoryPath สำหรับเก็บรูป'
screenshot_path = fr'{directory_path}\screenshot.png'

# Take a screenshot
web.save_screenshot(screenshot_path)

web.quit()
print("Answer:", answer)
