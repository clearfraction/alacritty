Name:           alacritty
Version:        0.10.1
Release:        1
URL:            https://github.com/alacritty
Source0:        https://github.com/alacritty/alacritty/archive/refs/tags/v%{version}.tar.gz
Source1:        https://github.com/alacritty/alacritty/releases/download/v%{version}/Alacritty.desktop
Source2:        https://github.com/alacritty/alacritty/releases/download/v%{version}/Alacritty.svg
Source3:        https://github.com/alacritty/alacritty/releases/download/v%{version}/alacritty.fish
Source4:        https://github.com/alacritty/alacritty/releases/download/v%{version}/alacritty.bash
Source5:        https://github.com/alacritty/alacritty/releases/download/v%{version}/_alacritty
Summary:        A GPU-accelerated terminal emulator
License:        Apache-2.0
BuildRequires:  rustc
BuildRequires:  pkg-config
BuildRequires:  libxcb-dev
BuildRequires:  freetype-dev
BuildRequires:  xclip
BuildRequires:  fontconfig-dev
BuildRequires:  mesa-dev
BuildRequires:  libxkbcommon-dev
BuildRequires:  ncurses-dev
BuildRequires:  expat-dev
 
%description
Alacritty is a terminal emulator written in Rust that leverages the GPU for
rendering.

%prep
%setup -q -n alacritty-%{version}
cargo fetch --locked

%build
export RUSTFLAGS="$RUSTFLAGS -C target-cpu=westmere -C target-feature=+avx -C opt-level=3"
env CARGO_INCREMENTAL=0 cargo build --release --locked --offline


%install
install -D -m755 target/release/alacritty %{buildroot}/usr/bin/alacritty
install -m644 %{SOURCE1} -pD %{buildroot}/usr/share/applications/Alacritty.desktop
install -m644 %{SOURCE2} -pD %{buildroot}/usr/share/pixmaps/Alacritty.svg
install -m644 %{SOURCE3} -pD %{buildroot}/usr/share/fish/vendor_completions.d/alacritty.fish
install -m644 %{SOURCE4} -pD %{buildroot}/usr/share/bash-completion/completions/alacritty
install -m644 %{SOURCE5} -pD %{buildroot}/usr/share/zsh/site-functions/_alacritty

%files
%license LICENSE-APACHE
/usr/bin/alacritty
/usr/share/applications/Alacritty.desktop
/usr/share/pixmaps/Alacritty.svg
/usr/share/bash-completion
/usr/share/fish
/usr/share/zsh
