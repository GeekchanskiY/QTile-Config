from subprocess import check_output

a = str(check_output(['docker container ps -a'], shell=True)).split('\\n')


a = a[1:len(a)-1]
for z in a:
    print(z)
    print('\n\n\n')
