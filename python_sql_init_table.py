with conn_input.cursor() as cursor:
    try:
        create_table_query = '''
        create table warning_contacts
        (
            user_id int not null,
            phone_numbers text not null,
            names text not null,
            contact_id int not null,
            is_special_name int not null,
            is_name_china int not null,
            is_name_simple int not null,
            is_name_bank int not null,
            is_connect_zalo int not null,
            is_missing int not null
        );
        '''
        cursor.execute(create_table_query)
        cursor.execute('create unique index warning_contacts_contact_id_uindex'
                       ' on warning_contacts (contact_id);')
        cursor.execute('alter table warning_contacts '
                       'add constraint warning_contacts_pk '
                       'primary key (contact_id);')
        conn_input.commit()
        print('init warning table')
        cursor.close()
        return 'init'
    except Exception as e:
        print('warning table exist')
        return 'exist'