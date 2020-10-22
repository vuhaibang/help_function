for _, user_id, score, method, updated in df.itertuples():
    operations.append(
        UpdateOne({'user_id': int(user_id)},
                  {'$set': {
                      'score': score,
                      'score_methods': method,
                      'updated_at': updated
                  }},
                  upsert=True))
    # Send once every 1000 in batch
    if (len(operations) == 1000):
        conn_mongodb.bulk_write(operations, ordered=False)
        print('bulk_write 1000')
        operations = []
    else:
        continue

if (len(operations) > 0):
    conn_mongodb.bulk_write(operations, ordered=False)
    print('bulk_write end')
else:
    pass