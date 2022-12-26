from datetime import datetime as dt
from os import remove, path


def log_to_file(action, f_path):
    def log(func):
        def wrapper(file):
            if func(file):
                with open(f_path, 'a') as f:
                    f.write(f'Action {action} executed on {file} on {dt.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
            else:
                with open(f_path, 'a') as f:
                    f.write(f'[FAILED] Action {action} executed on {file} on {dt.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
        return wrapper
    return log


@log_to_file('FILE_CREATE', r'file_create.txt')
def create_file(f_path):
    if not path.exists(f_path):
        open(f_path, 'x').close()
        return True
    else:
        return False


@log_to_file('FILE_DELETE', r'file_delete.txt')
def delete_file(f_path):
    if path.exists(f_path):
        remove(f_path)
        return True
    else:
        return False


if __name__ == '__main__':
    create_file(r'createdFile.txt')
    delete_file(r'createdFile.txt')
