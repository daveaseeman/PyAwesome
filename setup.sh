sudo apt-get update
sudo apt-get install python3-pip -y


sudo apt-get install python3-dev libxml2-dev libxslt1-dev zlib1g-dev libfreetype6-dev libxft-dev cython -y

sudo pip3 install lxml python-docx
sudo pip3 install pypdf2
sudo pip3 install jinja2


sudo pip3 install numpy
sudo apt-get install tree 

cd /tmp
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh -b
~/miniconda3/bin/conda install numba -y