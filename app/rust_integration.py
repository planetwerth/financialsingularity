import subprocess

def call_rust():
    result = subprocess.run(['cargo', 'run'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')
