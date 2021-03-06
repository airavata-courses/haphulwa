package hello;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class Application {
	@CrossOrigin(origins = "*")
    @RequestMapping("/")
    public String home() {
        return "Hello World from Java Microservice!";
    }

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }

}