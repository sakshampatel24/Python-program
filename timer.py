import winsound
import time

def beep_alarm():
    for repeats in range(7):
        winsound.Beep(3000, 500)
        winsound.Beep(6000, 300)
    
    timer_duration = int(input("Duration in seconds: "))
    
    hours, minutes, seconds = 1, 1, 1
    
    for _ in range(timer_duration):
        print('\n' * 100)
        seconds += 1
        
        if seconds == 60:
            minutes += 1
            seconds = 0
            
        if minutes == 60:
            hours += 1
            minutes = 0
            
        print(f"{hours:05d}:{minutes:05d}:{seconds:05d}")
        time.sleep(1)
        
if __name__ == '__main__':
    beep_alarm()
