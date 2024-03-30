#1. This company stores customer details 
#Key field: customerID (int(100001, 999999))
#CustomerName: max:30 CHAR
#Customer's orders total: currency in float
#PSEUDOCODE:

    #TYPE CustomerRecord()
    #    DECLARE CustomerID : INTEGER #identifier
    #    DECLARE CustomerName : STRING #max 30 characters
    #    DECLARE TotalOrders : REAL
    #ENDTYPE    

    #FUNCTION Hash(CustomerID : INTEGER) RETURNS INTEGER
    #    Address <- CustomerID MOD 1000
    #    RETURN Address
    #ENDFUNCTION

    #PROCEDURE AddRecord(Customer: CustomerRecord)
    #   OPENFILE CustomerFile FOR RANDOM
    #    Address <- Hash(Customer.CustomerID)
    #    SEEK CustomerFile, Customer 
    #    PUTRECORD CustomerFile, Customer
    #   CLOSEFILE CustomerFIle
    #ENDPROCEDURE
#Handle collisions by using the next available slot

    #PROCEDURE StoreRecordsToFile
    #    ASSIGN FileVar TO 'Customer.DAT'
    #    REWRITE FileVar
    #    FOR i FROM 0 TO 999 DO
    #        IF CustomerData[i].CustomerID <> 0 THEN
    #            WRITE FileVar, CustomerData[i]
    #        ENDIF
    #   ENDFOR
    #    CLOSE FileVar
    #END


import pickle

class CustomerRecord:
    def __init__(self):
        self.CustomerID : [10001, 999999]
        self.CustomerName : str[30]
        self.TotalOrders : 0.00
   
#Calc address
def Hash(CustomerID):
    return CustomerID % 1000

def add_record(Customer):
    try:
        with open('CustomerFile.DAT', 'rb+') as CustomerFile:
            Address = Hash(Customer.CustomerID)
            CustomerFile.seek(Address)
            pickle.dump(Customer, CustomerFile)
    except FileNotFoundError:
        print("Error: CustomerFile.DAT not found.")
    except Exception as e:
        print(f"Error: {e}")

def find_records_by_id(customer_id):
    try:
        with open('CustomerFile.DAT', 'rb') as CustomerFile:
            Address = Hash(customer_id)
            CustomerFile.seek(Address * pickle.HIGHEST_PROTOCOL)
            while True:
                try:
                    customer = pickle.load(CustomerFile)
                    if customer.CustomerID == customer_id:
                        print(f"Customer found: ID={customer.CustomerID}, Name={customer.CustomerName}, TotalOrders={customer.TotalOrders}")
                except EOFError:
                    break
    except FileNotFoundError:
        print("Error: CustomerFile.DAT not found.")
    except Exception as e:
        print(f"Error: {e}")


#Storing customer records in a direct-access binary file will eliminate the need for an
#array as a hash table, a larger array to accommodate the maximum possible range of 
#CustomerID values needs to be defined.
#Instead of computing the hash and seeking to the corresponding location, 
#the array needs to be directly accessed using the CustomerID as the index.
#The CustomerRecord class needs to be adjusted to store records in a list or array.

try:
    file_name = input("Which file do you want to use? ")
    with open(file_name, 'r') as file:
        print("File found: "), file_name
except FileNotFoundError:
        print("File not found, please enter a valid filename. ")