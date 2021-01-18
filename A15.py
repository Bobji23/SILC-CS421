class FAMILY:
    def __init__(self, list_of_family):
        self.list_of_family = list_of_family

    def __repr__(self):
        return 'FAMILY(list_of_classes=%s)' % (self.list_of_family)

    def __str__(self):
        return 'FAMILY(list_of_family=%s)' % (self.list_of_family)






class FAM_CLASS:
    def __init__(self, list_of_family):
        self.list_of_family = list_of_family

    def __repr__(self):
        return 'FAM_CLASS(list_of_family=%s)' % (self.list_of_family)

    def __str__(self):
        return 'FAM_CLASS(list_of_family=%s)' % (self.list_of_family)



class Member:
    def __init__(self, name, age, birthdate):
        self.name = name
        self.age = age
        self.birthdate = birthdate

    def __repr__(self):
        return 'Member(name=%s, age=%s, birthdate=%s)' % (self.name, self.age, self.birthdate)

    def __str__(self):
        return 'Member(name=%s, age=%s, birthdate=%s)' % (self.name, self.age, self.birthdate)



class Birthdate:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def __repr__(self):
        return 'Birthdate(month=%s, day=%s, year=%s)' % (self.month, self.day, self.year)

    def __str__(self):
        return 'Birthdate(month=%s, year=%s)' % (self.month, self.day)





birthday1 = Birthdate("November", 8, 2006)



birthday2= Birthdate("March", 25, 1979)




birthday3 = Birthdate("July", 23, 1973)




family_member1 = Member("Suhas", 14, birthday1)



family_member2 = Member("Purnima", 41, birthday2)




family_member3 = Member("Chandra", 47, birthday3)




family_list = [family_member1, family_member2, family_member3]
family_class = FAM_CLASS(family_list)




more_family = [family_member1, family_member2]
more_class = FAM_CLASS(more_family)



list_of_classes = [family_class, more_class]
my_family = FAMILY(list_of_classes)





print("Family --> ", my_family)
