import docker
import json

# Load the configuration from the JSON file
with open('config.json') as f:
    container_config = json.load(f)

# Create a Docker client
client = docker.from_env()

# Run the container based on the configuration
container = client.containers.run(**container_config)

# Print a message indicating that the container has been run
print(f"Container {container.id} has been run.")
