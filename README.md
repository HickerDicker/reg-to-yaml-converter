this needs pyyaml to be installed which can be done by running
pip install pyyaml
note this may not be 100% accurate but does the job may need a little bit of syntax fixing because you may end up with errors such as 
- !registryValue: {path: 'HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Directory\shell\TakeOwnership\command', value: 'IsolatedCommand', type: REG_SZ, data: 'powershell -windowstyle hidden -command \"Start-Process cmd -ArgumentList '/c takeown /f \\\"%1\\\" /r /d y && icacls \\\"%1\\\" /grant *S-1-3-4:F /t /c /l /q' -Verb runAs\"'}
(Line: 46, Col: 225, Idx: 5711) - (Line: 46, Col: 324, Idx: 5810): While parsing a flow mapping, did not find expected ',' or '}'.
but outside of that it works fine
