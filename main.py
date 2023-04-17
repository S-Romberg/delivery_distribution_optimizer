import csv
from package import Package
from location import Location

class Main:
    locations = []
    packages = []
    with open('data/Packages.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for index, row in enumerate(reader):
            packages.append(Package(*row))
    with open('data/Addresses and Hubs.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for index, row in enumerate(reader):
            locations.append(Location(*row))
    with open('data/Distance.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for index, row in enumerate(reader):
            locations[index].set_distance(row)

    def main(self):
        print("Hello World")

    def print_hi(self, name):
        print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


    # Press the green button in the gutter to run the script.
    if __name__ == '__main__':
        print_hi(None, 'PyCharm')
        main()

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
