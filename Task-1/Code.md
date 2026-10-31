# Hospital Billing and Patient Classification – Python Program

## 1. Problem Statement

Develop a Python program to process hospital billing by accepting consultation, diagnostic, and treatment charges. Calculate the total bill, apply conditional concessions based on billing rules, validate charges to ensure they are non-negative, and classify patients according to their final payment amount. Display the complete billing details and patient classification.

## 2. Algorithm

1. Start.
2. Enter the patient's name.
3. Accept consultation, diagnostic, and treatment charges.
4. Check whether all charges are non-negative.
5. If any charge is negative, display an invalid billing message.
6. Otherwise, calculate the total bill.
7. If the total bill is ₹5,000 or more, apply a 10% concession.
8. Calculate the final payable amount.
9. Classify the patient:
   - Below ₹2,000 – Low Payment.
   - ₹2,000 to below ₹10,000 – Medium Payment.
   - ₹10,000 and above – High Payment.
10. Display the billing details and patient classification.
11. Stop.


## 5. Sample Input

```
Enter Patient Name: Ravi
Enter Consultation Charges: 1000
Enter Diagnostic Charges: 2000
Enter Treatment Charges: 4000
```

## 6. Sample Output

```
----- HOSPITAL BILL -----
Patient Name: Ravi
Consultation Charges: 1000.0
Diagnostic Charges: 2000.0
Treatment Charges: 4000.0
Total Bill: Rs. 7000.0
Concession: Rs. 700.0
Final Payable: Rs. 6300.0
Patient Classification: Medium Payment
```

## 7. Mermaid Flowchart Code

``` mermaid

flowchart TD
    A([START]) --> B[/Enter Patient Name and Charges/]
    B --> C{Charges >= 0?}
    C -- No --> D[Display Invalid Charges]
    D --> Z([STOP])
    C -- Yes --> E[Calculate Total Bill]
    E --> F{Total >= 5000?}
    F -- Yes --> G[Apply 10% Concession]
    F -- No --> H[Concession = 0]
    G --> I[Calculate Final Payable]
    H --> I
    I --> J{Payable < 2000?}
    J -- Yes --> K[Low Payment]
    J -- No --> L{Payable < 10000?}
    L -- Yes --> M[Medium Payment]
    L -- No --> N[High Payment]
    K --> O[/Display Billing Details/]
    M --> O
    N --> O
    O --> Z

```

## 8. Result

The Python program successfully calculates hospital bills, applies conditional concessions, validates billing constraints, and classifies patients according to the payment amount.

Note: The 10% concession and classification limits are assumed for this example. They can be modified according to the actual payment policy provided in the assignment.
