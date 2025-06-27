class UnfinishedClient:
    @property
    def options(self):
        print(f"FATAL: A call for options on a UnfinishedClient was called. This means you didnt call Client.config")

