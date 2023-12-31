import paramiko
from cred import *

def download_file_from_pi(remote_path, local_path):

    # Create an SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the Raspberry Pi
        ssh.connect(pi_ip_address, username=pi_username, password=pi_password)

        # Create an SFTP session
        sftp = ssh.open_sftp()

        # Download the file
        sftp.get(remote_path, local_path)

        print(f"File downloaded from {remote_path} to {local_path}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the SFTP session and SSH connection
        if sftp:
            sftp.close()
        ssh.close()

if __name__ == "__main__":
    # Specify the remote and local paths
    remote_file_path = '/home/wraith/Desktop/output.txt'
    local_file_path = 'C:/Users/Wraith/Desktop/Project/Code/1.txt'

    # Download the file from the Raspberry Pi to the local machine
    download_file_from_pi(remote_file_path, local_file_path)
