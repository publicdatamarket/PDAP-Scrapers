import tabula
import os

cur_dir = os.getcwd()
directory = cur_dir + "/USA/GA/Norcross/pdfs/"
folder = directory + "/tables/"
"""
if not os.path.isdir(folder):
	os.makedirs(folder)

for file in os.listdir(directory):
	print(file)
	doc = directory + file
	folder_name = file.replace('.pdf','/')
	table = tabula.read_pdf(doc, pages='all')

	for i, table in enumerate(file	, start=1):
		table.to_excel(os.path.join(folder_name, f"table_{i}.xlsx"), index=False)

	#print(data_table)

"""


def save_file(file):
    print(file)
    tables = tabula.read_pdf(
        directory + file, pages="all"
    )  # This loads the pdf into tabula
    print("Read")

    folder_name = folder + file.replace(
        ".pdf", "/"
    )  # Converts the file's name into a folder
    print(folder_name)

    # save them in a folder
    if not os.path.isdir(folder_name):
        print("Making folder")
        os.makedirs(folder_name)

    # iterate over extracted tables and export as excel individually
    for i, table in enumerate(tables, start=1):
        table.to_excel(os.path.join(folder_name, f"table_{i}.xlsx"), index=False)


# read PDF file
for file in os.listdir(directory):
    save_file(file)
