#!/usr/bin/env python3

def file_extensions(filename):
    ext_files = {}
    no_ext_files = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if '.' in line:
                #print(line.rindex('.'))
                #ext = line[line.rindex('.')+1:]
                ext = line.split('.')[-1]
                if ext in ext_files:
                    ext_files[ext].append(line)
                else:
                    ext_files[ext] = [line]
            else:
                no_ext_files.append(line)
    return (no_ext_files, ext_files)

def main():
    noext, w_ext = file_extensions(r'C:\Users\soren\OneDrive\Desktop\PythonData-1\øvelser\e27_file_extensions\src\filenames.txt')
    print(noext, w_ext)
    print(len(noext), "files with no extension")
    for k, v in w_ext.items():
        print(k, len(v))

if __name__ == "__main__":
    main()
