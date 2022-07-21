Basic terminal file manager.

Current version supports back-forth navigation, directory creation, file replacement.

Commands:

  <go> <dir_name>               - goes forth to folder dir_name (nesting is supported)
  <back>                        - goes one directory back
  <make> <dir_name>             - creates folder dir_name in current folder (nesting is supported)
  <sel> <all> <extention>       - selects all files of given extension
  <sel> <file1_name file2_name>   or given files, saves them to buffer
  <put>                         - places files saved in buffer to current directory
                                  (deletes them from original directory)
                                  
                                  
 Examples:
 
 	go FolderFrom
 	sel test.py
 	back
 	go FolderTo/1/2
 	put
 	back
 	sel all txt
 	back
 	put
 	exit
  
