lst = ["Eric", "Eric", "Kat", "Kat",  "Linda", "Kelly", "Dani", "Kelly", "Julissa", "Kat", "Kelly", "Dani", "Kat", "Kat"]


def freq_hash(lst):
    count_dict = {}

    for item in lst:
        count_dict[item] = [count_dict, 0] + 1
