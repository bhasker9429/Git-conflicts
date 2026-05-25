# Define your hardcoded WildFly version info
wildfly_versions = {
    "dev": "35.0.0.Final",
}

# Select the target environment
env = "dev"

# Access the version
if env in wildfly_versions:
    print(f"Target WildFly version for {env} is {wildfly_versions[env]}")
else:
    print("Environment not found.")
