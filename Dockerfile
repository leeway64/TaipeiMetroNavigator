# Create the Python virtual environment and install the requirements
FROM archlinux AS install

WORKDIR /usr

# Copy all files in current local directory to the working directory
COPY . ./

RUN pacman -Syu --noconfirm

RUN pip install -r requirements.txt


# Run TaipeiMetroPlanner
FROM python AS exe

# Set the shell script to be an executable
RUN chmod +x run-TaipeiTripPlanner.sh

CMD ["./run-TaipeiTripPlanner"]

