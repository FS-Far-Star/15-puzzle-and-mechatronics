import paramiko
from cred import *

def take_picture_and_download(pi_ip_address, pi_username, pi_password, local_path):
    # Create an SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the Raspberry Pi
        ssh.connect(pi_ip_address, username=pi_username, password=pi_password)

        # Take a picture
        stdin, stdout, stderr = ssh.exec_command('raspistill -o /tmp/image.jpg')

        # Wait for the command to complete
        stdout.channel.recv_exit_status()

        # Create an SFTP session
        sftp = ssh.open_sftp()

        # Download the picture
        sftp.get('/tmp/image.jpg', local_path)

        print(f"Picture taken and downloaded to {local_path}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the SFTP session and SSH connection
        if sftp:
            sftp.close()
        ssh.close()

def get_picture():
    # Specify the Raspberry Pi credentials and local file path
    local_file_path = 'current_state.jpg'

    # Take a picture and download it from the Raspberry Pi
    take_picture_and_download(pi_ip_address, pi_username, pi_password, local_file_path)
    return None

if __name__ == '__main__':
    get_picture()