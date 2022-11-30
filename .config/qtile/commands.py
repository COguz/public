from subprocess import check_output
from os import path
def get_powermode():
        return check_output(['/usr/bin/bash', path.expanduser('~/Scripts/cpu_manage.sh'), 'getonlymode']).decode("utf-8")

def get_bat_percentage():
        return check_output(['/usr/bin/bash', path.expanduser('~/Scripts/bat-percentage.sh')]).decode("utf-8")

