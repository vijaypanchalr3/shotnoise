\NeedsTeXFormat{LaTeX2e}[2008/03/28]
\ProvidesClass{IWCOMP}
          [2008/03/28 v0.1c The Computer Journal class (DPC)]
\def\CJ@err#1{\ClassError{cj}{#1}\@eha}
\def\CJ@warn#1{\ClassWarningNoLine{cj}{#1}}
\newif\iffinal
\newif\ifrevises
\newif\ifgcopyright
\newif\ifopenacc
\newif\iflink
\newif\ifprinter
\newif\ifobituary
\newif\iffproof\fprooffalse %to make surname in magenta color
\newif\iffunding\fundingfalse % to make magenta color in funding text
\newif\ifnoquery
\newif\if@abstract@provided \@abstract@providedfalse %%5/7/2004

\DeclareOption{noquery}{\noquerytrue}\DeclareOption{track}{\tracktrue}
\DeclareOption{link}{\global\linktrue}
\DeclareOption{10pt}{}
\DeclareOption{11pt}{\CJ@warn{10pt used (not optional)}}
\DeclareOption{12pt}{\CJ@warn{10pt used (not optional)}}
\DeclareOption{twoside}{}
\DeclareOption{twocolumn}{}
\DeclareOption{onecolumn}{\CJ@warn{twocolumn used (not optional)}}
\DeclareOption{cmfonts}{%
  \let\CJ@fonts\relax}
\DeclareOption{epsfig}{\AtEndOfClass{\RequirePackage{epsfig}}}

\DeclareOption{openbib}{%
  \AtEndOfPackage{%
   \renewcommand\@openbib@code{%
      \advance\leftmargin\bibindent
      \itemindent -\bibindent
      \listparindent \itemindent
      \parsep \z@
      }%
   \renewcommand\newblock{\par}}%
}


\DeclareOption{final}{\finaltrue}
\DeclareOption{revises}{\revisestrue}
\DeclareOption{printer}{\printertrue}
\DeclareOption{openacc}{\openacctrue}
\DeclareOption{gcopyright}{\gcopyrighttrue}
\DeclareOption{crop}{\PassOptionsToPackage{cam}{crop}\global\@cropmarksontrue}
\DeclareOption{nocrop}{\PassOptionsToPackage{off}{crop}\global\@cropmarksonfalse}
\DeclareOption{fproof}{\fprooftrue}
\DeclareOption{funding}{\fundingtrue}
\DeclareOption{obituary}{\obituarytrue}

% Are we printing crop marks?
\newif\if@cropmarkson \@cropmarksontrue

\newcommand\copyedit[1]{\gdef\@copyedit{{\fontsize{8}{10}\selectfont \hfill Copy Edited by: #1}}}
\gdef\@copyedit{}

% Disallow widows and orphans
\clubpenalty 10000
\widowpenalty 10000

% Page break penalties
\@lowpenalty   51
\@medpenalty  151
\@highpenalty 301

% Disallow widows and orphans
\clubpenalty 10000
\widowpenalty 10000

% Disable page breaks before equations, allow pagebreaks after
% equations and discourage widow lines before equations.
\displaywidowpenalty 100
\predisplaypenalty   10000
\postdisplaypenalty  2500

% Allow breaking the page in the middle of a paragraph
\interlinepenalty 0

% Disallow breaking the page after a hyphenated line
\brokenpenalty 10000

% Hyphenation; don't split words into less than three characters
\lefthyphenmin=3
\righthyphenmin=3

\ExecuteOptions{cmfonts,epsfig,centre,info,twocolumn,openbib}
\ProcessOptions

\RequirePackage[T1]{fontenc}
\RequirePackage{vruler}
\RequirePackage{amsmath,amssymb,amsfonts}
\RequirePackage{stfloats}

\LoadClass[a4paper,twoside,twocolumn]{article}

\frenchspacing%%%%To control double spacing

\RequirePackage{amsthm}

\usepackage{vruler}
\def\linenos{\setvruler[50pt][1][5][1][1][590pt][590pt][-16pt][\textheight]
\setvruler[50pt][1][5][1][1][10pt][10pt][-16pt][\textheight]}


\def\DOI#1{\gdef\@DOI{#1}}
%\newcommand{\bxn}{bxn}

\newif\if@firstsetting
\newcommand{\firstproof}{%
  \global\@firstsettingtrue}


% tolerances
\pretolerance=6000
\tolerance=9500
\hbadness=5000
\vbadness=5000
\topmargin=0\p@
\emergencystretch=5pt
\sloppy
%
\RequirePackage[figuresright]{rotating}

\def\shortauthors#1{\gdef\@shortauthors{\scshape#1}}
\def\title{\@dblarg\CJ@title}
\def\CJ@title[#1]#2{%
  \def\@title{#2}%
  \def\@shorttitle{\scshape#1}}
\def\@title{\CJ@warn{No title}}
\def\@shorttitle{}
\newcounter{affil}
\newcounter{remaffil}
\def\author#1{%
  \g@addto@macro\@authors{%
    \@andorcomma,{\ignorespaces#1\unskip\affil@mark}}%
  \def\CJ@noaffil{\CJ@warn{No affiliation specified for #1}}}
\def\CJ@noaffil{%
 \CJ@err{No author specified}%
 \global\let\@andorcomma\relax
  \@gobbletwo}
\def\@authors{\relax\@gobbletwo}
\def\and{\CJ@err{\protect\and\space is not supported}}
\def\@andorcomma#1#2\@andorcomma#3{%
  \ifx#3\relax
    \ifx#1\relax%
      \let\@tempa\relax
    \else
    \def\@tempa{\space\andname\space #2\@gobbletwo}%
    \fi
  \else
    \def\@tempa{#1 #2\@andorcomma#3}%
  \fi
  \@tempa}
\def\affiliation#1{%
  \def\@tempa{#1}%
  \@tempswatrue
  \@affils
  \if@tempswa
    \stepcounter{affil}\setcounter{remaffil}{\theaffil}%
    \edef\@tempa##1{%
      \noexpand\g@addto@macro\noexpand\@affils{%
        \noexpand\doaffil{\theaffil}{##1}}}%
    \@tempa{#1}%
    \edef\@tempa{\noexpand\CJ@addaffil{\theaffil}}%
  \fi
  \expandafter\@tempa\@authors\relax\relax
  \let\CJ@noaffil\relax}
\let\@affils\@empty
\def\CJ@addaffil#1#2\relax#3\relax{%
  \def\@authors{#2\def\theaffil{#1}#3\relax}}
\def\doaffil#1#2{%
  \def\@tempb{#2}%
  \ifx\@tempa\@tempb
    \@tempswafalse
    \def\@tempa{\CJ@addaffil{#1}}%
  \fi}
\def\address#1{%
  \g@addto@macro\@authors{\textsuperscript{$*$}}%
  \def\@address{#1}%
  \def\address##1{%
    \CJ@err{You may only specify one correspondence address}}}


\def\email#1{\gdef\@email{Email: #1\vphantom{y}}}
\let\@email\@empty

\def\corrau#1{\gdef\@corrau{$^{\ast}$\!Corresponding author: #1\vphantom{y}}}
\let\@corrau\@empty

\def\editors#1{\gdef\@editors{#1\vphantom{y}\vskip2.5pt}}
\let\@editors\@empty

%\newif\if@dedication@provided \@dedication@providedfalse
%
\let\affil@mark\@empty
\def\keywords#1{%
  \gdef\@keywords{%
    \addvspace\medskipamount
    \noindent\strut{\itshape Keywords:\/} \ignorespaces#1\unskip}}
\def\@keywords{\ClassWarningNoLine{cj}{No keywords}}
\def\category#1{%
  \gdef\@category{%
    \addvspace\medskipamount
    \noindent\strut{\itshape Categories and subject descriptors:\/} \ignorespaces#1\unskip}}
\def\@category{\ClassWarningNoLine{cj}{No category}}
\def\editorial#1{%
  \gdef\@editorial{%
    \addvspace\medskipamount
    \noindent\strut{\itshape Responsible Editorial Board Member:\/} \ignorespaces#1\unskip}}
\def\@editorial{\ClassWarningNoLine{cj}{No editorial}}
\def\received#1{%
  \gdef\@received{\medskip\noindent\strut{\itshape Received #1}}}
\def\@received{\ClassWarningNoLine{cj}{No received date}}
\def\revised#1{%
  \gdef\@revised{{\itshape; revised #1}}} %SDH
\let\@revised\@empty
\def\accepted#1{%
  \gdef\@accepted{{\itshape; accepted #1}}}
\def\@accepted{\CJ@warn{No accepted date}}
\let\@dedication\@empty%
\def\dedication#1{\bgroup\def\@dedication{%
%\begin{minipage}{.726\textwidth}%
\fontsize{9}{11}\selectfont%
\leftskip\fill  %
\rightskip-\fill%
\parfillskip\stretch2%
\noindent\leftline{\textbf{Dedication}}\par%
#1\par\vspace{8\p@}%\end{minipage}
}}%

\newbox\@abstractbox
\renewenvironment{abstract}{\normalfont\bfseries\fontsize{9}{11}\selectfont\fontseries{b}\mathversion{bold}\global\@abstract@providedtrue%
  \global\setbox\@abstractbox\vbox\bgroup\hsize33pc
   \begin{center}%
   \hrule\@height.2pt
   \end{center}%
  \@afterindentfalse\@afterheading}{\par\egroup}%

\newcount\lncount
\newlength{\extraspace}
\setlength{\extraspace}{\z@}

\newskip\abovetitleskip
\ifobituary%
    \abovetitleskip10.5pt
    \def\titlefont{\fontsize{24}{30}\bfseries\selectfont}%
    \def\authorfont{\large}%
\else%
    \abovetitleskip15.5pt
    \def\titlefont{\fontsize{24}{30}\selectfont}%
    \def\authorfont{\large\scshape}%
\fi%

\def\maketitle{{%
  \let\footnote\thanks
   \renewcommand\thefootnote{\@fnsymbol\c@footnote}%
  \long\def\@makefntext##1{\hskip1.3em\noindent
    {\@makefnmark}##1}%
  \twocolumn[%
   \if@firstsetting\thispagestyle{pap}\else\thispagestyle{headings}\fi
    \label{FirstPage}%
    \normalfont\centering
\vspace*{\abovetitleskip}
{\parbox[b]{.75\textwidth}{\centering
      {\titlefont\@title\par}%
      \addvspace{19.5pt}%
      \ifnum\c@affil>\@ne
        \def\affil@mark{\textsuperscript{\theaffil}}%
        \def\doaffil##1##2{\noindent\textsuperscript{##1}##2\par}%
      \else
        \def\doaffil##1##2{\noindent##2\par}%
      \fi
      \setcounter{affil}{1}%
      \CJ@noaffil
      \renewcommand\thefootnote{\@fnsymbol\c@footnote}%
      \global\c@footnote\@ne
\ifnum\theremaffil>1 \typeout{caffil>1}
      \setcounter{footnote}{\theremaffil}
     \else \typeout{caffil not> 1}
      \setcounter{footnote}{0}\fi
      \def\@makefnmark{\@textsuperscript{\normalfont\@thefnmark}}%
      {\authorfont\@authors\@andorcomma\relax\@andorcomma\relax\par}%
       \addvspace{15pt}% 75mm - 15.5pc - 12pt baseline from affils
      {\small\itshape\@affils}\par              %%SDH affils made italic--should really be addresses
      {\small\itshape\@corrau}\par               %%SDH Emails moved to correct place
      {\small\itshape\@email}\par               %%SDH Emails moved to correct place
      \addvspace\bigskipamount
      \ifobituary\vskip7pt\fi%
      %\usebox\absbox\par
\if\@dedication\@empty\relax\else%\@dedicationbox\par\vspace{8\p@}
\@dedication\par%
\fi%
\if@abstract@provided%
    {\fontsize{8}{9}\selectfont\noindent\unvbox\@abstractbox\par}%
    \else
       \vspace{0\p@}%
     \fi
     \addvspace{12.9pt}
     \small\itshape
     \@category\par
     \small\itshape
     \@keywords\par
     \small\itshape
     \@editorial\par
     \@received\@revised\@accepted\par
     {\rm \@editors}\par\vskip1pt
     \addvspace{9pt}
}}%
\hrule\@height.5pt
  \vspace{22.5\p@ \@plus 4\p@ \@minus3\p@}%
  ]%
\@thanks
  \suppressfloats[t]}%
  \let\and\relax
  \let\affiliation\relax
  \let\author\relax
  \let\@affils\relax
  \let\keywords\relax
  \let\@keywords\relax
  \let\address\relax
%  \let\email\relax
  \let\@address\relax
  \let\maketitle\relax
  \let\thanks\@gobble
\if@firstsetting
\pagestyle{mypap}
\else
\pagestyle{revcj}
\fi
}
\def\runheadsc#1{\bgroup{\MakeUppercase{#1}}\egroup}
\def\ps@cj{
  \def\@oddhead{%
    \CJ@ruledhead
      \relax
      \@shorttitle%
      {\thepage~of~\@endpage}}%
  \def\@evenhead{%
    \vbox to \headheight{\vss
   \let\textsuperscript\@gobble
    \CJ@ruledhead
      {\thepage~of~\@endpage}
     {\@shortauthors}%
      \relax}}%
  \def\@oddfoot{%
    \CJ@ruledhead\relax{%
       \textsc\journalname~\textsc\volumename\space\@vol~\textsc\numbername\space\@issue,~\@copyrightyear}\relax}%
  \let\@evenfoot\@oddfoot}

\def\ps@headings{\def\@oddhead{\fontsize{10}{10}\selectfont%
\vbox to 41.5pt{\vss%
\vspace*{-14pt}
\vbox{\hbox to \textwidth {\hfill \@copyedit}\par
\hbox to \textwidth {\hfill $\copyright$ The Author \@papyear. Published by Oxford University Press on behalf of The British Computer Society. All rights reserved.
}\par
\hbox to \textwidth{\hfill For Permissions, please email: journals.permissions@oup.com}
\hbox to \textwidth{\hfill doi:10.1093/iwcomp/\@DOI}}\par
\vskip3pt
\removelastskip\nointerlineskip\nointerlineskip%
    \hrule \@height.5pt\@width\textwidth
    \vskip 14.5pt}\par}
  \let\@evenhead\@oddhead
\def\@oddfoot{%
        \CJ@ruledhead\relax{{\fontsize{11}{12}\selectfont%
       \textsc\journalname,}~\@copyrightyear}\relax}%
  \let\@evenfoot\@oddfoot}

\def\ps@revcj{%%%%%(for-revises)%
  \def\@oddhead{%
    \CJ@ruledhead
      \relax
      \@shorttitle%
      \thepage}%
  \def\@evenhead{%
    \vbox to \headheight{\vss
   \let\textsuperscript\@gobble
    \CJ@ruledhead
      \thepage
     {\@shortauthors}%
      \relax}}%
\iffinal
  \def\@oddfoot{%
    \CJ@ruledhead\relax{{\fontsize{11}{12}\selectfont%
       \textsc\journalname,}~\volumename\space\@vol~\numbername\space\@issue,~\@copyrightyear}\relax}%
\else
  \def\@oddfoot{%
    \CJ@ruledhead\relax{{\fontsize{11}{12}\selectfont%
       \textsc\journalname,}~\@copyrightyear}\relax}%
\fi
  \let\@evenfoot\@oddfoot}
\def\ps@pap{%(for-firstproof)
\def\@oddhead{%
\vbox to \headheight{%
\vspace*{-1pc}
\vbox{
\hbox to 42pc {\hfill\small $\copyright$ The Author 2005. Published by Oxford University Press on behalf of The British Computer Society. All rights reserved.}\par
\vskip2pt
\hbox to 42pc {\hfill\small For Permissions, please email: journals.permissions@oupjournals.org}
\vskip2pt
\hbox to 42pc{\hfill\small doi:10.1093/comjnl/\@DOI}}\par
\removelastskip\nointerlineskip\vskip3pt\nointerlineskip%
    \hrule \@height.5pt\@width\textwidth
    \vskip 14.5pt}}%
  \let\@evenhead\@oddhead
    \def\@oddfoot{%
        \CJ@ruledhead\relax{%
       \textsc\journalname,~\@copyrightyear}\relax}%
  \let\@evenfoot\@oddfoot}
\def\ps@mypap{%%%%%(for-Firstproof)%
  \def\@oddhead{%
    \CJ@ruledhead
      \relax
      \@shorttitle%
      {\thepage~of~\@endpage}}%
  \def\@evenhead{%
    \vbox to \headheight{\vss
   \let\textsuperscript\@gobble
    \CJ@ruledhead
      {\thepage~of~\@endpage}
     {\@shortauthors}%
      \relax}}%
  \def\@oddfoot{%
    \CJ@ruledhead\relax{%
       \textsc\journalname,~\@copyrightyear}\relax}%
  \let\@evenfoot\@oddfoot}
\def\CJ@ruledhead#1#2#3{%
  \vbox{\vspace*{-1pt}%
    \hrule \@height.5pt%
    \hbox to\textwidth{%
      \normalfont\vrule\@width\z@\@height 10.5pt\@depth 3.3pt%
      \rlap{#1}%
      {\hfil#2\hfil}%
      \llap{#3}}%
    \hrule\@height.5pt}}
\ps@cj
\def\@copyrightyear{????}
\def\@vol{??}
\def\@papyear{2012}
\def\@issue{??}
\def\@pubdate{??}
\def\@startpage{\pageref{FirstPage}}
\def\@endpage{\pageref{LastPage}}
\def\copyrightyear#1{\gdef\@copyrightyear{#1}}
\def\papyear#1{\gdef\@papyear{#1}}
\def\vol#1{\gdef\@vol{#1}}
\def\pubdate#1{\gdef\@pubdate{#1}}
\def\issue#1{\gdef\@issue{#1}}
\def\startpage#1{\gdef\@startpage{#1}\c@page#1}
\def\endpage#1{\gdef\@endpage{#1}}
\def\lastpage@putlabel{%
  \advance\c@page\m@ne
   \immediate\write\@auxout{\string
   \newlabel{LastPage}{{}{\thepage}}}%
   \advance\c@page\@ne}
\AtEndDocument{%
   \clearpage\lastpage@putlabel}%

% ******************************
% List numbering and lettering *
% ******************************

\def\labelenumi{{\rm(\roman{enumi})}}
\def\theenumi{\roman{enumi}}
\def\labelenumii{{\rm(\alph{enumii})}}
\def\theenumii{(\alph{enumii})}
\def\p@enumii{\theenumi}
\def\labelenumiii{{\rm\arabic{enumiii}.}}
\def\theenumiii{\arabic{enumiii}}
\def\p@enumiii{\theenumi(\theenumii)}
\def\labelenumiv{{\rm(\arabic{enumiv})}}
\def\theenumiv{\Alph{enumiv}}
\def\p@enumiv{\p@enumiii\theenumiii}
\def\labelitemi{$\bullet$}
\def\labelitemii{$\bullet$}
\def\labelitemiii{$\bullet$}
\def\labelitemiv{$\bullet$}

\setlength{\leftmargini}{18\p@}
\setlength{\leftmarginii}{\z@}
\setlength{\leftmarginiii}{\z@}
\setlength{\leftmarginiv}{\z@}

\def\enumargs{%
   \partopsep     \z@
   \itemsep       \z@
   \parsep        \z@
   \rightmargin   \z@
   \labelsep      0.5em
   \listparindent \parindent
   \itemindent    \z@}

\def\enumerate{%
    \@ifnextchar[{\@numerate}{\@numerate[3.]}}

\def\@numerate[#1]{%
     \ifnum \@enumdepth >3 \@toodeep\else
     \advance\@enumdepth \@ne
     \edef\@enumctr{enum\romannumeral\the\@enumdepth}
     \list{\csname label\@enumctr\endcsname}{%
       \enumargs
       \setlength{\leftmargin}{\csname leftmargin\romannumeral\the\@listdepth\endcsname}
       \usecounter{\@enumctr}
       \settowidth\labelwidth{#1}
       \addtolength{\leftmargin}{\labelwidth}
       \addtolength{\leftmargin}{\labelsep}
       \def\makelabel##1{\hss \llap{##1}}}%
     \fi
   }
\def\endenumerate{\endlist\advance \@listdepth -1}


% Changes to the list parameters for itemize
\def\itemargs{%
  \topsep 6pt%
   \leftmargini   1em
   \partopsep     3pt
   \itemsep       \z@
   \parsep        \z@
   \labelsep      0.5em
   \rightmargin   \z@
   \listparindent \parindent
   \itemindent    \z@}

\def\itemize{%
   \@ifnextchar[{\@itemize}{\@itemize[$\bullet$]}}

\def\@itemize[#1]{%
    \ifnum \@itemdepth >3 \@toodeep\else
   \advance\@itemdepth \@ne
  \edef\@itemctr{item\romannumeral\the\@itemdepth}
 \list{\csname label\@itemctr\endcsname}{%
  \itemargs
 \setlength{\leftmargin}{\csname leftmargin\romannumeral\the\@itemdepth\endcsname}
       \settowidth\labelwidth{#1}
       \addtolength{\leftmargin}{\labelwidth}
       \addtolength{\leftmargin}{\labelsep}
       \def\makelabel##1{\hss \llap{##1}}}%
     \fi
   }
\let\enditemize\endlist
\setlength\parskip{0pt}
\setlength\parindent{10pt}
\setlength\topsep{8pt plus 2pt minus 4pt}
\setlength\partopsep{0pt plus 2pt}
\setlength\itemsep{0pt plus 1pt}

%%%%Unnumbered list

\newenvironment{unlist}{%
  \begin{list}{}%
    {\setlength{\leftmargin}{2em}%
     \setlength{\itemindent}{-2em}%
     \setlength{\topsep}{\bigskipamount}%
     \setlength{\itemsep}{\z@}}}
{\end{list}}%


% Line spacing

\setlength\lineskip{1\p@}
\setlength\normallineskip{1\p@}
\renewcommand\baselinestretch{}


\def\@seccntformat#1{\csname the#1\endcsname.\quad}
\newdimen\asecdimen%
\asecdimen=24pt%

\def\section{%
  \@startsection
    {section}{1}{\z@}{-\asecdimen \@plus -2\p@ \@minus -2\p@}%
    {6\p@}{\normalfont\normalsize\raggedright\bfseries%\fontseries{b}\mathversion{bold}
    \MakeUppercase}}

\def\subsection{%
  \@startsection
    {subsection}{2}{\z@}{-18\p@ \@plus -2\p@ \@minus -2\p@}%
    {6\p@}{\normalfont\normalsize\bfseries\fontseries{b}\mathversion{bold}\raggedright}}

\def\subsubsection{%
  \@startsection
    {subsubsection}{3}{\z@}{-12\p@ \@plus -2\p@ \@minus-2\p@}%
    {1sp}{\normalfont\normalsize\itshape}}


\def\paragraph{%
  \@startsection
    {paragraph}{4}{\z@}{12\p@}%
    {-.5em}{\normalfont\normalsize\itshape}}

\def\subparagraph{%
  \@startsection
    {paragraph}{5}{\z@}{12\p@}%
    {-1em}{\normalfont\normalsize\itshape}}
\setcounter{secnumdepth}{4}
\setcounter{tocdepth}{2}

%%%%%%%%%% FIGURES AND TABLES %%%%%%%%%%%%%%%%%
\def\fps@eqnfloat{!tbp}
\def\ftype@eqnfloat{4}
\newenvironment{eqnfloat}
               {\@float{eqnfloat}}
               {\end@float}
\newenvironment{eqnfloat*}
               {\@dblfloat{eqnfloat}}
               {\end@dblfloat}

\def\fps@table{tpbH}

\setlength{\abovecaptionskip}{12pt}%

  \long\def\@makecaption#1#2{%
  \vskip\abovecaptionskip
  \sbox\@tempboxa{{\bfseries\small\vphantom{hf}#1.}\enskip \small#2}%
  \ifdim \wd\@tempboxa >\hsize\vskip-5\p@%
    {\bfseries\small#1.}\enskip \small#2\vphantom{hf}\par
  \else
    \global \@minipagefalse
    \hb@xt@\hsize{\hfil\box\@tempboxa\hfil}%
  \fi
  %\vskip\belowcaptionskip
  \vspace*{-2pt}
  }


  \let\@centercheck\@empty

\def\centertrue#1{\def\@centercheck{#1}}%

\newsavebox{\tablecaptionbox}
\long\def\@tablecaption#1#2{\vskip5pt\savebox{\tablecaptionbox}{%
  \small
  \textbf{#1.}\enskip{#2\strut\par}}
\ifdim\wd\tablecaptionbox>\hsize
\noindent\small\textbf{#1.}\enskip{#2\strut\par}
\else
\centerline{\usebox{\tablecaptionbox}}
\fi
 \vspace{\belowcaptionskip}\vskip1.5pt}

\newcounter{ALGORITHM}
\setcounter{ALGORITHM}{0}
  \def\thetable{\@arabic\c@table}
\def\fps@table{tbpH}
\def\ftype@figure{1}
\def\ftype@table{2}
\def\ftype@ALGORITHM{1}
\def\ext@table{lot}
\def\ext@ALGORITHM{loa}
\def\fnum@table{Table~\thetable}
\def\fnum@ALGORITHM{ALGORITHM~\theALGORITHM}
\def\table{\let\@makecaption\@tablecaption\let\source\tablesource\@float{table}}%\vspace*{.5\p@}\nointerlineskip
\def\endtable{\end@float}
\def\ALGORITHM{\@float{ALGORITHM}\vspace*{5\p@}\nointerlineskip}
\def\endALGORITHM{\end@float}
\@namedef{table*}{\let\@makecaption\@tablecaption\@dblfloat{table}}%\vspace*{5\p@}\nointerlineskip
\@namedef{endtable*}{\end@dblfloat}

\newif\if@rotate \@rotatefalse
\newif\if@rotatecenter \@rotatecenterfalse
\def\rotatecenter{\global\@rotatecentertrue}
\def\rotateendcenter{\global\@rotatecenterfalse}
\def\rotate{\global\@rotatetrue}
\def\endrotate{\global\@rotatefalse}
\newdimen\rotdimen
\def\rotstart#1{\special{ps: gsave currentpoint currentpoint translate
    #1 neg exch neg exch translate}}
\def\rotfinish{\special{ps: currentpoint grestore moveto}}
\def\rotl#1{\rotdimen=\ht#1\advance\rotdimen by \dp#1
    \hbox to \rotdimen{\vbox to\wd#1{\vskip \wd#1
    \rotstart{270 rotate}\box #1\vss}\hss}\rotfinish}
\def\rotr#1{\rotdimen=\ht #1\advance\rotdimen by \dp#1
    \hbox to \rotdimen{\vbox to \wd#1{\vskip \wd#1
    \rotstart{90 rotate}\box #1\vss}\hss}\rotfinish}

\newdimen\tempdime
\newbox\temptbox

% From ifmtarg.sty
% Copyright Peter Wilson and Donald Arseneau, 2000

\begingroup
\catcode`\Q=3
\long\gdef\@ifmtarg#1{\@xifmtarg#1QQ\@secondoftwo\@firstoftwo\@nil}
\long\gdef\@xifmtarg#1#2Q#3#4#5\@nil{#4}
\long\gdef\@ifnotmtarg#1{\@xifmtarg#1QQ\@firstofone\@gobble\@nil}
\endgroup

\def\tablesize{\@setfontsize\tablesize{9\p@}{12\p@}}

\newenvironment{processtable}[3]{\setbox\temptbox=\hbox{{\tablesize #2}}%
\tempdime\wd\temptbox\@processtable{#1}{#2}{#3}{\tempdime}}
{\relax}

\newcommand{\@processtable}[4]{%
\if@rotate
\setbox4=\vbox to \hsize{\vss\hbox to \textheight{%
\begin{minipage}{#4}%
\@ifmtarg{#1}{}{\caption{#1}}{\tablesize #2}%
\vskip7\p@\noindent
\parbox{#4}{\fontsize{9}{12}\selectfont #3\par}%
\end{minipage}}\vss}%
\rotr{4}
\else
\hbox to \hsize{\hfil\begin{minipage}[t]{#4}%
%\vskip2.9pt
\@ifmtarg{#1}{}{\caption{#1}}{\tablesize #2}%
\vskip.5\p@\noindent
\parbox{#4}{\fontsize{9}{12}\selectfont #3\par}%
\end{minipage}\hfil}\fi}%


\newenvironment{processfigure}[2]{%
\if@rotate
\setbox4=\hbox to \textheight{\vbox to \textwidth{\vss
\begin{minipage}[t]{\textheight}
{#1}%
\caption{#2}
\end{minipage}
\vss}\hss}
\else
\setbox4=\hbox to \textwidth{\hss\vbox{
\begin{minipage}[t]{\hsize}
{#1}%
\caption{#2}
\end{minipage}
}\hss}
\fi
\if@rotate\rotr{4}\else\box4\fi
}
{\par}

\RequirePackage{dcolumn}
\newcolumntype{P}[1]{>{\raggedright\let\\\@arraycr\hangindent1em}p{#1}}

%%%
\def\algoname{ALGORITHM}
\def\fnum@figure{\figurename~\thefigure}
\def\fnum@table{\tablename~\thetable}
\def\fnum@ALGORITHM{\MakeUppercase\algoname~\theALGORITHM}
\def\figure{\@float{figure}}%\vspace*{5\p@}\nointerlineskip
\let\endfigure\end@float
\def\fps@figure{tbpH}
\@namedef{figure*}{\@dblfloat{figure}}
\@namedef{endfigure*}{\end@dblfloat}

\def\fps@ALGORITHM{tbp}
\@namedef{ALGORITHM*}{\@dblfloat{ALGORITHM}}%\vspace*{5\p@}\nointerlineskip
\@namedef{endALGORITHM*}{\end@dblfloat}

\special{papersize=216mm,279mm}
\setlength\paperheight{279truemm}
\setlength\paperwidth{216truemm}%
\setlength\headsep{4.2mm}
\setlength\topskip\baselineskip
\setlength\marginparsep{1mm}
\setlength\marginparwidth{20\p@}
\setlength\headheight{4.6mm}
\setlength\topmargin{15mm}
\addtolength\topmargin{-1in}
\setlength{\footskip}{28.5pt\@killglue}%%
\setlength\@tempdima{240mm}%%%54 lines per page
\addtolength\@tempdima{-\headheight}
\addtolength\@tempdima{-\headsep}
  \divide\@tempdima\baselineskip
  \@tempcnta=\@tempdima
  \setlength\textheight{\@tempcnta\baselineskip}
\setlength\columnsep{2pc}
\setlength\textwidth{184.15mm}%

\setlength\oddsidemargin{15mm}%\paperwidth
\addtolength\oddsidemargin{-1in}
\setlength\@tempdima{\paperwidth}
\addtolength\@tempdima{-\textwidth}
\addtolength\@tempdima{-15mm}
\setlength\evensidemargin{\@tempdima}
\addtolength\evensidemargin{-1in}
\CJ@fonts

% Space between floats
\setlength\floatsep    {12\p@ \@plus 2\p@ \@minus 2\p@}

% Space between floats and text
\setlength\textfloatsep{20\p@ \@plus 2\p@ \@minus 4\p@}

% Space above and below an inline figure
\setlength\intextsep   {18\p@ \@plus 2\p@ \@minus 2\p@}

% For double column floats
\setlength\dblfloatsep    {12\p@ \@plus 2\p@ \@minus 2\p@}
\setlength\dbltextfloatsep{20\p@ \@plus 2\p@ \@minus 4\p@}

% Space left at top, bottom and inbetween floats on a float page.
\setlength\@fptop{0\p@}         % no space above float page figures
\setlength\@fpsep{12\p@ \@plus 1fil}
\setlength\@fpbot{0\p@}

% The same for double column
\setlength\@dblfptop{0\p@}
\setlength\@dblfpsep{12\p@ \@plus 1fil}
\setlength\@dblfpbot{0\p@}

\providecommand{\textsuperscript}[1]{%
  \ensuremath{{}^{\mbox{\normalfont\scriptsize#1}}}}
\providecommand{\@textsuperscript}[1]{%
  \ensuremath{{}^{\mbox{\normalfont\scriptsize#1}}}}
\providecommand\MakeUppercase[1]{%
  \protected@edef\@tempa{\uppercase{#1}}\@tempa}
\def\@sect#1#2#3#4#5#6[#7]#8{%
  \ifnum #2>\c@secnumdepth
    \let\@svsec\@empty
  \else
    \refstepcounter{#1}%
    \protected@edef\@svsec{\@seccntformat{#1}\relax}%
  \fi
  \@tempskipa #5\relax
  \ifdim \@tempskipa>\z@
    \begingroup
      #6{%
        \@hangfrom{\hskip #3\relax\@svsec}%
          \interlinepenalty \@M #8\@@par}%
    \endgroup
    \csname #1mark\endcsname{#7}%
    \addcontentsline{toc}{#1}{%
      \ifnum #2>\c@secnumdepth \else
        \protect\numberline{\csname the#1\endcsname}%
      \fi
      #7}%
  \else
    \def\@svsechd{%
      #6{\hskip #3\relax
      \@svsec #8}%
      \csname #1mark\endcsname{#7}%
      \addcontentsline{toc}{#1}{%
        \ifnum #2>\c@secnumdepth \else
          \protect\numberline{\csname the#1\endcsname}%
        \fi
        #7}}%
  \fi
  \@xsect{#5}}
\def\@ssect#1#2#3#4#5{%
  \@tempskipa #3\relax
  \ifdim \@tempskipa>\z@
    \begingroup
      #4{%
        \@hangfrom{\hskip #1}%
          \interlinepenalty \@M #5\@@par}%
    \endgroup
  \else
    \def\@svsechd{#4{\hskip #1\relax #5}}%
  \fi
  \@xsect{#3}}
\def\journalname{Interacting with Computers}
\def\copyrightname{Oxford University Press}
\def\andname{and}
\def\ppname{pp}
\def\numbername{No.\@}
\def\volumename{Vol.\@}

%extra macros

% Inserts space after macro unless followed by punctuation.
\def\@xspace{%
  \ifx\@let@token\bgroup\else%
  \ifx\@let@token\egroup\else%
  \ifx\@let@token\/\else%
  \ifx\@let@token\ \else%
  \ifx\@let@token~\else%
  \ifx\@let@token.\else%
  \ifx\@let@token!\else%
  \ifx\@let@token,\else%
  \ifx\@let@token:\else%
  \ifx\@let@token;\else%
  \ifx\@let@token?\else%
  \ifx\@let@token'\else%
  \ifx\@let@token)\else%
  \ifx\@let@token-\else%
  \ifx\@let@token$\else%
  \ifx\@let@token/\else%
   \space%
   \fi\fi\fi\fi\fi\fi\fi\fi\fi\fi\fi\fi\fi\fi\fi\fi}
\newcommand{\xspace}{\futurelet\@let@token\@xspace}

% Omit extra full stop after et al. if at end of sentence
\def\@etstop{%
  \ifx\@let@token.%
   \else.%
  \fi\xspace}
\def\etstop{\futurelet\@let@token\@etstop}
\def\etal{{\it et~al}\etstop}

\DeclareOldFontCommand{\rm}{\normalfont\rmfamily}{\mathrm}
\DeclareOldFontCommand{\sf}{\normalfont\sffamily}{\mathsf}
\DeclareOldFontCommand{\tt}{\normalfont\ttfamily}{\mathtt}
\DeclareOldFontCommand{\bf}{\normalfont\bfseries}{\mathbf}
\DeclareOldFontCommand{\it}{\normalfont\itshape}{\mathit}
\DeclareOldFontCommand{\sl}{\normalfont\slshape}{\@nomath\sl}
\DeclareOldFontCommand{\sc}{\normalfont\scshape}{\@nomath\sc}
\DeclareRobustCommand*\cal{\@fontswitch\relax\mathcal}
\DeclareRobustCommand*\mit{\@fontswitch\relax\mathnormal}
\DeclareMathAlphabet\mathbit
    \encodingdefault\rmdefault\bfdefault\itdefault
\DeclareOldFontCommand{\bi}{\normalfont\bfseries\itshape}{\mathbit}

%Appendix commands
\newcounter{appcounter}%
\setcounter{appcounter}{0}%

\def\appendix{\@@par
\refstepcounter{appcounter}%
 \@addtoreset{table}{section}
 \@addtoreset{figure}{section}
 \@addtoreset{equation}{section}
 \setcounter{section}{0}
 \setcounter{subsection}{0}
 \setcounter{subsubsection}{0}
 \setcounter{equation}{0}
 \setcounter{figure}{0}
 \setcounter{table}{0}
\def\thesection{\Alph{appcounter}.\arabic{section}}%
\def\thelemma{\Alph{appcounter}.\arabic{lemma}}
\def\thedefinition{\Alph{appcounter}.\arabic{definition}}
\def\thetheorem{\Alph{appcounter}.\arabic{theorem}}
\def\theproposition{\Alph{appcounter}.\arabic{proposition}}
\def\thecorollary{\Alph{appcounter}.\arabic{corollary}}
\def\theexample{\Alph{appcounter}.\arabic{example}}
\def\theRule{\Alph{appcounter}.\arabic{Rule}}
\def\theobservation{\Alph{appcounter}.\arabic{observation}}
\def\theaxiom{\Alph{appcounter}.\arabic{axiom}}
 \def\theequation{%
      \Alph{appcounter}.\arabic{equation}}
 \def\thetable{%
      \Alph{appcounter}\arabic{table}}
 \def\thefigure{%
      \Alph{appcounter}\arabic{figure}}
}

\newcommand{\centre}[2]{\multispan{#1}{\hfill #2\hfill}}
\newcommand{\crule}[1]{\multispan{#1}{\hrulefill}}

\def\lo#1{\llap{${}#1{}$}}

\def\tabnote#1{\par\rlap{\begin{minipage}[l]{\hsize}
\small#1
\end{minipage}}\\}

\def\lineup{\def\0{\hbox{\phantom{\small\rm 0}}}%
    \def\m{\hbox{$\phantom{-}$}}%
    \def\-{\llap{$-$}}}

\newcommand{\ms}{\noalign{\vspace{3\p@ plus2\p@ minus1\p@}}}
\newcommand{\ns}{\noalign{\vspace{-3\p@ plus-1\p@ minus-1\p@}}}

\def\specialverbatim@font{\fontsize{9}{12}\selectfont\ttfamily}%for display only

\def\@verbatim{\trivlist \item\relax
  \if@minipage\else\vskip\parskip\fi
  \leftskip\@totalleftmargin\rightskip\z@skip
  \parindent\z@\parfillskip\@flushglue\parskip\z@skip
  \@@par
  \@tempswafalse
  \def\par{%
    \if@tempswa
      \leavevmode \null \@@par\penalty\interlinepenalty
    \else
      \@tempswatrue
      \ifhmode\@@par\penalty\interlinepenalty\fi
    \fi}%
  \let\do\@makeother \dospecials
  \obeylines \specialverbatim@font \@noligs
  \hyphenchar\font\m@ne
  \everypar \expandafter{\the\everypar \unpenalty}%
}
\def\verbatim{\@verbatim \frenchspacing\@vobeyspaces \@xverbatim}
\def\endverbatim{\if@newlist \leavevmode\fi\endtrivlist}


%%Tables rules

\def\ptvhrule{\hrule height0.5pt}

\def\toprule{\noalign{\vskip2pt}\noalign{\ptvhrule}\noalign{\vskip4pt}}%
\def\midrule{\noalign{\vskip3pt}\noalign{\ptvhrule}\noalign{\vskip4pt}}%%
\def\botrule{\noalign{\vskip3pt}\noalign{\ptvhrule}\noalign{\vskip-3pt}}%

\newcommand{\boldarrayrulewidth}{1\p@}

% Width of bold rule in tabular environment.

\def\bhline{\noalign{\ifnum0=`}\fi\hrule \@height
\boldarrayrulewidth \futurelet \@tempa\@xhline}

\def\@xhline{\ifx\@tempa\hline\vskip \doublerulesep\fi
      \ifnum0=`{\fi}}


% Rules for tables with extra space around

\newcommand{\br}{\ms\bhline\ms}
\newcommand{\mr}{\ms\hline\ms}

\newcommand{\case}[2]{{\textstyle\frac{#1}{#2}}}

\newcommand{\ack}{\section*{Acknowledgements}}
\newcommand{\ackn}{\section*{Acknowledgement}}


%%%%Algorithm Macros%%%
\newcommand{\Algorithmtrue}{\parindent=0pt%
\renewcommand{\figurename}{\MakeUppercase{Algorithm}}%
\obeylines\obeyspaces}%

\newenvironment{Algorithm}[1]{\begingroup\parindent\z@%
\begin{ALGORITHM}{%
\hbox to 20pc{\hfill{%
\parbox{200\p@}{#1}\hfill}}%
}}{\end{ALGORITHM}\endgroup}%

\newenvironment{Algorithm*}[1]{\begingroup\parindent\z@%
\begin{ALGORITHM*}{%
\hbox to 42pc{\hfill{%
\parbox{450\p@}{#1}\hfill}}%
}}{\end{ALGORITHM*}\endgroup}%

% need to be explicit with `References' for \uppercase'ing

\usepackage{color}

\definecolor{gray}{cmyk}{0,0,0,.4}

\usepackage[authoryear]{natbib}

\usepackage{dcolumn}
\newcolumntype{d}[1]{D{.}{.}{#1}}


\iflink
\setcounter{tocdepth}{2}
\usepackage{nameref}
%\usepackage[bookmarks,dvips,raiselinks,hyperfootnotes,breaklinks]{hyperref}%[bookmarksnumbered,plainpages,backref]
\usepackage[bookmarks,raiselinks,hyperfootnotes,breaklinks]{hyperref}%
\hypersetup{
    colorlinks,%
    citecolor=blue,%
    filecolor=blue,%
    linkcolor=blue,%
    urlcolor=blue,
}
\fi

\renewcommand\bibname{\def\and{{\normalfont\rmfamily and }}%
                    \normalfont}%

\def\bibfont{\fontfamily{\rmdefault}\fontsize{9}{11}\fontseries{m}\fontshape{n}\selectfont}
\setlength\bibindent{11.5pt}
\renewcommand\refname{References}

\renewenvironment{thebibliography}[1]
     {%
     \section*{References}%
      \@mkboth{\MakeUppercase\refname}{\MakeUppercase\refname}
      \bibfont%
      \list{}%
           {\settowidth\labelwidth{0pt}%
            \leftmargin\labelwidth
%            \iflink\itemsep=4pt\fi%
\itemsep4pt
            \advance\leftmargin\labelsep
            \@openbib@code
            \setlength\leftmargin{9pt}
            \setlength\itemindent{-9pt}
            \usecounter{enumiv}%
            \let\p@enumiv\@empty
}%
      \sloppy
      \clubpenalty4000
      \@clubpenalty \clubpenalty
      \widowpenalty4000%
      \sfcode`\.\@m}
     {\def\@noitemerr
       {\@latex@warning{Empty `thebibliography' environment}}%
      \endlist}
\let\@openbib@code\@empty

%%%%for special square brackets%%%
\newcommand{\dsqo}{[\![}
\newcommand{\dsqc}{]\!]}

\hyphenpenalty=20


% Float placement parameters

% The total number of floats that can be allowed on a page.
\setcounter{totalnumber}{10}

% The maximum number of floats at the top and bottom of a page.

\setcounter{topnumber}{5}
\setcounter{bottomnumber}{5}

% The maximum part of the top or bottom of a text page that can be
% occupied by floats. This is set so that at least four lines of text
% fit on the page.

\renewcommand\topfraction{.9}
\renewcommand\bottomfraction{.9}

% The minimum amount of a text page that must be occupied by text.
% This should accomodate four lines of text.

\renewcommand\textfraction{.06}

% The minimum amount of a float page that must be occupied by floats.
\renewcommand\floatpagefraction{.95}

% The same parameters repeated for double column output
\renewcommand\dbltopfraction{.9}
\renewcommand\dblfloatpagefraction{.9}


%%%For equation above and belowskip%
\newdimen\equdimen%
\equdimen=12pt%

\newdimen\shortskipdimen%
\shortskipdimen=6pt%

   \abovedisplayskip \equdimen \@plus6\p@ \@minus3\p@
   \abovedisplayshortskip \z@ \@plus3\p@
   \belowdisplayshortskip \shortskipdimen \@plus3\p@ \@minus3\p@
   \belowdisplayskip \abovedisplayskip

\def\pageadjust#1{%
\advance \equdimen by #1pt%
\advance \asecdimen by #1pt%
}%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Extracts %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\def\quotation{\par\begin{list}{}{\fontsize{9}{11}\selectfont%  Extracts in small type
      \setlength{\topsep}{\medskipamount}%
      \setlength{\itemsep}{\z@}%
      \setlength\labelwidth{\z@}%
      \setlength\labelsep{\z@}%
      \setlength\leftmargin{1em}%
      \listparindent \parindent}%
  \item[\vrule width\z@ height 9\p@]}
\def\endquotation{\end{list}}
\let\quote\quotation
\let\endquote\endquotation
\newcommand{\source}[1]{\newline\hbox{}{#1}}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


\graphicspath{{G:/OupJournals/Artwork/comjnl/\@DOI/}}%


%\def\edot{\raisebox{-2pt}{${\cdot}$}}

%%Different Bonds

\def\sbond{\ensuremath{\raise.25ex\hbox{${-}\!\!\!\!{-}$}}\kern -.9pt}
\def\dbond{\ensuremath{\raise.25ex\hbox{=$\!$=}}}
\def\tbond{\ensuremath{\raise.20ex\hbox{${\equiv}\!\!\!{\equiv}$}}}

\renewcommand\footnoterule{%
  \kern-3\p@
  \hrule\@width 8pc\@height 0.45pt
  \vspace{2.5pt}}

\renewcommand\@makefntext[1]{\hspace*{4pt}%
    \fontsize{8}{9.5}\selectfont
    \parindent 1pc%
    \noindent\quad
    \@makefnmark#1\par}

\setlength{\skip\footins}{12\p@ \@plus 6\p@ \@minus 2\p@}

%\ProcessOptions

\hyphenation{section sections chapter chapters table tables figure figures Example}

\def\rpar{%
\def\leftpar{}%
\def\rightpar{}}%

\def\spar{%
\def\leftpar{(}%
\def\rightpar{)}}%

\def\leftpar{(}%
\def\rightpar{)}%
\def\thmhead@plain#1#2#3{%
  \thmname{#1}\thmnumber{\@ifnotempty{#1}{ }\@upn{#2}}%
  \thmnote{ {\the\thm@notefont \leftpar#3\rightpar}}}
\let\thmhead\thmhead@plain

\usepackage{color}
\definecolor{mag}{cmyk}{0,1,0,0}
\iffproof%
\def\surname#1{\fboxsep=1pt\colorbox{mag}{#1}}%
\else%
\def\surname#1{#1}%
\fi%

\iffunding%
\def\funtext#1{\fboxsep=1pt\textcolor{mag}{#1}}%
\else%
\def\funtext#1{#1}%
\fi%


\def\leftpar{(}
\def\rightpar{)}

\def\nothmpar{\def\leftpar{}\def\rightpar{}}
\def\resetthmpar{\def\leftpar{(}\def\rightpar{)}}
\def\thmhead@plain#1#2#3{%
  \thmname{#1}\thmnumber{\@ifnotempty{#1}{ }\@upn{#2}}%
  \thmnote{ {\the\thm@notefont\leftpar\normalfont#3\rightpar}}}
\let\thmhead\thmhead@plain
\def\swappedhead#1#2#3{%
  \thmnumber{#2}%
  \thmname{\@ifnotempty{#2}{~}#1}%
  \thmnote{ {\the\thm@notefont\leftpar\normalfont#3\rightpar}}}

\def\twocolfigright{%
\@rot@twosidefalse
\def\rot@LR{0}}

\makeatletter
\def\includegraphics{\vskip5pt%
  \@ifstar
    {\Gin@cliptrue\Gin@i}%
    {\Gin@clipfalse\Gin@i}}
\makeatother

\ifnoquery
\newcommand{\query}[2][0pt]{%
  \marginpar{%\vspace*{#1}%
    {\parbox{\marginparwidth}{%
     \raggedright\small{}}}}}
\newcommand{\leftquery}[2][0pt]{%
  \marginpar{%\vspace*{#1}%
    {\parbox{\marginparwidth}{%
     \raggedright\small{}}}}}
\newcommand{\rightquery}[2][0pt]{%
  \marginpar{%\vspace*{#1}%
    {\parbox{\marginparwidth}{%
     \raggedright\small{}}}}}
\def\mquery#1#2{}
\else
\newcommand{\query}[2][0pt]{%
  \marginpar{%\vspace*{#1}%
    {\parbox{\marginparwidth}{%
     \raggedright\small{\raisebox{10pt}{\hypertarget{#2}{\raisebox{-10pt}{#2}}}}}}}}%
\newcommand{\leftquery}[2][0pt]{\reversemarginpar%
  \marginpar{%\vspace*{#1}%
    {\parbox{\marginparwidth}{%
     \raggedright\small{\bf \raisebox{10pt}{\hypertarget{#2}{\raisebox{-10pt}{#2}}}}}}}}%
\newcommand{\rightquery}[2][0pt]{\normalmarginpar%
  \marginpar{%\vspace*{#1}%
    {\parbox{\marginparwidth}{%
     \raggedright\small{\bf \raisebox{10pt}{\hypertarget{#2}{\raisebox{-10pt}{#2}}}}}}}}%
\def\mquery#1#2{\marginpar{\small{\vspace*{#1}{\hypertarget{#2}{{#2}}}}}}
%\def\mquery#1#2{\marginpar{\small\hypertarget{#2}{\vskip#1#2}}}
\fi

\copyrightyear{2012}

\makeatletter
\def\@biblabel#1{}
\makeatother

\endinput
%% End of file `IWCOMP.cls'.