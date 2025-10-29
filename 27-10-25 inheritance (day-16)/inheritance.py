#1,
class personal:
    def name(self):
        return "karuppu"
    def email(self):
        print("karuppu29032005gmail.com")
    def mobile(self):
        print("8940297513")
    def address(self):
        print("avniyapuram")
class educational(personal):
    def bsc(self):
        print("BA Economice")
a=educational();
a.email()
print()

#2,
class personal:
    def name(self):
        print("karuppu")
    def email(self):
        print("karuppu29032005@gmail.com")
    def mobile(self):
        print("8940297513")
    def address(self):
        print("avaniyapuram")
class educational(personal):
    def bsc(self):
        print("BA Economice")
class bank(educational):
    def account(self):
        print("State Bank")
    def no(self):
        print("8940297513")
        
a=bank()
a.name()
a.email()
a.address()
a.account()
a.no()
print()

#3,
class school:
    def name1(self):
        print("st'mary's")
    def email1(self):
        print("karuppu29032005@gmail.com")
    def mobile1(self):
        print("8940297513")
    def address1(self):
        print("avaniyapuram")
class staff(school):
    def name2(self):
        print("samsung tamil teacher for 6 to 10")
    def mail2(self):
        print("samsung@gmail.com")
    def mobile2(self):
        print("95875878488")
    def address2(self):
        print("madurai")
    def dep2(self):
        print("economice Teacher")
class student(school):
    def name3(self):
        print("santhos")
    def Class3(self):
        print("10th class A")
a=student()
b=staff()
a.name3()
a.name1()
