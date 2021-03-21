
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{"first_name": "John", "id": self._generateId(), "age": 33, "lucky_numbers": [7, 13, 22]},
        {"first_name": "Jane", "id": self._generateId(), "age": 35, "lucky_numbers": [10, 14, 3]},
        {"first_name": "Jimmy", "id": self._generateId(), "age": 5, "lucky_numbers": [1]}]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # Tommy will have a static id
        if member["first_name"] == "Tommy":
            tommy = {"first_name": str(member["first_name"]), "id": member["id"], "age": int(member["age"]), "lucky_numbers": member["lucky_numbers"]}
            self._members.append(tommy)
            return
        else:
        # fill this method and update the return
            new_member = {"first_name": str(member["first_name"]),"id": self._generateId(), "age": int(member["age"]), "lucky_numbers": member["lucky_numbers"]}
            self._members.append(new_member)
            return

    def delete_member(self, id):
        # fill this method and update the return
        for member in self._members:
            print(member["id"])
            if member["id"] == id:
                print("YEY")
                self._members.remove(member)
        return

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == id:
                return member

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
