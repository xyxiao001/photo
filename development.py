import os
import sys
import paramiko
import re

class SshClient():

    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def execute_scp(self, dir_local, dir_remote):
        try:
            scp = paramiko.Transport((self.host, self.port))
            scp.connect(username=self.username, password=self.password)
            sftp = paramiko.SFTPClient.from_transport(scp) # create sftp
            result = sftp.put(dir_local, dir_remote)  # Upload
            print 'sftp result', result
            sftp.close()

        except paramiko.SSHException:
            print '[-] sftp connection %s fail!' % (self.host)
            sys.exit(1)

        except Exception, e:
            print 'Exception', str(e)
            sys.exit(1)

        else:
            print '[-] sftp connection %s correct!' % (self.host)


    def ssh_connect(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(self.host, username=self.username, password=self.password)

        except (paramiko.ssh_exception.AuthenticationException,
            paramiko.ssh_exception.NoValidConnectionsError):

            print '[-] ssh connection %s fail!' % (self.host)
            sys.exit(1)

        else:
            print '[-] ssh connection %s correct!' % (self.host)
            return ssh


    def execute_sudo(self, command):
        ssh = self.ssh_connect()
        command = "sudo -S -p '' %s" % command
        try:
            stdin, stdout, stderr = ssh.exec_command(command)
            stdin.write(self.password + "\n")
            stdin.flush()
            status = stdout.channel.recv_exit_status()
            if status != 0:
                print stderr.readlines()
                print 'this %s is fail' % (command)
                sys.exit(1)
        except Exception, e:
            print 'Exception', str(e)

        return {'out': stdout.readlines(),
                'err': stderr.readlines(),
                'retval': stdout.channel.recv_exit_status()}


    def close(self):
        ssh = self.ssh_connect()
        if ssh is not None:
            ssh.close()
            ssh = None


def execute(filename):
    os.system('mv dist %s' % (filename))
    status = os.system('tar cvzf %s.tar %s/' % (filename, filename))
    client = SshClient(host='192.168.1.104', port=22, username='shendu', password='P@55word')
    if status == 0:
        dir_local = '%s.tar' % (filename)
        dir_remote = '/home/shendu/record/%s.tar' %(filename)
        client.execute_scp(dir_local, dir_remote)
    ret = client.execute_sudo('tar -xzf /home/shendu/record/%s.tar -C /home/shendu/record/' % (filename))
    ret = client.execute_sudo('ln -sf /home/shendu/record/%s/*  /var/www/seer.cnshendu.com/html/' % (filename))
    ret = client.execute_sudo('nginx -t')
    if ret['retval'] == 0:
        client.execute_sudo('nginx -s reload')
    print "  ".join(ret["out"]), "  E ".join(ret["err"]), ret["retval"]

    client.close()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        execute(filename)
    else:
        sys.exit(2)