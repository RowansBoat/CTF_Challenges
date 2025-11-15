REGISTRY=harbor.neu-ctf.club
CTF=2025-11-15
TAG_PREFIX=${REGISTRY}/ctf-${CTF}

MELTDOWN_OVERRIDE_VERSION=v1.0.0

.PHONY: build
build:
	podman build -f Containerfile ./ -t ${TAG_PREFIX}/meltdown-override:${MELTDOWN_OVERRIDE_VERSION}

.PHONY: push
push:
	podman push ${TAG_PREFIX}/meltdown-override:${MELTDOWN_OVERRIDE_VERSION}
