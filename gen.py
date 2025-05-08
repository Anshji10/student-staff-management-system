import os
import sys
import django
from faker import Faker
from datetime import date
import random
from django.utils import timezone

# Add project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

# Debug: Print sys.path
print("sys.path:", sys.path)

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_management_system.settings')
django.setup()

# Import models from main_app
from main_app.models import CustomUser, Student, Course, Session

# Add custom Indian name provider to Faker
from fakerr import IndianNameProvider

# Initialize Faker and add custom provider
fake = Faker('en_IN')
fake.add_provider(IndianNameProvider)

# Function to generate dummy data
def generate_dummy_students(num_students=100):
    # Create or get a Course
    course, _ = Course.objects.get_or_create(
        name="Computer Science",
        defaults={'created_at': timezone.now(), 'updated_at': timezone.now()}
    )
    
    # Create or get a Session
    session, _ = Session.objects.get_or_create(
        start_year=date(2023, 4, 1),
        end_year=date(2024, 3, 31)
    )
    
    # Generate students
    for i in range(num_students):
        # Randomly choose gender
        gender = random.choice(["M", "F"])
        
        # Generate names based on gender
        full_name = fake.indian_full_name(gender=gender)
        first_name, last_name = full_name.split(" ")
        
        # Generate unique email
        email = f"{first_name.lower()}.{last_name.lower()}{random.randint(1, 999)}@example.com"
        
        # Create CustomUser
        try:
            user = CustomUser.objects.create_user(
                email=email,
                password="password123",
                first_name=first_name,
                last_name=last_name,
                user_type="3",  # Student
                gender=gender,
                profile_pic="",  # Assuming nullable
                address=fake.address().replace("\n", ", "),
                fcm_token=fake.uuid4()
            )
            print(f"Created user: {user.email}")
            
            # Manually create Student object
            student = Student.objects.create(
                admin=user,
                course=course,
                session=session
            )
            print(f"Created student: {student}")
            
        except Exception as e:
            print(f"Error creating user {email}: {str(e)}")

if __name__ == "__main__":
    print("Generating 100 dummy students...")
    generate_dummy_students(100)
    print("Done!")