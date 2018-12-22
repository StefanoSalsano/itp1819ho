#!/bin/sh

BASE_DIR=/home/user/mytests/ospf3routers/nodeconf
NODE_NAME=h3
IP_ADDR=10.103.0.2/16
GW_ADDR=10.103.0.1

ip addr add $IP_ADDR dev $NODE_NAME-eth0 
ip route add default via $GW_ADDR dev $NODE_NAME-eth0

