![image](https://github.com/emreyldzgl/Flood-Prediction-Docker-Kubernetes-Streamlit-APP/blob/main/data/image1.png) 

<h2 align="center"> <b> Flood Prediction App 🌊</b></h2>

<p> <a> Flood detection is a website used to calculate the presence or probability of flooding in a particular area. </a></p>


<h2> <b> Technologies Used ⚙️</b> </h2>

![image](https://github.com/emreyldzgl/Flood-Prediction-Docker-Kubernetes-Streamlit-APP/blob/main/data/orig.png)
<p> <a>  <b> CatboostRegressor :</b> Catboost Regressor was used because it showed high success as a machine learning model.</a></p>

![image](https://github.com/emreyldzgl/Flood-Prediction-Docker-Kubernetes-Streamlit-APP/blob/main/data/image2.png)
<a> <b> Docker - DockerHub :</b> Using Docker and DockerHub, we have enabled a machine learning model to run in a virtual machine environment. This allows us to run our machine learning model in any environment without having to set up the environment each time. For this purpose, I created a Dockerfile locally and included a requirements.txt file to set up the necessary environment. Then, I pushed the Docker image I created locally to a repository on DockerHub and made my Docker image available for sharing.</a>

![image](https://github.com/emreyldzgl/Flood-Prediction-Docker-Kubernetes-Streamlit-APP/blob/main/data/image3.png)
<p><a> <b> Google Cloud - Kubernetes :</b> I previously transferred the Docker image I created to a cluster I set up on Google Cloud Kubernetes Engine by cloning it from GitHub. To perform the deployment, I needed to create a workload, so I created a build.yaml file for this workload. By exposing the created workload, I obtained an endpoint, thus deploying the application.</a>

![image](https://github.com/emreyldzgl/Flood-Prediction-Docker-Kubernetes-Streamlit-APP/blob/main/data/streamlit.png)
<p> <a>  <b> Streamlit :</b> I coded an interface for my application using Streamlit and created a website where I can interactively obtain results.</a></p>

[Flood Prediction App - Streamlit](https://34.122.26.94/)
