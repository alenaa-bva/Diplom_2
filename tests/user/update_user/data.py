class TestParametersCreator:

    def get_valid_test_names(self) -> dict:

        user_names = {
            "name_1" : "Григорий",
            "name_2" : "Gleb",
            "name_3" : "рустам хасанов",
            "name_4" : "12345",
            "name_5" : "Р"
        }

        return user_names

    def get_valid_test_emails(self) -> dict:

        user_emails = {
            "email_1" : f"aaa",
            "email_2" : f"123"
        }

        return user_emails