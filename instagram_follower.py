# -*- coding: utf-8 -*-

import time;
import sys;

from selenium import webdriver;
import selenium.webdriver.chrome.service as service;
from selenium.webdriver.common.by import By;
from selenium.webdriver.common.keys import Keys;


count = 0;

print("Username: ");
USER = raw_input();

print("Password: ");
PASS = raw_input();

print("Working...");

f = open("data2.txt", "w")
f.close()

service = service.Service('../chromedriver');
service.start()
capabilities = {'chrome.binary': '/path/to/custom/chrome'}

driver = webdriver.Remote(service.service_url, capabilities);
driver.get('https://www.instagram.com/justinbieber/followers/');


username = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/article/div/div[1]/div/form/div[1]/input');
password = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/article/div/div[1]/div/form/div[2]/input');

login    = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/article/div/div[1]/div/form/span/button');

username.clear();
username.send_keys(USER);

password.clear();
password.send_keys(PASS);

login.click();

print("Please wait...");

time.sleep(8);

loop = 1;

while (loop) :

	driver.refresh();

	driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/article/header/div[2]/ul/li[2]').click();

	time.sleep(2.5);

	driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/ul/li[1]/div/div[2]/span/button').click();
	count = count + 1;
	driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/ul/li[2]/div/div[2]/span/button').click();
	count = count + 1;
	driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/ul/li[3]/div/div[2]/span/button').click();
	count = count + 1;
	driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/ul/li[4]/div/div[2]/span/button').click();
	count = count + 1;
	driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/ul/li[5]/div/div[2]/span/button').click();
	count = count + 1;
	driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/ul/li[6]/div/div[2]/span/button').click();
	count = count + 1;
	driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/ul/li[7]/div/div[2]/span/button').click();
	count = count + 1;
	driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/ul/li[8]/div/div[2]/span/button').click();
	count = count + 1;
	driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/ul/li[9]/div/div[2]/span/button').click();
	count = count + 1;
	print(count);
else:
	print("Finished");