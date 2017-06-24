# Test Driven Development Task List
## End-To-End Test
* Object Notification Integrity Test - Launch Application and Monitor Application for Update Indicating Button Click in GUI

the class `TestDivinatorEndToEnd` in the module `pensieve.core.tests` contains the test `test_launch_and_click`

## Unit Testing
### TheModel testing HasTraits object notifications 
* ~test_observer_x - mock an observer for x and modify x, confirming the mock's observations~
* ~test_chain_observer_x - build TheModel, copy traits from TheModel to TheSubModel, change TheSubModel.x and confirm
mocked observation in observer_x~
    * ~the truth is that chaining the observer system has to happen downstream.  This test will be included, but it will
    be clear that a scope local `HasTraits` will be defined, and the traits of TheModel must be caught.~

### Divinator (traitlets Application) tests
* Signal to GuiContext to close and delete windows
* Signal to GuiContext to open and create windows
* Test Methods used to Iterate the OpenCV VideoSource
    * test the iterator's identity as an abc.Iterator
* Test Methods used to write those iterations to TheModel
* Build a processing pipeline and pass data in one end to observe predictable change throughout

### CaptureProperties
* ~test accessors~
* ~test setters~

### WindowControl Tests
* Test throughput of events from gui to gui context
* Destroy yourself and observe the destruction
* Test the throughput of events from gui to TheModel

### PensieveViews Tests
* Create a View, attach its events, and confirm the wiring
