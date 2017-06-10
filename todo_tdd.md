# Test Driven Development Task List
## End-To-End Test
* Object Notification Integrity Test - Launch Application and Monitor Application for Update Indicating Button Click in GUI

## Unit Testing
### TheModel testing HasTraits object notifications 
* test_observer_x - mock an observer for x and modify x, confirming the mock's observations
* test_chain_observer_x - build TheModel, copy traits from TheModel to TheSubModel, change TheSubModel.x and confirm
mocked observation in observer_x

### Divinator (traitlets Application) tests
* Signal to GuiContext to close and delete windows
* Signal to GuiContext to open and create windows
* Test Methods used to Iterate the OpenCV VideoSource
* Test Methods used to write those iterations to TheModel
* Build a processing pipeline and pass data in one end to observe predictable change throughout

### WindowControl Tests
* Test throughput of events from gui to gui context
* Destroy yourself and observe the destruction
* Test the throughput of events from gui to TheModel

### PensieveViews Tests
* Create a View, attach its events, and confirm the wiring
