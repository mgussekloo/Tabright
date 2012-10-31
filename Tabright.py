import sublime, sublime_plugin

class TabrightEvent(sublime_plugin.EventListener):

	def move_tab_right(self,view):
		window = sublime.active_window()
		rightIndex = len(window.views()) - 1
		window.set_view_index(view, window.active_group(), rightIndex)
		window.run_command("select_by_index", {"index": rightIndex})

	def on_new(self,view):
		self.move_tab_right(view)

	def on_load(self,view):
		window = sublime.active_window()
		is_preview = window and view.file_name() not in [file.file_name() for file in window.views()]
		if not is_preview:
			if view.id()==window.active_view().id():
				self.move_tab_right(view)

	def on_close(self,view):
		window = sublime.active_window()
		group,index = window.get_view_index(view)
		window.run_command("select_by_index", {"index": index+1})