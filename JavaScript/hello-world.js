var wmiService = GetObject("winmgmts:\\\\.\\root\\cimv2");
var computerSystems = wmiService.ExecQuery("Select * from Win32_ComputerSystem");

var enumerator = new Enumerator(computerSystems);
for (; !enumerator.atEnd(); enumerator.moveNext()) {
    var computer = enumerator.item();
    var computerName = computer.Name;
    WScript.Echo("Hello, World! Your hostname is: " + computerName);
    break; // Solo necesitamos el primer resultado
}