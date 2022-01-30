if [[ -n $RCLONE_CONFIG_BASE64 ]]; then
	echo "Rclone config detected"
	echo "[FTP]" > rclone.conf
    mkdir -p /app/.config/rclone
	echo "$(echo $RCLONE_CONFIG_BASE64|base64 -d)" >> /app/.config/rclone/rclone.conf
fi

echo "SETUP COMPLETED"

gunicorn main:app