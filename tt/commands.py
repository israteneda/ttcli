from tt.instructions import help


def check(argv):
    if argv == "-h":
        print(help())
