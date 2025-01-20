class TestParametersCreator:

    def get_test_params(self, user_data) -> dict:

        register_data = {
            "valid_user": {
                "email": user_data["email"],
                "password": user_data["password"],
                "name": user_data["name"]
            },
            "invalid_email": {
                "email": "some_user_email",
                "password": user_data["password"],
                "name": user_data["name"]
            },
            "missing_password": {
                "email": user_data["email"],
                "password": "",
                "name": user_data["name"]
            },
            "missing_email": {
                "email": "",
                "password": user_data["password"],
                "name": user_data["name"]
            },
            "missing_name": {
                "email": user_data["email"],
                "password": user_data["password"],
                "name": ""
            }
        }

        return register_data