from argparse import ArgumentParser
parser = ArgumentParser()

parser.add_argument('-p','--path',help='path')
parser.add_argument('-v','--version',help = 'version',action = 'store_true')

args = parser.parse_args()
if(args.path):
    print(args.path)
if args.version:
    print("1.0")
