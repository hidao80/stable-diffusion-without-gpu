FROM pytorch/pytorch:latest

RUN apt-get update && apt-get install -y --no-install-recommends \
    git

RUN pip3 install --upgrade diffusers transformers scipy

WORKDIR /app
ARG HUGGING_FACE_TOKEN
RUN git clone https://github.com/CompVis/stable-diffusion.git /app/stable-diffusion
ADD draw.py /app/stable-diffusion/draw.py
RUN sed -i -e "s/HUGGING_FACE_TOKEN/${HUGGING_FACE_TOKEN}/" /app/stable-diffusion/draw.py

WORKDIR /app/stable-diffusion
