# Voting Eligibility Checker
# Accept age from user, check whether person is eligible for vote (Age should be 18 or above)
# Input - 19
# Output - Eligible to vote

def EligibilityCheck(value):
    if (value >= 18):
        print("Eligible to vote")
    else:
        print("Not eligible for vote")

def main():
    print("Enter a age")
    no = int(input())

    EligibilityCheck(no)

if __name__ == "__main__":
    main()