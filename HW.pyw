import time 
import psutil
import pynvml
import paho.mqtt.publish as publish

while True:
    cpu_val = psutil.cpu_percent() 
    mem_val = psutil.virtual_memory().percent 

    #def get_gpu_usage():
    pynvml.nvmlInit()
    device_count = pynvml.nvmlDeviceGetCount()
    
    percent = "%"

    for i in range(device_count):
        handle = pynvml.nvmlDeviceGetHandleByIndex(i)
        info = pynvml.nvmlDeviceGetUtilizationRates(handle)

        cpu = str(cpu_val) + percent
        mem = str(mem_val) + percent
        gpu = str(info.gpu) + percent

        #print(f"CPU:{cpu}, Mem: {mem} Usage: GPU: {info.gpu}%")

        publish.single("pc-cpu", cpu, hostname="broker.hivemq.com")
        publish.single("pc-mem", mem, hostname="broker.hivemq.com")
        publish.single("pc-gpu", gpu, hostname="broker.hivemq.com")

    
    time.sleep(10)

