parser = argparse.ArgumentParser(  
description='Search and replace using regex groups'
)
parser.add_argument(
  '-f', 
  type=argparse.FileType('r'), 
  help='the file or text to search')
parser.add_argument(
  '-i', 
  metavar='input string', 
  type=str,
  help='the string to be searched')
parser.add_argument(
  '-s', 
  metavar='search pattern', 
  type=str,
  help='the pattern to search for')
parser.add_argument(
  '-r', 
  metavar='replacement Pattern', 
  type=str,
  help='the replacement pattern')
parser.add_argument(
  '-o', 
  default=sys.stdout, 
  type=argparse.FileType('w'), 
  help='the file where the output should be written')

args = parser.parse_args()

string = args.i
pattern = args.s
replacement = args.r

args.o.write('tmp')
args.o.close()

