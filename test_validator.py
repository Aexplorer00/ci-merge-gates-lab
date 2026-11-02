from validator import validate_records

# Test 1: Clean valid records
assert validate_records([
    {"member_id": "M101"},
    {"member_id": "M102"}
]) == {"valid": True}

# Test 2: Duplicate IDs
assert validate_records([
    {"member_id": "M101"},
    {"member_id": "M101"}
]) == {"valid": False, "error": "Duplicate member_id"}

# Test 3: Missing key
assert validate_records([{"name": "Alice"}]) == {
    "valid": False, "error": "Missing member_id"
}

# Test 4: Blank, None, and whitespace strings
for blank_id in [None, "", "   "]:
    assert validate_records([{"member_id": blank_id}]) == {
        "valid": False, "error": "Blank member_id"
    }

print("[PASS] All validation tests passed cleanly!")
