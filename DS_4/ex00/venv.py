from os import getenv

def env_check():
    is_env = getenv('VIRTUAL_ENV')
    if is_env:
        print(f"Your current virtual env is {is_env}")
    else:
        print("Virtual environment is not activated")
        
if __name__ == '__main__':
    env_check()
    
# создать виртуальное окружение python3 -m venv helenwav
# активация \ деактивация вирт среды source helenwav/bin/activate \ deactivate
