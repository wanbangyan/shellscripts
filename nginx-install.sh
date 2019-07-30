
#!/usr/bin/env bash
#
# encoding: utf8
# author: wangbangyan
# date: 2019/07/30


yum -y install yum-utils

echo '[nginx-stable]
name=nginx stable repo
baseurl=http://nginx.org/packages/centos/$releasever/$basearch/
gpgcheck=1
enabled=1
gpgkey=https://nginx.org/keys/nginx_signing.key'>>/etc/yum.repos.d/nginx.repo

yum -y install nginx

systemctl start nginx
systemctl enable nginx
