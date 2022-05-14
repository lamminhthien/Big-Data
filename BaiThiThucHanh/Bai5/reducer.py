#!/usr/bin/python3

import sys

sum_of_temperature_of_year, number_of_temperature_measure = (0,0)

current_year = None
for line in sys.stdin:
  (year, temperature) = line.strip().split("\t")
  sum_of_temperature_of_year = sum_of_temperature_of_year + int(temperature)
  number_of_temperature_measure = number_of_temperature_measure + 1
  if current_year and current_year != year:
    print(f"{current_year}\t{round(sum_of_temperature_of_year/number_of_temperature_measure)}")
    current_year = year
    sum_of_temperature_of_year, number_of_temperature_measure = (0,0)
  else:
    current_year = year

if current_year:
  print(f"{current_year}\t{round(sum_of_temperature_of_year/number_of_temperature_measure)}")