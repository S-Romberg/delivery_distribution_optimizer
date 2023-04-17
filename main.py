import csv
from package import Package

class Main:
    with open('WGUPS Package File.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            package = Package(*row)
    with open('Addresses and Hubs.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            print(row)
    with open('Distance.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            print(row)

    def main(self):
        print("Hello World")

    def print_hi(self, name):
        # Use a breakpoint in the code line below to debug your script.
        print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


    # Press the green button in the gutter to run the script.
    if __name__ == '__main__':
        print_hi(None, 'PyCharm')
        main()

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
