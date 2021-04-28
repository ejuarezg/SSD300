# SSD300
Single Shot MultiBox Detector implemented with TensorFlow
## Dependencies ##
* python3.6.1 or greater
* numpy
* skimage
* TensorFlow
* matplotlib
* OpenCV
* tqdm

## Usage ##
1. Import required modules
```
import tensorflow as tf
import numpy as np

from util.util import *
from model.SSD300 import *
```

2. Load test-image  
```
img = load_image('./test.jpg')
img = img.reshape((300, 300, 3))
```

3. Start Session  
```
with tf.Session() as sess:
        ssd = SSD300(sess)
        sess.run(tf.global_variables_initializer())
        for ep in range(EPOCH):
            ...
```

4. Training or Evaluating
you must just call ssd.eval() !
```
...

_, _, batch_loc, batch_conf, batch_loss = ssd.eval(minibatch, actual_data, is_training=True)

...
```


## Test Training ##
you have to extract data-set from zip files.
decompress all zip files in datasets/ and move to voc2007/ dir.
```
$ ls voc2007/ | wc -l    #  => 4954
$ ./setup.sh
$ python train.py
```

## Using Manga109 dataset

- Create the environment file by installing the packages in `./environment/environment_snapshot.yml`.
- Unzip the Manga109 file. Rename folder to `Manga109` and place in the root of this repo. The dataset can be downloaded from the [Manga109 website](http://www.manga109.org/en/download.html) by requesting access.
- Ensure that the variable `USE_MANGA109` is set to true in `trainer.py` and run the script.
- After training, test an image using the command `python inference.py Manga109/images/ARMS/002.jpg`

## Present Circumstances ##
I'm checking and testing SSD model, so this model may not be complete.

If I have overlooked something, please tell me.

## Welcome PullRequest or E-mail ##
