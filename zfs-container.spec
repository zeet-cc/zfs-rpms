Name:           zfs-container
Version:        ZFS_VERSION
Release:        1%{?dist}
BuildArch:      noarch

Summary:        Kernel module(s)
Group:          System Environment/Kernel
License:        CDDL
URL:            https://github.com/openzfs/zfs

Requires:       zfs = %{version}
Provides:       zfs-kmod = %{version}
Conflicts:      zfs-kmod
Conflicts:      zfs-dkms
Obsoletes:      kmod-spl
Obsoletes:      spl-kmod

%description
This package fakes OpenZFS kernel modules package as installation dependency
for OpenZFS userland tools and masks all OpenZFS systemd unit files.

%prep
exit 0

%build
exit 0

%install
install -d %{buildroot}%{_sysconfdir}/systemd/system
ln -s /dev/null %{buildroot}%{_sysconfdir}/systemd/system/zfs-import-cache.service
ln -s /dev/null %{buildroot}%{_sysconfdir}/systemd/system/zfs-import-scan.service
ln -s /dev/null %{buildroot}%{_sysconfdir}/systemd/system/zfs-import.target
ln -s /dev/null %{buildroot}%{_sysconfdir}/systemd/system/zfs-mount.service
ln -s /dev/null %{buildroot}%{_sysconfdir}/systemd/system/zfs-share.service
ln -s /dev/null %{buildroot}%{_sysconfdir}/systemd/system/zfs-volume-wait.service
ln -s /dev/null %{buildroot}%{_sysconfdir}/systemd/system/zfs-zed.service
ln -s /dev/null %{buildroot}%{_sysconfdir}/systemd/system/zfs.target

%clean
exit 0

%files
/etc/systemd/system/zfs*

%changelog
* Tue Nov 30 2021 Marcin Skarbek <rpm@skarbek.name> ZFS_VERSION-1
- Initial package
