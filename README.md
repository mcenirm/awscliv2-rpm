# nosrcrpmawscliv2
Can I make a no-source RPM for AWS CLI v2?

(Better question: Is this a good idea? The installer is safe to redistribute, so maybe this would be better as a normal binary-only RPM.)


# experimenting using docker-compose

1. Download the [installer](https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip)
1. `docker-compose build builder`
1. `docker-compose run builder`
    1. `./rebuildit`
    1. `exit`
1. `docker-compose run tester`
    1. `./retestit`

This should result in:
* no-source RPM: `SRPMS/awscliv2-2.0.43-1.el7.nosrc.rpm`
* installable RPM: `RPMS/x86_64/awscliv2-2.0.43-1.el7.x86_64.rpm`
