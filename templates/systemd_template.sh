# Move to /etc/systemd/system/<TEMPLATE>.service
# systemctl daemon-reload
# systemctl enable --now <TEMPLATE>

[Unit]
Description=Descripcion de la app
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/opt/app/
ExecStart=/opt/app/app
Restart=on-failure

StandardOutput=append:/var/log/app.log StandardError=append:/var/log/app.err

[Install]
WantedBy=multi-user.target
