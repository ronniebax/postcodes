import csv


def read_zipcodes(csv_file):
    with open(csv_file) as file:
        reader = csv.reader(file)
        area = []
        for row in reader:
            area.append(int(row[0]))
        return area
                    

def postcode_ranges(csv_file):
    zips = read_zipcodes(csv_file)
    nums = sorted(set(zips))
    gaps = [[s, e] for s, e in zip(nums, nums[1:]) if s+1 < e]
    edges = iter(nums[:1] + sum(gaps, []) + nums[-1:])
    return list(zip(edges, edges))


def export_postcodes(postcodes, filename):
    with open(filename, 'w') as file:
        output = csv.writer(file)
        output.writerow(['first', 'last'])
        for row in postcodes:
            output.writerow(row)
        print(f'generated file: {filename}')


def read_excluded(filename):
    with open(filename) as file:
        reader = csv.reader(file)
        postcode_list = []
        next(file)
        for row in reader:
            postcode_list.append(row)
        return [[int(l) for l in r] for r in postcode_list]


def make_included_list(filename):
    [start,end]=[1000,9999]
    excl = read_excluded(filename)
    out = [r for r in [[start,excl[0][0]-1] if start!=excl[0][0] else []] + [[excl[i-1][1]+1, excl[i][0]-1] for i in range(1,len(excl))]+[[excl[-1][1]+1,end] if end!=excl[-1][1] else []] if r]
    return out
