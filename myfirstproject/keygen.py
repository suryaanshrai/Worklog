import secrets

def secret_key():
  """Generates a long and random value for the SECRET_KEY setting."""
  chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*(-_=+)'
  secret_key = ''.join(secrets.choice(chars) for _ in range(50))
  return secret_key