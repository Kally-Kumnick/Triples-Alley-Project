import pandas as pd

# Load the Excel files
b2b = pd.read_excel('B2B24_cleaned.xlsx')
drc = pd.read_excel('DRC24_cleaned_0617.xlsx')
tgr = pd.read_excel('TGR24_cleaned_0617.xlsx')

# Select relevant columns
b2b = b2b[['Last Name', 'First Name', 'Email']]
drc = drc[['Last Name', 'First Name', 'Email']]
tgr = tgr[['Last Name', 'First Name', 'Email']]

# Group 1: Signed up for all 3 marathons
group1 = b2b.merge(drc, on=['Last Name', 'First Name', 'Email']).merge(tgr, on=['Last Name', 'First Name', 'Email'])

# Group 2: Signed up for marathon 1 and 2 (B2B24 and DRC24)
group2 = b2b.merge(drc, on=['Last Name', 'First Name', 'Email'])

# Group 3: Signed up for marathon 1 and 3 (B2B24 and TGR24)
group3 = b2b.merge(tgr, on=['Last Name', 'First Name', 'Email'])

# Output the results to Excel file
with pd.ExcelWriter('marathon_signups.xlsx') as writer:
    group1.to_excel(writer, sheet_name='All_3_Marathons', index=False)
    group2.to_excel(writer, sheet_name='B2B_and_DRC', index=False)
    group3.to_excel(writer, sheet_name='B2B_and_TGR', index=False)

print("Output has been saved to marathon_signups.xlsx")