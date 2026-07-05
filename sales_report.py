import csv
import os

def analyze_sales(filename):
    # File exist karti hai?
    if not os.path.exists(filename):
        print(f"Error: '{filename}' file nahi mili.")
        print("Check karo ki file same folder me hai jahan script hai.")
        return

    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)

            # Check karo required columns hain ya nahi
            required_columns = ['product', 'quantity', 'price']

            first_row = next(reader, None)
            if first_row is None:
                print("Error: CSV file empty hai.")
                return

            for col in required_columns:
                if col not in first_row:
                    print(f"Error: '{col}' column nahi mila CSV me.")
                    return

            # Process first row + remaining rows
            all_rows = [first_row] + list(reader)

            total_sales = 0
            highest_item = ""
            lowest_item = ""
            highest_value = 0
            lowest_value = float('inf')
            item_count = 0

            for row in all_rows:
                try:
                    product = row['product']
                    quantity = int(row['quantity'])
                    price = int(row['price'])

                    item_total = quantity * price
                    total_sales += item_total
                    item_count += 1

                    if item_total > highest_value:
                        highest_value = item_total
                        highest_item = product

                    if item_total < lowest_value:
                        lowest_value = item_total
                        lowest_item = product

                    print(f"{product}: {quantity} units x Rs.{price} = Rs.{item_total}")

                except ValueError:
                    print(f"Warning: '{row['product']}' ki quantity/price invalid hai, skipping...")
                    continue

            if item_count == 0:
                print("Error: Koi valid data nahi mila.")
                return

            average_sale = total_sales / item_count

            print("------------------------------")
            print(f"Total Sales: Rs.{total_sales}")
            print(f"Average Sale per Product: Rs.{average_sale:.2f}")
            print(f"Highest Selling Product: {highest_item} (Rs.{highest_value})")
            print(f"Lowest Selling Product: {lowest_item} (Rs.{lowest_value})")

    except PermissionError:
        print("Error: File open hai kisi aur program me. Band karo pehle.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Run karo
analyze_sales('sales_data.csv')