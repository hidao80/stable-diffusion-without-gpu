#!/opt/conda/bin/python

import sys
from diffusers import StableDiffusionPipeline, StableDiffusionImg2ImgPipeline
from PIL import Image

MODEL_ID = "CompVis/stable-diffusion-v1-4"
# MODEL_ID = "runwayml/stable-diffusion-v1-5"
DEVICE = "cpu"
# DEVICE = "cuda"
YOUR_TOKEN = "HUGGING_FACE_TOKEN"

# Local time obtained at the host
timestamp = sys.argv[1]  

prompt = sys.argv[2]
sentence = prompt.replace(' ','_')

outputFileName = '/files/' + sentence[:50] + '_' + timestamp + '.png'

if len(sys.argv) == 3:
    pipe = StableDiffusionPipeline.from_pretrained(
        MODEL_ID,
        use_auth_token=YOUR_TOKEN
    ).to(DEVICE)

    image = pipe(prompt=prompt, strength=0.75, guidance_scale=7.5, staps=5).images[0]
    image.save(outputFileName)

elif len(sys.argv) == 4:
    pipeimg = StableDiffusionImg2ImgPipeline.from_pretrained(
        MODEL_ID, 
        use_auth_token=YOUR_TOKEN
    ).to(DEVICE)

    init_image = Image.open(sys.argv[3])
    init_image = init_image.convert("RGB")
    init_image = init_image.resize((512, 512))
    image = pipeimg(prompt=prompt, init_image=init_image, strength=0.5, guidance_scale=7.5).images[0]
    image.save(outputFileName)

else:
    print('Usage: generate.sh "prompt" ["image.png"]')
    exit
