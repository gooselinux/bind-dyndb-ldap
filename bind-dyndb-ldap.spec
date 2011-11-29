Name:           bind-dyndb-ldap
Version:        0.1.0
Release:        0.9.b%{?dist}
Summary:        LDAP back-end plug-in for BIND

Group:          System Environment/Libraries
License:        GPLv2+
URL:            https://fedorahosted.org/bind-dyndb-ldap
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#   git clone git://git.fedorahosted.org/git/bind-dyndb-ldap.git
#   cd bind-dyndb-ldap/
#   git checkout 597a7fe80b8486aacbaf8eeafea4da5cb6fd3656
#   autoreconf -fi
#   ./configure
#   make dist
Source0:        https://fedorahosted.org/released/%{name}/%{name}-%{version}b.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  bind-devel >= 32:9.6.1-0.3.b1
BuildRequires:  krb5-devel
BuildRequires:  openldap-devel

Requires:       bind >= 32:9.6.1-0.3.b1

%description
This package provides an LDAP back-end plug-in for BIND. It features
support for dynamic updates and internal caching, to lift the load
off of your LDAP server.


%prep
%setup -q -n %{name}-%{version}b


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

# Remove unwanted files
rm %{buildroot}%{_libdir}/bind/ldap.la
rm -r %{buildroot}%{_datadir}/doc/%{name}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README COPYING doc/{example.ldif,schema}
%{_libdir}/bind/ldap.so


%changelog
* Wed Mar 24 2010 Martin Nagy <mnagy@redhat.com> - 0.1.0-0.9.b
- update to the latest upstream release
- Resolves: #556554

* Thu Jan 28 2010 Adam Tkac <atkac redhat com> - 0.1.0-0.8.a1.20091210git
- rebuild against updated bind package

* Tue Dec 15 2009 Adam Tkac <atkac redhat com> - 0.1.0-0.7.a1.20091210git
- rebuild against new bind

* Thu Dec 10 2009 Martin Nagy <mnagy@redhat.com> - 0.1.0-0.6.a1.20091210git
- update to the latest git snapshot
- change upstream URL, project moved to fedorahosted
- change license to GPL version 2 or later
- add epoch to versioned requires
- add krb5-devel to the list of build requires

* Tue Dec 01 2009 Adam Tkac <atkac redhat com> - 0.1.0-0.5.a1
- rebuild against new bind

* Thu Nov 26 2009 Adam Tkac <atkac redhat com> - 0.1.0-0.4.a1
- rebuild against new bind

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-0.3.a1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 19 2009 Caolán McNamara <caolanm@redhat.com> - 0.1.0-0.2.a1
- rebuild for dependencies

* Sun May 03 2009 Martin Nagy <mnagy@redhat.com> - 0.1.0-0.1.a1
- initial packaging
