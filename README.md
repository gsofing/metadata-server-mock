# metadata-server-mock

## Remarks on the service

- `preImage` is present on the README examples, but not in the metadata files.
- `anSignatures` in the README is present as `signatures` in the metadata files.
- The POST service is used to get data, and not to write any. The HTTP protocol doesn't make difference between methods, but it's a good practice to use GET for getting information and POST to post or publish.
- `post "/metadata/query"` with properties is equivalent to `get "/metadata/:metadata/properties/:property"`, with a different strategy of getting the expected properties. The post strategy filters the properties that were not mentionned in the query among a list called 'known_properties'. Nevertheless this list is not coherent to the metadata files: the list contains 'unit' that is not present in the metadata files, and does not contains 'decimals' nor 'policy', which leads to an unwanted behaviour which is that no matter which properties we request, we will always have those two fields along with the requested ones.
- The signature checks are being skipped, as the verifications are failing. There are 3 possibilities for this failing:
	* The signing/verifying protocol is not one used to produce the signature.
	* The encoding of the information (considered value, public_key, signature) is not correct.
	* The provided signatures are not correct, which seams unlikely as all the signature verifications fail the same way.
