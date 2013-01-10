import sublime, sublime_plugin

class TabrightEvent(sublime_plugin.EventListener):

	def move_tab_right(self,view):
		if not view.settings().get("Tabright_processed"):
			window = sublime.active_window()
  			view.settings().set("Tabright_processed", True)
			group,index = window.get_view_index(view)
			rightIndex = len(window.views_in_group(group)) - 1
			window.set_view_index(view, group, rightIndex)
			window.focus_group(group)
			window.focus_view(view)

	def on_new(self,view):
		self.move_tab_right(view)

	def on_load(self,view):
		window = sublime.active_window()
		is_preview = window and view.file_name() not in [file.file_name() for file in window.views()]
		if not is_preview:
			self.move_tab_right(view)

	def on_close(self,view):
		window = sublime.active_window()
		group,index = window.get_view_index(view)
		views = window.views_in_group(group)
		lenViews = len(views)
		newIndex = index+1

		if (newIndex > lenViews):
			newIndex = lenViews

		window.focus_group(group)
		window.focus_view(views[newIndex])