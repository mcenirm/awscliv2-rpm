ARG build_as_root=no


FROM centos:7 AS base
RUN yum -y install \
    rpmdevtools \
    rpmlint
# for copying between host and container
RUN yum -y install \
    rsync


FROM base AS build_as_root_yes
WORKDIR /root


FROM base AS build_as_root_no
RUN useradd builder
USER builder
WORKDIR /home/builder


FROM build_as_root_${build_as_root}
RUN rpmdev-setuptree
