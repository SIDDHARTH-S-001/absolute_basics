import argparse

parser = argparse.ArgumentParser()
# 1) Basic operation.
# parser.add_argument("echo", help="echo the string you use here")
# args = parser.parse_args()
# print(args.echo)

# 2) Performing operations.
# parser.add_argument("square", help="display square of a given number", type=int)
# args = parser.parse_args()
# print(args.square**2)

# 3) Optional arguments, short options & actions.
# parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="store_true")
# args = parser.parse_args()
# if args.verbosity:
#     print("verbosity turned on")
# else:
#     print("verbose off")

# 4) Combining positional & optional args.
parser.add_argument("square", type=int, help="display square of teh requested number")
parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbose:
    print(f"Square of {args.square} = {answer}")
else:
    print(answer)