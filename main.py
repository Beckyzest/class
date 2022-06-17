class Student:    
    def _init_(self, name, age, tracks, score):
       self.name = name
       self.age = age
       self.tracks = tracks
       self.score= score


    #A function to change the name of student
    def change_name (self, new_name):
        self.name = new_name
        return(Bob.name)

    #A function to change the age of student
    def change_age (self, age_name):
        self.age = new_age
        return(Bob.age)


    #A function to change the to an existing list of tracks
    def change_tracks (self, added_track):
        self.tracks.append(added_tracks)
        return(Bob.tracks)

    #A function to change the age of student
    def get_score (self):
        return(self.score)

# Here i am creating an instance of the class toether with the properties
Bob = Student("Bob",26, ["FE", "BE"], 20.90)
# Expected methods
Print (Bob.change_name("Peter"))
Print (Bob.change_age(34))
print (Bob.add_track("UI/UX"))
print (Bob.get_score())
