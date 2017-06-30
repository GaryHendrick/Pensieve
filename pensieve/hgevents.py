from asyncio import set_event_loop

import cv2

from pensieve.guievents import GuiEventLoop


class _HgApp(object):
    def __init__(self):
        self.is_running = False

    def mainloop(self):
        while self.is_running:
            k = cv2.waitKey() & 0xFF
            if k == 0xFF:  # No windows opened
                continue
            else:
                continue  # fixme: propagate the keystroke event

    def update(self):
        cv2.waitKey(1)

    def quit(self):
        cv2.destroyAllWindows()


class HgEventLoop(GuiEventLoop):
    _default_executor = None

    def __init__(self):
        super().__init__()
        self._app = _HgApp()

    def mainloop(self):
        set_event_loop(self)
        try:
            self.run_forever()
        finally:
            set_event_loop(None)

    # Event Loop API
    def run(self):
        """Run the event loop.  Block until there is nothing left to do.
        Note that it may be necessary to add a means to listen for user events. """
        self._app.mainloop()

    def run_forever(self):
        """Run the event loop.  Block until stop() is called."""
        self._app.mainloop()

    def run_once(self, timeout=None):  # NEW!
        """ Run one complete cycle of the event loop."""
        self._app.update()

    def stop(self):  # NEW!
        """Stop the event loop as soon as reasonable.

        Exactly how soon that is may depend on the implementation, but
        no more I/O callbacks should be scheduled.
        """
        super().stop()
        self._app.quit()

    def call_later(self, delay, callback, *args):
        res = self.app.after(int(delay * 1000),
                             lambda cb, a: cb(*a),
                             callback,
                             args)
        return _CancelJob(self, res)


class _CancelJob(object):
    """Object that allows cancelling of a call_later"""

    def __init__(self, event_loop, after_id):
        self.event_loop = event_loop
        self.after_id = after_id

    def cancel(self):
        self.event_loop.app.after_cancel(self.after_id)
