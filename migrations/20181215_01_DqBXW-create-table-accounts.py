"""
Create database
"""

from yoyo import step

steps = [
    step("""
CREATE TABLE `accounts` (
  `id` int unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `cpf` varchar(11) UNIQUE NOT NULL,
  `creation` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) COLLATE 'utf8mb4_general_ci'
""", "DROP TABLE accounts")
]
