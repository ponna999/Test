import os

release = str(input("Enter the release name:"))
drop = str(input("Enter the drop details EX:- Drop1,Drop2,Drop3........"))



source ='D:\\pythontest\\original'
destination = 'R:\\Software\\MultiApp\\Extension_Packages\\WX\\HLR'
destination1 = 'R:\\Software\\MultiApp\\Extension_Packages\\WX\\3GPPHSS'
destination2 = 'R:\\Software\\MultiApp\\Extension_Packages\\WX\\5G'
destination3 = 'R:\\Software\\MultiApp\\Extension_Packages\\WX\\IMS\\HSSIMS'
destination4 = 'R:\\Software\\MultiApp\\Extension_Packages\\WX\\IMSLTE\\HSSEPS'
destination5 = 'R:\\Software\\MultiApp\\Extension_Packages\\WX\\3GPPHSS\\LI3GPPHSS'
destination6 = 'R:\\Software\\MultiApp\\Extension_Packages\\WX\\CommonHlrHss'


a = os.listdir(source)

# CommonHLRHSS
for i in a:
    if 'CommonHLRHSS' in i:
        os.popen('mkdir' + " " + destination6 + '\\' + release + '\\' + drop + '\\' )
        os.popen('copy ' + '\"'+source + '\\' + i + '\"'+ " " + '\"'+destination6 + '\\' + release + '\\' + drop + '\\')
    elif 'HLR' in i:
        os.popen('mkdir' + " " + destination + '\\' + release + '\\' + drop + '\\' )
        os.popen('copy ' + '\"'+source + '\\' + i + '\"'+ " " + '\"'+destination + '\\' + release + '\\' + drop + '\\')
    elif 'HSSIMS' in i:
        os.popen('mkdir' + " " + destination3 + '\\' + release + '\\' + drop + '\\' )
        os.popen('copy ' + '\"'+source + '\\' + i + '\"'+ " " + '\"'+destination3 + '\\' + release + '\\' + drop + '\\')
    elif 'HSSEPS' in i:
        os.popen('mkdir' + " " + destination4 + '\\' + release + '\\' + drop + '\\' )
        os.popen('copy ' + '\"'+source + '\\' + i + '\"'+ " " + '\"'+destination4 + '\\' + release + '\\' + drop + '\\')
    elif 'UDM5G' in i:
        os.popen('mkdir' + " " + destination2 + '\\' + release + '\\' + drop + '\\' )
        os.popen('copy ' + '\"'+source + '\\' + i + '\"'+ " " + '\"'+destination2 + '\\' + release + '\\' + drop + '\\')
    elif '3GPPHSS' in i:
        os.popen('mkdir' + " " + destination1 + '\\' + release + '\\' + drop + '\\' )
        os.popen('copy ' + '\"'+source + '\\' + i + '\"'+ " " + '\"'+destination1 + '\\' + release + '\\' + drop + '\\')
    elif 'LI3GPPHSS' in i:
        os.popen('mkdir' + " " + destination5 + '\\' + release + '\\' + drop + '\\' )
        os.popen('copy ' + '\"'+source + '\\' + i + '\"'+ " " + '\"'+destination5 + '\\' + release + '\\' + drop + '\\')
    else:
        continue

for i in a:
    if 'CommonHLRHSS_irn' in i:
        os.popen('copy ' + '\"' + source + '\\' + i + '\"' + " " + '\"' + destination6 + '\\' + release + '\\' + drop + '\\')
    elif 'HLR_irn' in i:
        os.popen('copy ' + '\"' + source + '\\' + i + '\"' + " " + '\"' + destination + '\\' + release + '\\' + drop + '\\')
    elif 'HSSIMS_irn' in i:
        os.popen('copy ' + '\"' + source + '\\' + i + '\"' + " " + '\"' + destination3 + '\\' + release + '\\' + drop + '\\')
    elif 'HSSEPS_irn' in i:
        os.popen('copy ' + '\"' + source + '\\' + i + '\"' + " " + '\"' + destination4 + '\\' + release + '\\' + drop + '\\')
    elif 'UDM5G_irn' in i:
        os.popen('copy ' + '\"' + source + '\\' + i + '\"' + " " + '\"' + destination2 + '\\' + release + '\\' + drop + '\\')
    elif '3GPPHSS_irn' in i:
        os.popen('copy ' + '\"' + source + '\\' + i + '\"' + " " + '\"' + destination1 + '\\' + release + '\\' + drop + '\\')
    elif 'LI3GPPHSS_irn' in i:
        os.popen('copy ' + '\"' + source + '\\' + i + '\"' + " " + '\"' + destination5 + '\\' + release + '\\' + drop + '\\')
    else:
        continue

for i in a:
    if 'CommonHLRHSS_crn' in i:
        os.popen('copy ' + '\"' + source + '\\' + i + '\"' + " " + '\"' + destination6 + '\\' + release + '\\' + drop + '\\')
    elif 'HLR_crn' in i:
        os.popen('copy ' + '\"' + source + '\\' + i + '\"' + " " + '\"' + destination + '\\' + release + '\\' + drop + '\\')
    elif 'HSSIMS_crn' in i:
        os.popen('copy ' + '\"' + source + '\\' + i + '\"' + " " + '\"' + destination3 + '\\' + release + '\\' + drop + '\\')
    elif 'HSSEPS_crn' in i:
        os.popen('copy ' + '\"' + source + '\\' + i + '\"' + " " + '\"' + destination4 + '\\' + release + '\\' + drop + '\\')
    elif 'UDM5G_crn' in i:
        os.popen('copy ' + '\"' + source + '\\' + i + '\"' + " " + '\"' + destination2 + '\\' + release + '\\' + drop + '\\')
    elif '3GPPHSS_crn' in i:
        os.popen('copy ' + '\"' + source + '\\' + i + '\"' + " " + '\"' + destination1 + '\\' + release + '\\' + drop + '\\')
    elif 'LI3GPPHSS_crn' in i:
        os.popen('copy ' + '\"' + source + '\\' + i + '\"' + " " + '\"' + destination5 + '\\' + release + '\\' + drop + '\\')
    else:
        continue