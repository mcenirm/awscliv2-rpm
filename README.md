# awscliv2-rpm

Automated RPM packaging of AWS CLI v2 using GitHub Actions

Only EL7 (RHEL, Centos, ???) are supported now, but other distros are in the [wishlist](goals.md).


# Building the RPM locally

1. `./check_for_new_installer` - download the [installer](https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip) and update various metadata files
1. `./respecit` - update the spec file to match the downloaded version
1. `docker-compose build builder` - create the builder image
1. `docker-compose run builder ./rebuildit` - rebuild the RPM
1. `docker-compose run tester ./retestit` - test installing the RPM

This should result in:
* no-source RPM: `SRPMS/awscliv2-${VERSION}-${RELEASE}.el7.nosrc.rpm`
* installable RPM: `RPMS/x86_64/awscliv2-${VERSION}-${RELEASE}.el7.x86_64.rpm`
