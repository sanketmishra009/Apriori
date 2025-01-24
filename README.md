# Apriori Algorithm Implementation

This repository contains an implementation of the Apriori algorithm, a popular method for association rule learning in data mining. The Apriori algorithm identifies frequent itemsets in a dataset and generates association rules based on those itemsets.

## Features

- Implements the Apriori algorithm to identify frequent itemsets.
- Generates association rules from frequent itemsets.
- Allows customization of minimum support and confidence thresholds.
- Provides insights into the relationships between items in a dataset.

## Getting Started

Follow these instructions to set up and use the project on your local machine.

### Prerequisites

- Python 3.6+
- Required Python libraries:
  - `pandas`
  - `numpy`

You can install the required libraries using:

```bash
pip install pandas numpy
```

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sanketmishra009/Apriori.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Apriori
   ```

3. Install dependencies if not already installed:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Apriori Algorithm

1. Prepare your dataset in a CSV format where each row represents a transaction, and each column represents an item (value is 1 if the item is present, 0 otherwise).

2. Modify the `main.py` file to point to your dataset and adjust parameters like `min_support` and `min_confidence` as needed.

3. Run the program:

   ```bash
   python main.py
   ```

### Example

Input dataset:

| Milk | Bread | Butter |
|------|-------|--------|
| 1    | 1     | 1      |
| 1    | 0     | 1      |
| 0    | 1     | 1      |
| 1    | 1     | 0      |

Output:

- Frequent Itemsets:
  - `{Milk, Bread}`
  - `{Milk, Butter}`
  - `{Bread, Butter}`
- Association Rules:
  - `{Milk} -> {Bread}` with confidence 0.8
  - `{Butter} -> {Milk}` with confidence 0.75

## Configuration

You can adjust the following parameters in the code:

- **Minimum Support (`min_support`)**: The minimum frequency for an itemset to be considered frequent.
- **Minimum Confidence (`min_confidence`)**: The minimum confidence for an association rule to be considered valid.

## File Structure

- `main.py`: The main script to run the Apriori algorithm.
- `apriori.py`: Core implementation of the Apriori algorithm.
- `utils.py`: Utility functions for data preprocessing and support calculations.
- `data/`: Directory to store your input dataset.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

### Steps to Contribute

1. Fork this repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your branch.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For any questions or suggestions, feel free to contact:

- **Name**: Sanket Mishra
- **Email**: [sanketmishra009@gmail.com](mailto:sanketmishra009@gmail.com)
- **GitHub**: [sanketmishra009](https://github.com/sanketmishra009)

---

Thank you for exploring the Apriori Algorithm repository! If you find this project helpful, please give it a ⭐.
