FROM archlinux AS arch

WORKDIR /usr

# Copy all files in current local directory to the working directory
COPY . ./

RUN pacman -Syu --noconfirm

FROM python AS exe

# Set the shell script to be an executable
RUN chmod +x run-TaipeiTripPlanner.sh

CMD ["./run-TaipeiTripPlanner"]

