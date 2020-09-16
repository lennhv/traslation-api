# traslation API

This API uses google spreadsheets to perform translations

The API has two endpoins

* api/v1/traslations/  
    
    This endpoint receives a JSON request and returns a job id that will be used in the second endpoint

    ```json
    {
        lang_source*	string ISO lang
        lang_target*	string ISO lang
        text*   [string]
    }
    ```


* api/v1/traslations/{uuid}/

    The translation is an async task and the result is obtained with this endpoint

    ```json
    {
        traslation* [string]
    }
    ```

