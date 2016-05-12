%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name multi_test

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.1.2
Release: 2%{?dist}
Summary: Wafter-thin gem to disable autorun of various testing libraries
Group: Development/Languages
License: MIT
URL: http://cukes.info
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:      %{?scl_prefix_ruby}ruby(release)
Requires:      %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch:     noarch
Provides:      %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
multi_test gives a uniform interface onto whatever testing library has been
loaded into a running Ruby process. It can be used to clobber autorun behaviour
from older versions of Test::Unit that automatically hook in when the user
requires them.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# Unfortunatelly tests depend heavily on Bundler
# and testing different versions of gems
#. test/all
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Makefile
%{gem_instdir}/Rakefile
# This is not the original file => makes no sense to ship it.
%exclude %{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/test

%changelog
* Wed Apr 06 2016 Pavel Valena <pvalena@redhat.com> - 0.1.2-2
- Add scl macros

* Wed Apr 06 2016 Vít Ondruch <vondruch@redhat.com> - 0.1.2-1
- Update to multi_test 0.1.2.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 18 2014 Josef Stribny <jstribny@redhat.com> - 0.1.1-1
- Initial package
