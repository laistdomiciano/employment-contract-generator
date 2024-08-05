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

                This Full-Time Employment Contract ("Contract") is made effective as of [Start Date], by and between [Company Name] ("Employer") and [Employee Name] ("Employee").
                
                Position
                Employer agrees to employ Employee as [Job Title]. Employee's duties and responsibilities will include [Job Responsibilities].
                
                Compensation
                Employer will pay Employee a salary of [Salary Amount] per year, payable in accordance with the company's standard payroll schedule.
                
                Benefits
                Employee will be entitled to participate in the company's benefits plans, including [List of Benefits].
                
                Work Hours
                Employee is expected to work [Work Hours] hours per week.
                
                Leave Policy
                Employee will be entitled to [Leave Days] days of paid leave per year.
                
                Termination
                This Contract may be terminated by either party upon [Notice Period] notice.
                
                Confidentiality
                Employee agrees to keep all company information confidential.
                
                Signed,
                [Company Representative]
                [Employee Name]

                """
        },
        {
            'name': 'Part-Time',
            'template': """
                PART-TIME EMPLOYMENT CONTRACT

                This Part-Time Employment Contract ("Contract") is made effective as of [Start Date], by and between [Company Name] ("Employer") and [Employee Name] ("Employee").
                
                Position
                Employer agrees to employ Employee as [Job Title] on a part-time basis. Employee's duties and responsibilities will include [Job Responsibilities].
                
                Compensation
                Employer will pay Employee at a rate of [Hourly Rate] per hour, payable in accordance with the company's standard payroll schedule.
                
                Hours of Work
                Employee is expected to work [Number of Hours] hours per week.
                
                Benefits
                Employee will be entitled to [List of Benefits] on a pro-rated basis.
                
                Leave Policy
                Employee will be entitled to [Leave Days] days of paid leave per year on a pro-rated basis.
                
                Termination
                This Contract may be terminated by either party upon [Notice Period] notice.
                
                Confidentiality
                Employee agrees to keep all company information confidential.
                
                Signed,
                [Company Representative]
                [Employee Name]
                """
        },
        {
            'name': 'Freelance',
            'template': """
                FREELANCE EMPLOYMENT CONTRACT

                This Freelance Contract ("Contract") is made effective as of [Start Date], by and between [Company Name] ("Client") and [Freelancer Name] ("Freelancer").

                Services
                Freelancer agrees to perform the following services for Client: [Description of Services].
                
                Compensation
                Client will pay Freelancer a fee of [Fee Amount], payable upon completion of the services or as otherwise agreed upon by the parties.
                
                Payment Schedule
                Payment will be made according to the following schedule: [Payment Schedule].
                
                Independent Contractor
                Freelancer is an independent contractor and not an employee of Client.
                
                Confidentiality
                Freelancer agrees to keep all client information confidential.
                
                Intellectual Property
                All intellectual property developed during the project will belong to [Ownership Terms].
                
                Termination
                This Contract may be terminated by either party upon [Notice Period] notice.
                
                Signed,
                [Client Representative]
                [Freelancer Name]
                """
        }
    ]

    for ct_data in contract_types:
        contract_type = ContractType(**ct_data)
        db.session.add(contract_type)

    db.session.commit()
