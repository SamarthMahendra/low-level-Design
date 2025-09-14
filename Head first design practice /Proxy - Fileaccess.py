from abc import ABC, abstractmethod


# --- Subject Interface ---
class FileAccess(ABC):
    @abstractmethod
    def read(self) -> str:
        pass

    @abstractmethod
    def write(self, data: str) -> None:
        pass


# --- Real Subject ---
class RealFileAccess(FileAccess):
    def __init__(self, filename: str):
        self.filename = filename

    def read(self) -> str:
        with open(self.filename, "r") as file:
            return file.read()

    def write(self, data: str) -> None:
        with open(self.filename, "w") as file:
            file.write(data)


# --- Proxy ---
class ProtectedFileAccess(FileAccess):
    def __init__(self, filename: str, user_role: str = "guest"):
        self.user_role = user_role
        self.filename = filename
        self.real_file = RealFileAccess(filename)

    def read(self) -> str:
        if self.filename == "secret.txt" and self.user_role != "admin":
            print(f"[Proxy] {self.user_role} cannot access {self.filename}.")
            return ""
        print(f"[Proxy] {self.user_role} is reading {self.filename}...")
        return self.real_file.read()

    def write(self, data: str) -> None:
        if self.user_role != "admin":
            print(f"[Proxy] {self.user_role} does not have permission to write to {self.filename}.")
            return
        print(f"[Proxy] {self.user_role} is writing to {self.filename}...")
        self.real_file.write(data)


# --- Demo ---
if __name__ == "__main__":
    # assume files already exist with some text
    admin_access = ProtectedFileAccess("public.txt", "admin")
    print(admin_access.read())

    secret_admin = ProtectedFileAccess("secret.txt", "admin")
    print(secret_admin.read())

    guest_access = ProtectedFileAccess("secret.txt", "guest")
    print(guest_access.read())  # denied
