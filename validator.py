def validate_records(records):
    seen = set()
    for record in records:
        if "member_id" not in record:
            return {"valid": False, "error": "Missing member_id"}
        member_id = record["member_id"]
        if member_id is None or member_id.strip() == "":
            return {"valid": False, "error": "Blank member_id"}
        if member_id in seen:
            return {"valid": False, "error": "Duplicate member_id"}
        seen.add(member_id)
    return {"valid": True}

if __name__=="__main__":
    print(validate_records([
        {"member_id": "M101"},
        {"member_id": "M102"}
    ]))
