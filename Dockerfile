# Create the Python virtual environment and install the requirements
FROM archlinux AS install

# Set working directory to /usr
WORKDIR /usr

# Copy all files in current local directory to the working directory
COPY . ./

RUN pacman -Syu --noconfirm


RUN python3 -m venv .venv
RUN source .venv/bin/activate
RUN pip install -r requirements.txt


# Run TaipeiMetroPlanner
FROM python AS exe

# Set working directory to /usr/local
WORKDIR /usr/local

# Copy the working directory of the install base to the working directory of the exe base
COPY --from=install /usr/ ./

# Set the shell script to be an executable
RUN chmod +x bin/run-TaipeiTripPlanner.sh

CMD ["./bin/run-TaipeiTripPlanner"]

