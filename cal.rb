def format_name(f_name , l_name , age )
    if f_name ==""  or l_name == "" or age ==""
       return "You Have not provided complete input!"
    end
    formated_f_name = f_name.upcase()
    formated_l_name =  l_name.upcase()
    return  "Your real name is "  + formated_f_name + " " + formated_l_name + " " + age
end
    puts "What is your First Name?"  
    f_name = gets.chomp()
    puts "What is your Last Name?"  
    l_name = gets.chomp()
    puts "What is your Age?"  
    age = gets.chomp()
message =  format_name(f_name , l_name  ,  age  ) 
p message 


 