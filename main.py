import serial
import serial.tools.list_ports
import time

print("xiaoniaoawa/slimeNRF52840-poweroff")
print("一个一键关闭所有配对的SlimeNRF52840追踪器的工具\n\n")

# 查找并发送关机命令
for port in serial.tools.list_ports.comports():
    if port.vid == 0x1209 and port.pid == 0x7690:  # VID=4617, PID=30352
        try:
            with serial.Serial(port.device, 9600, timeout=2) as ser:
                time.sleep(0.5)  # 等待连接稳定
                
                # 清除输入缓冲区
                ser.reset_input_buffer()
                
                # 发送关机命令
                ser.write(b"send all shutdown\r\n")
                print(f"已向serial port {port.device} 发送关机命令")
                
                # 等待并读取响应
                time.sleep(1)
                if ser.in_waiting > 0:
                    response = ser.read(ser.in_waiting)
                    print(f"\n===响应============ \n {response.decode('utf-8', errors='ignore')}\n===============")
                    print("程序将在10秒内退出喵")
                    time.sleep(5)
        except Exception as e:
            print(f"错误: {e}")