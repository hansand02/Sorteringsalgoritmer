import innlevering2runner
import sys
import svartest
ALGS = ["insertion", "quick", "merge", "selection", "bubble"]
def main(filename):
    with open(filename, 'r') as f:
        A = [int(x) for x in f.readlines()]
    innlevering2runner.run_algs_part1(A, filename)
    innlevering2runner.run_algs_part2(A, filename)
    
    with open(filename + "_is_sorted.out", 'w') as file:
        for algs in ALGS:
            string = svartest.testRekkefolge(filename+"_"+algs+".out")
            file.write(string + "\n")
if __name__ == '__main__':
    main(sys.argv[1])

