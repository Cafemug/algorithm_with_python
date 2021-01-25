import sys

def print_result(arr, i, j):
    for x in range(9):
        if x != i and x != j: 
            print(arr[x])
    
def filter_dwarf(dwarf_list):
    total_sum = sum(dwarf_list)
    for i in range(9):
        for j in range(9):
            if i != j:
                if total_sum - dwarf_list[i] - dwarf_list[j] == 100:
                    print_result(dwarf_list, i, j)
                    return
def main():
    dwarf_list = []
    for _ in range(9):
        dwarf_list.append(int(sys.stdin.readline()))

    dwarf_list.sort()
    filter_dwarf(dwarf_list)

main()
                
            
