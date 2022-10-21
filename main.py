import time

import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')
db = client['db']
updated_clinical_trials = db['updated_clinical_trials']
collection = db['clinical_trials']
organizations_collection = db['clinical_trials_organizations']
organizations = collection.distinct(
    key='FullStudy.Study.ProtocolSection.IdentificationModule.Organization.OrgFullName')
for organization in list(organizations):
    # organizations_collection.insert_one({"organization": organization})
    list_organization_trials = list(collection.find({'FullStudy.Study.ProtocolSection.IdentificationModule.Organization.OrgFullName': organization}))
    for i in list_organization_trials:
        print(i)
    updated_clinical_trials.insert_one({'organization': organization, 'Organization_trials': list_organization_trials})