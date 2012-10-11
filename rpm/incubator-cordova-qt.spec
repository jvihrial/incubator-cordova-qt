Name:		incubator-cordova-qt	
Version:	%{ver_maj}.%{ver_min}.%{ver_pat}
Release:	1%{?dist}
Summary:	PhoneGap harness for Qt4 and Qt5 systems

Group:		Applications/Internet
License:	Apache 2.0
URL:		https://github.com/apache/incubator-cordova-qt
Source0:	%{name}-%{version}.tar.gz	

BuildRequires:	pkgconfig(QtCore)

Provides:	html5

%description
Cordova/Qt is the Qt port of the Apache Cordova project. It should compile on any platform which is compatible with Qt and Qt Mobility.

%prep
%setup -q -n %{name}-%{version}


%build
%configure
qmake -r CONFIG+=mer
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc



%changelog

