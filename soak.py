import psutil
import os
import subprocess
import time
import csv
import datetime

headers = ['CPU (%)', 'Memory (%)', 'Disk (%)', 'Log Size (MB)', 'uptime(Minutes)', 'Pckt_sent', 'Pckt_recv', 'Bytes_sent', 'Bytes_recv']

with open('soak.csv', 'w') as fw:
  writer = csv.writer(fw)
  writer.writerow(headers)
fw.close()

while (1):
  cpu = psutil.cpu_percent(interval = 1)
  mem = psutil.virtual_memory().percent
  disk = psutil.disk_usage('/').percent
  network = psutil.net_io_counters()
  packets_sent = network.packets_sent
  packets_recv = network.packets_recv
  bytes_sent = network.bytes_sent
  bytes_recv = network.bytes_recv

  #p = subprocess.Popen(["sudo", "du", "-sh", "/var/log"], stdout=subprocess.PIPE)
  p = subprocess.Popen(["du", "-sh", "/var/log"], stdout=subprocess.PIPE)
  output, err = p.communicate()
  log_mb = ""
  for i in output:
    log_mb += i
    if (i == 'M'):
      break
  up_time = (time.time() - psutil.boot_time())/60
  fields = [cpu, mem, disk, log_mb, up_time, packets_sent, packets_recv, bytes_sent, bytes_recv]

  with open('soak.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
  f.close()

  time.sleep(3600)
