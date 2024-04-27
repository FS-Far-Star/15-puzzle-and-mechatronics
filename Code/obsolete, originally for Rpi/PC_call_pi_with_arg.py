import paramiko
from cred import *

def run_remote_command_with_argument(argument):
    
    # Command to run on the Raspberry Pi with an argument
    command_to_run = f'python3 /home/wraith/Desktop/1.py "{argument}"'

    # Create an SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the Raspberry Pi
        ssh.connect(pi_ip_address, username=pi_username, password=pi_password)

        # Run the command on the Raspberry Pi
        stdin, stdout, stderr = ssh.exec_command(command_to_run)

        # Display the output
        print(stdout.read().decode())
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the SSH connection
        ssh.close()

if __name__ == "__main__":
    # Specify the argument to pass to the Raspberry Pi script
    argument_from_pc = "Hello, Raspberry Pi!"

    # Run the remote command with the specified argument
    run_remote_command_with_argument(argument_from_pc)
