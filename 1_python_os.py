import os

def list_directory_contents(path):
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_dir():
                    print('Directory', entry.name)
                elif entry.is_file():
                    print('File:', entry.name)
                else:

                    print('Other:', entry.name)

    except FileNotFoundError:
        print('FileNotFoundError')

    except Exception as e:
        print('ExceptionError', e)

def main():
    path = input('Enter Directory Path: ')
    list_directory_contents(path)

if __name__ == '__main__':
    main()
