{pkgs ? import <nixpkgs> {}}:

pkgs.mkShell {
  name = "Python needed for lab";

  packages = [
    #for python
    (pkgs.python3.withPackages (ps: with ps; [
      numpy
      pandas
      scipy

      jupyterlab
      ipython

      black
      ruff
      debugpy
    ]))

  # for C code
  #for libraries
  BuildInputs = with pkgs; [

  ];

  #compiler
  nativeBuildInputs = with pkgs; [
    gcc
    pkg-config
    binutils
  ];

  shellHook=''
    echo "Python environment loaded"
    python --version
  '';
}
