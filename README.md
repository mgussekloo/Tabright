Sublime Text 2 plugin: Tabright
===============================

A small plugin for SublimeText 2 that opens new tabs on the far right (or far left), instead of directly next to the currently active tab. Closing a tab will move the focus to the tab directly to the right of it. This makes the interface of SublimeText 2 more predictable.

Installation
------------

Tabright is now, apparently, available from Package Control!

* through Package Control (http://wbond.net/sublime_packages/package_control)
    * After installing Package Control, restart Sublime Text 2
    * Bring up the Command Palette (Command+Shift+p on OS X, Control+Shift+p on Linux/Windows).
    * Select "Package Control: Install Package"
    * Select "Tabright"

* clone to your Sublime Text 2 `Packages` folder located at
    * Windows: %APPDATA%\Sublime Text 2
    * OS X: ~/Library/Application Support/Sublime Text 2
    * Linux: ~/.config/sublime-text-2

Preferences
-----------

You can change where Tabright opens new tabs in the User Settings for this plugin. (Preferences -> Package Settings -> Tabright -> Settings - User) 

```javascript
{
   "open_new_tabs_at": "far_right" // available options: far_right (default) or far_left
}
```

Thanks
------

I've been helped by really kind people in the SublimeText Forums and on Github, who reported bugs and pointed out improvements.
