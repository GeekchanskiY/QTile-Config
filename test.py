from subprocess import check_output

a = str(len(str(check_output(['docker container ps -a'], shell=True)).split('\\n')))

print(a)
