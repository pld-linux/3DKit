Summary:	GNU 3DKit - set of libraries based on OpenGL and GNUstep
Summary(pl):	GNU 3DKit - zestaw bibliotek opartych na OpenGL-u i GNUstepie
Name:		3DKit
Version:	0.3.0
Release:	5
License:	LGPL v2
Group:		Libraries
Source0:	ftp://ftp.gnustep.org/pub/gnustep/libs/%{name}-%{version}.tar.gz
# Source0-md5:	3606ad885ab12893c596e4c8951d019c
Patch0:		%{name}-make.patch
URL:		http://www.gnu.org/software/gnu3dkit/gnu3dkit.html
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.1.4
BuildRequires:	glut-devel
BuildRequires:	gnustep-gui-devel
BuildRequires:	perl-base
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/%{_lib}/GNUstep
%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%(echo %{_target_cpu} | sed -e 's/amd64/x86_64/;s/ppc/powerpc/')
%endif

%description
This is the GNU 3DKit, which is a set of general-purpose Objective-C
libraries that help writing 3D software, based on OpenGL/Mesa and
GNUstep. The libraries consist of everything from vector geometry
classes, such as matrices and vectors, to a complete scenegraph API.

%description -l pl
To jest GNU 3DKit - zestaw bibliotek Objective-C ogólnego
przeznaczenia maj±cych pomóc przy pisaniu oprogramowania 3D. Jest
oparty na OpenGL-u/Mesie oraz GNUstepie. Biblioteki zawieraj±
wszystko od klas geometrii wektorowej, takich jak macierze i wektory,
do pe³nego API opisu sceny.

%package devel
Summary:	Header files for 3DKit libraries
Summary(pl):	Pliki nag³ówkowe bibliotek 3DKit
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL-devel
Requires:	gnustep-gui-devel

%description devel
Header files for 3DKit libraries.

%description devel -l pl
Pliki nag³ówkowe bibliotek 3DKit.

%prep
%setup -q -n GNU%{name}
%patch0 -p1

sed -i -e 's@X11R6/lib@X11R6/%{_lib}@' Examples/glut/GNUmakefile

%build
. %{_prefix}/System/Library/Makefiles/GNUstep.sh
%{__make} -C 3DKit \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%{__make} -C GlutKit \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%{__make} -C SDLKit \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%{__make} -C Examples/glut \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%{__make} -C Examples/SDL \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_prefix}/System/Library/Makefiles/GNUstep.sh

%{__make} -j1 install -C 3DKit \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System

%{__make} install -C GlutKit \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System

%{__make} install -C SDLKit \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System

%{__make} install -C Examples/glut \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System

%{__make} install -C Examples/SDL \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc 3DKit/{README,TODO}
%{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libGeometryKit.so.*
%{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libRenderKit.so.*
%{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libGlutKit.so.*
%{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libSDLKit.so.*

%files devel
%defattr(644,root,root,755)
%{_prefix}/System/Library/Headers/%{libcombo}/GeometryKit
%{_prefix}/System/Library/Headers/%{libcombo}/RenderKit
%{_prefix}/System/Library/Headers/%{libcombo}/GlutKit
%{_prefix}/System/Library/Headers/%{libcombo}/SDLKit
%{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libGeometryKit.so
%{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libRenderKit.so
%{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libGlutKit.so
%{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/libSDLKit.so
