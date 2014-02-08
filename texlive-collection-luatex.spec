# revision 27227
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-luatex
Epoch:		1
Version:	20120810
Release:	2
Summary:	LuaTeX packages
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-luatex.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-checkcites
Requires:	texlive-chickenize
Requires:	texlive-interpreter
Requires:	texlive-lua-check-hyphen
Requires:	texlive-lua-visual-debug
Requires:	texlive-lua2dox
Requires:	texlive-luabibentry
Requires:	texlive-luacode
Requires:	texlive-luaindex
Requires:	texlive-luainputenc
Requires:	texlive-lualatex-doc
Requires:	texlive-lualatex-math
Requires:	texlive-lualibs
Requires:	texlive-luamplib
Requires:	texlive-luaotfload
Requires:	texlive-luapersian
Requires:	texlive-luasseq
Requires:	texlive-luatexbase
Requires:	texlive-luatextra
Requires:	texlive-showhyphens

%description
Packages for LuaTeX, a Unicode-aware extension of pdfTeX, using
Lua as an embedded scripting and extension language.
http://luatex.org/.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install


%changelog
* Fri Aug 10 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120810-1
+ Revision: 813958
- Update to latest release.

* Tue Mar 27 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120327-1
+ Revision: 787862
- Update to latest release.

* Wed Mar 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120307-1
+ Revision: 783101
- Update to latest release.

* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780501
- Update to latest release.
- Import texlive-collection-luatex
- Import texlive-collection-luatex

