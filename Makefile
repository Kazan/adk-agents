env ::
	python3 -m venv .venv

install ::
	pip3 install -r requirements.txt

run ::
	adk web ./local_agents

remote ::
	adk api_server --a2a --port 8001 ./remote_agents/
