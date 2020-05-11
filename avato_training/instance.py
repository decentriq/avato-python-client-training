from avato import Instance
from .proto.training_pb2 import (
    DataFormat,
    TrainingResponse,
    TrainingRequest,
)


class Configuration:
    def __init__(self, categories_columns, value_column, ***REMOVED***):
        self.categories_columns = categories_columns
        self.value_column = value_column
        self.***REMOVED*** = ***REMOVED***


class Training_Instance(Instance):
    @classmethod
    def get_type(cls):
        return "TRAINING"

    @Instance._secret_required
    @Instance._valid_fatquote_required
    def upload_configuration(self, configuration):
        request = TrainingRequest()
        request.uploadConfigurationRequest.***REMOVED*** = configuration.***REMOVED***
        request.uploadConfigurationRequest.dataFormat.categoriesColumns[
            :] = configuration.categories_columns
        request.uploadConfigurationRequest.dataFormat.valueColumn = configuration.value_column
        response = self._send_and_parse_message(request)
        if not response.HasField("uploadConfigurationResponse"):
            raise Exception(
                "Expected upload_configuration response, got "
                + response.WhichOneof("training_response")
            )

    def _send_and_parse_message(self, message):
        response = self._send_message(message)
        training_response = TrainingResponse()
        training_response.ParseFromString(bytes(response))
        if training_response.HasField("failure"):
            raise Exception(training_response.failure)
        return training_response

    @Instance._secret_required
    @Instance._valid_fatquote_required
    def get_data_format(self):
        request = TrainingRequest()
        request.getDataFormatRequest.SetInParent()
        response = self._send_and_parse_message(request)
        if not response.HasField("getDataFormatResponse"):
            raise Exception(
                "Expected get_data_format response, got "
                + response.WhichOneof("training_response")
            )
        return response.getDataFormatResponse.dataFormat

    @Instance._secret_required
    @Instance._valid_fatquote_required
    def submit_data(self, data):
        request = TrainingRequest()
        request.submitDataRequest.data = data
        response = self._send_and_parse_message(request)
        if not response.HasField("submitDataResponse"):
            raise Exception(
                "Expected submit_data response, got "
                + response.WhichOneof("training_response")
            )
        return (response.submitDataResponse.ingestedRows, response.submitDataResponse.failedRows)

    @Instance._valid_fatquote_required
    def start_execution(self, ***REMOVED***):
        request = TrainingRequest()
        request.triggerExecutionRequest.***REMOVED*** = ***REMOVED***
        response = self._send_and_parse_message(request)
        if not response.HasField("triggerExecutionResponse"):
            raise Exception(
                "Expected start_execution response, got "
                + response.WhichOneof("training_response")
            )

    @Instance._secret_required
    @Instance._valid_fatquote_required
    def get_results(self):
        request = TrainingRequest()
        request.getResultsRequest.SetInParent()
        response = self._send_and_parse_message(request)
        if not response.HasField("getResultsResponse"):
            raise Exception(
                "Expected get_results response, got "
                + response.WhichOneof("training_response")
            )
        return response.getResultsResponse.results
