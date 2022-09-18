from selenium import webdriver
from time import sleep
from func import initBrowser

url = ""
chooseLink = input("all - nimoshow - gta5 - lol - pubg - pubgm - csgo - luachua: ")
if chooseLink == "all":
    url = "https://www.nimo.tv/lives"
if chooseLink == "nimoshow":
    url = "https://www.nimo.tv/game/185"
if chooseLink == "gta5":
    url = "https://www.nimo.tv/game/gta5"
if chooseLink == "lol":
    url = "https://www.nimo.tv/game/lol"
if chooseLink == "pubg":
    url = "https://www.nimo.tv/game/pubg"
if chooseLink == "pubgm":
    url = "https://www.nimo.tv/game/pubgm"
if chooseLink == "csgo":
    url = "https://www.nimo.tv/game/csgo"
if chooseLink == "luachua":
    url = "https://www.nimo.tv/game/freefire"
if chooseLink == "":
    url = "https://www.nimo.tv/lives"

tabDemand = input("Nhập số Tab cần chạy: ")
timeTillNextTab = input("Nhập thời gian mở Tab mới: ")
country = input("Nhập vùng cần chạy('vn', 'gl', 'tr', 'mr', 'ind'): ")
initBrowser.Browser(url, tabDemand, timeTillNextTab, country)







# Close driver
# hello.driver.close()