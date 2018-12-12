#!/bin/sh

BASE_DIR=/home/user/mytests/nodeconf
NODE_NAME=r1

sysctl -w net.ipv4.ip_forward=1

chown quagga:quagga $BASE_DIR/$NODE_NAME

zebra -f $BASE_DIR/$NODE_NAME/zebra.conf -d -z $BASE_DIR/$NODE_NAME/zebra.sock -i $BASE_DIR/$NODE_NAME/zebra.pid

sleep 1

ospfd -f $BASE_DIR/$NODE_NAME/ospfd.conf -d -z $BASE_DIR/$NODE_NAME/zebra.sock -i $BASE_DIR/$NODE_NAME/ospfd.pid