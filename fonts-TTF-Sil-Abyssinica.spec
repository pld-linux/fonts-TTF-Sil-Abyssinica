Summary:	Free TrueType font for the scripts used by many languages of Ethiopia and Eritrea
Summary(pl.UTF-8):	Wolnodostępny font TrueType pisma używanego przez języki Etiopii i Erytrei
Name:		fonts-TTF-Sil-Abyssinica
Version:	1.0
Release:	1
License:	SIL OFL, distributable
Group:		Fonts
# Source0Download:	http://scripts.sil.org/cms/scripts/render_download.php?site_id=nrsi&format=file&media_id=AbyssinicaSIL1.0.zip&filename=abyssinicasil1.0.zip
Source0:	abyssinicasil%{version}.zip
# Source0-md5:	b63c5b9bbd2341a093c27f1253cc0ba3
URL:		http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&item_id=AbyssinicaSIL
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
The Ethiopic script is used for writing many of the languages of
Ethiopia and Eritrea. Abyssinica SIL supports all Ethiopic characters
which are in Unicode including the Unicode 4.1 extensions. Some
languages of Ethiopia are not yet able to be fully represented in
Unicode and, where necessary, we have included non-Unicode characters
in the Private Use Area.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ttffontsdir}

install *.ttf $RPM_BUILD_ROOT%{ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc *.txt *.pdf
%{ttffontsdir}/Abyssinica*.ttf
