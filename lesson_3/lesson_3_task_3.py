from adress import Adress
from mailing import Mailing


adress_1 = Adress(120250, 'г. Москва', 'ул. Лубянка', 21, 7)
adress_2 = Adress(270123, 'г. Санкт-Петербург', 'ул. Садовая', 10, 15)


mailing_1 = Mailing(adress_1.fulladress, adress_2.fulladress, 100, '1234567890')

mailing_1.printMailing()