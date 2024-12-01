# JJ's Food Court - Ordering System

Welcome to JJ's Food Court! This simple Python-based ordering system allows customers to place orders from a predefined menu of food items and calculate the total bill.

## Features

- Displays a menu with food items and their respective prices.
- Allows customers to choose items by name.
- Calculates the total cost of the selected items.
- Handles input dynamically, adding items to the order until the user is finished.
- Handles invalid inputs gracefully (e.g., unlisted items or incorrect commands).

## Prerequisites

Make sure you have Python installed on your system. This code works on Python 3.x.

To check if Python is installed, run:

```bash
python --version
```

## How to Use

1. Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/jjs-food-court.git
```

2. Navigate to the project folder:

```bash
cd jjs-food-court
```

3. Run the Python script:

```bash
python food_ordering_system.py
```

4. You will be presented with a menu of items available for purchase. You can select an item by typing its name exactly as it appears in the list.
   
   Example:
   ```
   classic burger
   cheeseburger
   small fries
   ```

5. To complete your order, type **'done'**. The system will then display your complete order with the total bill.

   Example of output:
   ```
   classic burger has been added to your order!
   small fries has been added to your order!
   Your Complete Order:
   classic burger = Rs50.00
   small fries = Rs60.00
   Your Total Bill: Rs110.00
   ```

6. If you type an item that is not on the menu, the system will inform you that the item is unavailable.

## Code Walkthrough

- **Menu**: The menu dictionary contains the available items and their respective prices in Rs (Indian Rupees).
  
  ```python
  menu = {
      "classic burger": 50, "cheeseburger": 75, "chicken burger": 100, 
      "maharaja burger": 160, "small fries": 60, "medium fries": 100, 
      "large fries": 150, "small wings bucket": 150, "medium wings bucket": 230,
      "large wings bucket": 320, "small cola": 80, "medium cola": 140, 
      "large cola": 200, "vanilla cone": 30, "strawberry cone": 40, 
      "chocolate cone": 40, "choco lava cake": 100
  }
  ```

- **Ordering**: The script takes user input continuously until the user types `done`. If the input is valid (i.e., it matches an item on the menu), the item is added to the order.

  ```python
  x = input("So, What would you like to have? (whenever you are done ordering, type 'done')")
  ```

- **Total Calculation**: Once the user finishes ordering, the script calculates the total bill by summing up the prices of the items selected and prints the complete order summary.

  ```python
  total = 0
  for item in order:
      total += menu[item]
  ```

- **Error Handling**: If the user inputs an item that is not on the menu, the system will notify them.

## Example Output

Here is an example of the interaction with the script:

```
--- Welcome to JJs Food Court ---
classic burger = Rs50.00
cheeseburger = Rs75.00
chicken burger = Rs100.00
maharaja burger = Rs160.00
small fries = Rs60.00
medium fries = Rs100.00
large fries = Rs150.00
small wings bucket = Rs150.00
medium wings bucket = Rs230.00
large wings bucket = Rs320.00
small cola = Rs80.00
medium cola = Rs140.00
large cola = Rs200.00
vanilla cone = Rs30.00
strawberry cone = Rs40.00
chocolate cone = Rs40.00
choco lava cake = Rs100.00

So, What would you like to have? (whenever you are done ordering, type 'done') classic burger
classic burger has been added to your order!
So, What would you like to have? (whenever you are done ordering, type 'done') small fries
small fries has been added to your order!
So, What would you like to have? (whenever you are done ordering, type 'done') done

Your Complete Order:
classic burger = Rs50.00
small fries = Rs60.00
Your Total Bill: Rs110.00
```

## Contributions

Feel free to fork this project and create pull requests for any improvements. If you'd like to contribute in any other way, open an issue and we'll be happy to collaborate!

## License

This project is open-source and available under the [MIT License](LICENSE).
