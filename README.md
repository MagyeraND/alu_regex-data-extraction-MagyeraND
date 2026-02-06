# alu_regex-data-extraction-MagyeraND


## Description
A Python program that uses regex to extract and validate structured data from raw text. Built with security awareness to handle and reject malicious or malformed input.

## Data Types Extracted
- Email addresses
- URLs
- Phone numbers
- Currency amounts
- phone numbers
- card numbers

## Security Features
- Detects and rejects SQL injection and XSS attempts
- Masks sensitive data (e.g., credit card numbers) in output
- Filters out malformed or unsafe input

## How to Run
```bash
node extractor.js
```
