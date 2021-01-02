variable "AWS_ACCESS_KEY" {}
variable "AWS_SECRET_KEY" {}
variable "AWS_REGION" {
   default = "ap-south-1"
 }
variable "AWS_AMIS" {
   default = {
    ap-south-1 = "ami-04b1ddd35fd71475a"
    }
 }


