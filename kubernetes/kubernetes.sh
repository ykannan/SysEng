yum install docker-ce -y

####add repo
yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo

systemctl start docker
systemctl enable docker

#Installing kubeadm,kubelet&kubectl
[root@ip-172-31-42-232 yum.repos.d]# cat kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg

sudo kubeadm init --pod-network-cidr=10.244.0.0/16

#run on worker (join worker to master)
kubeadm join 172.31.9.64:6443 --token mqskh6.kdr7urqz9fs3m200 \
    --discovery-token-ca-cert-hash sha256:d73d39f72897eb0dfbedbc3a1b685393f6e77b6c5ba2e7a0e588972f55d07331

#deploy flannel on master 
#run on both client and master
echo "net.bridge.bridge-nf-call-iptables=1" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
#run only on master
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/v0.12.0/Documentation/kube-flannel.yml




#loadbalancer
cat << EOF | kubectl create -f -
apiVersion: v1
kind: Service
metadata:
  name: example-service
spec:
  selector:
    app: example
  ports:
    - port: 8765
      targetPort: 9376
  type: LoadBalancer
EOF
