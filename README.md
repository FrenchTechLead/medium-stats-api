# USAGE
REQUEST :

```POST: https://jwt-fast-signer.herokuapp.com/```
```json
{
	"payload": {
		"aud": "A0487",
		"iss_profileid_lblogidn": " testconsul ",
		"iss": "A0533",
		"source": "ESP_CLIENT",
		"exp": 1593595163,
		"iat": 1593508763,
		"iss_profileid_idfid": 1
	},
	"private_key": "MIICdQIBADANBgkqhkiG9w0BAQEFAASCAl8wggJbAgEAAoGBAKCYogJbIQokdvUlVPjq/V15aZsaPiKARHEzQAhosbxSLM/llA59XTjihruYC233M6c/zMv/jQ4XNyCxT99dYhsXap0qIwbH5rdOVpSX5pdorbBYc6CoHqHiVCen6aLCrbrsI7DneId4TFtPQ3gwl7eXRilXfozNc05khYrSqYWfAgMBAAECgYAtDoWtqYmcgdyKLN4pNCy/k/fIF1XFcj1BkUJu2Yi8MEX4Ug32/r8v3YY1jZPvV0K7ss+vkFQv1t2Vo4moPlfuleQaSgb+yPqV9vW3viD8D1/0CelGsj7gcE+LWspn7krjwmLzX/zZs3OJLVgDXpLF5DRwykUmX/XWjA8rv8RFaQJBANft1y5ikV53CaHm1pMujaCdwjHTy6Cg+xdTokkUx2GLgrp+PvMRLQP2tyl3MdA8YP/4PYjQM9PDu58ZyXSLevsCQQC+ZhcqeReygyS05GDc0dk9x62+2ky+rhuIocQ6Qmfy81OXHslOxiUHNCXeaaYzDLyzpZDTSlSdrjOqWEenmh6tAkB78vd2lPZFd6d73HqH+k0qSeTTnXRiPIZmGYgq01awU9kzHI0eEln40ILLtrRNiJtV1DXed0WI5e6poa/WyspJAkAIJurbALBJDmBl9llHWxzIDmKcB1C94UqAgRybufglaNGtaL4Jx2YSduMgMLnS+bqinnYi9c3Fqo2/v2PiAzFJAkAGl3Yk4ow3kE08mJ0V+V/wSmsAPdE2ceYXjX4g56WjhUkjB0+JBrxMF+OtSlUlWYlc+5Lc9G2UuPA5g1HQA6PN"
}
```

RESPONSE :
```eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJBMDQ4NyIsImlzc19wcm9maWxlaWRfbGJsb2dpZG4iOiIgdGVzdGNvbnN1bCAiLCJpc3MiOiJBMDUzMyIsInNvdXJjZSI6IkVTUF9DTElFTlQiLCJleHAiOjE1OTM1OTUxNjMsImlhdCI6MTU5MzUwODc2MywiaXNzX3Byb2ZpbGVpZF9pZGZpZCI6MX0.ggm6vitGzanM6H7kKlkCTIatjxKA4UjgRmPSBYP578HLqVlqMDrAvdTD_MqBVk3njnLVCYCmaoTPpSfqKsaGIe-FUBJGAiGCVd7EIqtDMeQcGLgTro8AzDTOOYQB-m9Qr08xBsnY2-OvNM6wPC3WXes-sv2NLH7Ew6zdvmxrbtQ```