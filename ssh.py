import paramiko 

host = 'localhost'
user = 'sergey'
secret = '020986'
port = 2222

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=secret, port=port)
stdin, stdout, stderr = client.exec_command('rm ~/test.txt')
data = stdout.read() + stderr.read()
client.close()
