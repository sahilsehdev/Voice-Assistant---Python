from selenium import webdriver

driver = webdriver.Chrome("E:\My-Work\chromedriver.exe")
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ')
msg = input('Enter your message : ')
count = int(input('Enter the count : '))

input('Enter after scanning QR code')

user = driver.find_element_by_class_name('zoWT4'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_2vbn4')

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_4sWnG')
    button.click()