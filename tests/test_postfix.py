
def test_postfix_package_installed(host):
    postfix = host.package("postfix")
    assert postfix.is_installed
    assert postfix.version.startswith("3.4.8")

def test_postfix_service_running_and_enabled(host):
    postfix = host.service("postfix")
    assert postfix.is_running
    assert postfix.is_enabled
