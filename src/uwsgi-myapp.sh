#!/bin/bash
#
# Comments to support chkconfig
# chkconfig: - 98 02
# description: your_prog_name service script
#
# Source function library.
. /etc/init.d/functions

### Default variables
prog_name="uwsgi-myapp"
prog_path="/usr/bin/uwsgi"
pidfile="/var/run/${prog_name}.pid"
options="-i /etc/uwsgi-myapp/uwsgi-myapp.ini"

# Check if requirements are met
[ -x "${prog_path}" ] || exit 1

RETVAL=0

start(){
  echo -n $"Starting $prog_name: "
  daemon $prog_path $options
  RETVAL=$?
  return $RETVAL
}

stop(){
  echo -n $"Shutting down $prog_name: "
  killproc -p ${pidfile}
  RETVAL=$?
  return $RETVAL
}

restart() {
  stop
  start
}

case "$1" in
  start)
    start
    ;;
  stop)
    stop
    ;;
  restart)
    restart
    ;;
  status)
    status $prog_path
    RETVAL=$?
    ;;
  *)
    echo $"Usage: $0 {start|stop|restart|status}"
    RETVAL=1
esac

exit $RETVAL