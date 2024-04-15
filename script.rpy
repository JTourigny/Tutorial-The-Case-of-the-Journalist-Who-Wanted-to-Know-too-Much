# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define Stew = Character('Stew', color='#FF5733')
define Anon = Character('Anon', color='#3366ff')


# The game starts here.

#define images
image stew neutral:
    "stew_neutral.png"
    zoom 1.0

image stew thinking:
    "stew_thinking.png"
    zoom 1.0

image stew happy:
    "stew_happy.png"
    zoom 1.0

image stew sad:
    "stew_sad.png"
    zoom 1.0

image stew mad:
    "stew_mad.png"
    zoom 1.0

image stew scared:
    "stew_scared.png"
    zoom 1.0

image stew interested:
    "stew_interested.png"
    zoom 1.0

image package:
    "package.jpg"
    zoom 0.65

image frame:
    "frame.png"
    zoom 0.04

image alarm:
    "alarm.jpg"
    zoom 0.7

image box:
    "box.jpg"
    zoom 1.0

image finger:
    "finger.jpg"
    zoom 1.5

image anon:
    "anon.jpg"
    zoom 1.0

image texas:
    "texas.jpg"
    zoom 1.0

image phone:
    "phone.jpg"
    zoom 0.6

#position item
transform framefit:
    xalign 0.97
    yalign 0.025

#define backgrounds
image bg_desk:
    "bg_desk.jpg"
    zoom 1.0

image bg_black:
    "bg_black.jpg"
    zoom 3.0

image bg_hospital:
    "hospital.jpg"
    zoom 1.5

image bg_fbi:
    "fbi.jpg"
    zoom 3.0

image bg_alley:
    "alley.jpg"
    zoom 6.0

image bg_court:
    "court.jpg"
    zoom 2.0

image bg_farm:
    "farm.jpg"
    zoom 6.0

        
#Start
label start:
    "Early morning, October 13, 2020, Washington D.C.—"

label part1: 
    play music "audio/disco_ost.mp3" fadein 1.0 volume 0.25
    scene bg_desk
    show stew_sad
    Stew "I haven’t had my coffee yet and I didn’t get much sleep last night."
    show stew_happy
    Stew "I have been working on a story that may turn this capital upside down."
    show stew_interested
    Stew "It has a little bit of everything: corruption, threats to national security, money scams, oppression against US citizens, and a whole lot of finger-pointing in all directions."
    show stew_scared
    Stew "If I don’t get this one right, I may lose much more than my job… I can lose my freedom, my life, my credibility, and, what is worse, if I get this one wrong, millions will die or suffer in the hands of a corrupt tyrant."
    show stew_neutral
    Stew "Well, time to make some tough decisions."
    show stew_thinking

label choice1:
    show frame at topright
    show package at framefit
    Stew "Hmm… there is a package on my desk…"
    Stew "What should I do?"
menu:
    "Open the package.":
        jump choice1_a
    "Examine the package (you pick it up to check for weight, turn it around, etc.).":
        jump choice1_a
    "Examine the package without touching it.":
        jump choice1_c
    "Call 911 and run for your life screaming 'It’s a bomb!!!'":
        jump choice1_d
    "Ignore the package for now.":
        jump choice1_e

label choice1_a:
    scene bg_black
    show alarm at truecenter
    "It’s an alarm clock and it goes off as soon as you touch the package." 
    scene bg_hospital
    "You have a mild heart attack and needs to be taken to the hospital."
    jump choice1_common

label choice1_c:
    scene bg_black
    show box at truecenter
    "It’s a cubic box wrapped in an ugly red Christmas paper. A little card says “Stew Dent” and nothing else."
    jump choice1_common

label choice1_d:
    scene bg_fbi
    show alarm at truecenter
    "The bomb squad comes in and finds an alarm clock after a few hours of tense operations to defuse the possible bomb."
    "You are held for questioning for a few more hours. Everyone in your building is now a bomb suspect and needs to be questioned by the police."
    jump choice1_common

label choice1_e:
    scene bg_black
    show alarm at truecenter
    "The alarm goes off as soon as you leave the building." 
    hide alarm
    show finger at truecenter
    "One of your colleagues calls a bomb squad and the entire building is held for questioning by the police. They are looking for you now."
    jump choice1_common

label choice1_common:
    scene bg_black
    "End of Story 1"
    "Story 2"   

#Story 2
label start2:
    scene bg_desk
    show stew_happy
    "You sit down in front of your desktop and revise the case files."
    "It all began when an anonymous poster (yes, the poster’s nickname was “Anonymous Poster” …) posted a specific threatening message on the comment section of a story on the R.I. Post’s (the newspaper where you work) website."
    "It was a story about recently-elected U.S. Senator Paul Litik, an independent politician from Texas and possible candidate for the presidency,"
    "...who was defending the construction of a continental natural gas pipeline that would connect different pipeline systems from Canada all the way to Mexico."
    
label poster: 
    #play music "audio/disco_ost.mp3" fadein 1.0 volume 0.25
    scene bg_alley
    show anon
    Anon "They have built pipelines near my house similar to those."
    Anon "They leaked."
    Anon "I lost everything."
    Anon "Now, it’s their turn."
    Anon "I will make sure Senator Litik understands what losing everything is."
    Anon "I will take his family, his house, and burn everything to the ground, like he did with mine."
    Anon "Then, I will hunt him down and finish him."
    Anon "He will pay for what he did."
    Anon "I promise."

label choice2:
    scene bg_desk
    show stew_happy
    "You were the first one to see the post. What did you do with this information?"
menu:
    "You called your paper’s IT security chief and asked her to track down the poster’s IP address.":
        jump choice2_a
    "You called your paper’s legal counsel and asked him for help.":
        jump choice2_a
    "You deleted the post and kept it to yourself in order to investigate the poster on your own.":
        jump choice2_c
    "You did nothing. It was not your story, so it was not your problem.":
        jump choice2_d

label choice2_a:
    scene bg_court
    show texas at truecenter
    "The security chief and legal counsel contact the FBI and track down the IP address to an account in Texas." 
    jump choice2_common

label choice2_c:
    scene bg_black
    "Ok."
    jump choice2_common

label choice2_d:
    scene bg_court
    "Once the story’s author sees the post, she contacts legal counsel and they contact the FBI."
    jump choice2_common

label choice2_common:
    scene bg_farm
    "The FBI tracked the post to an account owned by a former farmer named Manny People."
    show phone at truecenter
    "The FBI quickly tried to locate Manny People, but they only found his smart phone left near the gate to Senator Litik’s farm,"
    "in the outskirts of Brownsville, Texas."

label choice3:
    "Choose the best answer:"
menu:
    "The FBI found the smart phone and they can search the phone’s contents, even private information in the email account, without a warrant from a judge.":
        jump choice3_a
    "The FBI found the smart phone, but they need a secret judge to allow them to search the more private contents of the smart phone.":
        jump choice3_a
    "The FBI found the smart phone and they need a regular warrant from a federal judge to search the private contents of the smart phone.":
        jump choice3_c
    "If the landowner had found the smart phone on his land, he could access any private information in the phone without fear of being prosecuted.":
        jump choice3_a

label choice3_a:
    scene bg_black
    "Incorrect." 
    jump choice3_common

label choice3_c:
    scene bg_black
    "Correct!"
    jump choice3_common

label choice3_common:
    scene bg_black
    "The phone was found during an investigation of a threat against a US Senator and, therefore,"
    "it’s a national security issue described in the Federal Rules of Criminal Procedures, Title VIII, Rule 41. Search and Seizure."
    centered "a magistrate judge—in an investigation of domestic terrorism or international terrorism—with authority in any district in which activities related to the terrorism may have occurred has authority to issue a warrant for a person or property within or outside that district;" 

label choice4:
    "Could Manny People argue in court that his threat was just his form of exercising his First Amendment rights in the same way artists and musicians can do in their lyrics?"
menu:
    "Yes, but he would probably lose the case as the Supreme Court Justices seem to be leaning towards the idea that the threats in themselves cause “fear and disruption to society and to the individuals who are targeted” (definition given by Michael Dreeben DOJ lawyer on the Elonis case), limiting the “proof of intent” defense.":
        jump choice4_c
    "Yes, he could. He can always argue that he had no real intent of causing harm and that his post was just a way to vent his frustrations. He would be successful as the Supreme Court Justices said they believe there is no difference between a threat posted on social media as a form of free expression and the lyrics of a rap song posted in the same way.":
        jump choice4_a
    "No, he cannot. The Supreme Court has decided that it is not a valid argument, so he is defended from using it in any court.":
        jump choice4_a

label choice4_a:
    scene bg_black
    "Incorrect." 
    jump choice4_common

label choice4_c:
    scene bg_black
    "Correct!"
    jump choice4_common

label choice4_common:
    scene bg_black
    "See http://www.latimes.com/nation/la-na-supreme-court-facebook-threats-free-speech-20141201-story.html"
    "End of Story 2"
