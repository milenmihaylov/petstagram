#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import re
import sys


def load_env_vars():
	"""Loads environment variables from a .env file."""
	try:
		env_file = os.path.join(os.path.dirname(__file__), "envs/.env")
		with open(env_file) as f:
			content = f.read()
	except IOError:
		content = ''
	for line in content.splitlines():
		m = re.split(r'\s*=(?=\s*)', line)
		if m and line:
			key, value = m[0], m[1]
			os.environ.setdefault(key, value)


def main():
	"""Run administrative tasks."""
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'petstagram.settings')
	try:
		from django.core.management import execute_from_command_line
	except ImportError as exc:
		raise ImportError(
			"Couldn't import Django. Are you sure it's installed and "
			"available on your PYTHONPATH environment variable? Did you "
			"forget to activate a virtual environment?"
		) from exc
	execute_from_command_line(sys.argv)


if __name__ == '__main__':
	load_env_vars()
	main()
