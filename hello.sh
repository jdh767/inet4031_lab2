#!/bin/bash
      a=2
      b=2
      c=$((a + b))
      echo "Bash says: Hello, World!"
      echo "$a + $b = $	"
      mylist=("user1" "user2" "user3")
      for i in ${mylist[@]};
      do 
	 echo $i
      done 
