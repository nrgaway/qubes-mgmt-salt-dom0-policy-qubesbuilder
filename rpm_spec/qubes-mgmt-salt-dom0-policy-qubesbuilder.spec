%{!?version: %define version %(cat version)}
%{!?rel: %define rel %(cat rel)}
%{!?formula_name: %define formula_name %(cat formula_name)}

Name:      qubes-mgmt-salt-dom0-policy-qubesbuilder
Version:   %{version}
Release:   %{rel}%{?dist}
Summary:   Installs or removes Qubes RPC policies in dom0 and domU to enable qubesbuilder to build in DispVMs
License:   GPL 2.0
URL:	   http://www.qubes-os.org/

Group:     System administration tools
BuildArch: noarch
Requires:  qubes-mgmt-salt-base
Requires:  qubes-mgmt-salt-config
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
# TODO:
# - Add formula path to file_roots
# - Add formula to salt top.sls
# - Add formula to pillar top.sls if contains pillar data
salt-call --local saltutil.sync_all -l quiet --out quiet > /dev/null || true

%files
%defattr(-,root,root)
%attr(750, root, root) %dir /srv/formulas/dom0/%{formula_name}
/srv/formulas/dom0/%{formula_name}/*

%changelog
