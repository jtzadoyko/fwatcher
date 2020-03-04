$FileSystemWatcher = New-Object System.IO.FileSystemWatcher 
$FileSystemWatcher.Path = 'C://Users/SDG/Desktop/file_watch'


Register-ObjectEvent -InputObject $FileSystemWatcher  -EventName Created  -Action {

Start-Process 'C:\Users\SDG\Desktop\file_watch\hello_world.py'

} 