module.exports = {
  apps: [
    {
      name: "Articles",
      script: "gunicorn --bind 0.0.0.0:9756 wsgi:app",
      autorestart: true,
      watch: false
    }
  ]
};
