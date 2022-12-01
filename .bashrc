#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias wifion='nmcli rad wif on'
alias wifioff='nmcli rad all off'
alias grep='grep --color=auto'

PS1='[\u@\h \W]\$ '
