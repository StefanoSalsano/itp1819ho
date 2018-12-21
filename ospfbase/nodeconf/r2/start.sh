#!/bin/sh

BASE_DIR=nodeconf
NODE_NAME=r2

sysctl -w net.ipv4.ip_forward=1

chown quagga:quagga $BASE_DIR/$NODE_NAME

zebra -f $PWD/$BASE_DIR/$NODE_NAME/zebra.conf -d -z $PWD/$BASE_DIR/$NODE_NAME/zebra.sock -i $PWD/$BASE_DIR/$NODE_NAME/zebra.pid

sleep 1

ospfd -f $PWD/$BASE_DIR/$NODE_NAME/ospfd.conf -d -z $PWD/$BASE_DIR/$NODE_NAME/zebra.sock -i $PWD/$BASE_DIR/$NODE_NAME/ospfd.pid