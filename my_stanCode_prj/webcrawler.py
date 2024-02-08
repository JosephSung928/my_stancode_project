"""
File: webcrawler.py
Name: Joseph_Sung
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #

        # get the tags from the table which class name is 't-stripe'
        tags = soup.find_all('table', {'class': 't-stripe'})

        # variables to calculate the total population of boys and girls
        male_num = 0
        female_num = 0

        for tag in tags:
            # get the text in the 'tbody'.
            target = tag.tbody.text
            print(target[:5])
            # split the text into a list and remove unnecessary content (the last 22 pieces of data)
            target = target.split()
            target = target[:-22]

            # divide the list into groups ( Every group contains five tokens)
            for i in range(len(target)//5):

                # get the second ones from every five pieces of data which represent the number of boys.
                male = target[2+i*5]
                # The number contains commas and needs to be processed. (EX. 197,000)
                male = male.split(',')
                male = int(male[0])*1000 + int(male[1])
                male_num += male

                # get the forth ones from every five pieces of data which represent the number of girls.
                female = target[4+i*5]
                # The number contains commas and needs to be processed. (EX. 197,000)
                female = female.split(',')
                female = int(female[0])*1000 + int(female[1])
                female_num += female

        print("Male Number: " + str(male_num))
        print(f"Female Number: {str(female_num)}")


if __name__ == '__main__':
    main()
