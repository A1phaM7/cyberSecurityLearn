from sys import stderr, stdout
import paramiko
transport = paramiko.Transport(('192.168.104.130'), 22)
transport.connect(username='root', password='')

ssh = paramiko.SSHClient()
ssh._transport = transport
sftp = paramiko.SFTPClient.from_transport(transport)

stdin, stdout, stderr = ssh.exec_command('ls /opt')
print(stdout.read().decode())

# 传输文件