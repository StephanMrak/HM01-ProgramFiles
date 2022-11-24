def players(threadname,q5):
    import time
    while True:
        time.sleep(0.5)
        Playernames = ["Marion","Stephan","Alex","Flo"]
        if not q5.full():
            q5.put(Playernames)
