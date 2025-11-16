# MLOps: Flask Kubernetes CI/CD Pipeline

This project is an academic assignment to design and implement a complete Continuous Integration and Continuous Delivery (CI/CD) pipeline for a simple Python Flask application.

The pipeline uses GitHub for version control, GitHub Actions for CI (testing/linting), Jenkins for CD (deployment), and Kubernetes (Minikube) for orchestration.

## Kubernetes Features Used

This project leverages several key Kubernetes features to ensure a robust deployment:

* **Deployments:** Manages the desired state of the application.
* **Services (NodePort):** Provides a stable "front door" (load balancer) to access the application, even as pods are created or destroyed.
* **Scaling:** The `deployment.yaml` is configured with `replicas: 3` to run three instances of the app, distributing traffic and ensuring high availability.
* **Rolling Updates:** The deployment strategy is set to `RollingUpdate` with `maxSurge: 1` and `maxUnavailable: 1`. This ensures that when we deploy a new version, the application updates one pod at a time with zero downtime.
* **Resource Limits:** We set CPU and memory `requests` (minimum guaranteed) and `limits` (maximum allowed) to ensure the app is a good "neighbor" and doesn't consume all cluster resources.

---

## How to Build and Run Locally (Docker)

You can build and run this application locally using Docker.

1.  **Build the Docker image:**
    ```bash
    docker build -t flask-app:local .
    ```

2.  **Run the container:**
    This command runs the container and maps your local port 8080 to the container's port 5000.
    ```bash
    docker run -p 8080:5000 flask-app:local
    ```

3.  **View the app:**
    Open your browser and go to `http://localhost:8080`.

---

## How to Deploy (CI/CD Pipeline)

This project is fully automated. The deployment process is handled by Jenkins.

1.  **CI (GitHub Actions):** On any `git push`, GitHub Actions automatically runs linters (`flake8`) and unit tests (`pytest`) to check code quality.

2.  **CD (Jenkins):** A new deployment to Kubernetes is **automatically triggered** every time a Pull Request is merged into the `main` branch.

To deploy a new change:
1.  Create a new branch (e.g., `feature/my-new-change`).
2.  Make your code changes.
3.  Commit and push your branch.
4.  Open a Pull Request to merge into `main`.
5.  Once the Admin reviews and merges the PR, the Jenkins pipeline will automatically run, build the new Docker image, and deploy it to the Kubernetes cluster.