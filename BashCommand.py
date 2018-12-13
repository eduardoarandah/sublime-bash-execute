import sublime
import sublime_plugin
import os

class BashExecCommand(sublime_plugin.TextCommand):
	# view.run_command('bash_exec')
	def run(self, edit):
		os.system("bash -c \"top\"")