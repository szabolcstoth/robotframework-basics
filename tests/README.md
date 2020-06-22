# Tests

Use the following command to execute the test cases without any issues:

``` bash
robot \
  --pythonpath libraries \
  --pythonpath listeners \
  --variable SSH_USERNAME:robotdev \
  --variable SSH_PASSWORD:Hn7c5%lyBpIn8*8Z \
  --outputdir output \
  .
```

The test cases in ``03-Remote`` suite will pass only if you started an ``openssh-server`` based container as it was suggested in the chapter ``3.0. Set up a remote host``.
