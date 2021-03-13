import pandas as pd
import re

col_names = ['id', 'user_name', 'user_description', 'text']
media_outlet_kw = 'news[a-z]*|channel[a-z]*|media[a-z]*|tv[a-z]*|abc[a-z]*|fox[a-z]*|cnn[a-z]*|' \
                  'radio[a-z]*|magazine[a-z]*|daily[a-z]*|times[a-z]*'
ind_media_ppl_kw = 'journalist[a-z]*|reporter[a-z]*|anchor[a-z]*|blogger[a-z]*|columnist[a-z]*|' \
                   'writer[a-z]*|author[a-z]*|novelist[a-z]*|presenter[a-z]*|host[a-z]*|editor[a-z]*' \
                   'director[a-z]*|publisher[a-z]*'

med_professions = 'Medical Assistant[a-z]*|Nursing Assistant[a-z]*|Health Aide[a-z]*|Licensed Practical Nurse[a-z]*|' \
                  'Physician[a-z]*|Therapist[a-z]*|Surgeon[a-z]*|Registered Nurse[a-z]*|pharmacist[a-z]*|sonographer[a-z]*|diagnostician[a-z]*|' \
                  'Lab technician[a-z]*|Dental assistant[a-z]*|emergency medical technician[a-z]*|EMT[a-z]*|radiologist[a-z]*|dentist[a-z]*|' \
                  'health information technician[a-z]*|occupational therapist[a-z]*|speech language pathologist[a-z]*|SLP[a-z]*|' \
                  'family practitioner[a-z]*|Nurse[a-z]*|Phlebotomist[a-z]*|Veterinarian[a-z]*|vet[a-z]*|medical transcriptionist[a-z]*|' \
                  'optician[a-z]*|dietitian[a-z]*'

med_specializations = 'Pediatrics[a-z]*|paediatrics[a-z]*|medicine[a-z]*|Surgery[a-z]*|Ophthalmology[a-z]*|Geriatrics[a-z]*|Obstetrics[a-z]*|Gynecology[a-z]*|' \
                    'Gynaecology[a-z]*|Orthopedics[a-z]*|Orthopaedics[a-z]*|Oncology[a-z]*|infectious[a-z]*|Infectious Diseases[a-z]*|Cardiology' \
                    'immunology[a-z]*|[a-z]*|Anesthesiology[a-z]*|[a-z]*|Dermatology[a-z]*|radiology[a-z]*|' \
                    'Emergency care[a-z]*|Emergency room[a-z]*|genetics[a-z]*|Neurology[a-z]*|Nuclear medicine[a-z]*|' \
                    'Pathology[a-z]*|rehabilitation[a-z]*|Global health[a-z]*|community medicine[a-z]*|Psychiatry[a-z]*|'\
                    'Radiation[a-z]*|Urology[a-z]*|Pulmonology[a-z]*|palliative[a-z]*|toxicology[a-z]*|hospice[a-z]*|' \
                    'otolaryngology[a-z]*|hospital[a-z]*|clinic[a-z]*|biomedical[a-z]*|virology[a-z]*'

med_specialists = 'Pediatrician[a-z]*|Paediatrician[a-z]*|Physician[a-z]*|surgeon[a-z]*|ophthalmologist[a-z]*|geriatrician[a-z]*|' \
                'obstetrician[a-z]*|gynecologist[a-z]*|gynaecologist[a-z]*|orthopedist[a-z]*|orthopaedist[a-z]*|oncologist[a-z]*|' \
                'cardiologist[a-z]*|immunologist[a-z]*|anesthetist[a-z]*|anesthesiologist[a-z]*|dermatologist[a-z]*|radiologist[a-z]*|' \
                'geneticist[a-z]*|neurologist[a-z]*|pathologist[a-z]*|psychiatrist[a-z]*|urologist[a-z]*|pulmonologist[a-z]*|' \
                'toxicologist[a-z]*|virologist[a-z]*'

User_Data_Vaccine = pd.read_csv(
    'vaccination_all_tweets.csv', usecols=col_names)

# print(User_Data_Vaccine.head())
# print(User_Data_Vaccine)

media_outlets = User_Data_Vaccine.loc[User_Data_Vaccine['user_name'].str.contains(
    media_outlet_kw, flags=re.I, regex=True)]
media_ppl = User_Data_Vaccine.loc[User_Data_Vaccine['user_description'].str.contains(
    ind_media_ppl_kw, na=False, flags=re.I, regex=True)]
media_outlets_names = set(list(media_outlets['user_name']))
media_ppl_names = set(list(media_ppl['user_name']))

medical_professionals1 = User_Data_Vaccine.loc[User_Data_Vaccine['user_description'].str.contains(
    med_professions, na=False, flags=re.I, regex=True)]
medical_professionals2 = User_Data_Vaccine.loc[User_Data_Vaccine['user_description'].str.contains(
    med_specialists, na=False, flags=re.I, regex=True)]
medical_professionals = pd.concat([medical_professionals1, medical_professionals2])


# print(media_outlets)
# print(media_ppl)
print(medical_professionals)

media_outlets.to_csv('media_corporations.csv')
media_ppl.to_csv('media_users.csv')
medical_professionals.to_csv('healthcare_workers.csv')
