# Python with Visual Studio Code

There I explain how I prepared my development environment for OpenCV+Python

## Step-by-Step Solution

1. Download & install Python

    There you need to get sure that it was successfully installed by calling 

    ```
    python --version
    ```

    in terminal

    For me it was `Python 3.8.2`

2. Than upgrade `pip` (Python installation manager) by calling 

    ```
    python -m pip install --upgrade pip
    ```

    On some resource you could find that `pip` update can be done by calling just

    ```
    pip install --upgrade pip
    ```

    however it ruins `pip` as it tries to update something that is executed at the same time

    If you accidentally done so call

    ```
    python -m ensurepip
    ```

    which should recover your installation

3. Install **OpenCV**

    ```
    pip install opencv-contrib-python
    ```

Now you are ready to develop with Python 3 & OpenCV. 

See `main.py` for example