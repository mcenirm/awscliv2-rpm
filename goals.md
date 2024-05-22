# Goals

## Minimum

- [X] build an installable RPM for AWS CLI v2
- [ ] ~~support~~ deprecate EL7 (RHEL, Centos)
- [ ] support EL8 (RHEL, Rocky)
- [X] bare minimum testing: Does it install?
- [ ] test it properly, so we get notified when an upstream change breaks an assumption

## Stretch

- [ ] support AMZN2, ___?
- [ ] conflict with RPM for AWS CLI v1 ("awscli")
- [ ] track versions for official releases of AWS CLI v2
- [X] publish RPM to releases on github project
- [X] use github actions so this is all automated
- [ ] simplify workflow using hub cli?
- [X] schedule workflow (daily check for new installer)
- [ ] be smarter about new versions than just checking every day
- [ ] avoid having to update this repo to handle new versions (TODO: clarify goal)
- [X] support notifications of new versions (at least, I get emails from the PR and releases)
- [ ] support other (?) notifications of new versions
- [ ] properly check PGP signature
- [ ] ~~look into similar package for the session manager plugin~~ (it's already an RPM)


# References

* [How to package proprietary software](https://developers.redhat.com/blog/2014/12/10/how-to-package-proprietary-software/)
* [Installing the AWS CLI version 2 on Linux](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html)
* [RPM Build](https://github.com/marketplace/actions/rpm-build) github action
* [Install the Session Manager Plugin for the AWS CLI](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html)
