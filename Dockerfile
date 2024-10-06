FROM ubuntu:focal
ARG TAGS
WORKDIR /root/.dotfiles 
ARG DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y software-properties-common && apt-add-repository -y ppa:ansible/ansible && apt update && apt install -y curl git ansible build-essential neovim

CMD ["sh", "-c", "ansible-playbook local.yml --tags $TAGS"] # this could be overriden from the docker-compose.yml file.
