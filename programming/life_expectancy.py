
file_path = "life-expectancy.csv"


overall_min_life_expectancy = float('inf')
overall_max_life_expectancy = float('-inf')
overall_min_year = None
overall_max_year = None
overall_min_country = None
overall_max_country = None


with open(file_path) as life_file:
    next(life_file)
    for line in life_file:
        data = line.strip().split(',')
        year = int(data[0])
        country = data[1]
        life_expectancy = float(data[2])

        if life_expectancy < overall_min_life_expectancy:
            overall_min_life_expectancy = life_expectancy
            overall_min_year = year
            overall_min_country = country
        
        if life_expectancy > overall_max_life_expectancy:
            overall_max_life_expectancy = life_expectancy
            overall_max_year = year
            overall_max_country = country


while True:
    try:
        input_year = int(input("Enter the year of interest: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid year.")


count = 0
sum_life_expectancy = 0.0
min_life_expectancy_year = float('inf')
max_life_expectancy_year = float('-inf')
min_country_year = None
max_country_year = None

with open(file_path) as life_file:
    next(life_file)
    
    for line in life_file:
        data = line.strip().split(',')
        year = int(data[0])
        country = data[1]
        life_expectancy = float(data[2])

        if year == input_year:
            count += 1
            sum_life_expectancy += life_expectancy
            
            if life_expectancy < min_life_expectancy_year:
                min_life_expectancy_year = life_expectancy
                min_country_year = country
            
            if life_expectancy > max_life_expectancy_year:
                max_life_expectancy_year = life_expectancy
                max_country_year = country


if count > 0:
    average_life_expectancy = sum_life_expectancy / count
else:
    average_life_expectancy = 0.0


print(f"\nThe overall max life expectancy is: {overall_max_life_expectancy:.3f} from {overall_max_country} in {overall_max_year}")
print(f"The overall min life expectancy is: {overall_min_life_expectancy:.3f} from {overall_min_country} in {overall_min_year}")

print(f"\nFor the year {input_year}:")
print(f"The average life expectancy across all countries was: {average_life_expectancy:.3f}")
print(f"The max life expectancy was in {max_country_year} with {max_life_expectancy_year:.3f}")
print(f"The min life expectancy was in {min_country_year} with {min_life_expectancy_year:.3f}")