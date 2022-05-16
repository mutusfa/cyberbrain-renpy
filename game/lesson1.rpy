define character.cybered = Character(name="CyberED", color="#37376b")
define character.cyberdi = Character(name="CyberDI", color="#6b0f38")

init python:
    import random
    import os

    wordlist = renpy.file("other_assets/eff_large_wordlist.txt").read().decode("utf-8").split()

    def generate_passphrase(num_words=4):
        return " ".join(random.sample(wordlist, num_words))

label lesson1_start:
    scene island map
    with dissolve

    show cybered happy at leftofcenter
    show cyberdi happy at rightofcenter

    cybered "Hey! We are the super heroes of Cyber ED and Cyber Di, standing by to protect your safety in the digital world."
    
    cyberdi "We will teach you the basics of security. It will be exciting and interesting and interesting adventures await you at the end!"
    
    cybered "Come with us! In the campaign, you will need Golden Talents. keep 100 coins!"

    $ coins += 100

    cyberdi """So you have incredibly important information.
    
    But it cannot be told to strangers and robots.
    
    Do you know what this information is?"""
    
    cybered "We will advise! This is your date of birth, age, phone number, home address, passwords, mail"

    cyberdi "Let's play. Tell me what data is important to you"

    "TODO: add a minigame here"

    cybered "Great! You have earned 500 experience points. Now you can buy yourself a Security Island and build a safe city on it."

    $ experience += 500

    cyberdi "Now let's buy an island, it costs 100 coins."

    $ coins -= 100

    $ island_name = renpy.input("What do you want to name your island?")

    jump island_bought

label island_bought:
    scene island map

    with dissolve

    $ renpy.pause(1.0)

    show cyberdi happy at rightofcenter

    cyberdi "Congratulations, you now have an island!"
    
    cyberdi "Let the island be your account and we will come up with a password with you to enter the island"

    show cybered happy at leftofcenter

    cybered "Do you know that the password should be complex?"

    cyberdi """Everyone knows that a password should be complex enough, but what does that mean?
    
    A good password should be at least 12 characters long to be difficult to crack
    """
    
    cybered "(count how many characters are in your social network password?)"
    
    cyberdi """The longer, the better.

    Easy way to create a long password that's strong and easy to remember is to use a passphrase of 4 random words
    """

    cybered """I will do that now. I will create a password with 4 random words.
    
    You can read more about how to choose random words here: https://www.eff.org/dice . We just think that 6 words is an overkill and a lot of websites won't allow entering passwords that long.
    """

    label cybered_thinksof_password:

        $ cybered_passphrase = generate_passphrase()

        cybered "I think of: [cybered_passphrase]"

        menu:
            cybered "Shall I think of another one?"

            "Yes":
                jump cybered_thinksof_password

            "No":
                pass

    cyberdi "Your turn!"

    python:
        while True:
            user_password = renpy.input("What is your password?")

            if len(user_password) < 12:
                character.cyberdi("Your password is too short. It should be at least 12 characters long.")
            else:
                break

            # I know md5 is way too weak,
            # this is just an mvp and we aren't even storing password or hash anywhere
            user_password_hash = hash(user_password)
            del user_password

    cybered """Now you are ready to move to a new level - your island has become 2 times larger and now you can build a house on it.
    
    Forward to a new level!"""

    return