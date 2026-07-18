%global tl_name texsis
%global tl_revision 79618
%global tl_bin_links texsis:pdftex

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.18
Release:	%{tl_revision}.1
Summary:	Plain TeX macros for Physicists
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/formats/texsis
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texsis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texsis.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(cm)
Requires:	texlive(hyphen-base)
Requires:	texlive(knuth-lib)
Requires:	texlive(pdftex)
Requires:	texlive(plain)
Requires:	texlive(tex)
Requires:	texlive(texsis.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
TeXsis is a TeX macro package which provides useful features for
typesetting research papers and related documents. For example, it
includes support specifically for: Automatic numbering of equations,
figures, tables and references; Simplified control of type sizes, line
spacing, footnotes, running headlines and footlines, and tables of
contents, figures and tables; Specialized document formats for research
papers, preprints and "e-prints", conference proceedings, theses, books,
referee reports, letters, and memoranda; Simplified means of
constructing an index for a book or thesis; Easy to use double column
formatting; Specialized environments for lists, theorems and proofs,
centered or non-justified text, and listing computer code; Specialized
macros for easily constructing ruled tables. TeXsis was originally
developed for physicists, but others may also find it useful. It is
completely compatible with Plain TeX.

