package com.ai25.team1.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.http.client.MultipartBodyBuilder;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.reactive.function.BodyInserters;
import org.springframework.web.reactive.function.client.WebClient;

@RestController
<<<<<<< HEAD
@RequestMapping("/tf/*")
=======
@RequestMapping("/tf")
>>>>>>> LYH
public class RestReqController {
    @Autowired
    private WebClient webClient;

    @PostMapping("/service")
    public String detectService(MultipartFile file, String message){
<<<<<<< HEAD
        System.out.println("java server_detect 시스템 실행----------");
=======
>>>>>>> LYH
        MultipartBodyBuilder bodyBuilder = new MultipartBodyBuilder();
        bodyBuilder.part("message", message);
        bodyBuilder.part("file", file.getResource());
        String result = webClient.post().uri("/detect")
                .contentType(MediaType.MULTIPART_FORM_DATA)
                .body(BodyInserters.fromMultipartData(bodyBuilder.build()))
                .retrieve().bodyToMono(String.class)
                .block();
<<<<<<< HEAD
        System.out.println("result 수행------");
=======
>>>>>>> LYH
        return result;
    }


}
