Name:           list-fs-files 
Version:        1.3.0 
Release:        1%{?dist}
Summary: List files with os.stat information       

Group: Utilities
License: Apache-2.0       
URL: https://github.com/MatthewBuchananAstley/list-fs-files         
Source0: %{name}-%{version}.tar.gz 
Packager: Matthew Buchanan Astley - <mbastley@gmail.com,matthewbuchanan@astley.nl>      

#BuildRequires:
#Requires: python3      
BuildArch: noarch

%description
List-fs-files lists files in a directory, includes os.stat information and a sha256sum in the output. The output can be saved to a zlib archive. It also reports errors if it encounters any.

%prep
%setup -q

%install

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp %{name} $RPM_BUILD_ROOT/%{_bindir}
cp list-fs-files.py $RPM_BUILD_ROOT/%{_bindir}

%files
%{_bindir}/%{name}
%{_bindir}/list-fs-files.py

%license LICENSE.md 
%doc CONTRIBUTING.md CHANGELOG.md COPYRIGHT.md README.md SECURITY.md


%changelog
* Thu Jun 19 2025 Matthew Buchanan Astley <matthewbuchanan@astley.nl, mbastley@gmail.com>
- 
