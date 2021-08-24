call MAKE_Install.bat

set GameExeArgs0=%GameExeArgs:"=%

::Run game
%GameRootDir%\%GameExeFile% %GameExeArgs0%
