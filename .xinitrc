#!/bin/sh

userresources=$HOME/.Xresources
usermodmap=$HOME/.Xmodmap
sysresources=/etc/X11/xinit/.Xresources
sysmodmap=/etc/X11/xinit/.Xmodmap

# merge in defaults and keymaps

if [ -f $sysresources ]; then







    xrdb -merge $sysresources

fi

if [ -f $sysmodmap ]; then
    xmodmap $sysmodmap
fi

if [ -f "$userresources" ]; then







    xrdb -merge "$userresources"

fi

if [ -f "$usermodmap" ]; then
    xmodmap "$usermodmap"
fi

# start some nice programs

if [ -d /etc/X11/xinit/xinitrc.d ] ; then
 for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
  [ -x "$f" ] && . "$f"
 done
 unset f
fi

# xrandr --output eDP1 --mode 1920x1080 --pos 0x0 --output HDMI2 --mode 2560x1440 --pos 1920x0 # 2560x0
#xrandr -s 1920x1080

#xwallpaper --zoom .wallpapers/wallpaper.png
#bash ~/Scripts/random_wallpaper.sh &

mate-power-manager &
#mate-volume-control-status-icon &
nm-applet &
blueman-applet &

bash ~/Scripts/xinput.sh &

#picom &

exec qtile start
