import org.springframework.web.reactive.function.client.WebClient;
import reactor.core.publisher.Mono;
import java.time.Duration;

public class ApiCaller {

    private final WebClient webClient;

    public ApiCaller() {
        this.webClient = WebClient.builder()
                .baseUrl("http://your-api-endpoint.com") // Base API URL
                .build();
    }

    public boolean makeApiCall() {
        try {
            String response = webClient.get()
                    .uri("/analyze") // API endpoint
                    .retrieve()
                    .bodyToMono(String.class)
                    .timeout(Duration.ofSeconds(10)) // Wait for max 10 seconds
                    .block(); // Blocking call to get the response

            System.out.println("Response: " + response);
            return true;
        } catch (Exception e) {
            System.out.println("API request timeout or error: " + e.getMessage());
            return false;
        }
    }

    public static void main(String[] args) {
        ApiCaller apiCaller = new ApiCaller();
        boolean result = apiCaller.makeApiCall();
        System.out.println("API call successful? " + result);
    }
}


{
  "type": "webhook",
  "url": "http://your-ai-service:5000/analyze",
  "method": "POST",
  "payload": {
    "metrics": "{{ execution.context.api_metrics }}"
  },
  "successConditions": {
    "rollback_triggered": true
  }
}

