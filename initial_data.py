from app import create_app, db
from app.models import ContractType

app = create_app()

contract_types = [
    ContractType(
        name="Full-Time Employment",
        description="Full-time employment contract.",
        template="""
            Full-Time Employment Contract

            This Full-Time Employment Contract ("Contract") is made effective as of [Start Date], by and between [Company Name] ("Employer") and [Employee Name] ("Employee").

            1. Position
            Employer agrees to employ Employee as [Job Title]. Employee's duties and responsibilities will include [Job Responsibilities].

            2. Compensation
            Employer will pay Employee a salary of [Salary Amount] per year, payable in accordance with the company's standard payroll schedule.

            3. Benefits
            Employee will be entitled to participate in the company's benefits plans, including [List of Benefits].

            4. Termination
            This Contract may be terminated by either party upon [Notice Period] notice.

            5. Confidentiality
            Employee agrees to keep all company information confidential.

            Signed,
            [Company Representative]
            [Employee Name]
        """
    ),
    ContractType(
        name="Part-Time Employment",
        description="Part-time employment contract.",
        template="""
            Part-Time Employment Contract

            This Part-Time Employment Contract ("Contract") is made effective as of [Start Date], by and between [Company Name] ("Employer") and [Employee Name] ("Employee").

            1. Position
            Employer agrees to employ Employee as [Job Title] on a part-time basis. Employee's duties and responsibilities will include [Job Responsibilities].

            2. Compensation
            Employer will pay Employee at a rate of [Hourly Rate] per hour, payable in accordance with the company's standard payroll schedule.

            3. Hours of Work
            Employee is expected to work [Number of Hours] hours per week.

            4. Termination
            This Contract may be terminated by either party upon [Notice Period] notice.

            5. Confidentiality
            Employee agrees to keep all company information confidential.

            Signed,
            [Company Representative]
            [Employee Name]
        """
    ),
    ContractType(
        name="Freelance Contract",
        description="Freelance contract.",
        template="""
            Freelance Contract

            This Freelance Contract ("Contract") is made effective as of [Start Date], by and between [Company Name] ("Client") and [Freelancer Name] ("Freelancer").

            1. Services
            Freelancer agrees to perform the following services for Client: [Description of Services].

            2. Compensation
            Client will pay Freelancer a fee of [Fee Amount], payable upon completion of the services or as otherwise agreed upon by the parties.

            3. Independent Contractor
            Freelancer is an independent contractor and not an employee of Client.

            4. Confidentiality
            Freelancer agrees to keep all client information confidential.

            5. Termination
            This Contract may be terminated by either party upon [Notice Period] notice.

            Signed,
            [Client Representative]
            [Freelancer Name]
        """
    )
]

with app.app_context():
    db.create_all()
    for contract_type in contract_types:
        db.session.add(contract_type)
    db.session.commit()
