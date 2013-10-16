Sublime Text 2 / 3 Plugin: Tabright
===================================

A plugin for Sublime Text 2 / 3 that opens new tabs on the far right (or far left), instead of directly next to the currently active tab. This makes the interface of Sublime Text more predictable and user-friendly.

Installation
------------

Tabright is available from Package Control!

* through Package Control (http://wbond.net/sublime_packages/package_control)
    * After installing Package Control, restart Sublime Text
    * Bring up the Command Palette (Command+Shift+p on OS X, Control+Shift+p on Linux/Windows).
    * Select "Package Control: Install Package"
    * Select "Tabright"

or

* clone to your Sublime Text 2 `Packages` folder located at
    * Windows: %APPDATA%\Sublime Text 2
    * OS X: ~/Library/Application Support/Sublime Text 2
    * Linux: ~/.config/sublime-text-2

Preferences
-----------

You can change where Tabright opens new tabs in the User Settings for this plugin. (Preferences -> Package Settings -> Tabright -> Settings -> User)

```javascript
{
   "open_new_tabs_at": "far_right" // available options: far_right (default) or far_left
}
```

You can also choose to have only files open at the far right (or far left). Newly created empty tabs will still open the regular way, if that suits your workflow.

```javascript
{
   "files_only": false // available options: false (default) or true
}
```

Thanks
------

I've been helped by awesome people in the Sublime Text Forums and here on Github, who reported bugs and pointed out improvements.