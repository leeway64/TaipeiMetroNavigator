# Multi-stage builds


FROM ubuntu AS install

# Set working directory to /usr/local
WORKDIR /usr/local

# Copy all necessary files in current local directory to the working directory.
# COPY doesn't copy the folders themselves, only the contents of the folders.
COPY bin/ include/ src/ requirements.txt ./


FROM archlinux AS exe

# Change the shell from sh to bash
SHELL ["/bin/bash", "-c"]

# Set working directory to /usr
WORKDIR /usr

# Copy the contents of the working directory of the install base to the working directory of the
# exe base
COPY --from=install /usr/local ./

# Create the Python virtual environment and install the requirements
RUN pacman -Sy --noconfirm python3
RUN pacman -Sy --noconfirm python-pip
# Need to install openssl, otherwise Python will complain that "the ssl module in Python is not available"
RUN pacman -Sy --noconfirm openssl

RUN python3 -m venv .venv
RUN source .venv/bin/activate
RUN pip install -r requirements.txt

# Set the shell script to be an executable
RUN chmod +x ./run-TaipeiMetroNavigator.sh

# Run TaipeiTripPlanner
CMD python print_ascii_logo.py && ./run-TaipeiMetroNavigator.sh

