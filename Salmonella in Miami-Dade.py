def calculate_salmonella_statistics(): 

    # Given data 

    cases_2022 = 1211 

    population = 2660000  # 2.66 million people 

    new_cases_2023 = 248 

    deaths_2023 = 1 

  

    # User input for each statistic 

    cases_2022_input = int(input("Enter the number of Salmonella cases in 2022 (Default is 1,211): ") or cases_2022) 

    population_input = int(input("Enter the Miami-Dade population (Default is 2.66 million): ") or population) 

    new_cases_2023_input = int(input("Enter the number of new Salmonella cases from Jan 1 to May 1, 2023 (Default is 248): ") or new_cases_2023) 

    deaths_2023_input = int(input("Enter the number of Salmonella deaths from Jan 1 to May 1, 2023 (Default is 1): ") or deaths_2023) 

  

    # Calculating Prevalence 

    prevalence = (cases_2022_input / population_input) * 100000 

    print(f"Salmonella Prevalence in Miami-Dade: {prevalence:.2f} per 100,000 people") 

  

    # Calculating Incidence 

    incidence = (new_cases_2023_input / population_input) * 100000 

    print(f"Salmonella Incidence in Miami-Dade: {incidence:.2f} per 100,000 people") 

  

    # Calculating Mortality Rate 

    mortality_rate = (deaths_2023_input / population_input) * 100000 

    print(f"Salmonella Mortality Rate in Miami-Dade: {mortality_rate:.2f} per 100,000 people") 

  

if __name__ == "__main__": 

    calculate_salmonella_statistics() 