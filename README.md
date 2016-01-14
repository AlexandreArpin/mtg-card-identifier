# Magic the Gathering Card Identifier

## Requirements

This project is built with Python 3.4. You will need Tesseract 3.0.4 and OpenCV 3.0 in order for this projet to work.

You can install Tesseract on Ubuntu with

    sudo apt-get install tesseract-ocr

Once it's installed, make sure to move the `mtg.traineddata` file to your `tessdata` folder (Usually `/usr/local/share/tessdata`)

As for OpenCV, it's best to follow this [guide](http://www.pyimagesearch.com/2015/07/20/install-opencv-3-0-and-python-3-4-on-ubuntu/).

Once OpenCV, Tesseract, Python and your virtual environnement is setup, you can install the python libraries.


    # Install requirements.txt
    pip install -r requirements.txt

And you're done! Now you can navigate in the mtg-card-identifier folder

	# Launch local debug server on 127.0.0.1:8000
    python manage.py runserver

    # Run the test suite
    python manage.py test

