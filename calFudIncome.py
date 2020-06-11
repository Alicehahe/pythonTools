#coding:utf-8
'''
 @author:HanLu
 @description:这段代码用于计算基金卖出时可获得收益及基金收益率
 
'''

def test():
    while 1:
        jingzhiNow = input("请输入当前净值：")
        jingzhiBuy = input("请输入购买时净值：")
        buy_num = input("请输入购买的净值份额：")
        buy_money = input("请输入你购买花费金额：")
        rate = input("请输入卖出收费利率：")

        shouxufei = float(jingzhiNow)*float(buy_num)*float(rate)
        income = (float(jingzhiNow)-float(jingzhiBuy))*float(buy_num)
        print("您的收益为：",'%.2f' %(income-shouxufei),"元")
        print("您的收益率为：",('%.2f' %(('.2f' %income)/int(buy_money)*100)),'%')
        print('=============================')

if __name__ == '__main__':
    test()