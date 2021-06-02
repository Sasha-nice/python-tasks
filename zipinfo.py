"""
Программа, которой на стандартный ввод подаётся zip-архив в виде 
шестнадцатеричного дампа (последовательность шестнадцатеричных цифр, возможно, 
разделённых пробелами и переводами строки), а на выходе она показывает 
количество и суммарный объём хранящихся в нём файлов, если их распаковать.
"""
import zipfile
import io
import re
print(
    len(
        re.findall(
            r"file_size=(\d+)",
            str(zipfile.ZipFile(
                io.BytesIO(bytes.fromhex(open('input.txt').read()))
            ).infolist())
        )
    ),
    sum(
        int(x) for x in re.findall(
            r"file_size=(\d+)",
            str(zipfile.ZipFile(
                io.BytesIO(bytes.fromhex(open('input.txt').read()))
            ).infolist())
        )
    )
)