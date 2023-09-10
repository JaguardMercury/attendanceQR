import cv2
from pyzbar import pyzbar
import csv

# Then we set a variable to store the information of the QR code we scanned. Every time we scan, we will check whether the scanned QR code was scanned before.
# If not, store it here. Then we call the method of opencv to instantiate a camera,
# Finally, we set the path of some tables where we store the QR code information.
found = set()
capture = cv2.VideoCapture(0)

# Store data table
qrcsv = "Absensi Laboratorium TT & BM.csv"

# Then we have to write an endless loop, we have to continuously use the camera to collect the QR code,
# So write the QR code collection code in an endless loop.
while True:
    # First, we need to use the camera we just instantiated to capture real-time photos.
    ret, frame = capture.read()

    # Then use the pyzbar function to analyze whether there is a QR code in the picture
    # Find the barcode in the image and decode it
    test = pyzbar.decode(frame)

    # Cycle detected barcodes
    for tests in test:
        # First convert it to a string
        testdate = tests.data.decode('utf-8')
        testtype = tests.type

        # Draw the barcode data and barcode type on the image
        printout = "{} ({})".format(testdate, testtype)

        if testdate not in found:
            # Print barcode data and barcode type to the terminal
            print("[INFO] Found {} barcode: {}".format(testtype, testdate))
            print(printout)
        # Store scan data
        if testdate not in found:
            with open(qrcsv, 'a+',newline='') as f:  #newline=``No blank lines will appear
                # a+ Open readable and writable files in append mode. If the file does not exist, it will be created. If the file exists, the written data will be added to the end of the file, that is, the original content of the file will be retained.
                csv_write = csv.writer(f)
                date = [testdate]
                csv_write.writerow(date)
            found.add(testdate)
    cv2.imshow('Test', frame)
    if cv2.waitKey(1) == ord('q'):
        break