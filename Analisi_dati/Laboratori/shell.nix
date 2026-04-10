{pkgs ? import <nixpkgs> {}}:

pkgs.mkShell {
  name = "Python needed for lab";

  packages = [
    #for python
    (pkgs.python3.withPackages (ps: with ps; [
      numpy
      pandas
      scipy
      matplotlib 

      jupyterlab
      ipython

      black
      ruff
      debugpy
    ]))];

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
    export PYTHONPATH="${toString ./.}:$PYTHONPATH"

    echo "Python environment loaded"
    python --version
  '';
}
