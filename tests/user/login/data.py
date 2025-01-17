class TestParametersCreator:

    def get_test_params(self, user_data) -> dict:

        login_data = {
            "valid_user": {
                "email": user_data["email"],
                "password": user_data["password"]
            },
            "invalid_email": {
                "email": "some_user_email",
                "password": user_data["password"]
            },
            "invalid_password": {
                "email": user_data["email"],
                "password": "some_user_password"
            },
            "missing_email": {
                "email": "",
                "password": user_data["password"]
            },
            "missing_password": {
                "email": user_data["email"],
                "password": ""
            }
        }

        return login_data