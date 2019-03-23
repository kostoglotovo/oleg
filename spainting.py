import matplotlib as mlt
from matplotlib import pyplot

def create_timeaxis(filepath):#获得打鼾时间点的列表
    fp=open('d:/sneeze.log',encoding='gb18030', errors='ignore')
    lines=fp.readlines()
    fp.close
    timeaxis=[]
    flag =0
    out=[]
    for item in lines:
        if item[-2]=="0":
            flag=0
        elif item[-2]=="1":
            if flag==0:
                out.append(item)
                flag=1
            else:
                continue

    for az in out:
        if az[11]=='2' and az[12]=='2':
            timeaxis.append('22')
        elif az[11]=='2' and az[12]=='3':
            timeaxis.append('23')
        elif az[11]=='2' and az[12]=='4':
            timeaxis.append('24')
        elif az[11]=='0' and az[12]=='1':
            timeaxis.append('01')
        elif az[11]=='0' and az[12]=='2':
            timeaxis.append('02')
        elif az[11]=='0' and az[12]=='3':
            timeaxis.append('03')
        elif az[11]=='0' and az[12]=='4':
            timeaxis.append('04')
        elif az[11]=='0' and az[12]=='5':
            timeaxis.append('05')
        elif az[11]=='0' and az[12]=='6':
            timeaxis.append('06')
        elif az[11]=='0' and az[12]=='7':
            timeaxis.append('07')
        else:
            timeaxis.append('08')
    return(timeaxis)

def spainting(snz):
    snz_freq={}#统计某一时间点的打鼾次数
    timexs=['22','23','24','01','02','03','04','05','06','07','08']
    for x in snz:
        snz_freq[x]=snz_freq.get(x,0)+1
    pyplot.bar(range(11),[snz_freq.get(xtick,0) for xtick in timexs], align='center')
    pyplot.xticks(range(11),timexs)
    pyplot.show()

filepath='d:/sneeze.log'
snz=create_timeaxis(filepath)
spainting(snz)