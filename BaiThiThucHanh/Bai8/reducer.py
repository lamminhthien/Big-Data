import sys

( current_year,  max_temperature ) = (None, -sys.maxsize)
elevation_in_max_temperature = None
for line in sys.stdin:
  (year,elevation,temperature) = line.strip().split("\t")
  if current_year != None and current_year != year:
    print("%s\t%s" % (current_year, elevation))
    (current_year, max_temperature) = (year, int(temperature))
  else:
    # (current_year, max_temperature) = (year, max(max_temperature, int(temperature)))
    current_year = year
    current_temperature = int(temperature)
    if (current_temperature > max_temperature):
        max_temperature = current_temperature
        elevation_in_max_temperature = elevation
        
  
# In ra kết quả cho năm cuối cùng:
if current_year:
  print("%s\t%s" % (current_year, elevation))