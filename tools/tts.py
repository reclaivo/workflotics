import json,sys,numpy as np,soundfile as sf
import espeakng_loader
from phonemizer.backend.espeak.wrapper import EspeakWrapper
EspeakWrapper.set_library(espeakng_loader.get_library_path()); EspeakWrapper.set_data_path(espeakng_loader.get_data_path())
from phonemizer import phonemize
from kokoro_onnx import Kokoro
k=Kokoro('kokoro-v1.0.onnx','voices-v1.0.bin')
R={
"r1":[("A customer calls at 8 PM.","A customer calls at eight pee em."),("Nobody answers.","Nobody answers."),("They call someone else.","They call someone else."),("Now picture an AI voice agent that picks up, speaks their language, and books the job.","Now picture an ay eye voice agent that picks up, speaks their language, and books the job."),("Contact us to learn more.","Contact us to learn more.")],
"r2":[("You are still doing this by hand?","You are still doing this by hand?"),("Copying leads.","Copying leads."),("Sending emails.","Sending emails."),("Chasing reminders.","Chasing reminders."),("Stop.","Stop."),("One automation can do all of it, even at 2 AM.","One automation can do all of it, even at two ay em."),("Contact us to learn more.","Contact us to learn more.")]}
R.update({
"r3":[("Is your website losing customers?","Is your website losing customers?"),("Check three things.","Check three things."),("Fast on a phone.","Fast on a phone."),("Clear in one line.","Clear in one line."),("Answers questions at any hour.","Answers questions at any hour."),("A built-in chatbot handles that last one.","A built in chatbot handles that last one."),("Contact us to learn more.","Contact us to learn more.")],
"r4":[("Why do people scroll past your ad?","Why do people scroll past your ad?"),("The first second decides.","The first second decides."),("Show the problem.","Show the problem."),("Give one clear idea.","Give one clear idea."),("Then say what to do next.","Then say what to do next."),("AI ad videos let you test many versions, fast.","A I ad videos let you test many versions, fast."),("Contact us to learn more.","Contact us to learn more.")],
"r5":[("Is your photo costing you bookings?","Is your photo costing you bookings?"),("Check three things.","Check three things."),("Light.","Light."),("Sharpness.","Sharpness."),("A clean background.","A clean background."),("AI can improve all three, from your existing photo.","A I can improve all three, from your existing photo."),("Contact us to learn more.","Contact us to learn more.")],
"r6":[("One studio. Four ways to grow.","One studio. Four ways to grow."),("Creative: ads, images, 3D sites.","Creative: ads, images, and three dee sites."),("Build: websites, chatbots, voice agents.","Build: websites, chatbots, and voice agents."),("Automate: workflows that run themselves.","Automate: workflows that run themselves."),("Shop: ready-made templates.","Shop: ready made templates."),("Contact us to learn more.","Contact us to learn more.")]})
import os
if os.path.exists('extra_tts.json'): R.update({k:[tuple(x) for x in v] for k,v in json.load(open('extra_tts.json')).items()})
only=sys.argv[1:] or list(R)
for r,segs in R.items():
    if r not in only: continue
    out=[]
    for i,(cap,say) in enumerate(segs):
        ph=phonemize(say.replace('A I ','ay eye '),language='en-us',backend='espeak',strip=True,preserve_punctuation=True).replace('aɪ aɪ','eɪ aɪ').replace('tuː aɪ ɛm','tuː eɪ ɛm'); print(ph)
        a,sr=k.create(ph,voice='af_heart',speed=1.04,lang='en-us',is_phonemes=True)
        a=np.trim_zeros(a,'fb') if False else a
        # trim leading/trailing silence
        idx=np.where(np.abs(a)>0.01)[0]
        a=a[max(0,idx[0]-300):idx[-1]+600]
        sf.write(f'{r}_{i}.wav',a,sr); out.append(dict(cap=cap,d=len(a)/sr))
        print(r,i,round(len(a)/sr,2))
    json.dump(out,open(f'{r}_segs.json','w'))
