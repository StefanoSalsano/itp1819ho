#!/bin/sh

BASE_DIR=nodeconf
NODE_NAME=r1

#enable IPv4 forwarding
sysctl -w net.ipv4.ip_forward=1

#disable reverse path filtering (needed for dynamic routing)
#sysctl -w net.ipv4.conf.all.rp_filter=0
#sysctl -w net.ipv4.conf.default.rp_filter=0
#the following for loop also disables all and default
for i in /proc/sys/net/ipv4/conf/*/rp_filter ; do
  echo 0 > $i 
done


chown quagga:quagga $BASE_DIR/$NODE_NAME

zebra -f $PWD/$BASE_DIR/$NODE_NAME/zebra.conf -d -z $PWD/$BASE_DIR/$NODE_NAME/zebra.sock -i $PWD/$BASE_DIR/$NODE_NAME/zebra.pid

sleep 1

ospfd -f $PWD/$BASE_DIR/$NODE_NAME/ospfd.conf -d -z $PWD/$BASE_DIR/$NODE_NAME/zebra.sock -i $PWD/$BASE_DIR/$NODE_NAME/ospfd.pid