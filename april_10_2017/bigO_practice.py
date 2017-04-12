lst = ["Eric", "Eric", "Kat", "Kat",  "Linda", "Kelly", "Dani", "Kelly", "Julissa", "Kat", "Kelly", "Dani", "Kat", "Kat"]


def freq_hash(lst):
    count_dict = {}

    for item in lst:
        count_dict[item] = count_dict.get(item, 0) + 1

    print count_dict


def find_mode(lst):
    count_dict = {}

    for item in lst:
        count_dict[item] = count_dict.get(item, 0) + 1

    highest_freq = []

    max_value = 0

    for key, value in count_dict.iteritems():
        if value > max_value:
            max_value = value

    for key, value in count_dict.iteritems():
        if value == max_value:
            highest_freq.append(key)

    print highest_freq

freq_hash(lst)
find_mode(lst)
