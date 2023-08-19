![](./assets/pheno-th.png)

# Pheno

> The Pheno Application is designed to... Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 



## Setting up Development Environment

- Fork the repository [https://github.com/siddhantprateek/pheno](https://github.com/siddhantprateek/pheno) to your GitHub account.
- Clone the forked repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/pheno.git
```
- Navigate to the project directory:
```bash
cd pheno
```

### **Running the Application using Docker Compose**:

- Make sure you have Docker and Docker Compose installed on your system.
- Run the application using Docker Compose with the following command:

```bash
docker-compose up -d
```

- The application should now be running in the background as defined in the `docker-compose.yml` file.

### **Installing Python Dependencies**:
   
- Ensure you have Python installed on your system.
- Install the Python dependencies specified in `requirements.txt` using the following command:

```bash
pip install -r requirements.txt
```

### **Running the Application Manually**:

- Navigate to the `app` directory:
```bash
 cd app
```
- Start the server using UVicorn with the following command:
```bash
 uvicorn main:app --reload
```
- The application should now be accessible at `http://localhost:8000`.

## Author

For questions or support, you can reach us at...
- [Siddhant Prateek Mahanayak]()