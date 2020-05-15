from pdf2image import convert_from_path
import os

current_path = os.getcwd()
# change to pdf files paths
if os.path.isdir(f'{current_path}\pdf_file'):
    current_path = f'{current_path}\pdf_files'
    print(os.listdir(current_path))
    list_files = os.listdir(current_path)
    for i in list_files:
        if i.split('.')[-1] == 'pdf':
            print(i)
            os.mkdir(f'{current_path}\{i}_extracted')
            pages = convert_from_path(f'{current_path}\{i}')
            count = 0
            for page in pages:
                page.save(f'{current_path}\{i}_extracted\{count}.jpg', 'JPEG')
                count += 1
else:
    print_stament = "please place your pdf file in the"
    # for color's lines in terminal
    print(f"\n\t|\x1b[1;30;44m {print_stament} \x1b[1;31;44m pdf_file"
          f" \x1b[0m\x1b[1;30;44m directory \x1b[0m \x1b[0m|", end="")
