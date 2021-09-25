# THIS IS A LITTLE PART OF Financial.py
# VARIABLES NAMES, TABLES, and DB releated names changed due to security

def cash_transaction(cid, amount=None):
    # Connecting to database
    db, cursor = db_connection("Financial_DB")

    # Extracting how much cash user have currently
    _query = "SELECT c_cash FROM transaction WHERE cid='{}'".format(cid)
    current_cash = cursor.execute(_query).fetchall()[0][0]

    # Validating this transaction
    auth_res, _cash_hash = auth.check(current_cash)
  
    if auth_res:
        # Updating DB with new information
        current_cash += amount + ":" + _cash_hash
        _query = "UPDATE transaction SET c_cash = '{}' WHERE cid = '{}'"
        _query.format(current_cash, cid)
        cursor.execute(_query)
        db.commit()
    
    # Returning operation result 
    return _cash_hash
