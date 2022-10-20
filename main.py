import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')
db = client['db']
collection = db['clinical_trials']
organizations_collection = db['clinical_trials_organizations']
organizations = collection.distinct(
    key='FullStudy.Study.ProtocolSection.IdentificationModule.Organization.OrgFullName')
for organization in list(organizations):
    organizations_collection.insert_one({"organization":organization})