# Welcome to this development project.

## DEVELOPMENT REQUIREMENTS

- Python3.8 or higher

# Redis is an open-source IN-MEMORY "DATA STRUCTURE STORE" you can use as a DATABASE SERVER to STORE "SESSION" DATA of web applications. Storing session data this way allows 
# for fast read and write operations, making it very suitable for high-traffic websites.
# Configuring the firewall to allow traffic on port 6379 (the default Redis port is 6379):
# Open Windows Defender Firewall: Press Win + R to open the Run dialog. Type control firewall.cpl and press Enter
# Click on "Advanced settings", In the left pane, click on "Advanced settings". In the left pane, click on "Inbound Rules". In the Actions pane (right pane), click on "New Rule...".
# Choose "Port" and click "Next". Select "TCP" and specify port 6379. Click "Next". Select "Allow the connection". Click "Next". Select all options for when the rule applies (Domain, 
# Private, Public). Click "Next". Enter a name and description for the rule, then click "Finish".
- Redis server

```
pip install -r requirements.txt
```

# Pre-Requisite:
- Ensures that Redis can function properly without being unnecessarily restricted by memory allocation policies. In Windows PowerShell:
Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Session Manager\Memory Management" -Name "MemoryOvercommit" -Value 1
- For app to work, an INSTANCE of a Redis database must ALREADY exist with its specific IP. 
- "--name some-redis" specifies a name for the CONTAINER to refer to it instead of using its ID
- "-d" to run the CONTAINER in detached mode INSTEAD OF holding up the terminal session.
- "v /path/on/host:/data": If persistence is enabled, your DB data is stored in the VOLUME "/data" (by convention is the path INSIDE THE CONTAINER where the volume is mounted/created)
   and "/path/on/host" is the path on the HOST machine where the data will be stored to ENSURE the DB data persists after the container shuts down or fails.
- redis is the name of the EXISTING Docker IMAGE to use
- "redis-server" is the process (command) that will be executed inside the container when it starts. Specifying this explicitly ensures that this process is started even if it's already set 
   as the default command in the image
- "--save 60 1 --loglevel warning"  saves a snapshot of the DB every 60 seconds if at least 1 write operation was performed. loglevel controls the amount of logs

In Powershell CLI type:
# just because a port is exposed doesn't mean it's accessible from outside the Docker environment by default; you may still need to map it to a port on the host system!!!!!!!!!!
docker run --name some-redis -d -p host_port:container_exposed_port -v /path/on/host:/data redis redis-server --appendonly yes --save 60 1 --loglevel warning
Ex: docker run --name my_redis_db -p 6379:6379/tcp -d -v /Docker:/data redis redis-server --appendonly yes --save 60 1 --loglevel warning
Ex: docker run --name my_redis_db -p 6379:6379/tcp -d -v /Docker:/data redis redis-server --appendonly yes --save 60 1 --loglevel warning




Then you can launch the app :
```
python main.py
```

## App information

- The API is running on port 5000
- The name of the redis service needs to be "redis"
