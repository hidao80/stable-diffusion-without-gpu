#!/opt/conda/bin/python

import sys
import torch
from diffusers import StableDiffusionPipeline
from torch import autocast

MODEL_ID = "CompVis/stable-diffusion-v1-4"
DEVICE = "cpu"
# DEVICE = "cuda"
YOUR_TOKEN = "HUGGING_FACE_TOKEN"

pipe = StableDiffusionPipeline.from_pretrained(MODEL_ID,  use_auth_token=YOUR_TOKEN)
pipe.to(DEVICE)

prompt = sys.argv[1]

image = pipe(prompt, guidance_scale=7.5).images[0]

sentence = prompt.replace(' ','_')
image.save('/files/' + sentence + '.png')
