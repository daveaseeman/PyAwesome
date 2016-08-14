#sudo apt-get update
#sudo apt-get install python3-pip -y


#sudo apt-get install python3-dev libxml2-dev libxslt1-dev zlib1g-dev libfreetype6-dev libxft-dev cython tree -y

sudo apt-get install tree -y
sudo apt-get install libxml2-dev libxslt1-dev libjpeg-dev python3-dev  -y

cd /tmp
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh -b

echo "PATH=/home/vagrant/miniconda3/bin:$PATH" >> ~/.bashrc

/home/vagrant/miniconda3/bin/conda install --file requirements.txt -y
/home/vagrant/miniconda3/bin/pip install -r pip_req.txt
echo "cd /vagrant" >> /home/vagrant/.bashrc
cd /vagrant