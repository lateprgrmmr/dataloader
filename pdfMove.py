import glob
import shutil

# for file in glob.glob('path_to_dir/apple*'):
#     shutil.move(file, new_dst)


# # a list of file types
# vendors =['path_to_dir/apple*', 'path_to_dir/intel*']

# for file in vendors:
#      for f in (glob.glob(file)):
#          if "apple" in f: # if apple in name, move to new apple dir
#              shutil.move(f, new_apple_dir)
#          else:
#              shutil.move(f, new_intel_dir) # else move to intel dir

filepaths = []
for filepath in glob.iglob('/Users/kevinbratt/Downloads/RollinsExport/*'):
    filepaths.append(filepath)

new_dest = '/Users/kevinbratt/Downloads/RollinsContracts'

contract_pdfs = []
for i in filepaths:
    for j in glob.iglob(i + '/Contracts/*.pdf'):
        contract_pdfs.append(j)
# print(contract_pdfs[1])
for pdf in contract_pdfs:
    # pdf = pdf.replace('/Users/kevinbratt/Downloads/RollinsExport/', '')
    shutil.move(pdf, new_dest)
# print(pdf)
