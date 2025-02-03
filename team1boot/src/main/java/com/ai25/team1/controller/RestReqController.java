package com.ai25.team1.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.http.client.MultipartBodyBuilder;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.reactive.function.BodyInserters;
import org.springframework.web.reactive.function.client.WebClient;

@RestController
@RequestMapping("/tf")
public class RestReqController {
    @Autowired
    private WebClient webClient;

    @CrossOrigin(origins = "http://영훈 IP") // 허용할 출처
    @PostMapping("/service")
    public String detectService(MultipartFile file, String message){

        MultipartBodyBuilder bodyBuilder = new MultipartBodyBuilder();
        bodyBuilder.part("message", message);
        bodyBuilder.part("file", file.getResource());
        String result = webClient.post().uri("/detect")
                .contentType(MediaType.MULTIPART_FORM_DATA)
                .body(BodyInserters.fromMultipartData(bodyBuilder.build()))
                .retrieve().bodyToMono(String.class)
                .block();
        return result;
    }




}
