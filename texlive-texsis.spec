# revision 31958
# category Package
# catalog-ctan /macros/texsis
# catalog-date 2012-06-05 22:22:59 +0200
# catalog-license lppl
# catalog-version 2.18
Name:		texlive-texsis
Version:	2.18
Release:	5
Summary:	Plain TeX macros for Physicists
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/texsis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texsis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texsis.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-tetex
Requires:	texlive-tex
Requires:	texlive-texsis.bin

%description
TeXsis is a TeX macro package which provides useful features
for typesetting research papers and related documents. For
example, it includes support specifically for: Automatic
numbering of equations, figures, tables and references;
Simplified control of type sizes, line spacing, footnotes,
running headlines and footlines, and tables of contents,
figures and tables; Specialized document formats for research
papers, preprints and ``e-prints,'' conference proceedings,
theses, books, referee reports, letters, and memoranda;
Simplified means of constructing an index for a book or thesis;
Easy to use double column formatting; Specialized environments
for lists, theorems and proofs, centered or non-justified text,
and listing computer code; Specialized macros for easily
constructing ruled tables. TeXsis was originally developed for
physicists, but others may also find it useful. It is
completely compatible with Plain TeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/texsis/texsis.bst
%{_texmfdistdir}/tex/texsis/base/AIP.txs
%{_texmfdistdir}/tex/texsis/base/CVformat.txs
%{_texmfdistdir}/tex/texsis/base/Elsevier.txs
%{_texmfdistdir}/tex/texsis/base/Exam.txs
%{_texmfdistdir}/tex/texsis/base/Formletr.txs
%{_texmfdistdir}/tex/texsis/base/IEEE.txs
%{_texmfdistdir}/tex/texsis/base/PhysRev.txs
%{_texmfdistdir}/tex/texsis/base/Spanish.txs
%{_texmfdistdir}/tex/texsis/base/Swedish.txs
%{_texmfdistdir}/tex/texsis/base/TXSconts.tex
%{_texmfdistdir}/tex/texsis/base/TXSdcol.tex
%{_texmfdistdir}/tex/texsis/base/TXSenvmt.tex
%{_texmfdistdir}/tex/texsis/base/TXSeqns.tex
%{_texmfdistdir}/tex/texsis/base/TXSfigs.tex
%{_texmfdistdir}/tex/texsis/base/TXSfmts.tex
%{_texmfdistdir}/tex/texsis/base/TXSfonts.tex
%{_texmfdistdir}/tex/texsis/base/TXShead.tex
%{_texmfdistdir}/tex/texsis/base/TXSinit.tex
%{_texmfdistdir}/tex/texsis/base/TXSletr.tex
%{_texmfdistdir}/tex/texsis/base/TXSmacs.tex
%{_texmfdistdir}/tex/texsis/base/TXSmemo.tex
%{_texmfdistdir}/tex/texsis/base/TXSprns.tex
%{_texmfdistdir}/tex/texsis/base/TXSrefs.tex
%{_texmfdistdir}/tex/texsis/base/TXSruled.tex
%{_texmfdistdir}/tex/texsis/base/TXSsects.tex
%{_texmfdistdir}/tex/texsis/base/TXSsite.tex
%{_texmfdistdir}/tex/texsis/base/TXSsymb.tex
%{_texmfdistdir}/tex/texsis/base/TXStags.tex
%{_texmfdistdir}/tex/texsis/base/TXStitle.tex
%{_texmfdistdir}/tex/texsis/base/Tablebod.txs
%{_texmfdistdir}/tex/texsis/base/WorldSci.txs
%{_texmfdistdir}/tex/texsis/base/color.txs
%{_texmfdistdir}/tex/texsis/base/nuclproc.txs
%{_texmfdistdir}/tex/texsis/base/printfont.txs
%{_texmfdistdir}/tex/texsis/base/spine.txs
%{_texmfdistdir}/tex/texsis/base/texsis.tex
%{_texmfdistdir}/tex/texsis/base/thesis.txs
%{_texmfdistdir}/tex/texsis/base/twin.txs
%{_texmfdistdir}/tex/texsis/config/texsis.ini
%_texmf_fmtutil_d/texsis
%doc %{_mandir}/man1/texsis.1*
%doc %{_texmfdistdir}/doc/man/man1/texsis.man1.pdf
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/COPYING
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/Example.tex
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/Fonts.tex
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/INSTALL
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/Install.tex
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/MANIFEST
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/Manual.fgl
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/Manual.ref
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/Manual.tbl
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/Manual.tex
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/NEWS
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/README
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/TXSapxF.doc
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/TXScover.doc
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/TXSdcol.doc
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/TXSdoc.doc
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/TXSdoc0.doc
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/TXSdocM.doc
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/TXSend.doc
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/TXSenvmt.doc
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/TXSeqns.doc
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/TXSfigs.doc
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/TXSfmts.doc
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/TXSfonts.doc
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/TXSinstl.doc
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/TXSintro.doc
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/TXSletr.doc
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/TXSmisc.doc
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/TXSprns.doc
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/TXSrefs.doc
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/TXSrevs.doc
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/TXSruled.doc
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/TXSsects.doc
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/TXSsite.000
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/TXSsymb.doc
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/TXStags.doc
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/index.tex
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/letr
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/penguin.eps
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/penguin2.eps
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/texsis.el
%doc %{_texmfdistdir}/doc/otherformats/texsis/base/texsis.lsm

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_texmf_fmtutil_d}
cat > %{buildroot}%{_texmf_fmtutil_d}/texsis <<EOF
#
# from texsis:
texsis pdftex - -translate-file=cp227.tcx texsis.ini
EOF
