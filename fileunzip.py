# 目录结构是否
# 目


# 往期人物卡下载

# 文件长度为1

# 例外情况，往期人物卡下载.txt
# 打印文件名
# 解压

# 不处理
# 符合规则的处理，不符合的不处理
# 如果没有同名子目录，且检查到mod文件，png文件 

#

import os
import zipfile
import rarfile
from pathlib import Path
import logging

rarfile.UNAR_TOOL = 'D:/Program Files/WinRAR/UnRAR.exe'


# 配置日志记录
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("batch_extract.log"),  # 将日志写入文件
        logging.StreamHandler()  # 同时输出到控制台
    ]
)


class FileMatch:
    def __init__(self,filetype, relate_dir):
        self.filetype = filetype
        self.relate_dir = relate_dir

    def check_file_dir_match(self, current_dir):
        if current_dir.endswith(self.filetype):
            if self.relate_dir in current_dir:
                return True
        return False

def extract_subdirectories(archive_path, target_dir):
    """
    从压缩文件中提取指定的子目录到目标目录。

    :param archive_path: 压缩文件的路径
    :param target_dir: 目标目录的路径
    :param subdirs: 需要提取的子目录列表
    """
    try:
        # 创建目标目录，如果它不存在的话
        Path(target_dir).mkdir(parents=True, exist_ok=True)

        if zipfile.is_zipfile(archive_path):
            with zipfile.ZipFile(archive_path, 'r') as zip_ref:
                #print(zip_ref.namelist(),zip_ref.infolist(),_)
                for member in zip_ref.infolist():
                    member.filename = member.filename.encode('cp437').decode(encoding='gbk')
                    print(member.filename)
                    try:
                        zip_ref.extract(member,path=target_dir)
                        logging.info(f"Extracted {member} from {archive_path} to {target_dir}")
                    except Exception as e:
                        logging.error(f"Failed to extract {member} from {archive_path}: {e}")
        elif rarfile.is_rarfile(archive_path):
            with rarfile.RarFile(archive_path, 'r') as rar_ref:
                for member in rar_ref.infolist():
                    #member.filename = member.filename.encode('cp437').decode(encoding='utf-8')
                    #print(member.filename)
                    try:
                        rar_ref.extract(member, path=target_dir)
                        logging.info(f"Extracted {member} from {archive_path} to {target_dir}")
                    except Exception as e:
                        logging.error(f"Failed to extract {member} from {archive_path}: {e}")
        else:
            logging.warning(f"Unsupported file format: {archive_path}")
    except Exception as e:
        logging.error(f"Failed to process {archive_path}: {e}")


def batch_extract(directory, target_dir):
    """
    批量解压目录中的 .zip 和 .rar 文件，并提取指定的子目录。

    :param directory: 包含压缩文件的目录
    :param target_dir: 目标目录的路径
    :param subdirs: 需要提取的子目录列表
    """
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.zip') or file.endswith('.rar'):
                    archive_path = os.path.join(root, file)
                    try:
                        extract_subdirectories(archive_path, target_dir)
                        logging.info(f"Processed {archive_path}")
                    except Exception as e:
                        logging.error(f"Failed to process {archive_path}: {e}")
    except Exception as e:
        logging.error(f"Failed to walk through directory {directory}: {e}")


# 示例用法
source_directory = 'D:/hs2-resources/test'  # 替换为你的源目录
target_directory = 'D:/hs2-resources/output'  # 替换为你的目标目录

modsFileMatch = FileMatch('zipmod','mods')
UserDataFileMatch = FileMatch('png','UserData')
abdataFileMatch = FileMatch('unity3d','abdata')

batch_extract(source_directory, target_directory)

source_file = 'D:/hs2-resources/test/zipmod.zip'
