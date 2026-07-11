%global tl_name scheme-small
%global tl_revision 78733

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	small scheme (basic + xetex, metapost, a few languages)
Group:		Publishing
URL:		https://www.ctan.org/pkg/scheme-small
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scheme-small.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(babel-basque)
Requires:	texlive(babel-czech)
Requires:	texlive(babel-danish)
Requires:	texlive(babel-dutch)
Requires:	texlive(babel-english)
Requires:	texlive(babel-finnish)
Requires:	texlive(babel-french)
Requires:	texlive(babel-german)
Requires:	texlive(babel-hungarian)
Requires:	texlive(babel-italian)
Requires:	texlive(babel-norsk)
Requires:	texlive(babel-polish)
Requires:	texlive(babel-portuges)
Requires:	texlive(babel-spanish)
Requires:	texlive(babel-swedish)
Requires:	texlive(collection-basic)
Requires:	texlive(collection-latex)
Requires:	texlive(collection-latexrecommended)
Requires:	texlive(collection-metapost)
Requires:	texlive(collection-xetex)
Requires:	texlive(ec)
Requires:	texlive(epstopdf)
Requires:	texlive(eurosym)
Requires:	texlive(hyphen-basque)
Requires:	texlive(hyphen-czech)
Requires:	texlive(hyphen-danish)
Requires:	texlive(hyphen-dutch)
Requires:	texlive(hyphen-english)
Requires:	texlive(hyphen-finnish)
Requires:	texlive(hyphen-french)
Requires:	texlive(hyphen-german)
Requires:	texlive(hyphen-hungarian)
Requires:	texlive(hyphen-italian)
Requires:	texlive(hyphen-norwegian)
Requires:	texlive(hyphen-polish)
Requires:	texlive(hyphen-portuguese)
Requires:	texlive(hyphen-spanish)
Requires:	texlive(hyphen-swedish)
Requires:	texlive(l3backend-dev)
Requires:	texlive(l3kernel-dev)
Requires:	texlive(latex-amsmath-dev)
Requires:	texlive(latex-base-dev)
Requires:	texlive(latex-bin-dev)
Requires:	texlive(latex-firstaid-dev)
Requires:	texlive(latex-graphics-dev)
Requires:	texlive(latex-lab)
Requires:	texlive(latex-lab-dev)
Requires:	texlive(latex-tools-dev)
Requires:	texlive(lm)
Requires:	texlive(ltx-talk)
Requires:	texlive(lua-unicode-math)
Requires:	texlive(lualibs)
Requires:	texlive(luamml)
Requires:	texlive(luaotfload)
Requires:	texlive(luatexbase)
Requires:	texlive(make4ht)
Requires:	texlive(pdfmanagement)
Requires:	texlive(revtex)
Requires:	texlive(synctex)
Requires:	texlive(tagpdf)
Requires:	texlive(tex4ebook)
Requires:	tex4ht
Requires:	texlive(times)
Requires:	texlive(tipa)
Requires:	texlive(ulem)
Requires:	texlive(unicode-math)
Requires:	texlive(upquote)
Requires:	texlive(zapfding)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a small TeX Live scheme, corresponding to MacTeX's BasicTeX
variant. It adds XeTeX, MetaPost, various hyphenations, and a few
recommended packages to scheme-basic, including the tagged pdf support
in LaTeX. It also provides the {pdf,xe,lua,...}latex-dev engines for
helping to test LaTeX.

