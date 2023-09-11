def calculate_influenza_statistics(): 

    # Given data 

    initial_cases = 500 

    new_cases = 2500 

    total_cases = initial_cases + new_cases 

    population = 100000 

    deaths = 40 

  

    # Calculating Prevalence 

    prevalence = (total_cases / population) * 100000 

    print(f"Influenza Prevalence: {prevalence:.2f} per 100,000 people") 

  

    # Calculating Incidence 

    incidence = (new_cases / population) * 100000 

    print(f"Influenza Incidence: {incidence:.2f} per 100,000 people") 

  

    # Calculating Mortality Rate 

    mortality_rate = (deaths / population) * 100000 

    print(f"Influenza Mortality Rate: {mortality_rate:.2f} per 100,000 people") 

  

if __name__ == "__main__": 

    calculate_influenza_statistics() 