import os

import cv2


DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 3
dataset_sizes = [50, 50, 50, 50]  #total=200
test_modes = ["Left Hand Normal", "Right Hand Normal", "Rotating Right Hand", "Rotating Left Hand"]

cap = cv2.VideoCapture(0)
for j in range(number_of_classes):
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print('Collecting data for class {}'.format(j))

    done = False
    for m, mode in enumerate(test_modes):
        while True:
            ret, frame = cap.read()
            cv2.putText(frame, f'Ready? Press "Q" ! :) Sign #{j}', (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
                        cv2.LINE_AA)
            cv2.putText(frame, f'{m+1}/4: {mode}', (100, 130), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
                        cv2.LINE_AA)
            cv2.imshow('frame', frame)
            if cv2.waitKey(25) == ord('q'):
                break

        counter = 0
        while counter < dataset_sizes[m]:
            ret, frame = cap.read()
            cv2.imshow('frame', frame)
            cv2.waitKey(25)
            cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)

            counter += 1

cap.release()
cv2.destroyAllWindows()