class Settings:
    def __init__(self):

        self.config = {
            "interval": 1,
            "s3_bucket": "S3 Bucket Name",
            "aws_access_key": "AWS Access Key",
            "aws_secret_key": "AWS Secret Key",
            "region_name": "ap-southeast-1",
            "timezone": "Asia Pacific (Singapore)",
            "capture_screenshots": True,
        }

    def update(self, new_config):
        """
        Update the configuration settings.
        """
        self.config.update(new_config)
        print("Configuration updated:", self.config)

    def get(self, key):
        """
        Get a configuration value by key.
        """
        return self.config.get(key, None)
