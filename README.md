# Thermal-imaging-workflow-code
Scripts required to compute calibrated thermal imagery with the Boson 640.

capture_image.py is a script that runs inside the Raspberry Pi in order to detect the trigger signal from the autopilot. At a trigger event, the Raspberry get a frame from the video output of the Boson 640.

undistort.py is a script that corrects the imagery, using the distortion coefficients and intrinsic matrix of the camera. This script performs the correction process over a set of images inside a specified folder.

missing code:

*matlab camera calibrator code*

*temperature calibration code*

*CWSI code*


Andres Montes de Oca <br />
PhD. Student <br />
andresmr@cio.mx

🍀
