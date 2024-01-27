import requests
import fake_useragent
import json
from bs4 import BeautifulSoup
import xlsxwriter

ua = fake_useragent.UserAgent()
mymyWookBook = xlsxwriter.Workbook('dongCheDi.xlsx')
mymyWookSheet = mymyWookBook.add_worksheet('sheet1')




# 根据系列号码查询具体数据



# 获取车品牌id号码
def getID():

    id = []
    idHeaders = {'User-Agent':ua.random}
    idAjaxUrl = 'https://www.dongchedi.com/motor/pc/car/brand/select_series_v2?aid=1839&app_name=auto_web_pc'
    
    for i in range(2):
        idAjaxResponse = requests.post(url=idAjaxUrl, data={'country':'3','sort_new':'hot_desc','city_name':'南京','limit':'30','page':str(i+1)}
                                    ,headers=idHeaders)
        idAjaxData = json.loads(idAjaxResponse.text)
        
        for k in range(len(idAjaxData["data"]["series"])):
            data = idAjaxData["data"]["series"][k]["id"]
            id.append(data)
            
    return id


    
# 根据id获取数据 datalist一维数组存放所有数据 [i/n][i/n+m]
# 结构: div(有data-row-anchor属性)->div->
def getData(id):
    allData = []
    datacount = 0

    #开始写入行数和列数
    dataWidthStart = 0
    dataHeightStart = 0
    

    
    
    
    for j in range(1):
        dataUrl = 'https://www.dongchedi.com/auto/params-carIds-x-' + str(id[j])
        dataHeader = {'User-Agent':ua.random}
        dataResponse = requests.get(url=dataUrl, headers=dataHeader)

        dataSoup = BeautifulSoup(dataResponse.text, 'lxml')

        # 获取类别
        for k in range(len(dataSoup.select('div[data-row-anchor]'))):
            
            dataWidth = len(list(dataSoup.select('div[data-row-anchor]')[k].children))
            dataWidthStart = dataWidthStart + 1
            index = 0
            dataHeightStart = 0

            # 将数据填入列表
            for l in dataSoup.select('div[data-row-anchor]')[k].children:

                
                allData.append(l.string)
                dataHeightStart = dataHeightStart + 1
                
                mymyWookSheet.write(dataWidthStart, dataHeightStart, l.string)
                print('write successful')
                
                
                print(allData[datacount])
                datacount = datacount+1
                index = index + 1
                
                



        


# 主函数
def main():
    carid = getID()
    print(carid)
    getData(carid)
    mymyWookBook.close()
    


    



main()
