import asyncio
import concurrent
import logging
import sys

import cv2


def trackChange(position):
    log = logging.getLogger('trackChange')
    log.info('received callback on trackChange with position {}'.format(position))


@asyncio.coroutine
def await_key():
    return cv2.waitKey() & 0xFF


@asyncio.coroutine
def await_key_loop():
    ''' a blocking function which polls a key '''
    log = logging.getLogger('await_key')
    log.info('running')
    while True:
        log.info('waiting for key press')
        k = yield from await_key()
        log.info('received pressed key: {}'.format(k))
        if k == 27:
            break
        elif k == 255:
            break
    cv2.destroyWindow('main window')
    log.info('done')


@asyncio.coroutine
def run_blocking(executor):
    log = logging.getLogger('run_blocking')
    log.info('starting')

    log.info('creating executor task')
    loop = asyncio.get_event_loop()
    task = loop.run_in_executor(executor, await_key_loop)
    log.info('waiting for executor tasks to run')
    completed = yield from task
    results = [t.result() for t in completed]
    log.info('results: {!r}'.format(results))
    log.info('exiting')


@asyncio.coroutine
def run_concurrently():
    log = logging.getLogger('run_concurrently')
    log.info('starting the concurrent loop')
    for i in range(10):
        yield from asyncio.sleep(1)
        log.info(i)
    log.info("finishing, running concurrently")


def build_gui():
    cv2.namedWindow('main window')
    cv2.createTrackbar('trackbar', 'main window', 5, 10, trackChange)


def main():
    executor = concurrent.futures.ThreadPoolExecutor(
        max_workers=3,
    )

    if sys.platform.startswith('win32'):
        asyncio.set_event_loop(asyncio.ProactorEventLoop())
    event_loop = asyncio.get_event_loop()

    build_gui()
    try:
        event_loop.run_until_complete(asyncio.wait([asyncio.async(run_blocking(executor)),
                                                    run_concurrently()
                                                    ])
                                      )
    finally:
        event_loop.close()


if __name__ == '__main__':
    ' run a simple highgui window, and another task concurrently'
    logging.basicConfig(
        level=logging.INFO,
        format='%(threadName)10s %(name)18s: %(message)s',
        stream=sys.stderr,
    )

    main()
