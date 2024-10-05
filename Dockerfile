FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
	python3-pip \
	ffmpeg \
	&& rm -rf /var/lib/apt/lists/*

RUN pip3 install yt-dlp

RUN mkdir /downloads

WORKDIR /downloads

ENTRYPOINT ["yt-dlp"]

CMD ["--help"]

