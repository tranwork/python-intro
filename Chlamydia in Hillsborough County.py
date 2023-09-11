def calculate_chlamydia_statistics(): 

    # Given data 

    cases_before_august = 12000 

    new_cases = 3000 

    population = 1780000  # 1.78 million people 

    deaths = 5 

    death_ages = [32, 45, 28, 37, 52] 

    average_life_expectancy = 77 

  

    # Calculating Prevalence 

    prevalence = ((cases_before_august + new_cases) / population) * 100000 

    print(f"Chlamydia Prevalence in Hillsborough County: {prevalence:.2f} per 100,000 people") 

  

    # Calculating Incidence 

    incidence = (new_cases / population) * 100000 

    print(f"Chlamydia Incidence in Hillsborough County: {incidence:.2f} per 100,000 people") 

  

    # Calculating Mortality Rate 

    mortality_rate = (deaths / population) * 100000 

    print(f"Chlamydia Mortality Rate in Hillsborough County: {mortality_rate:.2f} per 100,000 people") 

  

    # Calculating YPLL 

    ypll = sum([average_life_expectancy - age for age in death_ages]) 

    print(f"Years of Potential Life Lost due to Chlamydia in Hillsborough County: {ypll}") 

  

if __name__ == "__main__": 

    calculate_chlamydia_statistics() 