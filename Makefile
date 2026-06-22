PROJECT_NAME=hsbc-devops-lab
IMAGE_NAME=payment-api:local
NAMESPACE=hsbc-demo

.PHONY: kind-create kind-delete build load deploy verify smoke clean

kind-create:
	kind create cluster --config kind/cluster-2-workers.yaml

kind-delete:
	kind delete cluster --name $(PROJECT_NAME)

build:
	docker build -t $(IMAGE_NAME) app

load:
	kind load docker-image $(IMAGE_NAME) --name $(PROJECT_NAME)

deploy:
	kubectl apply -k k8s/base

verify:
	kubectl get nodes -o wide
	kubectl rollout status deployment/payment-api -n $(NAMESPACE) --timeout=180s
	kubectl get pods -n $(NAMESPACE) -o wide
	kubectl get svc -n $(NAMESPACE)
	kubectl get endpoints payment-api -n $(NAMESPACE)

smoke:
	python3 scripts/rest_api/smoke_test.py

clean:
	kubectl delete -k k8s/base --ignore-not-found=true
