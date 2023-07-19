import r2pipe
import argparse
import sys

parser = argparse.ArgumentParser(
    prog='getInfo',
    description='Get exports or imports from  binary.\n Requires Radare2.')
parser.add_argument('--file', type=str, help='file to open')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--exports', action='store_const', const=1)
group.add_argument('--imports', action='store_const', const=2)
args = parser.parse_args()

file_to_open = ""

if args.file:
    file_to_open = args.file
else:
    sys.exit(1)

pipe_cmd = ''

if args.exports == 1:
    pipe_cmd = 'iEj'
else:
    pipe_cmd = 'iij'

pipe = r2pipe.open(file_to_open)
json = pipe.cmdj('iEj')

for x in range(len(json)):
    print(json[x]['name'])









