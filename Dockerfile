#一═デ🟠𝗦𝗼𝘂𝗻𝗱𝗖𝗹𝗼𝘂𝗱 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗿🟠デ═一
FROM python:latest
ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"
#一═デ🟠𝗦𝗼𝘂𝗻𝗱𝗖𝗹𝗼𝘂𝗱 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗿🟠デ═一
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y ffmpeg opus-tools bpm-tools
RUN python -m pip install --upgrade pip
RUN git clone https://github.com/mentiontard/tele-sound.git
RUN cd tele-sound
#一═デ🟠𝗦𝗼𝘂𝗻𝗱𝗖𝗹𝗼𝘂𝗱 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗿🟠デ═一
WORKDIR /tele-sound
RUN pip install -r meow.txt
CMD python3 BOOTUP.py
#一═デ🟠𝗦𝗼𝘂𝗻𝗱𝗖𝗹𝗼𝘂𝗱 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗿🟠デ═一
