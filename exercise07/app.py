import os

def main():
    app_env = os.getenv("APP_ENV", "undefined")
    print(f"App environment: {app_env}")

if __name__ == "__main__":
    main()