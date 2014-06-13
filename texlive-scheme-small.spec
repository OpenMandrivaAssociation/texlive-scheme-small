# revision 30937
# category Scheme
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-scheme-small
Version:	20131013
Release:	6
Summary:	small scheme (basic + xetex, metapost, a few languages)
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
Requires:	texlive-zapfding
Requires:	texlive-babel-basque
Requires:	texlive-hyphen-basque
Requires:	texlive-babel-czech
Requires:	texlive-hyphen-czech
Requires:	texlive-babel-danish
Requires:	texlive-hyphen-danish
Requires:	texlive-babel-dutch
Requires:	texlive-hyphen-dutch
Requires:	texlive-babel-english
Requires:	texlive-hyphen-english
Requires:	texlive-babel-finnish
Requires:	texlive-hyphen-finnish
Requires:	texlive-babel-french
Requires:	texlive-hyphen-french
Requires:	texlive-babel-german
Requires:	texlive-hyphen-german
Requires:	texlive-babel-hungarian
Requires:	texlive-hyphen-hungarian
Requires:	texlive-babel-italian
Requires:	texlive-hyphen-italian
Requires:	texlive-babel-norsk
Requires:	texlive-hyphen-norwegian
Requires:	texlive-babel-polish
Requires:	texlive-hyphen-polish
Requires:	texlive-babel-portuges
Requires:	texlive-hyphen-portuguese
Requires:	texlive-babel-spanish
Requires:	texlive-hyphen-spanish
Requires:	texlive-babel-swedish
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
