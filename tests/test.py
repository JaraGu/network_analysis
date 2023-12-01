import os,sys
import unittest

# Set the working directory to the location of your test file
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# Add parent directory to path to import modules from src
rpath = os.path.abspath('..')
if rpath not in sys.path:
    sys.path.insert(0, rpath)
from src.loader import SlackDataLoader

class TestSlackDataLoader(unittest.TestCase):

    def setUp(self):
        # Create an instance of SlackDataLoader for testing
        self.data_loader = SlackDataLoader("../anonymized/")

    def test_get_users_columns(self):
        # Test if the 'get_users' method returns a DataFrame with the expected columns
        expected_columns = ['id', 'name', 'real_name', 'tz', 'tz_label', 'tz_offset', 'is_admin', 'is_owner', 'is_primary_owner', 'is_restricted', 'is_ultra_restricted', 'is_bot']
        users_df = self.data_loader.get_users()
        self.assertTrue(set(expected_columns).issubset(users_df.columns), f"Missing columns in 'get_users' DataFrame: {set(expected_columns) - set(users_df.columns)}")

    def test_get_channels_columns(self):
        # Test if the 'get_channels' method returns a DataFrame with the expected columns
        expected_columns = ['id', 'name', 'is_channel', 'is_group', 'is_im', 'created', 'is_archived', 'is_general', 'unlinked', 'name_normalized', 'is_shared', 'parent_conversation', 'creator', 'is_ext_shared', 'is_org_shared', 'shared_team_ids', 'pending_shared', 'pending_connected_team_ids', 'is_pending_ext_shared', 'is_member', 'is_private', 'is_mpim', 'topic', 'purpose', 'previous_names']
        channels_df = self.data_loader.get_channels()
        self.assertTrue(set(expected_columns).issubset(channels_df.columns), f"Missing columns in 'get_channels' DataFrame: {set(expected_columns) - set(channels_df.columns)}")

    def test_get_users_data(self):
        # Test if the 'get_users' method returns a DataFrame with the expected data
        expected_data = [
            {"id": "U03T89ACUUW", "name": "Carlos", "real_name": "Carlos Gross", "tz": "Africa/Harare", "is_admin": True, "is_owner": True, "is_primary_owner": False, "is_restricted": False, "is_ultra_restricted": False, "is_bot": False},
            {"id": "U03TEPYRM2P", "name": "Garrett", "real_name": "Garrett Bell", "tz": "Africa/Algiers", "is_admin": True, "is_owner": True, "is_primary_owner": True, "is_restricted": False, "is_ultra_restricted": False, "is_bot": False}
            # Add more entries as needed
        ]
        users_df = self.data_loader.get_users()
        for data in expected_data:
            self.assertTrue(any(users_df['id'] == data['id']), f"User with id {data['id']} not found in 'get_users' DataFrame")

    def test_get_channels_data(self):
        # Test if the 'get_channels' method returns a DataFrame with the expected data
        expected_data = [
            {"id": "C03T0APHX63", "name": "all-community-building", "created": 1660301317, "creator": "U03TEPYRM2P", "is_archived": False, "is_general": False, "members": ["U03T89ACUUW", "U03TEPYRM2P", "U03TNP8Q8CT"], "topic": {"value": "", "creator": "", "last_set": 0}, "purpose": {"value": "", "creator": "", "last_set": 0}},
            {"id": "C03T0AX4K6K", "name": "all-technical-support", "created": 1660301462, "creator": "U03TEPYRM2P", "is_archived": False, "is_general": False, "members": ["U03T89ACUUW", "U03TEPYRM2P", "U03TNP8Q8CT"], "topic": {"value": "", "creator": "", "last_set": 0}, "purpose": {"value": "", "creator": "", "last_set": 0}}
            # Add more entries as needed
        ]
        channels_df = self.data_loader.get_channels()
        for data in expected_data:
            self.assertTrue(any(channels_df['id'] == data['id']), f"Channel with id {data['id']} not found in 'get_channels' DataFrame")

if __name__ == '__main__':
    unittest.main()
