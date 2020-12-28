FROM python:3.6.6 as base

SHELL ["/bin/bash", "-c"]

ENV PYTHONFAULTHANDLER=1 \
  PYTHONHASHSEED=random \
  PYTHONUNBUFFERED=1 \
  VIRTUAL_ENV=/venv

FROM base as builder

ARG PKG_CACHE_DIR_OUT=/tmp/poetry
ARG PKG_CACHE_DIR_IN=poetry-cache

ENV PIP_DEFAULT_TIMEOUT=100 \
  PIP_DISABLE_PIP_VERSION_CHECK=1 \
  PIP_USE_WHEEL=true \
  PIP_FIND_LINKS=$PKG_CACHE_DIR_OUT/wheelhouse \
  PIP_CACHE_DIR=$PKG_CACHE_DIR_OUT \
  POETRY_VERSION=1.0.0b9

RUN python -m venv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN mkdir -p $PIP_FIND_LINKS \
  && mkdir -p $PIP_CACHE_DIR \
   && pip install "poetry==$POETRY_VERSION" \
    wheel

COPY poetry.lock pyproject.toml ./

RUN poetry export --without-hashes -f requirements.txt > requirements.txt \
  && pip wheel -w $PIP_FIND_LINKS -r requirements.txt \
  && pip install --no-deps -r requirements.txt

FROM base as final

RUN mkdir /app
WORKDIR /app
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY --from=builder $VIRTUAL_ENV $VIRTUAL_ENV
COPY . /
WORKDIR /app