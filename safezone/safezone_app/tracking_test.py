# tracking

import subprocess
from collections import deque


deque3 = deque(maxlen=70)
deque2 = deque([1, 2, 3])
for i in deque2:
    print(i)



# count = {'0' : 1, '1' : 2, '2' : 0, '3' : 0, '4' : 5, '5' : 0}
# string_test = '17:1 2 4 '
# string_test_split = string_test.split(':')[1].split(' ')

# print(string_test_split)
# for count_index in count:                
#     if count_index in string_test_split:
#         count[count_index] += 1
#     else:
#         count[count_index] = 0
                
# print(count)

# test = {'0' : 1, '1' : 2, '2' : 3, '3' : 4, '4' : 5, '5' : 6}
# for test_check in test:
#     print(test_check)
# tracking = subprocess.check_output('python C:/Users/leeyo/Project/yolov5/detect.py --weights C:/Users/leeyo/Project/yolov5/runs/train/yolov5s_third/weights/best.pt --source C:/Users/leeyo/Project/yolov5/runs/detect/exp/video_test.mp4 --save-txt ', shell=True, universal_newlines=True)

# print('tracking = ', tracking)