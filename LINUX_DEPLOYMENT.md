# Linux & Nginx Deployment Guide

This guide covers deploying the INSBHRS Flask portfolio application on Linux with Nginx as a reverse proxy.

## Prerequisites

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip nginx gunicorn -y
```

## Setup Steps

### 1. Clone/Deploy Application

```bash
sudo mkdir -p /var/www/insbhrs
sudo chown $USER:$USER /var/www/insbhrs
cd /var/www/insbhrs
# Copy your project files here
```

### 2. Create Python Virtual Environment

```bash
cd /var/www/insbhrs
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install gunicorn
```

### 3. Set Up Systemd Service

```bash
sudo cp insbhrs.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable insbhrs
sudo systemctl start insbhrs
sudo systemctl status insbhrs
```

### 4. Configure Nginx

```bash
# Copy nginx configuration to sites-available
sudo cp nginx.conf /etc/nginx/sites-available/insbhrs

# Enable the site
sudo ln -s /etc/nginx/sites-available/insbhrs /etc/nginx/sites-enabled/insbhrs

# Remove default site if needed
sudo rm /etc/nginx/sites-enabled/default

# Test nginx configuration
sudo nginx -t

# Restart nginx
sudo systemctl restart nginx
```

### 5. Set Proper Permissions

```bash
sudo chown -R www-data:www-data /var/www/insbhrs
sudo chmod -R 755 /var/www/insbhrs
sudo chmod -R 755 /var/www/insbhrs/static
```

## SSL/HTTPS Setup (Using Let's Encrypt)

```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d your-domain.com
```

Then uncomment the SSL configuration section in `nginx.conf` and update the domain name.

## Verification

### Check Service Status

```bash
sudo systemctl status insbhrs
journalctl -u insbhrs -f  # View live logs
```

### Check Nginx

```bash
sudo systemctl status nginx
sudo nginx -t  # Test configuration
```

### Access Application

Visit `http://your-server-ip` or `http://your-domain.com` in your browser.

## Troubleshooting

### Service won't start
```bash
journalctl -u insbhrs -n 50  # View last 50 log entries
```

### Nginx errors
```bash
sudo nginx -t  # Test config syntax
tail -f /var/log/nginx/error.log
```

### Permission denied errors
```bash
sudo chown -R www-data:www-data /var/www/insbhrs
sudo chmod 755 /var/www/insbhrs
```

## Useful Commands

```bash
# Restart services
sudo systemctl restart insbhrs
sudo systemctl restart nginx

# View logs
sudo journalctl -u insbhrs -f
tail -f /var/log/nginx/access.log

# Check if app is running
curl http://127.0.0.1:5000/health
```

## Security Best Practices

1. Keep the system and packages updated
2. Use HTTPS/SSL certificates
3. Configure firewall rules (UFW)
4. Set up monitoring and log rotation
5. Use environment variables for sensitive data
6. Regularly backup application and data

## Environment Variables

Create a `.env` file in `/var/www/insbhrs` if needed and update the systemd service to source it:

```ini
EnvironmentFile=/var/www/insbhrs/.env
```
