def calculate_statistics(): 

    # Given data 

    cases_2022 = 80 

    population = 1780000  # 1.78 million people 

    new_cases_2023 = 19 

    deaths_2023 = 2 

    death_ages = [64, 74] 

    average_life_expectancy = 77 

  

    # User input for each statistic 

    cases_2022_input = int(input("Enter the number of cases in 2022 (Default is 80): ") or cases_2022) 

    population_input = int(input("Enter the population (Default is 1.78 million): ") or population) 

    new_cases_2023_input = int(input("Enter the number of new cases from Jan 1 to May 1, 2023 (Default is 19): ") or new_cases_2023) 

    deaths_2023_input = int(input("Enter the number of deaths from Jan 1 to May 1, 2023 (Default is 2): ") or deaths_2023) 

  

    # Calculating Prevalence 

    prevalence = (cases_2022_input / population_input) * 100000 

    print(f"Prevalence: {prevalence:.2f} per 100,000 people") 

  

    # Calculating Incidence 

    incidence = (new_cases_2023_input / population_input) * 100000 

    print(f"Incidence: {incidence:.2f} per 100,000 people") 

  

    # Calculating Mortality Rate 

    mortality_rate = (deaths_2023_input / population_input) * 100000 

    print(f"Mortality Rate: {mortality_rate:.2f} per 100,000 people") 

  

    # Calculating YPLL 

    ypll = sum([average_life_expectancy - age for age in death_ages]) 

    print(f"Years of Potential Life Lost: {ypll}") 

  

if __name__ == "__main__": 

    calculate_statistics() 