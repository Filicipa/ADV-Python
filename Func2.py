

def create_record(name, tel, address):
    """Create record"""
    record = {
        "name": name,
        "tel": tel,
        "address": address
    }
    return record


user1 = create_record("Shasha", "0977", "Dnipro")


user2 = create_record("Petja", "02222", "New York")

print(user1)
print(user2)


def give_award(medal, *persons):
    """Give Medals to persons"""
    for person in persons:
        print("Tovarish " + person.title() + " nagrazhdaetsa " + medal)


give_award("Za Berlin", "Vasya", "petja")


give_award("Za London", "sasha", "valik")
