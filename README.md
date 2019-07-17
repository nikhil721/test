**MAC ADDRESS QUERY BUILDER**

macaddress query builder is a simple tool to query data obtained  from the api _https://macaddress.io/ _ 

**Steps to run the command**

1.Build the Docker Image

```docker build -t <image-name>```

2.Run the Docker Image in order to build the Docker Container

```docker run <image-name>```

3.Log into the OS Bash 

```docker run -it <image_name> /bin/bash```

4.Run ```python mac-address-query.py <your-mac-address>```

5.Alternatively you can also run during the third step 
        ```python-docker-dev python mac-address-query <your-mac-address>```
        
**Elaboration on Security**
The best way to secure the API key is storing it in an ENV VARIABLE , however we have hardcoded it in the python file for the convenience 

```export NEW_VAR="at_kM8JCU2bTmFymZ9X2jdxgGqfRygWH"```
