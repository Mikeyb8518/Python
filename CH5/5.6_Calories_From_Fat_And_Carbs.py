# Write a program that takes the user number of grams from fat and carbohydrate 
# and calculates the number of calories from fat and carbohydrate using functions

# Main function to prompt the user for input and call the functions
def main():
    
    # Prompt the user for the number of grams from fat and carbohydrate
    grams_from_fat = float(input("Enter the number of grams from fat: "))
    grams_from_carbohydrate = float(input("Enter the number of grams from carbohydrate: "))
    calories_From_Fat(grams_from_fat)
    calories_From_Carbohydrate(grams_from_carbohydrate)
    
# Function to calculate the number of calories from fat
def calories_From_Fat(grams_from_fat):
    # Formula to calculate colories from grams of fat
    fat_calories = grams_from_fat * 9
    # Display results
    print(f"\nCalories from fat: {fat_calories} calories")
    
# Function to calculate the number of calories from carbohydrate
def calories_From_Carbohydrate(grams_from_carbohydrate):
    # Formula to calculate colories from grams of carbohydrate
    carbohydrate_calories = grams_from_carbohydrate * 4
    # Display results
    print(f"Calories from carbohydrate: {carbohydrate_calories} calories")
    
main()