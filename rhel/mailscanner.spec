%define name    MailScanner
%define version VersionNumberHere
%define release ReleaseNumberHere

# make the rpm backwards compatible
%define _source_payload w0.gzdio
%define _binary_payload w0.gzdio

Name:        %{name}
Version:     %{version}
Release:     %{release}
Summary:     Email Gateway Virus Scanner with Malware, Phishing, and Spam Detection
Group:       System Environment/Daemons
License:     GPLv2
Vendor:      MailScanner Community
Packager:    Jerry Benton <mailscanner@mailborder.com>
URL:         http://www.mailscanner.info
Requires:     perl >= 5.005
Provides:	  perl(MailScanner), perl(MailScanner::Antiword), perl(MailScanner::BinHex), perl(MailScanner::Config), perl(MailScanner::ConfigSQL), perl(MailScanner::CustomConfig), perl(MailScanner::FileInto), perl(MailScanner::GenericSpam), perl(MailScanner::LinksDump), perl(MailScanner::Lock), perl(MailScanner::Log), perl(MailScanner::Mail), perl(MailScanner::MCP), perl(MailScanner::MCPMessage), perl(MailScanner::Message), perl(MailScanner::MessageBatch), perl(MailScanner::Quarantine), perl(MailScanner::Queue), perl(MailScanner::RBLs), perl(MailScanner::MCPMessage), perl(MailScanner::Message), perl(MailScanner::MCP), perl(MailScanner::SA), perl(MailScanner::Sendmail), perl(MailScanner::SMDiskStore), perl(MailScanner::SweepContent), perl(MailScanner::SweepOther), perl(MailScanner::SweepViruses), perl(MailScanner::TNEF), perl(MailScanner::Unzip), perl(MailScanner::WorkArea), perl(MIME::Parser::MailScanner)
Source:      %{name}-%{version}.tgz
BuildRoot:   %{_tmppath}/%{name}-root
BuildArchitectures: noarch
AutoReqProv: yes


%description
MailScanner is a freely distributable email gateway virus scanner with
malware, phishing, and spam detection. It supports Postfix, sendmail, 
ZMailer, Qmail or Exim mail transport agents and numerous open source 
and commercial virus scanning engines for virus scanning.  It will also 
selectively filter the content of email messages to protect users from 
offensive content such as pornographic spam. It also has features which 
protect it against Denial Of Service attacks.

After installation, you must install one of the supported open source or
commercial antivirus packages if not installed using the MailScanner
installation script.

This has been tested on Red Hat Linux, but should work on other RPM 
based Linux distributions.

%prep
%setup

%build

%install

mkdir -p $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}/usr/sbin/
mkdir -p ${RPM_BUILD_ROOT}/etc/MailScanner/{conf.d,rules,mcp}
mkdir -p ${RPM_BUILD_ROOT}/etc/{cron.hourly,cron.daily}
mkdir -p ${RPM_BUILD_ROOT}/usr/share/MailScanner/reports/{hu,de,se,ca,cy+en,pt_br,fr,es,en,cz,it,dk,nl,ro,sk}
mkdir -p ${RPM_BUILD_ROOT}/usr/share/MailScanner/perl/{MailScanner,custom}
mkdir -p ${RPM_BUILD_ROOT}/var/{lib/MailScanner/wrapper,lib/MailScanner/init}
mkdir -p ${RPM_BUILD_ROOT}/var/spool/MailScanner/{archive,incoming,quarantine}

### etc
install etc/cron.daily/mailscanner ${RPM_BUILD_ROOT}/etc/cron.daily/
install etc/cron.hourly/mailscanner ${RPM_BUILD_ROOT}/etc/cron.hourly/

### etc/MailScanenr
install etc/MailScanner/conf.d/README ${RPM_BUILD_ROOT}/etc/MailScanner/conf.d/

while read f
do
  install etc/MailScanner/mcp/$f ${RPM_BUILD_ROOT}/etc/MailScanner/mcp/
done << EOF
10_example.cf
mcp.spamassassin.conf
EOF

while read f 
do
  install etc/MailScanner/rules/$f ${RPM_BUILD_ROOT}/etc/MailScanner/rules
done << EOF
bounce.rules
EXAMPLES
max.message.size.rules
README
spam.whitelist.rules
EOF

while read f 
do
  install etc/MailScanner/$f ${RPM_BUILD_ROOT}/etc/MailScanner/
done << EOF
archives.filename.rules.conf
archives.filetype.rules.conf
country.domains.conf
defaults
filename.rules.conf
filetype.rules.conf
MailScanner.conf
phishing.bad.sites.conf
phishing.safe.sites.conf
spam.lists.conf
spamassassin.conf
virus.scanners.conf
EOF

### usr/sbin

install usr/sbin/MailScanner        				${RPM_BUILD_ROOT}/usr/sbin/MailScanner
install usr/sbin/ms-check      						${RPM_BUILD_ROOT}/usr/sbin/ms-check
install usr/sbin/ms-clean-quarantine				${RPM_BUILD_ROOT}/usr/sbin/ms-clean-quarantine
install usr/sbin/ms-create-locks 					${RPM_BUILD_ROOT}/usr/sbin/ms-create-locks
install usr/sbin/ms-cron            				${RPM_BUILD_ROOT}/usr/sbin/ms-cron
install usr/sbin/ms-d2mbox             				${RPM_BUILD_ROOT}/usr/sbin/ms-d2mbox
install usr/sbin/ms-df2mbox            				${RPM_BUILD_ROOT}/usr/sbin/ms-df2mbox
install usr/sbin/ms-msg-alert 						${RPM_BUILD_ROOT}/usr/sbin/ms-msg-alert
install usr/sbin/ms-peek         					${RPM_BUILD_ROOT}/usr/sbin/ms-peek
install usr/sbin/ms-perl-check     					${RPM_BUILD_ROOT}/usr/sbin/ms-perl-check
install usr/sbin/ms-sa-cache     					${RPM_BUILD_ROOT}/usr/sbin/ms-sa-cache
install usr/sbin/ms-update-bad-emails 				${RPM_BUILD_ROOT}/usr/sbin/ms-update-bad-emails
install usr/sbin/ms-update-bad-sites 				${RPM_BUILD_ROOT}/usr/sbin/ms-update-bad-sites
install usr/sbin/ms-update-sa 						${RPM_BUILD_ROOT}/usr/sbin/ms-update-sa
install usr/sbin/ms-update-safe-sites 				${RPM_BUILD_ROOT}/usr/sbin/ms-update-safe-sites
install usr/sbin/ms-update-vs 						${RPM_BUILD_ROOT}/usr/sbin/ms-update-vs
install usr/sbin/ms-upgrade-conf 					${RPM_BUILD_ROOT}/usr/sbin/ms-upgrade-conf


### usr/share/MailScanner

for lang in ca cy+en cz de dk en es fr hu it nl pt_br ro se sk
do
  while read f 
  do
    install usr/share/MailScanner/reports/$lang/$f ${RPM_BUILD_ROOT}/usr/share/MailScanner/reports/$lang
  done << EOF
deleted.content.message.txt
deleted.filename.message.txt
deleted.size.message.txt
deleted.virus.message.txt
disinfected.report.txt
inline.sig.html
inline.sig.txt
inline.spam.warning.txt
inline.warning.html
inline.warning.txt
languages.conf
languages.conf.strings
recipient.mcp.report.txt
recipient.spam.report.txt
rejection.report.txt
sender.content.report.txt
sender.error.report.txt
sender.filename.report.txt
sender.mcp.report.txt
sender.size.report.txt
sender.spam.rbl.report.txt
sender.spam.report.txt
sender.spam.sa.report.txt
sender.virus.report.txt
stored.content.message.txt
stored.filename.message.txt
stored.size.message.txt
stored.virus.message.txt
EOF
done

install usr/share/MailScanner/perl/MailScanner.pm ${RPM_BUILD_ROOT}/usr/share/MailScanner/perl/

while read f 
do
  install usr/share/MailScanner/perl/MailScanner/$f ${RPM_BUILD_ROOT}/usr/share/MailScanner/perl/MailScanner/
done << EOF
Antiword.pm
Config.pm
ConfigDefs.pl
ConfigSQL.pm
CustomConfig.pm
Exim.pm
EximDiskStore.pm
FileInto.pm
GenericSpam.pm
LinksDump.pm
Lock.pm
Log.pm
Mail.pm
MCP.pm
MCPMessage.pm
Message.pm
MessageBatch.pm
PFDiskStore.pm
Postfix.pm
Qmail.pm
QMDiskStore.pm
Quarantine.pm
Queue.pm
RBLs.pm
SA.pm
Sendmail.pm
SMDiskStore.pm
SweepContent.pm
SweepOther.pm
SweepViruses.pm
SystemDefs.pm
TNEF.pm
Unzip.pm
WorkArea.pm
ZMailer.pm
ZMDiskStore.pm
EOF

while read f 
do
  install usr/share/MailScanner/perl/custom/$f ${RPM_BUILD_ROOT}/usr/share/MailScanner/perl/custom/
done << EOF
CustomAction.pm 
GenericSpamScanner.pm
LastSpam.pm
MyExample.pm
Ruleset-from-Function.pm
SpamWhitelist.pm
ZMRouterDirHash.pm
EOF

### var/lib/MailScanner

install var/lib/MailScanner/init/mailscanner ${RPM_BUILD_ROOT}/var/lib/MailScanner/init/

while read f 
do
  install var/lib/MailScanner/wrapper/$f ${RPM_BUILD_ROOT}/var/lib/MailScanner/wrapper
done << EOF
avg-autoupdate
avg-wrapper
bitdefender-wrapper
bitdefender-autoupdate
clamav-autoupdate
clamav-wrapper
f-secure-wrapper
f-secure-autoupdate
generic-autoupdate
generic-wrapper
sophos-autoupdate
sophos-wrapper
EOF

%clean
rm -rf ${RPM_BUILD_ROOT}

%pre

%post

# group for users to run under
if ! getent group mtagroup >/dev/null 2>&1; then
	groupadd -f mtagroup >/dev/null 2>&1
fi

# check for common users and add to the mtagroup
if id -u clam >/dev/null 2>&1; then
	usermod -a -G mtagroup clam >/dev/null 2>&1
fi

if id -u clamav >/dev/null 2>&1; then
	usermod -a -G mtagroup clamav >/dev/null 2>&1
fi

if id -u clamscan >/dev/null 2>&1; then
	usermod -a -G mtagroup clamscan >/dev/null 2>&1
fi

if id -u vscan >/dev/null 2>&1; then
	usermod -a -G mtagroup vscan >/dev/null 2>&1
fi

if id -u sophosav >/dev/null 2>&1; then
	usermod -a -G mtagroup sophosav >/dev/null 2>&1
fi

if id -u postfix >/dev/null 2>&1; then
	usermod -a -G mtagroup postfix >/dev/null 2>&1
fi

if id -u mail >/dev/null 2>&1; then
	usermod -a -G mtagroup mail >/dev/null 2>&1
fi

if [ ! -d "/var/spool/MailScanner/archive" ]; then
	mkdir -p /var/spool/MailScanner/archive
fi

if [ ! -d "/var/spool/MailScanner/incoming" ]; then
	mkdir -p /var/spool/MailScanner/incoming
fi

if [ ! -d "/var/spool/MailScanner/quarantine" ]; then
	mkdir -p /var/spool/MailScanner/quarantine
fi

# remove old link if present
if [ -L '/etc/spamassassin/mailscanner.cf' ]; then
	rm -f /etc/spamassassin/mailscanner.cf
fi

if [ -L '/etc/spamassassin/MailScanner.cf' ]; then
	rm -f /etc/spamassassin/MailScanner.cf
fi

# create symlink for spamasassin
if [ -d '/etc/spamassassin' -a ! -L '/etc/spamassassin/mailscanner.cf' -a -f '/etc/MailScanner/spamassassin.conf' -a ! -f '/etc/spamassassin/mailscanner.cf' ]; then
	ln -s /etc/MailScanner/spamassassin.conf /etc/spamassassin/mailscanner.cf 
fi

# fix the clamav wrapper if the user does not exist
if [ -d '/etc/clamav' ]; then

	DISTROCAVUSER='ClamUser="clamav"';
	DISTROCAVGRP='ClamGroup="clamav"';
	
	# check for common users and add to the mtagroup
	if id -u clam >/dev/null 2>&1; then
		CAVUSR='ClamUser="clam"';
	fi

	if id -u clamav >/dev/null 2>&1; then
		CAVUSR='ClamUser="clamav"';
	fi
	
	if id -u clamscan >/dev/null 2>&1; then
		CAVUSR='ClamUser="clamscan"';
	fi

	if getent group clamav >/dev/null 2>&1; then
		CAVGRP='ClamGroup="clamav"';
	fi

	if getent group clam >/dev/null 2>&1; then
		CAVGRP='ClamGroup="clam"';
	fi
	
	if getent group clamscan >/dev/null 2>&1; then
		CAVGRP='ClamGroup="clamscan"';
	fi
	
	if [ -f '/var/lib/MailScanner/wrapper/clamav-wrapper' ]; then
		sed -i "s/${DISTROCAVUSER}/${CAVUSR}/g" /var/lib/MailScanner/wrapper/clamav-wrapper
		sed -i "s/${DISTROCAVGRP}/${CAVGRP}/g" /var/lib/MailScanner/wrapper/clamav-wrapper
	fi
	
	# fix old style clamav Monitors if preset in old mailscanner.conf
	CAVOLD='^Monitors for ClamAV Updates.*';
	CAVNEW='Monitors for ClamAV Updates = \/usr\/local\/share\/clamav\/\*\.cld \/usr\/local\/share\/clamav\/\*\.cvd \/var\/lib\/clamav\/\*\.inc\/\* \/var\/lib\/clamav\/\*\.\?db \/var\/lib\/clamav\/\*\.cvd';
	if [ -f '/etc/MailScanner/MailScanner.conf' ]; then
		sed -i "s/${CAVOLD}/${CAVNEW}/g" /etc/MailScanner/MailScanner.conf
	fi

fi

# postfix fix
if [ -f "/etc/postfix/master.cf" ]; then
	sed -i "s/pickup    unix/pickup    fifo/g" /etc/postfix/master.cf
	sed -i "s/qmgr      unix/qmgr      fifo/g" /etc/postfix/master.cf
fi

# update web bug link
OLD="^Web Bug Replacement.*";
NEW="Web Bug Replacement = https\:\/\/s3\.amazonaws\.com\/msv5\/images\/spacer\.gif";
if [ -f '/etc/MailScanner/MailScanner.conf' ]; then
	sed -i "s/${OLD}/${NEW}/g" /etc/MailScanner/MailScanner.conf
fi

# fix reports directory
OLDTHING='\/etc\/MailScanner\/reports';
NEWTHING='\/usr\/share\/MailScanner\/reports';
if [ -f '/etc/MailScanner/MailScanner.conf' ]; then
	sed -i "s/${OLDTHING}/${NEWTHING}/g" /etc/MailScanner/MailScanner.conf
fi

# fix custom functions directory
OLDTHING='\/usr\/share\/MailScanner\/MailScanner\/CustomFunctions';
NEWTHING='\/usr\/share\/MailScanner\/perl\/custom';
if [ -f '/etc/MailScanner/MailScanner.conf' ]; then
	sed -i "s/${OLDTHING}/${NEWTHING}/g" /etc/MailScanner/MailScanner.conf
fi

# we need to ensure that the old spam list names do not get used
OLD="^Spam List = .*";
NEW="Spam List = # see the new spam.lists.conf for options";
if [ -f '/etc/MailScanner/MailScanner.conf' ]; then
	sed -i "s/${OLD}/${NEW}/g" /etc/MailScanner/MailScanner.conf
fi

# softlink for custom functions
if [ -d '/usr/share/MailScanner/perl/custom' -a ! -L '/etc/MailScanner/custom' ]; then
	ln -s /usr/share/MailScanner/perl/custom/ /etc/MailScanner/custom
fi

# create init.d symlink
if [ -d '/etc/rc.d/init.d' -a ! -L '/etc/rc.d/init.d/ms' -a -f '/var/lib/mailscanner/init/ms-init' ]; then
	ln -s /var/lib/mailscanner/init/ms-init /etc/rc.d/init.d/ms
fi

# Sort out the rc.d directories
chkconfig --add mailscanner

echo
echo
echo To configure MailScanner, edit the following files:
echo
echo /etc/MailScanner/defaults
echo /etc/MailScanner/MailScanner.conf
echo
echo
echo To activate MailScanner run the following commands:
echo
echo    chkconfig mailscanner on
echo    service mailscanner start
echo
echo

%preun
if [ $1 = 0 ]; then
    # We are being deleted, not upgraded
    service mailscanner stop >/dev/null 2>&1
    chkconfig mailscanner off
    chkconfig --del mailscanner
fi
exit 0

%postun
# delete old ms files if this is an upgrade
if [ -d "/usr/lib/MailScanner" ]; then
	rm -rf /usr/lib/MailScanner
fi
exit 0

%files
%defattr (644,root,root)
%attr(755,root,root) %dir /etc/MailScanner
%attr(755,root,root) %dir /etc/MailScanner/rules
%attr(755,root,root) %dir /etc/MailScanner/mcp
%attr(755,root,root) %dir /etc/MailScanner/conf.d
%attr(755,root,root) %dir /var/lib/MailScanner/wrapper
%attr(755,root,root) %dir /var/lib/MailScanner/init
%attr(755,root,root) %dir /var/spool/MailScanner/archive
%attr(755,root,root) %dir /var/spool/MailScanner/incoming
%attr(755,root,root) %dir /var/spool/MailScanner/quarantine
%attr(755,root,root) %dir /usr/share/MailScanner
%attr(755,root,root) %dir /usr/share/MailScanner/perl
%attr(755,root,root) %dir /usr/share/MailScanner/perl/custom
%attr(755,root,root) %dir /usr/share/MailScanner/perl/MailScanner
%attr(755,root,root) %dir /usr/share/MailScanner/reports

%attr(755,root,root) /usr/sbin/MailScanner
%attr(755,root,root) /usr/sbin/ms-check
%attr(755,root,root) /usr/sbin/ms-clean-quarantine
%attr(755,root,root) /usr/sbin/ms-create-locks
%attr(755,root,root) /usr/sbin/ms-cron
%attr(755,root,root) /usr/sbin/ms-d2mbox
%attr(755,root,root) /usr/sbin/ms-df2mbox
%attr(755,root,root) /usr/sbin/ms-msg-alert
%attr(755,root,root) /usr/sbin/ms-peek
%attr(755,root,root) /usr/sbin/ms-perl-check
%attr(755,root,root) /usr/sbin/ms-sa-cache
%attr(755,root,root) /usr/sbin/ms-update-bad-emails
%attr(755,root,root) /usr/sbin/ms-update-bad-sites
%attr(755,root,root) /usr/sbin/ms-update-sa
%attr(755,root,root) /usr/sbin/ms-update-safe-sites
%attr(755,root,root) /usr/sbin/ms-update-vs
%attr(755,root,root) /usr/sbin/ms-upgrade-conf

%attr(755,root,root) /var/lib/mailscanner/init/ms-init

%attr(755,root,root) /var/lib/MailScanner/wrapper/avg-autoupdate
%attr(755,root,root) /var/lib/MailScanner/wrapper/avg-wrapper
%attr(755,root,root) /var/lib/MailScanner/wrapper/bitdefender-autoupdate
%attr(755,root,root) /var/lib/MailScanner/wrapper/bitdefender-wrapper
%attr(755,root,root) /var/lib/MailScanner/wrapper/clamav-autoupdate
%attr(755,root,root) /var/lib/MailScanner/wrapper/clamav-wrapper
%attr(755,root,root) /var/lib/MailScanner/wrapper/f-secure-autoupdate
%attr(755,root,root) /var/lib/MailScanner/wrapper/f-secure-wrapper
%attr(755,root,root) /var/lib/MailScanner/wrapper/generic-autoupdate
%attr(755,root,root) /var/lib/MailScanner/wrapper/generic-wrapper
%attr(755,root,root) /var/lib/MailScanner/wrapper/sophos-autoupdate
%attr(755,root,root) /var/lib/MailScanner/wrapper/sophos-wrapper

%config(noreplace) /usr/share/MailScanner/perl/custom/CustomAction.pm
%config(noreplace) /usr/share/MailScanner/perl/custom/GenericSpamScanner.pm
%config(noreplace) /usr/share/MailScanner/perl/custom/LastSpam.pm
%config(noreplace) /usr/share/MailScanner/perl/custom/MyExample.pm
%config(noreplace) /usr/share/MailScanner/perl/custom/Ruleset-from-Function.pm
%config(noreplace) /usr/share/MailScanner/perl/custom/SpamWhitelist.pm
%config(noreplace) /usr/share/MailScanner/perl/custom/ZMRouterDirHash.pm

%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/Antiword.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/Config.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/ConfigDefs.pl
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/ConfigSQL.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/CustomConfig.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/Exim.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/EximDiskStore.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/FileInto.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/GenericSpam.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/LinksDump.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/Lock.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/Log.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/Mail.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/MCP.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/MCPMessage.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/Message.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/MessageBatch.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/PFDiskStore.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/Postfix.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/Qmail.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/QMDiskStore.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/Quarantine.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/Queue.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/RBLs.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/SA.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/Sendmail.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/SMDiskStore.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/SweepContent.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/SweepOther.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/SweepViruses.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/SystemDefs.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/TNEF.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/Unzip.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/WorkArea.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/ZMailer.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/ZMDiskStore.pm

%attr(755,root,root) /etc/cron.daily/mailscanner
%attr(755,root,root) /etc/cron.hourly/mailscanner

%config(noreplace) /etc/MailScanner/archives.filename.rules.conf
%config(noreplace) /etc/MailScanner/archives.filetype.rules.conf
%attr(644,root,root) /etc/MailScanner/country.domains.conf
%config(noreplace) /etc/MailScanner/defaults
%config(noreplace) /etc/MailScanner/filename.rules.conf
%config(noreplace) /etc/MailScanner/filetype.rules.conf
%config(noreplace) /etc/MailScanner/MailScanner.conf
%attr(644,root,root) /etc/MailScanner/phishing.safe.sites.conf
%attr(644,root,root) /etc/MailScanner/phishing.bad.sites.conf
%attr(644,root,root) /etc/MailScanner/spam.lists.conf
%config(noreplace) /etc/MailScanner/spamassassin.conf
%attr(644,root,root) /etc/MailScanner/virus.scanners.conf

%attr(644,root,root) /etc/MailScanner/conf.d/README

%config(noreplace) /etc/MailScanner/mcp/10_example.cf
%config(noreplace) /etc/MailScanner/mcp/mcp.spamassassin.conf

%config(noreplace) /etc/MailScanner/rules/bounce.rules
%attr(644,root,root) /etc/MailScanner/rules/EXAMPLES
%config(noreplace) /etc/MailScanner/rules/max.message.size.rules
%attr(644,root,root) /etc/MailScanner/rules/README
%config(noreplace) /etc/MailScanner/rules/spam.whitelist.rules

%config(noreplace) /usr/share/MailScanner/reports/en/deleted.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/en/stored.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/en/sender.content.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en/deleted.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/en/deleted.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/en/deleted.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/en/disinfected.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en/inline.sig.html
%config(noreplace) /usr/share/MailScanner/reports/en/inline.sig.txt
%config(noreplace) /usr/share/MailScanner/reports/en/inline.spam.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/en/inline.warning.html
%config(noreplace) /usr/share/MailScanner/reports/en/inline.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/en/languages.conf
%config(noreplace) /usr/share/MailScanner/reports/en/languages.conf.strings
%config(noreplace) /usr/share/MailScanner/reports/en/recipient.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en/recipient.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en/rejection.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en/sender.error.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en/sender.filename.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en/sender.spam.rbl.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en/sender.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en/sender.spam.sa.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en/sender.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en/sender.size.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en/sender.virus.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en/stored.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/en/stored.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/en/stored.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/deleted.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/stored.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/sender.content.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/deleted.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/deleted.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/deleted.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/disinfected.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/inline.sig.html
%config(noreplace) /usr/share/MailScanner/reports/cy+en/inline.sig.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/inline.spam.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/inline.warning.html
%config(noreplace) /usr/share/MailScanner/reports/cy+en/inline.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/languages.conf
%config(noreplace) /usr/share/MailScanner/reports/cy+en/languages.conf.strings
%config(noreplace) /usr/share/MailScanner/reports/cy+en/recipient.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/recipient.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/rejection.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/sender.error.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/sender.filename.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/sender.spam.rbl.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/sender.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/sender.spam.sa.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/sender.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/sender.size.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/sender.virus.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/stored.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/stored.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/stored.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/de/deleted.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/de/stored.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/de/sender.content.report.txt
%config(noreplace) /usr/share/MailScanner/reports/de/deleted.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/de/deleted.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/de/deleted.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/de/disinfected.report.txt
%config(noreplace) /usr/share/MailScanner/reports/de/inline.sig.html
%config(noreplace) /usr/share/MailScanner/reports/de/inline.sig.txt
%config(noreplace) /usr/share/MailScanner/reports/de/inline.spam.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/de/inline.warning.html
%config(noreplace) /usr/share/MailScanner/reports/de/inline.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/de/languages.conf
%config(noreplace) /usr/share/MailScanner/reports/de/languages.conf.strings
%config(noreplace) /usr/share/MailScanner/reports/de/recipient.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/de/recipient.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/de/rejection.report.txt
%config(noreplace) /usr/share/MailScanner/reports/de/sender.error.report.txt
%config(noreplace) /usr/share/MailScanner/reports/de/sender.filename.report.txt
%config(noreplace) /usr/share/MailScanner/reports/de/sender.spam.rbl.report.txt
%config(noreplace) /usr/share/MailScanner/reports/de/sender.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/de/sender.spam.sa.report.txt
%config(noreplace) /usr/share/MailScanner/reports/de/sender.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/de/sender.size.report.txt
%config(noreplace) /usr/share/MailScanner/reports/de/sender.virus.report.txt
%config(noreplace) /usr/share/MailScanner/reports/de/stored.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/de/stored.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/de/stored.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/deleted.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/stored.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/sender.content.report.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/deleted.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/deleted.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/deleted.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/disinfected.report.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/inline.sig.html
%config(noreplace) /usr/share/MailScanner/reports/fr/inline.sig.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/inline.spam.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/inline.warning.html
%config(noreplace) /usr/share/MailScanner/reports/fr/inline.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/languages.conf
%config(noreplace) /usr/share/MailScanner/reports/fr/languages.conf.strings
%config(noreplace) /usr/share/MailScanner/reports/fr/recipient.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/recipient.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/rejection.report.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/sender.error.report.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/sender.filename.report.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/sender.spam.rbl.report.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/sender.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/sender.spam.sa.report.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/sender.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/sender.size.report.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/sender.virus.report.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/stored.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/stored.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/stored.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/es/deleted.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/es/stored.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/es/sender.content.report.txt
%config(noreplace) /usr/share/MailScanner/reports/es/deleted.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/es/deleted.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/es/deleted.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/es/disinfected.report.txt
%config(noreplace) /usr/share/MailScanner/reports/es/inline.sig.html
%config(noreplace) /usr/share/MailScanner/reports/es/inline.sig.txt
%config(noreplace) /usr/share/MailScanner/reports/es/inline.spam.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/es/inline.warning.html
%config(noreplace) /usr/share/MailScanner/reports/es/inline.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/es/languages.conf
%config(noreplace) /usr/share/MailScanner/reports/es/languages.conf.strings
%config(noreplace) /usr/share/MailScanner/reports/es/recipient.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/es/recipient.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/es/rejection.report.txt
%config(noreplace) /usr/share/MailScanner/reports/es/sender.error.report.txt
%config(noreplace) /usr/share/MailScanner/reports/es/sender.filename.report.txt
%config(noreplace) /usr/share/MailScanner/reports/es/sender.spam.rbl.report.txt
%config(noreplace) /usr/share/MailScanner/reports/es/sender.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/es/sender.spam.sa.report.txt
%config(noreplace) /usr/share/MailScanner/reports/es/sender.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/es/sender.size.report.txt
%config(noreplace) /usr/share/MailScanner/reports/es/sender.virus.report.txt
%config(noreplace) /usr/share/MailScanner/reports/es/stored.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/es/stored.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/es/stored.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/deleted.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/stored.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/sender.content.report.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/deleted.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/deleted.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/deleted.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/disinfected.report.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/inline.sig.html
%config(noreplace) /usr/share/MailScanner/reports/nl/inline.sig.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/inline.spam.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/inline.warning.html
%config(noreplace) /usr/share/MailScanner/reports/nl/inline.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/languages.conf
%config(noreplace) /usr/share/MailScanner/reports/nl/languages.conf.strings
%config(noreplace) /usr/share/MailScanner/reports/nl/recipient.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/recipient.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/rejection.report.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/sender.error.report.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/sender.filename.report.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/sender.spam.rbl.report.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/sender.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/sender.spam.sa.report.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/sender.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/sender.size.report.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/sender.virus.report.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/stored.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/stored.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/stored.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/deleted.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/stored.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/sender.content.report.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/deleted.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/deleted.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/deleted.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/disinfected.report.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/inline.sig.html
%config(noreplace) /usr/share/MailScanner/reports/pt_br/inline.sig.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/inline.spam.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/inline.warning.html
%config(noreplace) /usr/share/MailScanner/reports/pt_br/inline.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/languages.conf
%config(noreplace) /usr/share/MailScanner/reports/pt_br/languages.conf.strings
%config(noreplace) /usr/share/MailScanner/reports/pt_br/recipient.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/recipient.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/rejection.report.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/sender.error.report.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/sender.filename.report.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/sender.spam.rbl.report.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/sender.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/sender.spam.sa.report.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/sender.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/sender.size.report.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/sender.virus.report.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/stored.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/stored.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/stored.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/deleted.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/stored.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/sender.content.report.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/deleted.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/deleted.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/deleted.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/disinfected.report.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/inline.sig.html
%config(noreplace) /usr/share/MailScanner/reports/sk/inline.sig.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/inline.spam.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/inline.warning.html
%config(noreplace) /usr/share/MailScanner/reports/sk/inline.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/languages.conf
%config(noreplace) /usr/share/MailScanner/reports/sk/languages.conf.strings
%config(noreplace) /usr/share/MailScanner/reports/sk/recipient.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/recipient.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/rejection.report.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/sender.error.report.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/sender.filename.report.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/sender.spam.rbl.report.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/sender.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/sender.spam.sa.report.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/sender.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/sender.size.report.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/sender.virus.report.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/stored.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/stored.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/stored.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/deleted.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/stored.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/sender.content.report.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/deleted.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/deleted.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/deleted.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/disinfected.report.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/inline.sig.html
%config(noreplace) /usr/share/MailScanner/reports/dk/inline.sig.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/inline.spam.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/inline.warning.html
%config(noreplace) /usr/share/MailScanner/reports/dk/inline.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/languages.conf
%config(noreplace) /usr/share/MailScanner/reports/dk/languages.conf.strings
%config(noreplace) /usr/share/MailScanner/reports/dk/recipient.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/recipient.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/rejection.report.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/sender.error.report.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/sender.filename.report.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/sender.spam.rbl.report.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/sender.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/sender.spam.sa.report.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/sender.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/sender.size.report.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/sender.virus.report.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/stored.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/stored.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/stored.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/it/deleted.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/it/stored.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/it/sender.content.report.txt
%config(noreplace) /usr/share/MailScanner/reports/it/deleted.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/it/deleted.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/it/deleted.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/it/disinfected.report.txt
%config(noreplace) /usr/share/MailScanner/reports/it/inline.sig.html
%config(noreplace) /usr/share/MailScanner/reports/it/inline.sig.txt
%config(noreplace) /usr/share/MailScanner/reports/it/inline.spam.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/it/inline.warning.html
%config(noreplace) /usr/share/MailScanner/reports/it/inline.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/it/languages.conf
%config(noreplace) /usr/share/MailScanner/reports/it/languages.conf.strings
%config(noreplace) /usr/share/MailScanner/reports/it/recipient.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/it/recipient.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/it/rejection.report.txt
%config(noreplace) /usr/share/MailScanner/reports/it/sender.error.report.txt
%config(noreplace) /usr/share/MailScanner/reports/it/sender.filename.report.txt
%config(noreplace) /usr/share/MailScanner/reports/it/sender.spam.rbl.report.txt
%config(noreplace) /usr/share/MailScanner/reports/it/sender.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/it/sender.spam.sa.report.txt
%config(noreplace) /usr/share/MailScanner/reports/it/sender.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/it/sender.size.report.txt
%config(noreplace) /usr/share/MailScanner/reports/it/sender.virus.report.txt
%config(noreplace) /usr/share/MailScanner/reports/it/stored.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/it/stored.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/it/stored.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/deleted.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/stored.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/sender.content.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/deleted.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/deleted.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/deleted.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/disinfected.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/inline.sig.html
%config(noreplace) /usr/share/MailScanner/reports/ro/inline.sig.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/inline.spam.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/inline.warning.html
%config(noreplace) /usr/share/MailScanner/reports/ro/inline.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/languages.conf
%config(noreplace) /usr/share/MailScanner/reports/ro/languages.conf.strings
%config(noreplace) /usr/share/MailScanner/reports/ro/recipient.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/recipient.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/rejection.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/sender.error.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/sender.filename.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/sender.spam.rbl.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/sender.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/sender.spam.sa.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/sender.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/sender.size.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/sender.virus.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/stored.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/stored.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/stored.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/se/deleted.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/se/stored.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/se/sender.content.report.txt
%config(noreplace) /usr/share/MailScanner/reports/se/deleted.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/se/deleted.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/se/deleted.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/se/disinfected.report.txt
%config(noreplace) /usr/share/MailScanner/reports/se/inline.sig.html
%config(noreplace) /usr/share/MailScanner/reports/se/inline.sig.txt
%config(noreplace) /usr/share/MailScanner/reports/se/inline.spam.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/se/inline.warning.html
%config(noreplace) /usr/share/MailScanner/reports/se/inline.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/se/languages.conf
%config(noreplace) /usr/share/MailScanner/reports/se/languages.conf.strings
%config(noreplace) /usr/share/MailScanner/reports/se/recipient.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/se/recipient.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/se/rejection.report.txt
%config(noreplace) /usr/share/MailScanner/reports/se/sender.error.report.txt
%config(noreplace) /usr/share/MailScanner/reports/se/sender.filename.report.txt
%config(noreplace) /usr/share/MailScanner/reports/se/sender.spam.rbl.report.txt
%config(noreplace) /usr/share/MailScanner/reports/se/sender.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/se/sender.spam.sa.report.txt
%config(noreplace) /usr/share/MailScanner/reports/se/sender.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/se/sender.size.report.txt
%config(noreplace) /usr/share/MailScanner/reports/se/sender.virus.report.txt
%config(noreplace) /usr/share/MailScanner/reports/se/stored.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/se/stored.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/se/stored.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/deleted.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/stored.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/sender.content.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/deleted.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/deleted.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/deleted.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/disinfected.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/inline.sig.html
%config(noreplace) /usr/share/MailScanner/reports/cz/inline.sig.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/inline.spam.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/inline.warning.html
%config(noreplace) /usr/share/MailScanner/reports/cz/inline.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/languages.conf
%config(noreplace) /usr/share/MailScanner/reports/cz/languages.conf.strings
%config(noreplace) /usr/share/MailScanner/reports/cz/recipient.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/recipient.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/rejection.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/sender.error.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/sender.filename.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/sender.spam.rbl.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/sender.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/sender.spam.sa.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/sender.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/sender.size.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/sender.virus.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/stored.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/stored.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/stored.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/deleted.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/stored.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/sender.content.report.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/deleted.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/deleted.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/deleted.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/disinfected.report.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/inline.sig.html
%config(noreplace) /usr/share/MailScanner/reports/hu/inline.sig.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/inline.spam.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/inline.warning.html
%config(noreplace) /usr/share/MailScanner/reports/hu/inline.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/languages.conf
%config(noreplace) /usr/share/MailScanner/reports/hu/languages.conf.strings
%config(noreplace) /usr/share/MailScanner/reports/hu/recipient.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/recipient.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/rejection.report.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/sender.error.report.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/sender.filename.report.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/sender.spam.rbl.report.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/sender.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/sender.spam.sa.report.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/sender.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/sender.size.report.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/sender.virus.report.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/stored.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/stored.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/stored.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/deleted.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/stored.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/sender.content.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/deleted.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/deleted.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/deleted.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/disinfected.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/inline.sig.html
%config(noreplace) /usr/share/MailScanner/reports/ca/inline.sig.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/inline.spam.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/inline.warning.html
%config(noreplace) /usr/share/MailScanner/reports/ca/inline.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/languages.conf
%config(noreplace) /usr/share/MailScanner/reports/ca/languages.conf.strings
%config(noreplace) /usr/share/MailScanner/reports/ca/recipient.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/recipient.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/rejection.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/sender.error.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/sender.filename.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/sender.spam.rbl.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/sender.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/sender.spam.sa.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/sender.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/sender.size.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/sender.virus.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/stored.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/stored.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/stored.virus.message.txt


%changelog
* Sun Apr 30 2016 Jerry Benton <mailscanner@mailborder.com>
- v5 initial release

* Wed Jan 27 2016 Jerry Benton <mailscanner@mailborder.com>
- moved directory structure

* Tue Jan 12 2016 Jerry Benton <mailscanner@mailborder.com>
- Updated group permissions for sendmail directories

* Sun Mar 1 2015 Jerry Benton <mailscanner@mailborder.com>
- Moved structure to /usr/share/MailScanner

* Thu Feb 12 2015 Jerry Benton <mailscanner@mailborder.com>
- Many updates. See the changelog for details.
  
* Mon Jan 09 2006 Julian Field <mailscanner@ecs.soton.ac.uk>
- Added analyse_SpamAssassin_cache

* Sun Oct 09 2005 Julian Field <mailscanner@ecs.soton.ac.uk>
- Added ms-update-safe-sites

* Thu Jan 22 2004 Julian Field <mailscanner@ecs.soton.ac.uk>
- Changed version numbering scheme, added recipient spam/mcp reports

* Thu Jun 26 2003 Julian Field <mailscanner@ecs.soton.ac.uk>
- Added bitdefender-autoupdate

* Sun May 18 2003 Julian Field <mailscanner@ecs.soton.ac.uk>
- Added */inline.spam.warning.txt

* Thu May 15 2003 Julian Field <mailscanner@ecs.soton.ac.uk>
- Added bitdefender-wrapper

* Mon May 12 2003 Julian Field <mailscanner@ecs.soton.ac.uk>
- Added Hungarian (hu) translation

* Mon Apr 28 2003 Julian Field <mailscanner@ecs.soton.ac.uk>
- Added Czech (cz) translation

* Sat Mar 01 2003 Julian Field <mailscanner@ecs.soton.ac.uk>
- Added nod32 and kaspersky autoupdate scripts

* Sat Feb 15 2003 Julian Field <mailscanner@ecs.soton.ac.uk>
- Added ms-upgrade-conf script

* Fri Dec 27 2002 Julian Field <mailscanner@ecs.soton.ac.uk>
- Updated for 4.11-1, added se translation

* Sun Nov 17 2002 Julian Field <mailscanner@ecs.soton.ac.uk>
- Updated for 4.06-2, added EximDiskStore.pm and languages.conf

* Sun Nov 10 2002 Julian Field <mailscanner@ecs.soton.ac.uk>
- Updated for 4.06-1, added /usr/sbin/ms-df2mbox

* Sun Oct 27 2002 Julian Field <mailscanner@ecs.soton.ac.uk>
- Updated for 4.03-1, added CustomConfig.pm and trend-wrapper

* Sun Oct 20 2002 Julian Field <mailscanner@ecs.soton.ac.uk>
- Updated for 4.01-1

* Thu Oct 10 2002 Julian Field <mailscanner@ecs.soton.ac.uk>
- Updated for 4.00.0a12

* Sat Oct 05 2002 Julian Field <mailscanner@ecs.soton.ac.uk>
- Added SweepContent.pm and updated for 4.00.0a9

* Fri Oct 04 2002 Julian Field <mailscanner@ecs.soton.ac.uk>
- Updated for RedHat 8.0

* Tue Oct 01 2002 Julian Field <mailscanner@ecs.soton.ac.uk>
- Added German reports

* Sun Sep 29 2002 Julian Field <mailscanner@ecs.soton.ac.uk>
- Rewritten for MailScanner version 4

* Fri Jul 26 2002 Richard Keech <rkeech@ender.keech.cx>
- initial tested version

* Fri Jul 19 2002 Richard Keech <rkeech@redhat.com>
- v3.22 Re-packaged entirely.
