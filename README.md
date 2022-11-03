# stable-diffusion-without-gpu

[日本語版](README_ja.md)
## INSTALL

For Windows, we recommend using Ubuntu on WSL2.

1. Install `docker` and `docker-compose`.
2. After creating an account at Hugging Face and completing the email verification, you will download the model and obtain a token.
3. Open `docker-compose.yml` in an editor and replace the value of `HUGGING_FACE_TOKEN` with your Hugging Face token string.
4. Execute the following command:  

    ```sh
    $ git clone https://github.com/hidao80/stable-diffusion-without-gpu
    ```

## USAGE

1. Enter the following command in the terminal to start the stable diffusion environment:  

    ```sh
    $ cd stable-diffusion-without-gpu
    $ docker-compose up --build -d
    ```

2. Continue to type the following command in the terminal to create the image.  

    ```sh
    $ ./generate.sh "green apple"
    ```

3. An image will be generated in `stable-diffusion-without-gpu/files/output.png`.
