import random
import time

class Trainer:
    """The player is a kickboxing athlete training for conditioning, strength, and if need be, a fight!
    They will have the opportunity to do multiple workouts to gain experience points and move
    on to the next level."""

    def __init__(self):
        """Starting conditions for the kickboxer."""
        self.level = 0
        self.experience = 0
        self.workout = Workout()

    def set_level_exp(self):
        """Takes input from user on level of experience with kickboxing."""

        print ("Let's design a workout schedule!")
        time.sleep(2)

        # Gets input from user and allows for multiple entries in case of user error.
        while True:
            level = input('What level are you? Are you A) beginner, B) intermediate, or C) advanced?'
                       ' Type (Help) for more information.   ').lower()

            # Gives information to user on experience points and what the levels mean.
            if level == 'help':
                print('\n----------------------------')
                print ('A) "Beginner" refers to anyone who has never taken kickboxing lessons before,'
                       ' or has only taken one or two. As a beginner, you start with 0 experience points.')
                print ('B) "Intermediate" refers to someone who knows the basics of kickboxing, but has'
                      ' never trained for a specific purpose. As an intermediate, you start with 5 experience points.')
                print ('C) "Advanced" refers to someone who is well-versed in kickboxing, has trained'
                      ' for a specific purpose before, and wants to train again. Advanced kickboxers'
                      ' start with 10 experience points.', '\n')
                print('\n----------------------------')

            # Sets experience points based on user level.
            elif level == 'a' or level == 'beginner':
                self.experience = 0
                break

            elif level == 'b' or level == 'intermediate':
                self.experience = 5
                break

            elif level == 'c' or level == 'advanced':
                self.experience = 10
                break

            else:
                print ('Invalid entry: Please try again')


    def review(self, day):
        """Prints out a review of workouts completed, and how many remain
        until the player reaches the goal."""

        print('\n----------------------------')
        print('Daily review for day #', day)
        print('You worked out for: ', self.workout.min, 'minutes.')
        print('You now have', self.experience, 'experience points.')
        print('You have', (20 - float(self.experience)), 'points remaining before you reach your goal.')
        print('\n----------------------------')

    def ready(self):
        """Checks to see if player has reached the goal of 20 experience points."""
        return self.experience >= 20

    def rungame(self):
        """Starts the trainer engine and loops until training is complete."""

        # Starting on Day 1 - gives the initial setting of the parameters.
        day = 1
        print ('Day 1. You have started your kickboxing journey!')
        time.sleep(2)
        print ('Your goal is to reach 20 experience points.')
        time.sleep(2)
        print ('To achieve this, you will need to complete a certain \n'
              'number of kickboxing workouts, depending on your current \n'
              'experience level.')
        time.sleep(2)

        # Sets the level of experience using the set_level_exp method.
        self.set_level_exp()

        # Loops through and creates workouts, updating experience points each time.
        # Continues until the user has reached 20 experience points, then breaks.
        while True:
            # Calls workout_structure method from Workout class.
            self.workout.workout_structure()
            # Updates experience points based on length of workout.
            if self.workout.min == 30:
                self.experience += 0.5
            elif self.workout.min == 45:
                self.experience += 0.75
            elif self.workout.min == 60:
                self.experience += 1
            # After each day, prints a review of the day and the experience points gained.
            self.review(day)
            # Checks if the user has reached the 20 point goal.
            if self.ready():
                print ("Congratulations! You have achieved your goal in", day, "days!")
                break
            # Each time it goes through the loop, adds 1 to the day.
            day += 1

class Workout:
    """Creates random workouts based on the time specified by the user."""

    def __init__(self):
        self.min = 0

    def set_min(self):
        """Sets the number of minutes for the workout, a choice between
        30, 45, and 60."""

        # Checks for user error without raising exceptions, looping until a valid
        # time is chosen.
        while True:
            self.min = int(input("How many minutes can you work out today? Please enter 30, 45, or 60: "))

            # checks user input is within the limits of the program
            if self.min in [30,45,60]:
                print ('\n', "You have chosen a", self.min, "minute workout.")

                # Prints what the workout consists of, given the time chosen by the user.
                if self.min == 30:
                    print ('\n', "This workout will include a 7-minute warmup, four 3-minute rounds of kickboxing,"
                       " and 7 minutes of core.")
                    time.sleep(2)
                elif self.min == 45:
                    print ('\n', "This workout will include a 7-minute warmup, eight 3-minute rounds of kickboxing,"
                       " and 7 minutes of core.")
                    time.sleep(2)
                elif self.min == 60:
                    print ('\n', "This workout will include a 15-minute warmup, eight 3-minute rounds of kickboxing,"
                       " and 15 minutes of core.")
                    time.sleep(2)
                break

            else:
                print ("Invalid entry. Please enter 30, 45, or 60 for length of workout.")

    def cardiowarmup(self, min):
        """Defines the cardio warmup portion of the workout.
        Reads the warmup.txt document and returns a random list of warmup exercises.
        Length of the list depends on user input of time."""

        # Opens and reads text document, appending to a list.
        with open("warmup.txt","r") as infile:
            raw_input = infile.readlines()
            warmup = [datum.strip('\n') for datum in raw_input]

        # Based on user input of time, the length of the cardio section changes.
        # Creates a list of time increments for the cardio portion.
        if self.min == 30 or self.min == 45:
            cardio_vals = ["30 sec", "30 sec", "30 sec", "30 sec", "30 sec", "30 sec"]
        elif self.min == 60:
            cardio_vals = ["30 sec", "30 sec", "30 sec", "30 sec", "30 sec", "30 sec",
                      "30 sec", "30 sec", "30 sec", "30 sec"]

        # Creates a list of random cardio exercise moves that is the same length as
        # the list of cardio time increments.
        cardio_keys = [random.sample(warmup, len(cardio_vals))]
        # Flattens the list of random cardio exercises to individual items in a list.
        flattened_cardiokeys = [val for sublist in cardio_keys for val in sublist]
        # Creates a dictionary from both lists - with the random cardio exercises as the keys
        # and the time increments as the values.
        dictcardio = dict(zip(flattened_cardiokeys, cardio_vals))
        # Returns a formatted dictionary of key value pairs.
        return ("\n".join("{}, {}".format(k, v) for k, v in dictcardio.items()))


    def shadowwarmup(self, min):
        """Defines the shadow kickboxing warmup portion of the workout.
        Reads the shadowboxing.txt document and returns a random list of warmup exercises.
        Length of the list depends on user input of time."""

        # Opens and reads text document, appending to a list.
        with open("shadowboxing.txt","r") as infile:
            raw_input = infile.readlines()
            shadowboxing = [datum.strip('\n') for datum in raw_input]

        # Based on user input of time, the length of the shadowboxing section changes.
        # Creates a list of time increments for the shadowboxing portion.
        if self.min == 30 or self.min == 45:
            shadow_vals = ["30 sec", "30 sec", "30 sec", "30 sec", "30 sec", "30 sec"]
        elif self.min == 60:
            shadow_vals = ["30 sec", "30 sec", "30 sec", "30 sec", "30 sec", "30 sec",
                  "30 sec", "30 sec", "30 sec", "30 sec", "30 sec", "30 sec", "30 sec", "30 sec"]

        # Creates a list of random shadowboxing exercise moves that is the same length as
        # the list of shadowboxing time increments.
        shadow_keys = [random.sample(shadowboxing, len(shadow_vals))]
        # Flattens the list of random shadowboxing exercises to individual items in a list.
        flattened_shadowkeys = [val for sublist in shadow_keys for val in sublist]
        # Creates a dictionary from both lists - with the random shadowboxing exercises as the keys
        # and the time increments as the values.
        dictshadow = dict(zip(flattened_shadowkeys, shadow_vals))
        # Returns a formatted dictionary of key value pairs.
        return ("\n".join("{}, {}".format(k, v) for k, v in dictshadow.items()))

    def round_structure(self, min):
        """Defines the structure of the kickboxing rounds portion of the workout.
        Reads 3 documents to produce rounds: kickboxingmoves.txt, cardiointensity.txt,
        and warmup.txt. Returns a random list of kickboxing exercises, and structures
        the rounds using the other exercises.The number of rounds depends on user input of time."""

        # Opens and reads text document, appending to a list.
        with open("kickboxingmoves.txt","r") as infile:
            raw_input = infile.readlines()
            kickboxingmoves = [datum.strip('\n') for datum in raw_input]

        # Opens and reads text document, appending to a list.
        with open("cardiointensity.txt","r") as infile:
            raw_input = infile.readlines()
            cardiointensity = [datum.strip('\n') for datum in raw_input]

        # Opens and reads text document, appending to a list.
        with open("warmup.txt","r") as infile:
            raw_input = infile.readlines()
            warmup = [datum.strip('\n') for datum in raw_input]

        # Based on user input of time, the number of kickboxing rounds changes.
        if self.min == 30:
            num_rounds = 4
        elif self.min == 45 or self.min == 60:
            num_rounds = 8

        # The round is constructed of multiple segments. The combination comes first
        # (a random sample of 5 kickboxing moves), then some cardio intensity moves.
        # The same structure and moves are repeated after switching feet to southpaw stance.
        # The round is always followed by 1 minute of active rest.

        # Creates the string for the combination time.
        combo_time = ("1 min 10 sec")
        # Creates randomly generated lists of kickboxing moves, one for each round.
        combo_moves = [random.sample(kickboxingmoves, 5) for _ in range(num_rounds)]
        # Creates the string for the cardio intensity time.
        c_intensity_time = ("20 sec")
        # Creates randomly generated list of cardio intensity moves, one for each round.
        c_intensity_moves = [random.sample(cardiointensity, 1) for _ in range(num_rounds)]
        # Creates the string for the combination time.
        active_rest_time = ("1 min")
        # Creates randomly generated list of active rest moves, one for each round.
        active_rest_moves = [random.sample(warmup, 1) for _ in range(num_rounds)]

        # Formats the round for the user.
        for rnd in range(num_rounds):
            print('\n----------------------------')
            print ("Round", rnd+1, '\n', combo_time)
            print (*combo_moves[rnd], sep = ', ')
            print (c_intensity_time)
            print (*c_intensity_moves[rnd], sep = ',')
            print ("Switch feet to southpaw stance!", '\n', combo_time)
            print (*combo_moves[rnd], sep = ', ')
            print (c_intensity_time)
            print (*c_intensity_moves[rnd], sep = ', ')
            print (active_rest_time, "ACTIVE REST")
            print (*active_rest_moves[rnd], sep = ', ')
            print('\n----------------------------')

    def core(self, min):
        """Defines the core portion of the workout.Reads the core.txt document and
        returns a random list of core exercises.Length of the list depends on
        user input of time."""

        # Opens and reads text document, appending to a list.
        with open("core.txt","r") as infile:
            raw_input = infile.readlines()
            core = [datum.strip('\n') for datum in raw_input]

        # Based on user input of time, the length of the core section changes.
        # Creates a list of time increments for the core portion.
        if self.min == 30 or self.min == 45:
            core_vals = ["30 sec", "30 sec", "30 sec", "30 sec", "30 sec", "30 sec",
                    "30 sec", "30 sec", "30 sec", "30 sec", "30 sec", "30 sec",]
        elif self.min == 60:
            core_vals = ["30 sec", "30 sec", "30 sec", "30 sec", "30 sec", "30 sec",
                    "30 sec", "30 sec", "30 sec", "30 sec", "30 sec", "30 sec",
                    "30 sec", "30 sec", "30 sec", "30 sec", "30 sec", "30 sec",
                    "30 sec", "30 sec", "30 sec", "30 sec", "30 sec", "30 sec",
                    "30 sec", "30 sec", "30 sec", "30 sec"]

        # Creates a list of random core exercise moves that is the same length as
        # the list of core time increments.
        core_keys = [random.sample(core, len(core_vals))]
        # Flattens the list of random shadowboxing exercises to individual items in a list.
        flattened_corekeys = [val for sublist in core_keys for val in sublist]
        # Creates a dictionary from both lists - with the random core exercises as the keys
        # and the time increments as the values.
        dictcore = dict(zip(flattened_corekeys, core_vals))
        # Returns a formatted dictionary of key value pairs.
        return ("\n".join("{}, {}".format(k, v) for k, v in dictcore.items()))


    def workout_structure(self):
        """Creates a whole workout, which includes a warmup, a certain number of
        kickboxing rounds, and core exercises."""

        # Defines the time of the workout as designated by the user.
        min = self.min
        # Calls the set_min function to set the time.
        self.set_min()
        # Formats the workout in a readable way.
        print('\n----------------------------')
        # Warmup first (includes both cardio and shadowboxing).
        print ('\n', "Warmup: ")
        print (self.cardiowarmup(min))
        print (self.shadowwarmup(min), '\n')
        time.sleep(2)
        # Then Rounds
        print (self.round_structure(min), '\n')
        time.sleep(2)
        # Then Core
        print ("Core", '\n', self.core(min), '\n')
        time.sleep(2)
        print ("Congratulations! Now go take a shower.")
        print('\n----------------------------')


trainer = Trainer()
trainer.rungame()
