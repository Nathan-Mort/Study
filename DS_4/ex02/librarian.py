import os

def install_libs():
    is_env = os.getenv('VIRTUAL_ENV')
    try:
        if is_env and os.path.basename(is_env) == 'helenwav':
            os.system('pip install -r install.txt')
            os.system('pip freeze')
            os.system('pip freeze > requirements.txt')
            os.system('tar -cf helenwav.tar helenwav')
        else:
            print("No active env or incorrect env")
    except KeyError:
        print("No active env")
    
if __name__ == '__main__':
    install_libs()