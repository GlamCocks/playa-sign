# Playa Sign - GLAMCOCKS!
description	"Fadecandy server"

start on runlevel [2345]
stop on runlevel [!2345]

respawn
=respawn limit 1000 5
umask 022

console log

script
	su pi
	/home/pi/playa-sign/server/fadecandy/bin/fcserver-rpi /home/pi/playa-sign/server/fadecandy-config.json
end script
