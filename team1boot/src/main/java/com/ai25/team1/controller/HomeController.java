package com.ai25.team1.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
<<<<<<< HEAD
@RequestMapping("/tf/*")
public class HomeController {
    @GetMapping(value = {"/", "/home"})
=======
@RequestMapping("/tf")
public class HomeController {
    @GetMapping("/")
>>>>>>> LYH
    public String home(){
        return "index";
    }

    @GetMapping("/train")
    public String train(){
        return "train";
    }
}
