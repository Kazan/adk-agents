install::
	pip3 install -r requirements.txt

remote ::
	adk api_server --a2a --port 8001 ./remote_agents/
