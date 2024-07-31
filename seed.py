from app import create_app, db
from app.models import User, Employee, ContractType

app = create_app()

with app.app_context():
    db.create_all()

    # Create Users
    users = [
        {'username': 'user1', 'password': 'password1'},
        {'username': 'user2', 'password': 'password2'},
        {'username': 'user3', 'password': 'password3'},
        {'username': 'user4', 'password': 'password4'},
        {'username': 'user5', 'password': 'password5'},
    ]

    for user_data in users:
        user = User(username=user_data['username'])
        user.set_password(user_data['password'])
        db.session.add(user)

    # Create Employees
    employees = [
        {'name': 'John Doe', 'position': 'Software Engineer', 'department': 'Engineering'},
        {'name': 'Jane Smith', 'position': 'Product Manager', 'department': 'Product'},
        {'name': 'Alice Johnson', 'position': 'Designer', 'department': 'Design'},
    ]

    for emp_data in employees:
        employee = Employee(**emp_data)
        db.session.add(employee)

    # Create Contract Types
    contract_types = [
        {
            'name': 'Full-Time',
            'template': """
                FULL-TIME EMPLOYMENT CONTRACT

                This Employment Agreement is made between [employee_name], employed as [employee_position] in the [employee_department] department, and [company_name].

                Terms and conditions:
                - Full-time employment
                - Salary: [salary]
                - Benefits: [benefits]
                """
        },
        {
            'name': 'Part-Time',
            'template': """
                PART-TIME EMPLOYMENT CONTRACT

                This Employment Agreement is made between [employee_name], employed as [employee_position] in the [employee_department] department, and [company_name].

                Terms and conditions:
                - Part-time employment
                - Hourly rate: [hourly_rate]
                - Benefits: [benefits]
                """
        },
        {
            'name': 'Freelance',
            'template': """
                FREELANCE EMPLOYMENT CONTRACT

                This Freelance Agreement is made between [employee_name], working as [employee_position] in the [employee_department] department, and [company_name].

                Terms and conditions:
                - Freelance basis
                - Project fee: [project_fee]
                - Payment terms: [payment_terms]
                """
        }
    ]

    for ct_data in contract_types:
        contract_type = ContractType(**ct_data)
        db.session.add(contract_type)

    db.session.commit()
