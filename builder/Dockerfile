FROM centos:7
RUN yum -y install \
    rpmdevtools \
    rpmlint

# for copying between host and container
RUN yum -y install \
    rsync

RUN useradd builder

USER builder
WORKDIR /home/builder
RUN rpmdev-setuptree
