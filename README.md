udm\_script (Ultimate Dev. Machine Script)
==========

A Python script that will automatically turn any apt-posessing virtual machine into a programmer's heaven.

<hr/>

Running
---------
 - Navigate to `udm_script/` and run the command `sudo ./udm.py`

<hr/>

Adding and Removing Packages
---------
To remove or add a cluster (container) of packages:

 - Navigate to `udm_script/packs`
 - Open `desired_packages.py` in an editor
 - Remove or add `<mypack>.container` to the `package_containers` list at the bottom of the file. If you are adding a new package container, be sure to import its module above this list.

To remove or add individual packages:

 - Navigate to `udm_script/packs`
 - Open the container of the package that you want to add or remove.
 - Add or remove items from the `packages` dictionary in the following form: <br/>`'<user-friendly-name>': '<actual-package-name>'` (note that the `<actual-package-name>` is what `apt` will be expecting)