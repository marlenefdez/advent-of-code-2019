# advent of code, day 1, puzzle one
def get_mass(module_mass):
    return module_mass // 3 - 2 

module_masses = open('input-aof-2019-12-01-01.txt','r')

total_sum = 0
for module_mass in module_masses:
    total_sum += get_mass(int(module_mass))

module_masses.close()

print("the total sum is {}".format(total_sum))

