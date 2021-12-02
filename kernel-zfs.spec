Name:           kernel-zfs-ZFS_VERSION
Version:        KERNEL_VERSION
Release:        KERNEL_RELEASE_SHORT%{?dist}
BuildArch:      noarch

Summary:        Kernel module(s)
Group:          System Environment/Kernel
License:        CDDL
URL:            https://github.com/openzfs/zfs

Requires:       zfs-kmod = ZFS_VERSION
Requires:       kernel-core = %{version}
Conflicts:      kernel-core > %{version}
Conflicts:      kernel-headers > %{version}
Conflicts:      zfs-dkms

%description
Meta package that prevents Kernel updates without corresponding OpenZFS kmod package.

%prep
exit 0

%build
exit 0

%install
exit 0

%clean
exit 0

%files

%changelog
* Tue Nov 30 2021 Marcin Skarbek <rpm@skarbek.name> KERNEL_VERSION-KERNEL_RELEASE_SHORT
- Initial package
