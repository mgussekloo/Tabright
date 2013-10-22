import os
import sys
import sublime
import sublime_plugin

class TabrightListener(sublime_plugin.EventListener):
	ready = False
	busy = False

	def get_ready(self):
		settings = sublime.load_settings("Tabright.sublime-settings")
		self.open_new_tabs_at = settings.get("open_new_tabs_at", "far_right")
		self.files_only = settings.get("files_only", False)
		self.view_ids = []
		self.run_at_reload()
		self.ready = True

	def on_close(self, view):
		if (view.id() not in self.view_ids):
			self.focus_last()
			return

		if len(self.view_ids) > 1:
			window = sublime.active_window()
			views = window.views()

			oldIndex = self.view_ids.index(view.id())
			index = self.view_ids.index(view.id())

			if len(self.view_ids) > index + 1:
				index += 1
			else:
				index = len(self.view_ids)-2

			view_id = self.view_ids[index]
			self.focus_view_id(view_id)
			del(self.view_ids[oldIndex])

	def on_activated(self, view):
		if self.busy:
			return

		if not self.ready:
			self.get_ready()

		def callback(view=view):
			return self.process_tabs(view)
		sublime.set_timeout(callback,10)

	def run_at_reload(self):
		window = sublime.active_window()
		if window==None:
			return
		views = window.views()
		if (len(views)>0):
			self.process_tabs(window.active_view())

	def process_tabs(self, view):
		self.busy = True

		window = sublime.active_window()

		if int(sublime.version()) < 3000:
			is_preview = view.file_name() is not "None" and window and view.file_name() not in [file.file_name() for file in window.views()]
			if is_preview:
				if view.id() not in self.view_ids:
					self.view_ids.append(view.id())
				self.busy = False
				return

		old_group, old_index = window.get_view_index(view)
		views = window.views_in_group(old_group)

		if len(views)==0:
			self.busy = False
			return

		view_ids = []
		new_view_ids = []
		old_view_ids = []

		for v in views:
			if v.id() not in self.view_ids:
				if self.files_only and v.file_name() == None:
					old_view_ids.append(v.id())
				else:
					new_view_ids.append(v.id())
			else:
				old_view_ids.append(v.id())
			view_ids.append(v.id())

		if len(new_view_ids) == 0:
			self.busy = False
			return

		view_ids = [0] * len(view_ids)
		offset = 0

		for v in views:
			group, index = window.get_view_index(v)
			if v.id() not in new_view_ids:
				index = old_view_ids.index(v.id())
				if (self.open_new_tabs_at == "far_left"):
					index += len(new_view_ids)
			else:
				if (self.open_new_tabs_at == "far_left"):
					index = offset
				else:
					index = len(old_view_ids)+offset
				offset += 1

			view_ids[index] = v.id()
			window.set_view_index(v, group, index)

		self.view_ids = view_ids

		self.busy = False

		if len(new_view_ids)==1:
			self.focus_last()
		else:
			self.focus_view_id(view_ids[old_index])

	def focus_last(self):
		if (self.open_new_tabs_at == "far_left"):
			self.focus_view_id(self.view_ids[0])
		else:
			self.focus_view_id(self.view_ids[-1])

	def focus_view_id(self, view_id):
		window = sublime.active_window()
		views = window.views()
		for v in views:
			if v.id() == view_id:
				window.focus_view(v)