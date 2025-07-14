# Data/model layer for group data access
from firebase.firestore_client import db

def create_group(group_data):
    doc_ref = db.collection("groups").document()
    group_data["id"] = doc_ref.id
    write_time = doc_ref.set(group_data)
    return {"write_time": str(write_time), "id": doc_ref.id}

def get_group_by_key(group_id):
    doc_ref = db.collection("groups").document(group_id).get()
    print(doc_ref)
    if doc_ref:
        return doc_ref.to_dict()
    return None

def update_group(group_id, group_data):
    doc_ref = db.collection("groups").document(group_id)
    doc_ref.update(group_data)

def delete_group_by_key(unique_key):
    # TODO: Implement delete group by unique key
    return {}