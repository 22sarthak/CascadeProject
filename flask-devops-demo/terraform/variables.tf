variable "ssh_key_name" {
  description = "Name of the SSH key pair to use for the EC2 instance"
  type        = string
}

variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-west-2"
}
