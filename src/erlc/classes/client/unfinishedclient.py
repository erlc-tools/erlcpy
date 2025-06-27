class UnfinishedClient:
    @property
    def options(self):
        print(f"FATAL: A call for options on a UnfinishedClient was called. This means you didnt call Client.config")
        return
    
    def config(self):
        print(f"FATAL: A call for config on a UnfinishedClient was called. This means you are calling config on the wrong thing.")
        return

