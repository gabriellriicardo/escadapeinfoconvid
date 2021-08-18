from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import os


#By Gabriel Ricardo.

chrome_options = Options()
chrome_options.add_argument("-headless")
nav = webdriver.Chrome(options = chrome_options , executable_path = 'chromedriver.exe')
nav.get("https://transparencia.escada.pe.gov.br/app/pe/escada/1/covid-19/gerar_gadget_fluid?boletins=true&vacinacao=true")
os.system ("cls")
time.sleep(2)
f = open('escada.txt', 'r')
g = f.read()
print (g)
time.sleep(5)
os.system ("cls")
print("\n\n---- INFORMES SOBRE O CORONAVÍRUS ESCADA-PE ----")
time.sleep(3)
print("\nCarregando...")
time.sleep(2)
print("Aqui está os informes")
time.sleep(3)
os.system ("cls")
f = open('escada.txt', 'r')
g = f.read()
print (g)
print("\n\n\n---- INFORMES SOBRE O CORONAVÍRUS ESCADA-PE ----")
#DOSES RECEBIDAS E ATUALIZAÇÕES
dosi = nav.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div/div/div/div[1]/div[2]/h2')
atd = nav.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div/div/div/div[2]/div/small')
doses = dosi.text
atd1 = atd.text
print ("\n\nPESSOAS QUE RECEBERAM A 1º DOSE: ({}) ----------- {} ".format(doses, atd1))

#DOSES APLICADAS E ATUALIZAÇÕES
dosia = nav.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/h2')
atda = nav.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/small')
dosesa = dosia.text
atda1 = atda.text
print ("\nPESSOAS QUE RECEBERAM A 2º DOSE: ({}) ----------- {} ".format(dosesa, atda1))

#1º DOSE APLICADA E ATUALIZAÇÕES
dosia1 = nav.find_element_by_xpath('/html/body/div/div/div/div[2]/div[3]/div/div/div/div[1]/div[2]/h2')
atda1 = nav.find_element_by_xpath('/html/body/div/div/div/div[2]/div[3]/div/div/div/div[2]/div/small')
dosesa1 = dosia1.text
atda11 = atda1.text
print ("\nDOSE UNICA: ({}) ----------------------------------- {} ".format(dosesa1, atda11))

#2º DOSE APLICADA E ATUALIZAÇÕES
dosia2 = nav.find_element_by_xpath('/html/body/div/div/div/div[2]/div[4]/div/div/div/div[1]/div[2]/h2')
atda2 = nav.find_element_by_xpath('/html/body/div/div/div/div[2]/div[4]/div/div/div/div[2]/div/small')
dosesa2 = dosia2.text
atda12 = atda2.text
print ("\nDOSES APLICADAS: ({}) --------------------------- {} ".format(dosesa2, atda12))

#CASOS INVESTIGADOS
dosiai = nav.find_element_by_xpath('/html/body/div/div/div/div[3]/div[1]/div/div/div/h2')
atdai = nav.find_element_by_xpath('/html/body/div/div/div/div[3]/div[5]/div/div/div/h5')
dosesai = dosiai.text
atda1i = atdai.text
print ("\nCASOS INVESTIGADOS: ({}) ------------------------- Atualizado {}".format(dosesai, atda1i))

#CASOS CONFIRMADOS
dosiac = nav.find_element_by_xpath('/html/body/div/div/div/div[3]/div[2]/div/div/div/h2')
atdac = nav.find_element_by_xpath('/html/body/div/div/div/div[3]/div[5]/div/div/div/h5')
dosesac = dosiac.text
atda1c = atdac.text
print ("\nCASOS CONFIRMADOS: ({}) ---------------------------- Atualizado {}".format(dosesac, atda1c))

#CASOS RECUPERADOS
dosiar = nav.find_element_by_xpath('/html/body/div/div/div/div[3]/div[3]/div/div/div/h2')
atdar = nav.find_element_by_xpath('/html/body/div/div/div/div[3]/div[5]/div/div/div/h5')
dosesar = dosiar.text
atda1r = atdar.text
print ("\nCASOS RECUPERADOS: ({}) ---------------------------- Atualizado {}".format(dosesar, atda1r))

#OBITOS
dosiao = nav.find_element_by_xpath('/html/body/div/div/div/div[3]/div[4]/div/div/div/h2')
atdao = nav.find_element_by_xpath('/html/body/div/div/div/div[3]/div[5]/div/div/div/h5')
dosesao = dosiao.text
atda1o = atdao.text
print ("\nOBITOS: ({}) ---------------------------------------- Atualizado {}".format(dosesao, atda1o))
sair = input ("\n\n\nPRESSIONE ENTER PARA SAIR: ")
print("SAINDO...")
time.sleep(2)
nav.quit()

#By Gabriel Ricardo
