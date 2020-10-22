# Add time
pd.to_datetime(df['lent_at'], errors='coerce') + timedelta(hours=7)
pd.to_datetime(df['lent_at'], errors='coerce').dt.year

# Add day in else columns
borrowing_df['time_add'] = pd.to_timedelta(borrowing_df['duration'],'d')
borrowing_df['full_payment_date'] = borrowing_df['lent_at'] + borrowing_df['time_add']