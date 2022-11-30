#!/bin/bash
wall_dir=".wallpapers"
wall_pic=`ls ~/$wall_dir | shuf | head -n 1`
xwallpaper --zoom ~/$wall_dir/$wall_pic
