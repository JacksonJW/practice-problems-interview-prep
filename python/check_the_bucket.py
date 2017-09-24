def check_the_bucket(bucket):
    for x in bucket:
        if x == 'gold':
            return True
    return False

print(check_the_bucket(['stone','gold']))
