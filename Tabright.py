import sublime, sublime_plugin

class TabrightEvent(sublime_plugin.EventListener):

	def move_tab(self,view):
		if not view.settings().get("Tabright_processed"):
			view.settings().set("Tabright_processed", True)

			settings = sublime.load_settings("Tabright.sublime-settings")
			open_new_tabs_at = settings.get("open_new_tabs_at")

			window = sublime.active_window()
			group,index = window.get_view_index(view)
			newIndex = len(window.views_in_group(group)) - 1

			if (open_new_tabs_at == "far_left"):
				newIndex = 0;

			window.set_view_index(view, group, newIndex)
			window.focus_group(group)
			window.focus_view(view)

	def on_new(self,view):
	    def callback(view=view):
			return self.move_tab(view)
	    sublime.set_timeout(callback,1)

	def on_activated(self,view):
		if not view.settings().get("Tabright_processed"):
			def callback(view=view):
				return self.view_presented(view)
			sublime.set_timeout(callback,100)

	def view_presented(self,view):
		window = sublime.active_window()
		is_preview = view.file_name() is not "None" and window and view.file_name() not in [file.file_name() for file in window.views()]
		if is_preview:
			return
		else:
			def callback(view=view):
				return self.move_tab(view)
			sublime.set_timeout(callback,1)

	def on_close(self,view):
		window = sublime.active_window()
		group,index = window.get_view_index(view)
		def callback(index=index):
			return self.focus_tab(index)
		sublime.set_timeout(callback,1)

	def focus_tab(self,index):
		window = sublime.active_window()
		group = window.active_group()
		views = window.views_in_group(group)
		lenViews = len(views)

		if (lenViews>0):
			if index > lenViews-1:
				index = lenViews-1

			window.focus_group(group)
			window.focus_view(views[index])