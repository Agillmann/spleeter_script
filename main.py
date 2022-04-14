# Spleeter script from deezer for directory
#
# example usage:
# python main.py -f '/home/agq3/dev/python-script/spleeter_script/test-folder' -s 4

import os
import argparse
from numba import cuda
from timeit import default_timer as timer

parser = argparse.ArgumentParser(description=f'Spleeter script\n - example usage : python main.py -f \'/home/agq3/dev/python-script/spleeter_script/test-folder\' -s 4')
parser.add_argument('-f', required=True, help='Input file or directory')
parser.add_argument('-s', required=True, help='2, 4 or 5 for more spleet audio')
parser.add_argument('--gpu', required=False, help='Run with gpu', action='store_true')

args = parser.parse_args()

input_folder = args.f
stems = args.s
gpu = args.gpu

def process(input_folder, stems):
  # For one file
  if os.path.isfile(input_folder):
    file = input_folder.split('/')[-1]
    file_name = file.split('.')[0]
    folder_path = input_folder.split(file)[0]
    print(f"\n##### Start Process {file_name} #####\n")
    start_file = timer()
    os.system(f'spleeter separate -p spleeter:{stems}stems -o {folder_path} \'{input_folder}\'')
    print(f"\nOutput : {folder_path}/{file_name}\n")
    print(f"##### End of {file} -- time: {timer() - start_file}s #####\n")

  # For directory 
  if os.path.isdir(input_folder):
    print(f"\n##### Start Process on {input_folder} #####")
    start = timer()
    for file in os.listdir(input_folder):
      if os.path.isfile(os.path.join(input_folder, file)):
        with open(os.path.join(input_folder, file),'r') as f:
          file_name = file.split('.')[0]
          print(f"\n##### Start Process {file} #####\n")
          start_file = timer()
          os.system(f'spleeter separate -p spleeter:{stems}stems -o {input_folder} \'{input_folder}/{file}\'')
          print(f"\nOutput : {input_folder}/{file_name}\n")
          print(f"##### End of {file} - time: {timer() - start_file}s #####\n")
    print(f"##### End of Process - time: {timer() - start}s #####\n")

# function optimized to run on gpu
@cuda.jit  
def process_gpu(input_folder, stems):
  print('passla')
  process(input_folder, stems)


if gpu is True:
  process_gpu(input_folder, stems)
else: 
  process(input_folder, stems)