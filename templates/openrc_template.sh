#!/sbin/openrc-run

# Move file to /etc/init.d/template
# rc-service <TEMPLATE> start
# rc-update add <TEMPLATE> default

description="Descripcion"

command="/opt/app/app"
command_args="-V"

export VAR="VAR"

command_background="true"
pidfile="/run/${RC_SVCNAME}.pid"

output_log="/var/log/${RC_SVCNAME}.log"         
error_log="/var/log/${RC_SVCNAME}.err"        

depend() {                         
    # Start after the network is up
    need net                       
}                           

stop() {                    
    kill -- -$(cat $pidfile)
}
