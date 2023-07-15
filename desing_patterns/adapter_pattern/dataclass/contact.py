class Contact:

    def __init__(self, full_name: str, email: str, phone_number: str, is_friend: str):
        self.full_name = full_name
        self.email = email
        self.phone_number = phone_number
        self.is_friend = is_friend

    def __str__(self):
        return f"{self.full_name}-{self.email}-{self.full_name}{'Friend' if self.is_friend else ''}"
