\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{jib}[2012/08/06 v2.0 by Stephan Weise]
\DeclareOption*{%
   \PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions
%  article.cls Version: 2004/02/16 v1.4f
\LoadClass[12pt]{article}
% calc -> Tools Package
% textcomp -> base Package
% url -> ltxmisc Package
\RequirePackage{calc}[1998/07/07 v4.1b Infix arithmetic (KKT,FJ)]
\RequirePackage{url}[2004/03/15 ver 3.1 Verb mode for urls, etc.]
\RequirePackage{listings}[2004/09/07 1.3 Carsten Heinz]
\RequirePackage{caption}[2004/07/16 v3.0c Customising captions (AS)]
\RequirePackage{textcomp}[2004/02/22 v1.99f Standard LaTeX package]
\RequirePackage{times}[2004/02/22 v1.99f Standard LaTeX package]
% graphicx -> graphics Package
% epsfig -> graphics Package
\RequirePackage{graphicx}[1999/02/16 v1.0f  Enhanced LaTeX Graphics (DPC,SPQR)]
\RequirePackage{epsfig}[1999/02/16 v1.7a (e)psfig emulation (SPQR)]
% vmargin Package
\RequirePackage{vmargin}[2004/07/15 V2.5 set document margins (VK)]

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% In Case of using latex compiler (Standard)
%\RequirePackage[dvipdfm]{hyperref}[2003/11/30 v6.74m Hypertext links for LaTeX]

% In Case of using pdflatex compiler
\RequirePackage{hyperref}[2003/11/30 v6.74m Hypertext links for LaTeX]
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\hypersetup{
  naturalnames=true,
  hypertexnames=false,
  pageanchor=false,
  plainpages=false,
  breaklinks=true,
  colorlinks=true,
  linkcolor=black,
  citecolor=black,
  urlcolor=black,
  filecolor=black,
  bookmarks=true,
  bookmarksopen=true,
}

\RequirePackage{eso-pic}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%	Titelseitendefinition
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\newenvironment{jibtitlepage}{%
  \sffamily% 
  \newcounter{institution}
  \renewcommand{\theinstitution}{\arabic{institution}}
  \newcommand{\addjibinstitution}{%
    \@ifstar{\@addjibinstitution}
            {\@addjibinstitutionwithreference}}
  \newcommand{\@addjibinstitution}[1]{
    \begin{center}{\small ##1}\end{center}}
  \newcommand{\@addjibinstitutionwithreference}[2]{%
    \begin{center}%
    \refstepcounter{institution}\label{##1}%
    \textsuperscript{\scriptsize{\theinstitution}}{\small ##2}%
    \end{center}\vspace{-0.5cm}}
    
  \newcommand{\jibtitle}[1]{\begin{center}\large\bfseries ##1\end{center}}
  \newcommand{\iref}[2][]{\textsuperscript{\scriptsize{\ref{##2}##1}}}
  \newcommand{\jibauthor}[1]{\begin{center}\small\bfseries ##1\end{center}}
  
  \newcommand{\jibfootnotemark}{}
  \newcommand{\jibfurtherfootnotes}{}
  \renewcommand{\@makefnmark}{\textsuperscript{\scriptsize{\jibfootnotemark\jibfurtherfootnotes}}}%
  \renewcommand\@makefntext[1]{%
    \parindent 1em%
    \noindent
    \hb@xt@1.8em{\hss\textsuperscript{\scriptsize{\jibfootnotemark}}}##1}
  \newcommand{\jibauthorfootnote}[3][]{%
    \renewcommand{\jibfurtherfootnotes}{##1}%
    \renewcommand{\jibfootnotemark}{##2}%
    \footnote{##3}}
}
{\setcounter{footnote}{0}}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%	Definition des Satzspiegels und Seitenlayouts
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\setpapersize{A4}
%\setlength{\paperwidth}{210mm}
%\setlength{\paperheight}{297mm}
\setmarginsrb{1in}%Rand links
             {12.5mm}%Rand oben
             {1in}%Rand rechts
             {12.5mm}%Rand unten
             {1cm}%Kopfhoehe
             {1cm}%Kopfabstand
             {2cm}%Fusshoehe
             {2.25cm}%Fussabstand
             
\setlength{\parindent}{0pt}
\setlength{\parskip}{1.5ex plus.2ex minus.2ex}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%	URL-Definitionen und Anpassungen
%%  Infos: Package url
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\def\url@emailstyle{%
 \@ifundefined{selectfont}{\def\UrlFont{\sf}}{\def\UrlFont{\sffamily}}}
\DeclareUrlCommand\email{\urlstyle{email}}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%	Header/Footer-Definition
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\def\jibvolume#1{\gdef\@jibvolume{#1}}\jibvolume{00}
\def\jibissue#1{\gdef\@jibissue{#1}}\jibissue{00}
\def\jibpages#1{\gdef\@jibpages{#1}}\jibpages{0000}
\def\jibyear#1{\def\@jibyear{#1}}\jibyear{0000}

\def\jibfooter{\footnotesize\sffamily doi:10.2390/biecoll-jib-\@jibyear-\@jibpages \hfil \thepage}

\def\ps@jibheadings{%
    \renewcommand{\@oddfoot}{\jibfooter}%
	\renewcommand{\@evenfoot}{\jibfooter}%
    \renewcommand{\@evenhead}{\leftmark\hfil\rightmark}%
    \renewcommand{\@oddhead}{\leftmark\hfil\rightmark}%
    }

\newcommand{\makeHeaderFooter}[1]{
\markboth{\footnotesize\sffamily Journal of Integrative Bioinformatics, \@jibvolume(\@jibissue):\@jibpages, \@jibyear}{\href{http://journal.imbio.de/}{\footnotesize\sffamily http://journal.imbio.de/}}}
\makeHeaderFooter{}
\pagestyle{jibheadings}

% Copyright
\AddToShipoutPictureFG{%
   \put(635,60){%
      \rotatebox{90}{\scriptsize{
        \begin{minipage}[t]{200mm}
            \textcolor[rgb]{0.67,0.67,0.67}{Copyright \@jibyear~The Author(s). Published by Journal of Integrative Bioinformatics. \\
          This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License (http://creativecommons.org/licenses/by-nc-nd/3.0/).}
        \end{minipage}
      }}%
   }%
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%	Abstract ohne Indent
%%  - nutzt intern die Quotation-Umgebung zum Erzeugen des Abstracts
%%    (im notitlepage und onecolumn Modus
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\renewcommand{\abstractname}{Summary}
\renewenvironment{quotation}
               {\list{}{\listparindent 0em%
                        \itemindent    \listparindent
                        \rightmargin   \leftmargin
                        \parsep        \z@ \@plus\p@}%
                \item\relax}
               {\endlist}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%	Font-Anpassung
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\renewcommand\section{\@startsection {section}{1}{\z@}%
                                   {-3.5ex \@plus -1ex \@minus -.2ex}%
                                   {2.3ex \@plus.2ex}%
                                   {\normalfont\sffamily\large\bfseries}}
\renewcommand\subsection{\@startsection{subsection}{2}{\z@}%
                                     {-3.25ex\@plus -1ex \@minus -.2ex}%
                                     {1.5ex \@plus .2ex}%
                                     {\normalfont\sffamily\normalsize\bfseries}}
\renewcommand\subsubsection{\@startsection{subsubsection}{3}{\z@}%
                                     {-3.25ex\@plus -1ex \@minus -.2ex}%
                                     {1.5ex \@plus .2ex}%
                                     {\normalfont\sffamily\normalsize}}
\renewcommand\paragraph{\@startsection{paragraph}{4}{\z@}%
                                    {3.25ex \@plus1ex \@minus.2ex}%
                                    {-1em}%
                                    {\normalfont\sffamily\normalsize\bfseries}}
\renewcommand\subparagraph{\@startsection{subparagraph}{5}{\parindent}%
                                       {3.25ex \@plus1ex \@minus .2ex}%
                                       {-1em}%
                                      {\normalfont\sffamily\normalsize\bfseries}}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%	Caption Anpassung fuer Figuren- und Tabellenunterschriften
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\captionsetup{font={footnotesize,bf},%
              margin=0.7cm,%
              parskip=5pt,%
              aboveskip=0pt,%
              belowskip=0pt}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%	Sonderzeichenanpassung
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% \texorpdfstring{...}, weil z.B. \textreg eventuell in section, subsection etc. genutzt wird
%% und hyperref bzw. in bookmarks Probleme mit Sonderzeichen auftreten
%% werden die originalen Befehle, wie \textregistered etc., verwendet, treten keine Probleme auf
\newcommand{\textreg}{\texorpdfstring{\textsuperscript{\textregistered}}{\textregistered}}
\newcommand{\textcright}{\texorpdfstring{\textsuperscript{\textcopyright}}{\textcopyright}}