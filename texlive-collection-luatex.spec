# revision 25623
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-luatex
Epoch:		1
Version:	20120327
Release:	1
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
Requires:	texlive-interpreter
Requires:	texlive-lua-visual-debug
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
