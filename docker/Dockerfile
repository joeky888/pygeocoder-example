FROM python:3.6-alpine

################
#              #
# Update Repos #
#              #
################

RUN echo "ipv6" >> /etc/modules
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/main/" > /etc/apk/repositories; \
    echo "http://dl-cdn.alpinelinux.org/alpine/edge/community/" >> /etc/apk/repositories; \
    echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing/" >> /etc/apk/repositories

#####################
#                   #
# Install Softwares #
#                   #
#####################

RUN apk add --upgrade --no-cache --force apk-tools
RUN apk update
RUN apk upgrade
RUN apk add --update --no-cache vim tzdata git
RUN pip install --no-cache-dir aiohttp geocoder
RUN rm -f /var/cache/apk/*

######################
#                    #
#       Service      #
#                    #
######################

RUN mkdir -p /root/geoip
ADD . /root/geoip/

####################################
#                                  #
# Update /root/.profile (Optional) #
#                                  #
####################################

RUN echo $'export CHARSET=UTF-8           \n\
export PAGER=less                         \n\
umask 022                                 \n\
for script in /etc/profile.d/*.sh ; do    \n\
if [ -r \$script ] ; then                 \n\
  . \$script                              \n\
fi                                        \n\
done                                      \n\
alias ls="ls --color=auto"                \n\
alias ll="ls --color=auto -alh"           \n\
alias l="ls --color=auto -alh"            \n\
alias vimlog="vim -c \\"%s/[\u001b]\[[0-9]\{2,3}m//g\\"" \n\
export BRed="\e[1;31m"                    \n\
export BGre="\e[1;32m"                    \n\
export BWhi="\e[1;37m"                    \n\
export PS1="╭─${BRed}\\\\u@\h ${BGre}\w${BWhi} \n╰─# " \n\
export LC_ALL="en_US.UTF-8"               \n\
export LANG="en_US.UTF-8"' > /root/.profile
RUN sed -i "s/\s*$//g" /root/.profile

#######################
#                     #
#     Environment     #
#                     #
#######################

EXPOSE 8080
ENTRYPOINT ["python", "/root/geoip/server.py"]
ENV ENV="/root/.profile"
ENV EDITOR vim
ENV USER root
ENV user root

SHELL ["/bin/ash"]

# docker build -f ./Dockerfile-pm2/Dockerfile . -t han:20180101
# docker run -d --name controller -p 8080:8080 --restart=always -t han:20180101
# docker exec -it controller sh
