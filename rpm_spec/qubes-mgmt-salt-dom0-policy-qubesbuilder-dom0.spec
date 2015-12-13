%{!?version: %define version %(cat version)}

Name:      qubes-mgmt-salt-dom0-policy-qubesbuilder
Version:   %{version}
Release:   1%{?dist}
Summary:   Installs or removes Qubes RPC policies in dom0 and domU to enable qubesbuilder to build in DispVMs.
License:   GPL 2.0
URL:	   http://www.qubes-os.org/

Group:     System administration tools
BuildArch: noarch
Requires:  qubes-mgmt-salt
Requires:  qubes-mgmt-salt-dom0

%define _builddir %(pwd)

%description
Installs or removes Qubes RPC policies in dom0 and domU to enable qubesbuilder to build in DispVMs.

%prep
# we operate on the current directory, so no need to unpack anything
# symlink is to generate useful debuginfo packages
rm -f %{name}-%{version}
ln -sf . %{name}-%{version}
%setup -T -D

%build

%install
make install DESTDIR=%{buildroot} LIBDIR=%{_libdir} BINDIR=%{_bindir} SBINDIR=%{_sbindir} SYSCONFDIR=%{_sysconfdir}

%post
# Update Salt Configuration
qubesctl state.sls config -l quiet --out quiet > /dev/null || true
qubesctl saltutil.clear_cache -l quiet --out quiet > /dev/null || true
qubesctl saltutil.sync_all refresh=true -l quiet --out quiet > /dev/null || true

# Disable States (Work in Progress)
qubesctl top.disable policy-qubesbuilder saltenv=dom0 -l quiet --out quiet > /dev/null || true
qubesctl top.disable policy-qubesbuilder.absent saltenv=dom0 -l quiet --out quiet > /dev/null || true

%files
%defattr(-,root,root)
%doc LICENSE README.rst
%attr(750, root, root) %dir /srv/formulas/dom0/policy-qubesbuilder-formula
/srv/formulas/dom0/policy-qubesbuilder-formula/*

%changelog
