package main

import (
	"log"

	client "github.com/ory/kratos-client-go"
)

func main() {
	configuration := client.NewConfiguration()
	configuration.Servers = []client.ServerConfiguration{
		{
			URL: "http://127.0.0.1:4434", // Kratos Admin API
		},
	}
	apiClient := client.NewAPIClient(configuration)
	// resp, r, err := apiClient.FrontendApi.ToSession(context.Background()).Cookie("ory_Kratos_session").Execute()
	log.Println(apiClient)
}
