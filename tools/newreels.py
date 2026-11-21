# Data for reels 7+ : topic, segments (caption, spoken), visual items, caption. Run: python3 newreels.py (writes rN_gen.json, extra_tts.json, captions-batch2.json)
import json
I=dict(
mail='<path d="M3 5h18v14H3z"/><path d="M3 7l9 6 9-6"/>',cube='<path d="M12 2l9 5v10l-9 5-9-5V7z"/><path d="M12 22V12M3 7l9 5 9-5"/>',
game='<rect x="2" y="7" width="20" height="11" rx="5"/><path d="M7 12h4M9 10v4"/><circle cx="16" cy="11" r="1"/><circle cx="18" cy="14" r="1"/>',
home='<path d="M3 11l9-8 9 8v10H3z"/><path d="M9 21v-7h6v7"/>',cal='<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
globe='<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',cart='<path d="M6 7h12l-1 13H7zM9 7a3 3 0 0 1 6 0"/>',
star='<path d="M12 3l2.6 5.6L21 10l-4.5 4.4L17.6 21 12 18l-5.6 3 1.1-6.6L3 10l6.4-1.4z"/>',bolt='<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
chat='<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/>',clock='<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
layers='<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',link='<path d="M10 14a5 5 0 0 0 7 0l3-3a5 5 0 0 0-7-7l-1 1"/><path d="M14 10a5 5 0 0 0-7 0l-3 3a5 5 0 0 0 7 7l1-1"/>',
mic='<rect x="9" y="3" width="6" height="12" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/>',send='<path d="M22 2L11 13M22 2l-7 20-4-9-9-4z"/>',
inbox='<path d="M3 13l3-8h12l3 8v6H3z"/><path d="M3 13h5l1 3h6l1-3h5"/>',phone='<rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/>',
eye='<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',touch='<path d="M9 11V5a2 2 0 0 1 4 0v6l5 1v6a4 4 0 0 1-4 4h-3a4 4 0 0 1-3-1.5L5 16z"/>',
gift='<rect x="3" y="8" width="18" height="13" rx="1"/><path d="M12 8v13M3 12h18M12 8c-3 0-5-4-2-4s2 4 2 4zm0 0c3 0 5-4 2-4s-2 4-2 4z"/>',
code='<path d="M16 18l6-6-6-6M8 6l-6 6 6 6"/>',pen='<path d="M12 20h9M16.5 3.5l4 4L8 20l-5 1 1-5z"/>',move='<path d="M5 12h14M13 6l6 6-6 6"/>')
R={
'r7':dict(file='reel-7-email-automation',topic='email automation',title='Email automation',sub='Reply. Follow up. Sort.',icon='mail',
 segs=[("Still answering the same emails by hand?","Still answering the same emails by hand?"),("Automate three things.","Automate three things."),("Instant replies.","Instant replies."),("Smart follow ups.","Smart follow ups."),("A sorted inbox.","A sorted inbox."),("AI email automation does all three, quietly.","A I email automation does all three, quietly."),("Contact us to learn more.","Contact us to learn more.")],
 items=[("Instant replies","Answers within seconds",'send'),("Follow ups","Nobody gets forgotten",'clock'),("Sorted inbox","Urgent mail on top",'inbox')],final="Same emails.<br>Zero typing.",
 caption="""If you reply to the same five questions every day, your inbox is doing a job a workflow should be doing.

Email is where small businesses quietly lose time. A customer asks about prices, opening hours or availability. Someone replies late, or forgets to follow up, and the enquiry goes cold. None of it is difficult, but all of it is repetitive.

Three parts of your email that can run on their own:
1. Instant replies. The common questions get a clear, accurate answer within seconds, at any hour, instead of whenever someone is free.
2. Smart follow ups. If a lead does not answer, a polite reminder goes out on schedule, so no enquiry is left to go cold.
3. A sorted inbox. Messages are labelled and routed, so urgent and high value mail rises to the top and routine mail never buries it.

This is the practical side of AI automation. The goal is not to replace the personal touch. It is to protect it, by handling the routine messages automatically so your team has time to write the replies that truly need a human voice.

Here is a small task for this week. Open your sent folder and count how many times you wrote nearly the same message. Pick the one you wrote most often and write it down as a template. That single message is your first candidate for automation, and a good brief for a conversation with us.

Workflotics builds AI email automation, chatbots, voice agents, websites and workflow automation for growing businesses. Contact us to learn more.

#EmailAutomation #AIAutomation #WorkflowAutomation #BusinessGrowth #SmallBusiness"""),
'r8':dict(file='reel-8-3d-websites',topic='3D websites',title='3D websites',sub='Depth that gets remembered',icon='cube',
 segs=[("Is your website forgettable?","Is your website forgettable?"),("Three ways to stand out.","Three ways to stand out."),("Depth you can feel.","Depth you can feel."),("Smooth on a phone.","Smooth on a phone."),("Made to be remembered.","Made to be remembered."),("A 3D website turns visitors into fans.","A three dee website turns visitors into fans."),("Contact us to learn more.","Contact us to learn more.")],
 items=[("Real depth","Move, tilt, explore",'cube'),("Smooth on phones","Built for mobile first",'phone'),("Memorable","People remember it",'star')],final="Visitors stay.<br>Brands stick.",
 caption="""Most websites look like every other website. A 3D website gives people a reason to stop scrolling.

When a visitor lands on your page, you have a few seconds to earn their attention. A flat layout with a stock photo does not give them much to remember. A well built 3D experience does, because people move, tilt and explore it, and what they interact with is what they recall later.

What makes a 3D website work:
1. Depth you can feel. Objects, products or scenes that respond to movement make the page feel alive instead of static.
2. Smooth on a phone. Most visitors arrive on mobile, so the experience must load quickly and run without lag on a small screen.
3. Made to be remembered. A distinctive look helps your business stand out from competitors who all use the same templates.
4. A clear next step. Beautiful is not enough. The page still needs one obvious action, such as booking, calling or asking a question.

Here is the bigger lesson. Design is not decoration. It is how a visitor decides, within seconds, whether your business feels credible. Combine a memorable look with a built in chatbot that answers questions at any hour, and the site works for you around the clock.

A small task for this week: open your homepage on your phone and ask a friend what they remember after five seconds. If the answer is vague, your site is blending in, and that is worth fixing.

Workflotics builds 3D websites, AI chatbots, voice agents and workflow automation for growing businesses. Contact us to learn more.

#3DWebsite #WebDesign #AIAutomation #BusinessGrowth #DigitalMarketing"""),
'r9':dict(file='reel-9-playable-game-ads',topic='playable game ads',title='Playable ads',sub='Try before you tap',icon='game',
 segs=[("Do people skip your ad?","Do people skip your ad?"),("Three reasons playable ads win.","Three reasons playable ads win."),("Hands on in seconds.","Hands on in seconds."),("Attention stays longer.","Attention stays longer."),("A clear call to action.","A clear call to action."),("Playable game ads turn viewers into players.","Playable game ads turn viewers into players."),("Contact us to learn more.","Contact us to learn more.")],
 items=[("Hands on fast","Play within seconds",'touch'),("Longer attention","Interaction holds eyes",'eye'),("Clear next step","Install or visit",'link')],final="Don't just show it.<br>Let them play.",
 caption="""Most people skip your ad. They rarely skip a game they can play.

A playable game ad lets a viewer try a small, interactive piece of your game or product before they commit. Instead of watching a clip and guessing what it feels like, they tap, swipe and find out for themselves. For game studios and app brands, that is a very different level of attention.

Why playable ads work:
1. Hands on in seconds. There is no long intro. The viewer is playing almost immediately, which keeps them from scrolling away.
2. Attention stays longer. Interaction holds the eye far better than passive video, because the viewer is part of the experience.
3. Better matched players. People who choose to keep playing already know what to expect, so the ones who install are more likely to be a good fit.
4. A clear call to action. The ad ends with one obvious step, such as install, visit or learn more.

The AI automation angle: creating many versions of a playable ad used to take weeks. With AI assisted workflows you can produce variations of the hook, the mechanic and the ending, test them quickly and keep the version that performs best.

A small task for this week: write down the single most fun ten seconds of your game or product. That moment is the heart of your playable ad, and it is the part worth showing first.

Workflotics creates AI ad videos, playable game ads, 3D websites and workflow automation for growing businesses. Contact us to learn more.

#PlayableAds #GameMarketing #AIAutomation #MobileGaming #BusinessGrowth"""),
'r10':dict(file='reel-10-why-workflotics',topic='promo: why Workflotics',title='Why Workflotics',sub='One studio, many skills',icon='star',
 segs=[("Why work with Workflotics?","Why work with Workflotics?"),("Three reasons.","Three reasons."),("Creative and automation.","Creative and automation."),("Built for growth.","Built for growth."),("Easy to start.","Easy to start."),("One studio. Many ways to grow.","One studio. Many ways to grow."),("Contact us to learn more.","Contact us to learn more.")],
 items=[("Build + automate","Ads, sites, workflows",'layers'),("Built for growth","Made for real businesses",'bolt'),("Easy to start","One chat, clear steps",'chat')],final="One studio.<br>Many ways to grow.",
 caption="""Growing a business often means juggling five people for five problems. There is another way.

Workflotics is one studio that brings creative work and automation together, so you do not need to coordinate a separate agency for every task. Ads, websites, chatbots, voice agents and workflow automation can all be planned as one connected system instead of disconnected projects.

Three reasons businesses choose to work with us:
1. Creative and automation under one roof. AI ad videos, product images, 3D websites and playable game ads sit next to email, content and workflow automation, so the pieces fit together.
2. Built for growth. Everything we make is meant to bring more attention, more conversations and more bookings, not just look good in a portfolio.
3. Easy to start. You begin with a conversation about what slows you down. We suggest a clear first step, and you decide how far to go.
4. Ready made options too. The Workflotics Shop offers templates, digital products and prompts if you prefer to start on your own.

Here is the idea behind it all. Automation is not about replacing people. It is about taking repetitive, time sensitive work off their plate so they can focus on what only humans do well.

A small task for this week: list the three tasks that eat the most of your time. Bring that list to us and we will help you find the best place to begin.

Workflotics helps growing businesses with creative, websites, voice agents and automation. Contact us to learn more.

#AIAutomation #BusinessGrowth #DigitalGrowth #WorkflowAutomation #SmallBusiness"""),
'r11':dict(file='reel-11-3d-property-walkthroughs',topic='3D property walkthroughs',title='3D walkthroughs',sub='Tour any space online',icon='home',
 segs=[("Can buyers see the home before visiting?","Can buyers see the home before visiting?"),("Check three things.","Check three things."),("Walk every room.","Walk every room."),("Any time, any device.","Any time, any device."),("Share with one link.","Share with one link."),("A 3D walkthrough lets buyers explore from anywhere.","A three dee walkthrough lets buyers explore from anywhere."),("Contact us to learn more.","Contact us to learn more.")],
 items=[("Every room","Walk through the space",'home'),("Any device","Phone, tablet, laptop",'phone'),("One link","Easy to share",'link')],final="Tour it online.<br>Anywhere.",
 caption="""Buyers decide fast, and photos alone rarely tell them how a space feels.

A 3D property walkthrough lets someone move through a home, office or venue from their phone or laptop, room by room, at their own pace. For agents, developers and hospitality businesses, that means more informed enquiries and fewer wasted viewings.

What to check in a good walkthrough:
1. Walk every room. Viewers should be able to move through the whole space, see how rooms connect and get a true sense of scale.
2. Any time, any device. The tour should run smoothly on a phone, because that is where many buyers and guests first look.
3. Share with one link. A single link can go into a listing, an email, a message or a social post, with no app to install.
4. A clear next step. After the tour, the viewer should know exactly how to book a visit or ask a question.

The AI automation angle: pair the walkthrough with a chatbot or voice agent that answers questions about the property and books viewings at any hour. The tour creates the interest, and automation catches it before it cools.

A small task for this week: take your most popular listing and ask yourself what a buyer still cannot tell from the photos. Layout, light and flow are usually the answers, and a walkthrough shows all three.

Workflotics builds 3D property walkthroughs, AI chatbots, voice agents and workflow automation for growing businesses. Contact us to learn more.

#3DWalkthrough #RealEstateMarketing #PropTech #AIAutomation #BusinessGrowth"""),
'r12':dict(file='reel-12-content-automation',topic='content automation',title="Content automation",sub='Plan. Create. Publish.',icon='pen',
 segs=[("Posting again at midnight?","Posting again at midnight?"),("Automate three steps.","Automate three steps."),("Plan the ideas.","Plan the ideas."),("Create the drafts.","Create the drafts."),("Publish on time.","Publish on time."),("AI content automation keeps you consistent.","A I content automation keeps you consistent."),("Contact us to learn more.","Contact us to learn more.")],
 items=[("Plan ideas","A steady content pipeline",'cal'),("Create drafts","Captions and visuals",'pen'),("Publish on time","Scheduled, never forgotten",'send')],final="Consistent content.<br>Less effort.",
 caption="""If you post when you remember, your content calendar is running on willpower. A workflow runs on a schedule.

Consistency is what builds an audience, and consistency is exactly what busy owners struggle with. Ideas get lost, drafts pile up and posts go out late or not at all. The work itself is not hard. It is repetitive, and that makes it ideal for automation.

Three steps of content that can run on their own:
1. Plan the ideas. A simple system collects topics, questions your customers ask and recurring themes, so you never start from a blank page.
2. Create the drafts. AI helps turn each idea into a caption, a script or a visual brief that you review and approve, instead of writing everything from scratch.
3. Publish on time. Approved posts are scheduled across your accounts and go out when planned, whether you are at your desk or not.
4. Review the results. A short weekly summary shows what worked, so the next round of ideas improves.

The key point: automation handles the routine mechanics, while you keep control of the message. You stay the author. The workflow just makes sure the work gets done.

A small task for this week: write down ten questions your customers ask most often. Each one is a ready made content idea, and together they are the start of a month of posts.

Workflotics builds content automation, email automation, chatbots, voice agents and workflow automation for growing businesses. Contact us to learn more.

#ContentAutomation #AIAutomation #SocialMediaMarketing #WorkflowAutomation #BusinessGrowth"""),
'r13':dict(file='reel-13-voice-agent-languages',topic='voice agent languages',title='Voice agents',sub='Many languages, one agent',icon='mic',
 segs=[("A customer calls in another language?","A customer calls in another language?"),("Your voice agent handles it.","Your voice agent handles it."),("Answers instantly.","Answers instantly."),("Speaks their language.","Speaks their language."),("Books the job.","Books the job."),("One AI voice agent. Many languages.","One A I voice agent. Many languages."),("Contact us to learn more.","Contact us to learn more.")],
 items=[("Instant answer","Picks up every call",'phone'),("Their language","Replies the way they speak",'globe'),("Books the job","Straight to your calendar",'cal')],final="One voice agent.<br>Many languages.",
 caption="""A customer calls in a language nobody on your team speaks. What happens next?

For most small businesses the honest answer is a missed sale. The caller struggles, hangs up and tries a competitor. Hiring staff for every language is not realistic, yet customers are increasingly diverse, and they notice when a business makes things easy.

What an AI voice agent changes:
1. Answers instantly. Every call is picked up, including nights, weekends and busy periods, with no waiting on hold.
2. Speaks their language. The agent replies in the language the caller uses, so you are not limited to the languages your team knows.
3. Books the job. It answers common questions and books the appointment while the customer is still on the line.
4. Passes the details on. The booking and conversation notes go straight to your calendar or CRM, so nothing depends on someone remembering to call back.

This is AI automation at its most practical. The agent handles the repetitive, time sensitive part of the call, and your team handles the work that needs a human.

A small task for this week: look at your last twenty enquiries and note which languages your customers use. If you see more than one, a multilingual voice agent could be paying for itself quickly.

Workflotics builds AI voice agents, chatbots, websites and workflow automation for growing businesses. Contact us to learn more.

#AIVoiceAgent #AIAutomation #CustomerExperience #BusinessGrowth #WorkflowAutomation"""),
'r14':dict(file='reel-14-shop',topic='Shop: templates and prompts',title='The Shop',sub='Templates and prompts',icon='cart',
 segs=[("Want to start automating today?","Want to start automating today?"),("Visit the Workflotics Shop.","Visit the Workflotics Shop."),("Ready made templates.","Ready made templates."),("Digital products.","Digital products."),("Prompts that save time.","Prompts that save time."),("Start small. Grow when you are ready.","Start small. Grow when you are ready."),("Contact us to learn more.","Contact us to learn more.")],
 items=[("Templates","Ready to use automations",'layers'),("Digital products","Practical, downloadable",'gift'),("Prompts","Save hours of writing",'pen')],final="Start small.<br>Grow when ready.",
 caption="""You do not need a big project to start automating. You need one small win.

Many owners put automation off because it sounds large, technical and expensive. In reality, the first step can be small: one template that handles one repeated task. Once you see the time it saves, the next step becomes obvious.

What you will find in the Workflotics Shop:
1. Ready made templates. Automation templates that handle common jobs, so you are not building from a blank page.
2. Digital products. Practical, downloadable resources designed to help you get a result quickly.
3. Prompts that save time. Carefully written prompts for everyday business writing and planning, so you spend minutes instead of hours.
4. A path to more. If you later want something built for you, the same studio can create custom websites, chatbots, voice agents and workflows.

The idea behind it: automation should be accessible. Start with something you can try on your own, learn what works for your business, and bring in help when you want to go further.

A small task for this week: write down the one task you repeat most often. Check whether a template or a good prompt could take it off your plate. If it can, you have just found your first automation.

Workflotics offers creative, websites, voice agents, workflow automation and a Shop for those who prefer to start themselves. Contact us to learn more.

#AIAutomation #WorkflowAutomation #Templates #SmallBusiness #BusinessGrowth""")}
out={};tts={}
for r,d in R.items():
    json.dump(dict(icon=I[d['icon']],title=d['title'],sub=d['sub'],final=d['final'],items=[[a,b,I[c]] for a,b,c in d['items']]),open(f'{r}_gen.json','w'))
    tts[r]=d['segs']
    out[d['file']]=dict(topic=d['topic'],caption=d['caption'],chars=len(d['caption']),hashtags=d['caption'].count('#'))
    assert '—' not in d['caption'] and '–' not in d['caption'] and 'Reclaivo' not in d['caption']
json.dump(tts,open('extra_tts.json','w'));json.dump(out,open('captions-batch2.json','w'),indent=1)
for k,v in out.items(): print(k,v['chars'],v['hashtags'])
