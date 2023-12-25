import unidecode as unide
from read_file import get_data 
from constant import filepath   

result = get_data(filepath)

def remove_command():
    with open("text_processing\output_remove_com,and.txt", "w", encoding="UTF8") as outputfile:
        for sublist in result:
            updated_sublist = [unide.unidecode(text) for text in sublist]
            updated_line = '\t'.join(updated_sublist) + '\n'  
            outputfile.write(updated_line)

remove_command()
