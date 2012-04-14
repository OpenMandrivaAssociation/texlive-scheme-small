# revision 25850
# category Scheme
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-scheme-small
Version:	20120413
Release:	1
Summary:	small scheme (essentials, xetex, recommended packages)
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scheme-small.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-collection-latex
Requires:	texlive-collection-latexrecommended
Requires:	texlive-collection-metapost
Requires:	texlive-collection-xetex
Requires:	texlive-lualibs
Requires:	texlive-luaotfload
Requires:	texlive-luatexbase
Requires:	texlive-revtex
Requires:	texlive-synctex
Requires:	texlive-times
Requires:	texlive-tipa
Requires:	texlive-hyphen-basque
Requires:	texlive-hyphen-danish
Requires:	texlive-hyphen-dutch
Requires:	texlive-hyphen-english
Requires:	texlive-hyphen-finnish
Requires:	texlive-hyphen-french
Requires:	texlive-hyphen-german
Requires:	texlive-hyphen-hungarian
Requires:	texlive-hyphen-italian
Requires:	texlive-hyphen-norwegian
Requires:	texlive-hyphen-polish
Requires:	texlive-hyphen-portuguese
Requires:	texlive-hyphen-spanish
Requires:	texlive-hyphen-swedish

%description
This is a small TeX Live scheme, corresponding to MacTeX's
BasicTeX variant.  It adds XeTeX, MetaPost, various
hyphenations, and some recommended packages to scheme-basic.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
