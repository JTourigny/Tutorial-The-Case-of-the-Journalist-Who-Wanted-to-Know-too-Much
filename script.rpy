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

#new images
image barn_trace:
    "barn_trace.jpg"
    zoom 8.0

image alley_trace:
    "alley_trace.jpg"
    zoom 5.0

image wash_trace:
    "wash_trace.jpg"
    zoom 5.0

image texas_trace:
    "texas_trace.jpg"
    zoom 8.0

image phone_trace:
    "phone_trace.jpg"
    zoom 8.0

image package_trace:
    "package_trace.jpg"
    zoom 8.0

image desk2_trace:
    "desk2_trace.jpg"
    zoom 5.0

image desk_trace:
    "desk_trace.jpg"
    zoom 5.0

image curious_trace:
    "curious_trace.jpg"
    zoom 1.5

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
    scene wash_trace
    "Early morning, October 13, 2020, Washington D.C.—"

label part1: 
    play music "audio/disco_ost.mp3" fadein 1.0 volume 0.25
    scene desk_trace
    #show stew_sad
    Stew "I haven’t had my coffee yet and I didn’t get much sleep last night."
    #show stew_happy
    Stew "I have been working on a story that may turn this capital upside down."
    #show stew_interested
    Stew "It has a little bit of everything: corruption, threats to national security, money scams, oppression against US citizens, and a whole lot of finger-pointing in all directions."
    #show stew_scared
    Stew "If I don’t get this one right, I may lose much more than my job… I can lose my freedom, my life, my credibility, and, what is worse, if I get this one wrong, millions will die or suffer in the hands of a corrupt tyrant."
    #show stew_neutral
    Stew "Well, time to make some tough decisions."
    #show stew_thinking

label choice1:
    show package_trace
    show frame at topright
    show curious_trace at framefit
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
    scene desk_trace
    #show stew_happy
    "You sit down in front of your desktop and revise the case files."
    "It all began when an anonymous poster (yes, the poster’s nickname was “Anonymous Poster” …) posted a specific threatening message on the comment section of a story on the R.I. Post’s (the newspaper where you work) website."
    "It was a story about recently-elected U.S. Senator Paul Litik, an independent politician from Texas and possible candidate for the presidency,"
    "...who was defending the construction of a continental natural gas pipeline that would connect different pipeline systems from Canada all the way to Mexico."
    
label poster: 
    #play music "audio/disco_ost.mp3" fadein 1.0 volume 0.25
    scene alley_trace
    #show anon
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
    scene desk2_trace
    #show stew_happy
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
    scene texas_trace
    #show texas at truecenter
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
    scene barn_trace
    "The FBI tracked the post to an account owned by a former farmer named Manny People."
    #show phone at truecenter
    scene phone_trace
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

#Story 3
label start3:
    # play music "audio/disco_ost.mp3" fadein 1.0 volume 0.25
    scene desk_trace
    "At the time, you were investigating a local lobbyist named Payton Agg, who suddenly had become the “go-to” fundraiser for many local politicians."
    "You found out that Agg had created a non-profit organization that would expressly advocate, inclusively with donations, for candidates that publicly defended his views of the First Amendment rights,.."
    "especially freedom of religion against government interference in certain economic practices by organizations linked to specific denominations."
    
    
label choice5:
    scene desk2_trace
    "After your story, the FEC, based on FECA and on the Supreme Court decision on Citizens United v. FEC, mandated Payton Agg to:"
menu:
    "Pay taxes on his organization’s earnings":
        jump choice5_c
    "Register as a political committee (PAC)":
        jump choice5_a
    "Limited the organization’s contributions to candidates":
        jump choice5_c
    "Change nothing":
        jump choice5_c

label choice5_a:
    scene bg_black
    "Correct, as decided in Speechnow.org v. FEC." 
    jump choice5_common

label choice5_c:
    scene bg_black
    "Incorrect. Register as a political committee (PAC), as decided in Speechnow.org v. FEC."
    jump choice5_common

label choice5_common:
    scene desk_trace
    "During your investigation, you found out that Agg was particularly targeting politicians from areas that formed a straight line on the map within a corridor that linked Alberta in Canada to…"
    "the Mexican city of Matamoros, right at the border with Brownsville, TX. The corridor crossed Montana, Wyoming, Colorado, New Mexico, and Texas."
    "Litik’s name came up in your investigation as one of the politicians targeted by Agg, but you didn’t have time to pursue that angle before the deadline."
    "Now, that you know Litik’s plan and Agg’s targets, what do you do?"
menu:
    "Write a breaking news story about the connection between Agg and Litik’s pipeline. You have enough information to publish a short piece and you can continue to investigate later as the story develops.":
        jump choice6_a
    "Talk to your editor about your suspicions and ask her if you can investigate the story further.":
        jump start4
    "Immediately start doing some background research on Litik, Agg, and all the other politicians targeted by Agg and the ones involved in the pipeline campaign. Then, you talk to your editor and ask if you can investigate the story further.":
        jump start4
    "Call both Agg and Litik to try to get interviews with them about what you found out.":
        jump choice6_d
    "Go after Agg to see if you can find out more about his involvement. ":
        jump start3b

label choice6_a:
    scene bg_black
    "You would be sued and fired. Try again." 
    jump choice5_common

label choice6_d:
    scene bg_black
    "You would get a SLAPP suit. Try again."
    jump choice5_common

label start3b:
    scene desk_trace
    "You find Agg in his usual watering hole. He obviously knows you after the story you wrote about him, so he would recognize you if you tried approaching him directly."
    "Agg is at the bar, speaking on the phone with his back turned to you."
    "What do you do?"
menu:
    "Keep your distance and just observe him.":
        jump choice7_a
    "Go to the bar when he is not looking and bribe the bartender to try to listen to his conversation.":
        jump choice7_b
    "Sneak to the stool next to him while he is not looking and turn on your recorder with the mic turned to him.":
        jump choice7_c
    "Walk straight to him and ask if you can ask him a few questions.":
        jump choice7_c
    "Sneak to the stool next to him while he is not looking and listen to his conversation on the phone. Once he is done talking, start asking him a few questions.":
        jump choice7_c
    "Go back to the newspaper. You changed your mind about how to approach this situation.":
        jump choice7_a

label choice7_a:
    jump start3c

label choice7_b:
    scene bg_black
    "Bartender takes your money and tells you he didn’t say anything. Try again."
    jump start3b

label choice7_c:
    scene bg_black
    "He recognizes you and tells you to go away or he will call the police. Try again." 
    jump start3b


label start3c:
    " You keep your distance and observe Agg without getting noticed."
    "After 30 minutes of seemed to be a hot exchange in the phone, Agg gets up and leave."
    "What do you do?"
menu:
    "Approach him and ask if you can ask a few questions.":
        jump choice8_a
    "Try to find a cab quickly. ":
        jump choice8_b
    "Realize that this whole thing was a bad idea and go back to the newspaper.":
        jump choice8_c
    "Call your friend in the police and ask about the license plate.":
        jump choice8_d

label choice8_a:
    scene bg_black
    "He recognizes you and tells you to go away or he will call the police. Try again." 
    jump start3b

label choice8_b:
    jump start3d

label choice8_c:
    jump start3b

label choice8_d:
    scene bg_black
    "Your friend tells you that what you are doing is illegal and hangs up on you. Try again." 
    jump start3b


label start3d:
    "You get in a cab and follow Agg until his apartment."
    "There is a hotel across the street that could give you a good view of his apartment."
    "What do you do?"
menu:
    "Stay downstairs and wait until Agg leaves the building. Then, keep following him.":
        jump choice9_a
    "Stay downstairs and wait until Agg leaves the building. Then, try to break into his apartment to find out more about his dealings.":
        jump choice9_b
    "Get a room across the street and use a surveillance set to try to spy on Agg.":
        jump choice9_c
    "Well, you don’t know how long it will take for him to go out again, so you decide to head back to the newsroom.":
        jump choice9_d

label choice9_a:
    scene bg_black
    "You wait outside until early morning. Agg leaves his apartment and goes directly to his workplace.“
    “You just wasted a night of sleep and many hours of work. Oh yeah, you also need a shower." 
    jump choice9_common

label choice9_b:
    scene bg_black
    "You wait until morning. When Agg leaves his building, you manage to squeak in without getting noticed.“
    “You break into his apartment and start looking for anything suspicious. After a few frustrating minutes, you are jumped by a couple of police officers and arrested for trespassing. You also get fired." 
    jump choice9_common


label choice9_c:
    scene bg_black
    "You watch him all night, but cannot see anything useful.“
    “You just wasted a night of sleep and work and you also have an expensive hotel room bill to pay with your reporter’s salary. Good luck with that one!" 
    jump choice9_common

label choice9_d:
    jump choice9_common

label choice9_common:
    scene bg_black
    "End of Story 3"


label start4:
    " During your investigation, you find out that Agg has been in constant contact with a multinational oil company with headquarters in the United Arab Emirates (UAE) named UAE Oil."
    "You also find out that a few of the politicians supporting Litik’s project are former employees of UAE Oil or of their subsidiaries in the US, such as American Oil and USA Oil."
    "You believe the company is behind the investments for the pipeline, but you have no definitive proof."
    "What do you do?"
menu:
    "Call your hacker friend and see if he can get the data from Agg’s and Litik’s cell phones, emails, and social media to find evidence that they are working with UAE Oil.":
        jump choice10_a
    "Call the FBI with what you know and say it is a national security threat.":
        jump choice10_b
    "Write and publish a story with what you have gathered so far.":
        jump choice10_c
    "Schedule interviews with Agg, Litik, and the representatives of UAE Oil in the US and in the UAE.":
        jump choice10_d
    "Enter with a Freedom of Information Act (FOIA) request to get information about American Oil and USA Oil with Energy Information Administration (EIA), Environmental Protection Agency (EPA), and the Department of the Interior (DOI). Look into UAE laws for information access. Investigate all the lands owned by the targeted politicians and cross-check them with the proposed pipeline. Call local representatives of any larger group of people who owns land in the proposed pipeline path to see what they think about it.":
        jump choice10_e
    "Investigate American Oil and USA Oil using local registries for property and land use documents. Enter a FOIA request not on oil, but on property and land use on federal lands located within the corridor. Look into UAE laws for information access. Investigate all the lands owned by the targeted politicians and cross-check them with the proposed pipeline. Call local representatives of any larger group of people who owns land in the proposed pipeline path to see what they think about it.":
        jump choice10_f
    "Do nothing. This is waaaay too much trouble and I don’t want to get involved in an international conspiracy. I always wanted to be a pastry chef anyway…":
        jump choice10_g

label choice10_a:
    scene bg_black
    "You get arrested for espionage on a US Senator, sued for infringement on privacy, sued for causing an international crisis, and, of course, fired."
    jump choice10_common

label choice10_b:
    scene bg_black
    "Your suspicions are not enough to cause anyone in the FBI to get bothered with it. You also get reprimanded by your boss for not pursuing the story."
    jump choice10_common

label choice10_c:
    scene bg_black
    "You get sued for defamation by American Oil, USA Oil, Litik, and Agg. The court decided that you published the story without conducting due diligence in your investigation and acted out of malice."
    "You are ordered to pay millions in damages and you are fired." 
    jump choice10_common

label choice10_d:
    scene bg_black
    "All of them deny your requests and sue you to prevent you from publishing any stories on the topic."
    jump choice10_common

label choice10_e:
    scene bg_black
    "Your FOIA requests are denied as they are oil companies. UAE does not have such laws. Most groups are against the pipeline. Many of them are either Native American Nations or other disenfranchised groups."
    "Many of the politicians have lands in cities that could benefit financially from the pipelines, but none has lands on the pipelines path. The path seems to specifically go around some of their properties to avoid passing through them."
    jump choice10_common

label choice10_f:
    scene bg_black
    "As the Freedom of Information Act (FOIA) does not apply to any information related to gas and oil wells, including pipelines, you manage to gather information from different agencies about federal land uses."
    jump choice10_common

label choice10_g:
    jump choice10_common


label choice10_common:
    scene bg_black
    "End of Story 3"
