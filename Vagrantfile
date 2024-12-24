
ENV['VAGRANT_NO_PARALLEL'] = 'yes'

Vagrant.configure("2") do |config|

  config.vm.box = "generic/ubuntu2204"

  config.vm.hostname = "test-postfix"

  config.vm.network "private_network", type: "dhcp"

  config.vm.provider :libvirt do |libvirt|
    libvirt.cpus = 2
    libvirt.memory = 2048
    libvirt.driver = "kvm"
  end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "tests/test.yml"
    ansible.verbose = "vvvv"
    ansible.compatibility_mode = "2.0"
  end

end
