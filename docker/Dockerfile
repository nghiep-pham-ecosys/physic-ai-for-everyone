# Physical AI for Everyone — CPU development image.
# ROS 2 Jazzy + Gazebo Harmonic (via ros_gz) on Ubuntu 24.04 (ADR-1, ADR-4).
#
# Pinned:
#   - Base image: ros:jazzy-ros-base (Docker Official Image), by index digest.
#   - Node.js: exact LTS version, verified against the official SHASUMS256.
# Not pinned (the ROS and Ubuntu apt repositories keep only current versions):
#   - ROS / Gazebo apt packages and just; the PR records the installed versions.

# ros:jazzy-ros-base, resolved 2026-10-24. Digest-only form: the Dev Containers
# CLI cannot parse "name:tag@digest" references.
FROM ros@sha256:103b6c417973394659af6804d4917cd489b91e5ed22eb7bef263025a3bed2410

ARG TARGETARCH
ARG USERNAME=ubuntu
ARG NODE_VERSION=24.22.1
ARG NODE_SHA256_X64=6c172a9ab6718f7b801fb5a7bd486af2ee5e32758086a04b84fcce2aa77095e6
ARG NODE_SHA256_ARM64=dbabf7a1cbf947e6059ffad2c27b80041db97dea1e553b62afdee7f13fca336e

ENV DEBIAN_FRONTEND=noninteractive

# ROS 2 / Gazebo Harmonic integration and tools
RUN apt-get update && apt-get install -y --no-install-recommends \
      ros-jazzy-ros-gz \
      ros-jazzy-xacro \
      ros-jazzy-robot-state-publisher \
      ros-jazzy-rviz2 \
      just \
      sudo \
      curl \
      ca-certificates \
      xz-utils \
    && rm -rf /var/lib/apt/lists/*

# Node.js LTS (official tarball, checksum-verified)
RUN set -eux; \
    case "${TARGETARCH:-amd64}" in \
      amd64) NODE_ARCH=x64;   NODE_SHA256="${NODE_SHA256_X64}" ;; \
      arm64) NODE_ARCH=arm64; NODE_SHA256="${NODE_SHA256_ARM64}" ;; \
      *) echo "unsupported arch: ${TARGETARCH}"; exit 1 ;; \
    esac; \
    NODE_TAR="node-v${NODE_VERSION}-linux-${NODE_ARCH}.tar.xz"; \
    curl -fsSLO "https://nodejs.org/dist/v${NODE_VERSION}/${NODE_TAR}"; \
    echo "${NODE_SHA256}  ${NODE_TAR}" | sha256sum -c -; \
    tar -xJf "${NODE_TAR}" -C /usr/local --strip-components=1 --no-same-owner; \
    rm "${NODE_TAR}"; \
    node --version; npm --version

# Non-root user: reuse the image's existing "ubuntu" user (UID 1000).
RUN echo "${USERNAME} ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/${USERNAME} \
    && chmod 0440 /etc/sudoers.d/${USERNAME} \
    && echo "source /opt/ros/jazzy/setup.bash" >> /home/${USERNAME}/.bashrc

# Stable workspace path, mounted by the devcontainer.
RUN mkdir -p /workspace && chown ${USERNAME}:${USERNAME} /workspace
WORKDIR /workspace

USER ${USERNAME}

# rosdep is initialised by the base image; refresh the cache for this user.
RUN rosdep update --rosdistro jazzy

CMD ["bash"]
