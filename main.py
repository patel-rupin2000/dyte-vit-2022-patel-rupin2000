def versionCompare(v1, v2):
    arr1 = v1.split(".")
    arr2 = v2.split(".")
    n = len(arr1)
    m = len(arr2)

    arr1 = [int(i) for i in arr1]
    arr2 = [int(i) for i in arr2]
    if n > m:
        for i in range(m, n):
            arr2.append(0)
    elif m > n:
        for i in range(n, m):
            arr1.append(0)
    for i in range(len(arr1)):
        if arr1[i] > arr2[i]:
            return 1
        elif arr2[i] > arr1[i]:
            return -1
    return 0
import sys
import json
import wget
print("\nArguments passed:", end=" ")
for i in range(1, len(sys.argv)):
    print(sys.argv[i], end=" ")
import pandas as pd
df = pd.read_csv(str(sys.argv[1]))
t=df['repo']
names=df['name']
t.to_numpy()
names.to_numpy()
s=""
print(t)
versions=[]
check=[]
for i in range (0,len(t)):
    s=t[i].replace("github.com","raw.githubusercontent.com")
    s+="master/package.json"
    print(s)
    file_name = wget.download(s,"jsonfiles/"+names[i]+'.json')
    f = open("jsonfiles/"+names[i]+'.json')
    data = json.load(f)
    print(data['dependencies'][sys.argv[2].split('@')[0]])
    current_version=data['dependencies'][str(sys.argv[2].split("@")[0])][1:]
    versions.append(current_version)
    ans = versionCompare(current_version, sys.argv[2].split('@',1)[1])
    if ans < 0:
        check.append(False)
    else:
        check.append(True)
df['version']=versions
df['version_satisfied']=check
df.to_csv('result.csv')



