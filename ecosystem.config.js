module.exports = {
  apps : [{
    // 1. The display name for the process in PM2 (e.g., when you run 'pm2 status')
    name: "python-scraper",

    // 2. The command to run. Since we are using uvicorn as a module, 
    // we use 'python3' as the starting point.
    script: "python3",

    // 3. These are the flags passed to the script.
    // -u: Forces Python to be "unbuffered" so logs appear in PM2 instantly.
    // -m uvicorn: Runs the uvicorn module.
    // main:app: Looks for the 'app' variable inside 'main.py'.
    args: "-u -m uvicorn scraper:app --host 0.0.0.0 --port 8000",

    // 4. Tells PM2 not to look for Node.js; we provided the full command in 'script'.
    interpreter: "none",

    // 5. If the app crashes (due to a code error or memory leak), PM2 will restart it.
    autorestart: true,

    // 6. PM2 will wait 5 seconds before restarting. 
    // This prevents "infinite loop" crashes from pegging your CPU.
    restart_delay: 5000,

    // 7. If the app uses more than 1GB of RAM, PM2 will kill and restart it.
    // This is the "fix" for slow memory leaks over several days.
    max_memory_restart: '1G',

    // 8. Environment variables passed to your Python code.
    env: {
      NODE_ENV: "production",
      // Another layer of protection to ensure logs aren't cached in memory.
      PYTHONUNBUFFERED: "1" 
    },

    // 9. Where the "red" error text (Tracebacks) will be saved.
    error_file: "./logs/err.log",

    // 10. Where the "standard" output (print statements/requests) will be saved.
    out_file: "./logs/out.log",

    // 11. Adds a timestamp to every line in your logs. 
    // Crucial for seeing EXACTLY when those crashes happened over the "last few days."
    log_date_format: "YYYY-MM-DD HH:mm:ss"
  }]
}