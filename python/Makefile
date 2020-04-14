app_name = tic_tac_toe_bot

build:
	@docker build -t $(app_name) .

run:
	@docker run --detach -p 80:80 $(app_name)

kill:
	@echo 'Killing container...'
	@docker ps | grep $(app_name) | awk '{print $$1}' | xargs docker

train:
	python3 scripts/train_deploy_model.py
