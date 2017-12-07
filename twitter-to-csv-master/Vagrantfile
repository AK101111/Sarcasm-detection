# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
    config.package.name = "precise.box"
    config.vm.box = "precise32"
    config.vm.box_url = "http://files.vagrantup.com/precise32.box"
    config.vm.provider :virtualbox do |vb|
        vb.customize ["modifyvm", :id, "--memory", 128]
        vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
        vb.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
    end
    #config.vm.provision :shell, :path => "setup/make_vagrant.sh"
end
