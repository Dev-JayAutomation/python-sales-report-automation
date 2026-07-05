# Python Sales Report Automation

Automatically analyzes CSV/Excel sales data and generates 
a complete summary report in seconds.

## What It Does

- Reads any CSV sales file
- Calculates total revenue
- Finds average sale per product
- Identifies highest and lowest performing products
- Handles errors gracefully (missing files, invalid data, duplicates)

## Why Use This

Manual Excel calculations take time and are prone to human error.
This script processes your entire sales file instantly and gives 
you a clean, accurate summary every time.

## Requirements

- Python 3.x
- No external libraries needed (uses built-in csv module)

## How To Use

1. Clone this repository
2. Place your CSV file in the same folder as the script
3. Your CSV must have these columns: `product`, `quantity`, `price`
4. Run the script:

```bash
python sales_report.py
```

## Sample Input (sales_data.csv)

product,quantity,price  
Laptop,2,45000  
Mouse,10,500  
Keyboard,5,1200  

## Sample Output

Laptop: 2 units x Rs.45000 = Rs.90000  
Mouse: 10 units x Rs.500 = Rs.5000  
Keyboard: 5 units x Rs.1200 = Rs.6000  
Total Sales: Rs.101000  
Average Sale per Product: Rs.33666.67  
Highest Selling Product: Laptop (Rs.90000)  
Lowest Selling Product: Mouse (Rs.5000)

## Customization

The script can be easily modified to:
- Support different column names
- Export results to a new CSV file
- Handle multiple currencies
- Process multiple files in batch

## License

MIT License - free to use and modify
