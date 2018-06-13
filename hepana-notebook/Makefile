DOCKER_USER = avitase

.PHONY: all clean notebook push

all: notebook 

clean:
	docker rmi phd-notebook
	rm scripts/lhcb-symbols-def.tex

scripts/lhcb-symbols-def.tex: ../lhcb-symbols-def.tex
	cp ../lhcb-symbols-def.tex scripts/
	chmod 0444 scripts/lhcb-symbols-def.tex

notebook: scripts/lhcb-symbols-def.tex
	docker build --rm -t hepana-notebook:local .

push: notebook
	if ! docker info 2>&- | grep -q "Username: $(DOCKER_USER)"; then \
		echo -e "\n#####################################"; \
		echo -e "############             ############"; \
		echo -e "############  ATTENTION  ############"; \
		echo -e "############             ############"; \
		echo -e "#####################################"; \
		echo -e "\nApparently, you are not login ..."; \
		echo "Username: $(DOCKER_USER)"; \
		docker login --username $(DOCKER_USER); \
	fi
	docker tag hepana-notebook:local $(DOCKER_USER)/hepana-notebook:latest
	docker push $(DOCKER_USER)/hepana-notebook:latest
