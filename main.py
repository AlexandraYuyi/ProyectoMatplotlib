import csv
import matplotlib.pyplot as plt


def read_csv(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data


def filter_data(data, year, continent):
    index = str(year) + " Population"
    filtered_countries = list(
        filter(lambda country: country['Continent'] == continent, data))
    filtered_countries = {country['Country/Territory']: int(country[index]) for country in filtered_countries}
    return filtered_countries


def barchart(data):

    labels = list(data.keys())
    values = list(data.values())
    plt.barh(labels, values)
    plt.show()


if __name__ == '__main__':
    filename = './Data/world_population.csv'

    band = True
    print("Population by yearn and continent")
    try:
        while band == True:
            band1 = True
            band2 = True
            while band1 == True:
                print("""
                    1. 2022
                    2. 2020
                    3. 2015
                    4. 2010
                    5. 2000
                    6. 1990
                    7. 1980
                    8. 1970
                    9. Exit program""")
                year = input("Select the year: ")
                if year.isnumeric() and year <= "9" and year >= "1":
                    band1 = False
                    match year:
                        case "1":
                            year = 2022
                        case "2":
                            year = 2020
                        case "3":
                            year = 2015
                        case "4":
                            year = 2010
                        case "5":
                            year = 2000
                        case "6":
                            year = 1990
                        case "7":
                            year = 1980
                        case "8":
                            year = 1970
                        case "9":
                            print("\nExiting Program...")
                            quit()
                else:
                    print("Input must be a number between 1 and 9")
            while band2 == True:
                print("""
                    1. Asia
                    2. Africa
                    3. Europe
                    4. North America
                    5. South America
                    6. Exit program""")
                continent = input("Select the continent: ")
                if continent.isnumeric() and (continent <= "6" and continent >= "1"):
                    band2 = False
                    match continent:
                        case "1":
                            continent = "Asia"
                        case "2":
                            continent = "Africa"
                        case "3":
                            continent = "Europe"
                        case "4":
                            continent = "North America"
                        case "5":
                            continent = "South America"
                        case "6":
                            print("\nExiting Program...")
                            quit()
                else:
                    print("Input must be a number between 1 and 6")

                if band1 == False and band2 == False:
                    data = read_csv(filename)
                    data = filter_data(data, year, continent)
                    print(data)
                    print(len(data))
                    barchart(data)
    except Exception as e:
        print(e)
        print("Error, please try again")
        band = True
