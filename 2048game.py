from fpdf import FPDF

# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size=12)

# Add content to the PDF

# Title
pdf.cell(200, 10, txt="Caner AKCASU - Resume", ln=True, align='C')

# Contact Information
contact_info = """Contact Information:
Address: Wroclaw, 53-443 Poland
Phone: +48 571 079 459
Email: Canerlimited@gmail.com
Website: https://bold.pro/my/caner-akcasu/281r
"""
pdf.multi_cell(0, 10, contact_info)

# Objective
objective = """Objective:
I am a dedicated and hardworking individual currently studying Software Engineering at WSB Merito Wroclaw. I am seeking a part-time job in the internet industry or at the beginner level to further develop my skills and gain more experience.
"""
pdf.multi_cell(0, 10, objective)

# Work History
work_history = """Work History:

Product Testing Specialist
Cinno Poland · Part-time
Apr 2024 - Present · 4 mos
Wrocław, Dolnośląskie, Poland · On-site

Product Testing and Repair:
- Conducted manual and automated tests on Xiaomi products, including scooters, cellphones, and smart home devices.
- Identified faulty or defective products, performed necessary repairs, and ensured they were suitable for reuse.
- Reset IMEI and other codes on cellphones, updated software, and resolved motherboard issues to prepare devices for resale.

Logistics and Distribution:
- Coordinated logistics processes for repaired products across Europe.
- Ensured timely and seamless delivery of products.

Quality Control:
- Managed quality control processes to ensure high standards for all products.
- Developed and improved test procedures and standards to continuously enhance processes.

Operator (Scanner)
iMile Delivery (Shein), Bielany Wroclawskie
Jan 2024 - Apr 2024
...
"""
# Uzun metinler için multi_cell yerine cell kullanılabilir
pdf.multi_cell(0, 10, work_history)

# Education
education = """Education:

Bachelor of Science: Computer Science
Wroclaw University of Applied Informatics - Wroclaw, Poland
May 2022 - May 2023

Bachelor of Science: Software Engineering
Uniwersytet WSB Merito - Wroclaw, Poland
May 2023 - Current
"""
pdf.multi_cell(0, 10, education)

# Skills
skills = """Skills:

- Machine Operation
- Reading and Determining Measurements
- Visual Inspection
- Time Management Abilities
- MS Office
- Marketing
- Data Analysis
- Blockchain
- Wordpress
- Windows-IOS Systems
"""
pdf.multi_cell(0, 10, skills)

# Languages
languages = """Languages:

- Turkish
- English
- Polish
- Russian
"""
pdf.multi_cell(0, 10, languages)

# Certifications
certifications = """Certifications:

- Digital Marketing (Google) - Sep 2020
- Python Programming - Aug 2020
"""
pdf.multi_cell(0, 10, certifications)

# References
references = """References:
Available upon request.
"""
pdf.multi_cell(0, 10, references)

# Save the PDF
output_path = "/mnt/data/Caner_AKCASU_Updated_Resume.pdf"
pdf.output(output_path)

print(f"PDF saved successfully at: {output_path}")
