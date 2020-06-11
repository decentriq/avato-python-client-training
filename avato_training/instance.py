from avato import Instance
import re
import numpy as np
from avato_training.classifier import LogisticRegressionClassifier

from .proto.csv_pb2 import (
    CsvResponse,
    CsvRequest,
)

from .proto.logregr_pb2 import (
    LogregrResult
)

import pandas as pd

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
        for category_name in configuration.categories_columns:
            if "|" in category_name:
                raise Exception(
                    "category name must not include pipe character (|) got "
                    + category_name
                )
        request = CsvRequest()
        request.uploadConfigurationRequest.***REMOVED*** = configuration.***REMOVED***
        request.uploadConfigurationRequest.dataFormat.categoriesColumns[:] = configuration.categories_columns
        request.uploadConfigurationRequest.dataFormat.valueColumn = configuration.value_column
        response = self._send_and_parse_message(request)
        if not response.HasField("uploadConfigurationResponse"):
            raise Exception(
                "Expected upload_configuration response, got "
                + response.WhichOneof("csv_response")
            )

    @Instance._secret_required
    @Instance._valid_fatquote_required
    def get_data_format(self):
        request = CsvRequest()
        request.getDataFormatRequest.SetInParent()
        response = self._send_and_parse_message(request)
        if not response.HasField("getDataFormatResponse"):
            raise Exception(
                "Expected get_data_format response, got "
                + response.WhichOneof("csv_response")
            )
        return response.getDataFormatResponse.dataFormat

    @Instance._secret_required
    @Instance._valid_fatquote_required
    def submit_data(self, data):
        if not isinstance(data, pd.DataFrame):
            raise Exception("data must be passed as pandas.DataFrame, got "
                + type(data).__name__
            )
        delimited_data = data.to_csv(index=False, sep="|")
        encoded_data = delimited_data.encode('utf-8')
        request = CsvRequest()
        request.submitDataRequest.data = encoded_data 
        response = self._send_and_parse_message(request)
        if not response.HasField("submitDataResponse"):
            raise Exception(
                "Expected submit_data response, got "
                + response.WhichOneof("csv_response")
            )
        return response.submitDataResponse.ingestedRows, response.submitDataResponse.failedRows

    @Instance._valid_fatquote_required
    def start_execution(self, ***REMOVED***):
        request = CsvRequest()
        request.triggerExecutionRequest.***REMOVED*** = ***REMOVED***
        response = self._send_and_parse_message(request)
        if not response.HasField("triggerExecutionResponse"):
            raise Exception(
                "Expected start_execution response, got "
                + response.WhichOneof("csv_response")
            )

    @Instance._secret_required
    @Instance._valid_fatquote_required
    def get_results(self):
        request = CsvRequest()
        request.getResultsRequest.SetInParent()
        response = self._send_and_parse_message(request)
        if not response.HasField("getResultsResponse"):
            raise Exception(
                "Expected get_results response, got "
                + response.WhichOneof("csv_response")
            )

        serialized_result = response.getResultsResponse.serializedResult
        logregr_result = LogregrResult()
        logregr_result.ParseFromString(bytes(serialized_result))
        params = self._convert_to_params(logregr_result.logregrResult)
        clf = LogisticRegressionClassifier(params)
        return clf

    def _convert_to_params(self, results):

        def parse_param(p):
            pattern = 'model \((\S+)\) - param \((\d+),(\d+)\)'
            match = re.search(pattern, p)
            class_label, ir, ic = match.group(1,2,3)
            return class_label, int(ir), int(ic)

        parsed_params = {}
        for r in results:
            class_label, ir, ic = parse_param(r.parameterName)
            parsed_params[(class_label, ir, ic)] = r.parameterValue

        max_ir = max([ir for _, ir,  _ in parsed_params.keys()])
        max_ic = max([ic for _,  _, ic in parsed_params.keys()])
        class_labels = list(set(cl for cl,  _, _ in parsed_params.keys()))

        assert max_ir == 0

        params = {}
        for cl in class_labels:
            p = []
            for ic in range(max_ic+1):
                p.append(parsed_params[(cl, ir, ic)])
            params[cl] = np.array([p])

        return params

    def _send_and_parse_message(self, message):
        response = self._send_message(message)
        csv_response = CsvResponse()
        csv_response.ParseFromString(bytes(response))
        if csv_response.HasField("failure"):
            raise Exception(csv_response.failure)
        return csv_response

