Summary: AWS CLI version 2
License: Apache License 2.0
# Group: ???
Name: awscliv2
URL: https://docs.aws.amazon.com/cli/
Version: 2.2.37
Release: 1%{?dist}
Source0: https://awscli.amazonaws.com/awscli-exe-linux-%{_arch}.zip
Source1: awscli-exe-linux-%{_arch}.zip.sha256
NoSource: 0

# skip debuginfo
%define debug_package %{nil}

%description
The AWS Command Line Interface (AWS CLI) is an open
source tool that enables you to interact with AWS
services using commands in your command-line shell.

%prep
cp "%{S:0}" ./
sha256sum -c "%{S:1}"
%setup -q -n aws

%build

%install
sh -x ./install --install-dir %{buildroot}/usr/libexec/awscliv2 --bin-dir %{buildroot}/usr/bin
# redo symlinks to avoid complaint about them containing RPM_BUILD_ROOT
ln -sf ../libexec/awscliv2/v2/current/bin/aws %{buildroot}/usr/bin/aws
ln -sf ../libexec/awscliv2/v2/current/bin/aws_completer %{buildroot}/usr/bin/aws_completer
rm -f %{buildroot}/usr/libexec/awscliv2/v2/current
ln -sf 2.2.37 %{buildroot}/usr/libexec/awscliv2/v2/current

%check
%{buildroot}/usr/bin/aws --version

%files
/usr/bin/aws
/usr/bin/aws_completer
/usr/libexec/awscliv2
