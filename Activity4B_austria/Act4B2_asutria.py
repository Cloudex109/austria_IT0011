import csv

def load_currency_data(file_path="currency.csv"):
    """Load currency data from CSV file with flexible encoding."""
    # Try different encodings
    encodings = ['utf-8', 'latin-1', 'cp1252', 'ISO-8859-1']
    
    for encoding in encodings:
        try:
            currencies = {}
            with open(file_path, 'r', encoding=encoding) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    currencies[row['code']] = {
                        'name': row['name'],
                        'rate': float(row['rate'])
                    }
            print(f"Successfully loaded using {encoding} encoding")
            return currencies
        except UnicodeDecodeError:
            continue
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
            return None
        except Exception as e:
            print(f"Error loading currency data: {e}")
            return None
    
    print("Could not decode the file with any of the attempted encodings")
    return None

def convert_currency(amount, target_currency, currencies):
    """Convert USD to target currency."""
    if target_currency not in currencies:
        print(f"Error: Currency code '{target_currency}' not found.")
        return None
    
    conversion_rate = currencies[target_currency]['rate']
    converted_amount = amount * conversion_rate
    return converted_amount

def main():
    # Load currency data from the CSV file in the current directory
    currencies = load_currency_data()
    
    if not currencies:
        print("Could not load currency data. Please make sure currency.csv exists in the current directory.")
        return
    
    try:
        # Get user input
        amount = float(input("How much dollar do you have? "))
        target_currency = input("What currency you want to have? ").upper()
        
        # Convert the currency
        converted_amount = convert_currency(amount, target_currency, currencies)
        
        if converted_amount is not None:
            currency_name = currencies[target_currency]['name']
            print(f"Dollar: {amount} USD")
            print(f"{currency_name}: {converted_amount}")
    except ValueError:
        print("Please enter a valid number for the dollar amount.")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()