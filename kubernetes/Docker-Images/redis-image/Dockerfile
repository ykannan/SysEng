# use an exisitng docker image as base. 
FROM centos
#Download and install dependency 
RUN yum install -y redis
# Tell image what to do when started as a container
CMD ["redis-server"]
#expose port 8000 for the container
EXPOSE 8000

# version: '2'
# services:
#     myservice:
#         restart: "no"

#         build: .

#         ports:
#             - 8080:8080/tcp