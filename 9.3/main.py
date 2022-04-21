from pathlib import Path
from loguru import logger
import mkdir

logger.add ('record.log')

our_files = Path.cwd() / 'directory'


'''files содержит имеено файлы из директории (directory)'''
files = (file_dir for file_dir in our_files.iterdir() if file_dir.is_file())

'''итерация по последнему компоненту без suffix'''
for file in files:
    old_name = file.stem
       
    '''разложл название файла в три переменнеы'''
    year, month, date = old_name.split('-')

    '''задал новое имя фалов'''
    new_file = f'{date}{file.suffix}'

    '''объединение пути с каждым аргументом по очереди'''
    new_dir = our_files.joinpath(year, month)
         
    '''создание новых каталогов по году имесяцу'''
    new_dir.mkdir(parents=True, exist_ok=True)

    new_file_path = new_dir.joinpath(new_file)
    logger.info ("Join file")
    
    '''перемещение файлов с новым именем в нужные директории'''
    file.replace(new_file_path)
    logger.critical ("Replace")
    '''логи добавил но бесцельно, пока разбираюсь как их применять =)'''
    
    
    



