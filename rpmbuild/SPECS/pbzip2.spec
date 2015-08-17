Name:           pbzip2
Version:        1.1.12
Release:        pl%{?dist}
Summary:        PBZIP2 is a parallel implementation of the bzip2 block-sorting file compressor that uses pthreads and achieves near-linear speedup on SMP machines.

Group:          UTILS
License:        GPLv2+
URL:            http://compression.ca/pbzip2/
Packager: 	Karpychev Evgeniy <shprot@gmail.com>
Source0:        http://compression.ca/pbzip2/pbzip2-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, bzip2-devel

%description
PBZIP2 is a parallel implementation of the bzip2 block- sorting file
compressor that uses pthreads and achieves near-linear speedup on SMP
machines.

%prep
%setup
%{__perl} -npi -e "s|.PREFIX./man|(PREFIX)/share/man|g;" Makefile
%{__perl} -npi -e "s|..PREFIX./bin/pbzip2( ..PREFIX./bin/pbunzip2)|%{_bindir}/pbzip2 \1|g;" Makefile
%{__perl} -npi -e "s|..PREFIX./bin/pbzip2( ..PREFIX./bin/pbzcat)|%{_bindir}/pbzip2 \1|g;" Makefile

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install PREFIX=%{buildroot}%{_prefix}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README
%doc %{_mandir}/man1/pbzip2.1*
%{_bindir}/pbzip2
%{_bindir}/pbunzip2
%{_bindir}/pbzcat


%changelog
* Mon Aug  17 2015 Karpychev Evgeniy aka ShPRoT <shprot@gmail.com> - 1.1.12
- Complied for Centos 7
