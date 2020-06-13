import hashlib
import csv


def hash_password_hack(input_file_name, output_file_name):
    acc_list = dict()
    with open(input_file_name) as csv_file_in:
        reader = csv.reader(csv_file_in)
        for row in reader:
            # reading All Name & Password Data from csv
            acc_list[row[0]] = row[1]

    password_list = dict()
    for i in range(1000, 10000):
        hash_list_obj = hashlib.sha256()
        hash_list_obj.update(bytes(str(i).encode()))
        # Collecting All sha in range 1000 to 9999
        password_list[hash_list_obj.hexdigest()] = str(i)

    hacked_acc = dict()
    for this_person_name, this_person_password in acc_list.items():
        for this_password in password_list.keys():
            if this_person_password == this_password:
                hacked_acc[this_person_name] = password_list[this_password]

    with open(output_file_name, 'w') as csv_file_out:
        writer = csv.writer(csv_file_out)
        for this_tuple in hacked_acc.items():
            writer.writerow(this_tuple)

