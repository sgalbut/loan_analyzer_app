# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

 
 
 
 
 
 
 
 
 
 
 
 #SAVE THE QUALIFYING LOANS TO A FILE
def save_csv(qualifying_loans, file_location):
    with open(file_location, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Lender', 'Max Loan Amount', 'Max LTV', 'Max DTI', 'Min Credit Score', 'Interest Rate'])

        for i in range(len(qualifying_loans)):
            bank_name = qualifying_loans[i][0]
            loan_amount = qualifying_loans[i][1]
            max_ltv = qualifying_loans[i][2]
            max_dti = qualifying_loans[i][3]
            min_credit_score = qualifying_loans[i][4]
            interest_rate = qualifying_loans[i][5]

            writer.writerow([bank_name, loan_amount, max_ltv, max_dti, min_credit_score, interest_rate])