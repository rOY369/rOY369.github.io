# mqtt refactored library with callback mechanism

- Mqtt library still involves just stuff related to mqtt protocol - connects, reconnects and exposes some public methods like publish and subscribe and nothing else. 
- Callback mechanism is an interface which provides a readable simple abstracted way to produce callbacks and get them triggered as per a condition.
- This callback mechanism is completely separate from mqtt library since both functionalities are completely different, mqtt library can be used in isolation just like before without any callback mechanism.
- The power of defining your own on_connect, on_disconnect and on_message is still with the users of the library.
- Callback mechanism simply wraps your on_connect, on_disconnect and on_message to provide the extra utility.
- simple functions can simply be decorated with one line and can be trigerred as a callback without any complex if/else in on_message --> keeps function signatures more informative and readable.
- Naming convention - all callback functions can be named as callback_* for better readability. More naming conventions like this can be enforced.

Please take a look in the following order -
- wrapped_mqtt
- mqtt_callback_mechanism
- user_example

Please provide feedback/suggestion. I did this mainly as a side task just to see how this can work out. I just had this idea which could bring more simplicity and readability in our code. This functionality could even be used by any IoT module/service which deals with callbacks - hostservice,firmware,application etc. This requires refactoring of the current on_message triggers and callbacks first. When there is enough refactoring done and code is simple enough - then we can think about having this callback mechanism.

