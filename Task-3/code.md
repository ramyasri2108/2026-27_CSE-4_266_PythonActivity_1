# Campus Event Financial Planning Using Python

## 1. Problem Statement

Develop a Python program to calculate the total expenses of a campus event, including venue, equipment, catering, transport, and certificate costs. Calculate the total budget, participant contribution, sponsorship amount, and any sponsorship shortfall. Also determine the minimum number of registrations required to break even and ensure that the event expenses are covered.

## 2. Algorithm

1. Start the program.
2. Enter the number of participants.
3. Enter venue, equipment, catering, transport, and certificate costs.
4. Enter the sponsorship amount.
5. Validate that all inputs are non-negative.
6. Calculate the total event expenses.
7. Calculate the cost per participant.
8. Calculate the participant contribution.
9. Calculate the sponsorship shortfall, if any.
10. Calculate the minimum registrations required to break even.
11. Display the total expenses, contributions, sponsorship shortfall, and break-even registrations.
12. Stop.



## 5. Sample Input

```
Enter number of participants: 100
Enter venue cost: 10000
Enter equipment cost: 5000
Enter catering cost per participant: 200
Enter transport cost per participant: 50
Enter certificate cost per participant: 50
Enter sponsorship amount: 10000
Enter contribution per participant: 400
```

## 6. Sample Output

```
--- CAMPUS EVENT FINANCIAL REPORT ---
Total Participants: 100
Fixed Cost: 15000.0
Variable Cost: 30000.0
Total Event Expense: 45000.0
Participant Contribution: 40000.0
Sponsorship: 10000.0
Sponsorship Shortfall: 0
Break-Even Registrations: 17
```

## 7. Break-Even Calculation

The minimum number of registrations is calculated using:

\\[ BE = \left\lceil \frac{F-S}{C-V} \right\rceil \\]

Where:

- \\(F\\) = Fixed cost (venue + equipment)
- \\(S\\) = Sponsorship amount
- \\(C\\) = Contribution per participant
- \\(V\\) = Variable cost per participant

Revenue

Total cost

Loss

Profit

10203040506050010001500Quantity$Q\*

\\(Q^\*=\frac{F}{p-v}=\frac{\text{600}}{\text{35}-\text{15}}=\text{30}\\)

Q\* is the break-even quantity where total revenue matches total cost.

\\(F\\)

$

\\(v\\)

$/unit

\\(p\\)

$/unit

Give feedback

For the sample:

- Fixed cost = ₹15,000
- Sponsorship = ₹10,000
- Contribution = ₹400
- Variable cost = ₹300

\\[ BE = \frac{15000-10000}{400-300}=50 \\]

Correct break-even registrations: 50.

## 8. Mermaid Flowchart Code

```mermaid

flowchart TD
    A([START]) --> B[/Enter Participants and Event Costs/]
    B --> C[/Enter Sponsorship and Contribution/]
    C --> D{Are Inputs Valid?}
    D -- No --> E[Display Invalid Input]
    E --> Z([STOP])
    D -- Yes --> F[Calculate Fixed Cost]
    F --> G[Calculate Variable Cost]
    G --> H[Calculate Total Event Expense]
    H --> I[Calculate Participant Contribution]
    I --> J[Calculate Total Funds]
    J --> K[Calculate Sponsorship Shortfall]
    K --> L{Contribution > Variable Cost?}
    L -- No --> M[Break-Even Not Possible]
    L -- Yes --> N[Calculate Break-Even Registrations]
    M --> O[/Display Financial Report/]
    N --> O
    O --> Z

```

## 9. Result

The Python program successfully calculates campus event expenses, participant contributions, sponsorship shortfalls, and minimum break-even registrations based on the given financial details.

Note: All amounts and financial rules are assumed for this academic programming exercise.
