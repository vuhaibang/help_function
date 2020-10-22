SQL = '''
REPLACE INTO warning_contacts
(user_id,
phone_numbers,
contact_id,
names,
is_name_china,
is_special_name,
is_name_simple,
is_name_bank,
is_connect_zalo,
is_missing)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s),
(user_id,
phone_numbers,
contact_id,
names,
is_name_china,
is_special_name,
is_name_simple,
is_name_bank,
is_connect_zalo,
is_missing)
'''
with conn_input.cursor() as cursor:
    my_data = []
    for _, user_id, phone_number, contact_id, name, is_name_china, \
        is_special_name, is_name_simple, is_name_bank, is_connect_zalo, \
        is_missing in contacts_df.itertuples():
        my_data.append((
            user_id,
            phone_number,
            contact_id,
            name,
            is_name_china,
            is_special_name,
            is_name_simple,
            is_name_bank,
            is_connect_zalo,
            is_missing
        ))
        if len(my_data) >= 1000:
            cursor.executemany(SQL, my_data)
            conn_input.commit()
            my_data = []
    if len(my_data) > 0:
        cursor.executemany(SQL, my_data)
        conn_input.commit()
        cursor.close()
        conn_input.close()