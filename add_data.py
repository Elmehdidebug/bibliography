from app import create_app, db
from app.models import User, Bibliography
import pandas as pd


app = create_app()

# with app.app_context():
#     # Create a user
#     user = User(username='aoukarroum', email='aoukarroum@um6p.com')
#     user.set_password('aoukarroum')
#     db.session.add(user)
#     db.session.commit()
    
#     # Create a bibliography for the user
#     biblio_content = """Overview

#     What is the researcher best known for?
#     Abdallah Oukarroum is best known for his research in plant physiology, stress responses, and environmental impact on agriculture.
#     The fields of study they are best known for.
#     Plant physiology, Environmental sciences, Agriculture
#     Main research concerns and frequent connections to adjacent fields.
#     The impact of environmental stressors on plant health, particularly drought and heavy metals, and the development of methods to mitigate these effects.
#     Most Cited Work

#     Chlorophyll a fluorescence as a tool to monitor physiological status of plants under stress conditions, Acta Physiologiae Plantarum, 2016 - 910 citations.
#     Probing the responses of barley cultivars (Hordeum vulgare L.) to water deficit, Environmental and Experimental Botany, 2007 - 421 citations.
#     Identification of nutrient deficiency in maize leaves using hyperspectral data, Plant Physiology and Biochemistry, 2014 - 344 citations.
#     Inhibitory effects of silver nanoparticles in aquatic environments, Ecotoxicology and Environmental Safety, 2012 - 321 citations.
#     Drought stress effects on photosystem I content and activity in barley leaves, Physiologia Plantarum, 2009 - 261 citations.
#     Main Themes of Work
#     Abdallah Oukarroum's research primarily revolves around the physiological responses of plants to environmental stressors, including drought and heavy metals. He frequently integrates knowledge from environmental sciences and agricultural practices to explore and propose mitigation strategies. His work includes examining the effects of various stressors on plant health and productivity, and developing methods to assess and improve plant resilience.

#     Recent Work Highlights (last 5 years)

#     Sequential co-processing of olive mill wastewater and livestock manure using composting technology, Process Safety and Environmental Protection, 2024 - 1 citation.
#     Impact and toxicity of heavy metals on human health and the environment, International Journal of Environmental Science and Technology, 2024 - 2 citations.
#     Advances in controlled release fertilizers: Concept, application, and future directions, Journal of Controlled Release, 2021 - 128 citations.
#     Recent progress on emerging technologies for the treatment of municipal and industrial wastewater, Science of the Total Environment, 2021 - 27 citations.
#     Composting date palm residues promotes circular economy and sustainable agriculture, Bioresource Technology, 2020 - 48 citations.
#     Publication Fields
#     Abdallah Oukarroum's publications are distributed across various fields, with notable frequency in the following journals:

#     Science of the Total Environment (5 publications)
#     Water, Air, and Soil Pollution (4 publications)
#     Plant Physiology and Biochemistry (4 publications)
#     Environmental and Experimental Botany (4 publications)
#     Scientific Reports (3 publications)"""
    
#     biblio = Bibliography(title='Sample Bibliography', content=biblio_content, author=user)
#     db.session.add(biblio)
#     db.session.commit()


# Load the Excel file
file_path = 'CAES Faculty List_August 2024.xlsx'
xls = pd.ExcelFile(file_path)

# Load the specified sheet and select relevant columns
faculty_data = pd.read_excel(xls, sheet_name='CAES Faculty')[['Last Name', 'First Name', 'Bios']].dropna()

# Generating outputs and inserting into the database
with app.app_context():
    for index, row in faculty_data.iterrows():
        last_name = row['Last Name']
        first_name = row['First Name']
        bios = row['Bios']

        # Generating username and email
        username = f"{first_name[0].lower()}{last_name.lower()}"
        email = f"{first_name.lower()}.{last_name.lower()}@cleverlytics.com"
        affil_name = "Mohammed 6 Polytechnic University"
        bibliography_content = bios

        # Creating the user
        user = User(username=username, email=email)
        
        # Set a password (use appropriate hashing in practice)
        password = username  # Simplified for this example; hash in practice
        user.set_password(password)  # Assuming you have a method to set the password
        db.session.add(user)  # Add the user to the session

        # Committing the user to the database to generate an ID for the bibliography
        db.session.commit()

        # Creating the bibliography
        biblio = Bibliography(title=f"{first_name} {last_name}",
                            content=bibliography_content, author=user)
        db.session.add(biblio)  # Add the bibliography to the session
        db.session.commit()  # Commit the bibliography to the database

print("All users and bibliographies have been added to the database.")
