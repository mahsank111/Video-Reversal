import cv2

cap = cv2.VideoCapture('video.mp4')

frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('reversed video.mp4', fourcc, fps, (width, height))

frame_index = frames - 1

if cap.isOpened():
    print('Reversing video in progress...')
    while frame_index >= 0:
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        ret, frame = cap.read()
        if not ret:
            print('Failed to reverse video')
            break
        out.write(frame)
        frame_index -= 1

    print('Reversed the video successfully')
    print('Open the folder to check the video!')

    out.release()
    cap.release()
    cv2.destroyAllWindows()