#!/bin/bash

function press_enter {
	printf "\n"
	printf "Press Enter to continue..."
	read
	clear
}


selection=
until [ "$selection" = "0" ]; do
	printf "\nSelect from the menu: \n\n"
	printf "  1) VM Connection Test\n"
	printf "  2) List all Containers\n"
	printf "  3) List Running Containers\n"
	printf "  4) Inspect a Container\n"
	printf "  5) Delete a Container\n"
	printf "  6) Delete all Containers\n"
	printf "  7) Create a Container from an Image\n"
	printf " 10) Show Logs from a Container\n"
	printf " 11) List all Images\n"
	printf " 12) Delete an Image\n"
	printf " 13) Delete all Images\n"
	printf " 14) TAG an Image\n"
	printf " 15) Create Docker Images from Local Dockerfile\n"
	printf " \n 99) Exit\n"


	printf "\nSelection: "
	read selection

	case $selection in
		1  ) 	ping localhost
			press_enter
			;;
		2  )  curl -X GET -H 'Accept: application/json' localhost:8080/containers?state=running | python -mjson.tool
			press_enter
			;;
		3  ) 	curl -X GET -H 'Accept: application/json' localhost:8080/containers?state=running | python -mjson.tool
			    press_enter
			;;
		4  ) 	printf "\nEnter ID: "
          $id
          read id
          curl -X GET -H 'Accept: application/json' localhost:8080/containers/$id?state=running | python -mjson.tool
			    press_enter
			;;
		5  ) 	printf "\nEnter ID: "
          $id
          read id
          curl -X DELETE -H 'Accept: application/json' localhost:8080/containers/$id | python -mjson.tool
			    press_enter
			;;
		6  ) 	curl -X DELETE -H 'Accept: application/json' localhost:8080/containersDel | python -mjson.tool
			press_enter
			;;
		7  ) 	printf "\nEnter ID: "
          $id
          read id
          curl -X POST -H 'Content-Type: application/json' localhost:8080/containers/$id | python -mjson.tool
			    press_enter
			;;
		8  )	printf "\nEnter ID: "
          $id
          read id
          curl -X PATCH -H 'Content-Type: application/json' localhost:8080/containers/$id -d '{"state": "running"}'
			    press_enter
			;;
		9  ) 	printf "\nEnter ID: "
          $id
          read id
          curl -X PATCH -H 'Content-Type: application/json' localhost:8080/containers/$id -d '{"state": "stopped"}'
			    press_enter
			;;
		10 )	printf "\nEnter ID: "
          $id
          read id
          curl -X GET -H 'Accept: application/json' localhost:8080/containers/$id/logs | python -mjson.tool
			    press_enter
			;;
		11 )	curl -X GET -H 'Accept: application/json' localhost:8080/images | python -mjson.tool
			press_enter
			;;
		12 )	curl -X DELETE -H 'Accept: application/json' localhost:8080/images/imgID | python -mjson.tool
			press_enter
			;;
		13 )	curl -X DELETE -H 'Accept: application/json' localhost:8080/containersDel | python -mjson.tool
			press_enter
			;;
		14 )	curl -X PATCH -H 'Content-Type: application/json' localhost:8080/images/id -d '{"tag": "test:1.0"}'
			press_enter
			;;
		15 )	curl -H 'Accept: application/json' -F file=@Dockerfile http://localhost:8181/images | python -mjson.tool
			press_enter
			;;
		99) exit
			;;
		* ) printf "You did not choose a valid option!\n"
	esac
done

printf "\n"
