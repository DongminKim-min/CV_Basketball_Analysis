import cv2

import sys
sys.path.append("../")
from utils import get_bbox_center, get_bbox_width

def draw_ellipse(frame, bbox, color, track_id = None):
    y2 = int(bbox[3])
    x_center,_ = get_bbox_center(bbox) # y_center is not used -> _
    # width = get_bbox_width(bbox)

    cv2.ellipse(
                img=frame, 
                center=(x_center, y2), 
                # axes=(int(width), int(0.35*width)), 
                axes=(70, 25), 
                angle=0, 
                startAngle=-45, 
                endAngle=235, 
                color=color, 
                thickness=2,
                lineType=cv2.LINE_4,
        )
        
    rectangle_width = 40
    rectangle_height = 20
    x1_rect = x_center - rectangle_width//2
    x2_rect = x_center + rectangle_width//2 
    y1_rect = y2 - rectangle_height//2 + 15 ## 15 ??
    y2_rect = y2 + rectangle_height//2 + 15

    if track_id is not None:
        cv2.rectangle(
            frame,
            (int(x1_rect), int(y1_rect)),
            (int(x2_rect), int(y2_rect)),
            color,
            cv2.FILLED,
        )

        x1_text = x1_rect + 12
        if track_id > 99:
            x1_text -= 10 # spacing for 3 digit number

        cv2.putText(
            frame,
            str(track_id),
            (int(x1_text), int(y1_rect+15)),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=0.5,
            color=(0,0,0),
            thickness=2,
            )
        
    return frame




