import os

table = '_abcdefghijklmnopqrstuvwxyz{}ABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@[\\]^\`\|~0123456789'

#'_abcdefghijklmnopqrstuvwxyz{}ABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@[\\]^\`\|~0123456789'
pin = '/root/echo/Tools/pin-3.7/pin'
binary = '/root/echo/ctf/StrangeInterpreter'
#binary = 'C:\\Users\\echo\\Desktop\\task\\rc4\\simple_rc4.exe'
dll = '/root/echo/Tools/pin-3.7/source/tools/ManualExamples/obj-intel64/inscount0.so'
mfile='/root/echo/Tools/pin-3.7/source/tools/ManualExamples/inscount.out'
def getCount(flag):
    os.system('echo '+flag+' |'+pin+' -t '+dll+' -o '+mfile+' -- '+binary+'>ins9.out')
    with open("/root/echo/Tools/pin-3.7/source/tools/ManualExamples/inscount.out") as f:
        count = int(f.read().split(" ")[1])
    return count
# print getCount('1')
# print getCount('E')
# print getCount('EI')

# '''
ans = 'X-NUCA{5e77'
flag = list(ans)

for i in range(21):
    flag.append('+')
#'X-NUCA{1e3c3c5ed75e5e771e11115e'
# print flag
# '''
base =  getCount(''.join(flag))
print base

print flag
for j in range(len(ans),40):
    print '-------------------Round %d-------------'%j
    for i in table:
        flag[j] = i
        data =  getCount(''.join(flag))
        print data,''.join(flag)
        if data == base-650:
            print ''.join(flag)
            base = data
            break

print ''.join(flag)
# '''
