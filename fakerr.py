from faker.providers import BaseProvider

class IndianNameProvider(BaseProvider):
    first_names_male = [
        "Rahul", "Rohit", "Amit", "Vikram", "Suresh", "Ramesh", "Sanjay", "Arjun", "Kiran", "Vivek",
        "Anil", "Sunil", "Deepak", "Nikhil", "Ajay", "Vijay", "Prakash", "Manoj", "Sachin", "Yash",
        "Kunal", "Ravi", "Harish", "Pankaj", "Gaurav", "Vinod", "Mahesh", "Shiva", "Krishna", "Aditya"
    ]
    
    first_names_female = [
        "Priya", "Anjali", "Sneha", "Pooja", "Riya", "Neha", "Shalini", "Kavita", "Divya", "Suman",
        "Rekha", "Manisha", "Aarti", "Swati", "Jyoti", "Lata", "Meena", "Radha", "Vandana", "Geeta",
        "Sarita", "Anita", "Komal", "Nisha", "Ritu", "Sonia", "Tara", "Uma", "Vidya", "Zoya"
    ]
    
    last_names = [
        "Sharma", "Verma", "Gupta", "Singh", "Kumar", "Patel", "Mehta", "Jain", "Shah", "Pandey",
        "Mishra", "Yadav", "Rao", "Reddy", "Nair", "Chauhan", "Thakur", "Das", "Joshi", "Srivastava",
        "Malhotra", "Bhatia", "Agarwal", "Kapoor", "Rathore", "Bose", "Nagar", "Pillai", "Menon", "Iyer"
    ]

    def indian_first_name_male(self):
        return self.random_element(self.first_names_male)
    
    def indian_first_name_female(self):
        return self.random_element(self.first_names_female)
    
    def indian_last_name(self):
        return self.random_element(self.last_names)
    
    def indian_full_name(self, gender="M"):
        last_name = self.indian_last_name()
        if gender == "M":
            first_name = self.indian_first_name_male()
        else:
            first_name = self.indian_first_name_female()
        return f"{first_name} {last_name}"