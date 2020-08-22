# Goals

## Minimum

- [ ] build a no-source RPM for AWS CLI v2
- [ ] support EL7 (RHEL, Centos)
- [ ] test it properly, so we get notified when an upstream change breaks an assumption
- [ ] document procedure for building real RPM from nosrc RPM (download and rpmbuild)

## Stretch

- [ ] support AMZN2, EL8, ___?
- [ ] conflict with RPM for AWS CLI v1
- [ ] track versions for official releases of AWS CLI v2
- [ ] publish RPM to releases on github project
- [ ] use github actions so this is all automated
- [ ] automate trigger (releases? weekly?) for new versions
- [ ] avoid having to update this repo to handle new versions
- [ ] properly check PGP signature
- [ ] look into similar package for the session manager plugin


# References

* [How to package proprietary software](https://developers.redhat.com/blog/2014/12/10/how-to-package-proprietary-software/)
* [Installing the AWS CLI version 2 on Linux](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html)
* [RPM Build](https://github.com/marketplace/actions/rpm-build) github action
* [Install the Session Manager Plugin for the AWS CLI](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html)
