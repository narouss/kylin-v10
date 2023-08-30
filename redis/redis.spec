Name:           redis
Version:        7.2.0 
Release:        1%{?dist}
Summary:        redis is memory database

License:        GPLv3+
URL:            https://github.com/%{name}
Source0:        https://github.com/%{name}/%{name}/archive/%{name}-%{version}.tar.gz

#BuildRequires:  
#Requires:       

%description
The open source, in-memory data store used by millions of developers as a database, cache, streaming engine, and message broker.

%prep
%autosetup


%build
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
#%license add-license-file-here
#%doc add-docs-here
/usr/local/bin/redis-server
/usr/local/bin/redis-benchmark
/usr/local/bin/redis-cli
%{_sysconfdir}/%{name}/redis.conf

%changelog
* Mon Aug 28 2023 root
- 
