import re
def check_reg_num(reg_num: str):
    reg_num = reg_num.upper()
    if re.match(r'[АВЕКМНОРСТУХ]{1}[0-9]{3}[АВЕКМНОРСТУХ]{2}[0-9]{2,3}$',reg_num):#проверяем номер на соответствие шаблону
        number = re.search(r'[АВЕКМНОРСТУХ]{1}[0-9]{3}[АВЕКМНОРСТУХ]{2}',reg_num).group(0)#берем номер
        region = re.search(r'.{2}(?=($|\r|\n))',reg_num).group(0)#берем регион (две последних цифры)
        print(f'Номер {number} валиден, регион {region}')
    else:
        print('Номер не валиден')
        
check_reg_num('У162УС777')
check_reg_num('А343ВС77')
check_reg_num('А943ИС77')
check_reg_num('А675ВС7777')
check_reg_num('е777кх777')

check_reg_num('У128ЕР999')
check_reg_num('ш128хф325')