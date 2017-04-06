def underpaid(file_path):
    """ This function displays list of underpaying customers.

    Given path to a data file of customer data in the format:
    Customer #|customer name|# melons|customer paid
    This function will calculate which customers have underpaid
    and print a list of the underpaying customers in format:
    customer name, paid {how much they paid}, expected {how much the should have paid}
    """

    #open the data file
    the_file = open(file_path)

    #initialize variables
    melon_cost = 1.00

    #iterate through and tokenize the data from the file
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        customer_name = words[1]
        customer_melons = int(words[2])
        customer_paid = float(words[3])
        expected = customer_melons * melon_cost

        #print those who underpaid
        if customer_paid < expected:
            print customer_name, "paid {:.2f}, expected {:.2f}".format(
                customer_paid, expected)
    the_file.close()

underpaid("customer-orders.txt")
