from concurrent import futures
import grpc
import logging

import predictor_pb2
import predictor_pb2_grpc



class PredictorService(predictor_pb2_grpc.PredictorServiceServicer):

    def predict(self, request, context):
        print ("Bonjour")
        return predictor_pb2.AccResponse( sides = AccRequest.sides, updown = AccRequest.updown, aboveunder = AccRequest.aboveunder )



def server () :

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    predictor_pb2_grpc.add_PredictorServiceServicer_to_server(PredictorService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

       

if __name__ == '__main__':
    print("Test server")
    logging.basicConfig()
    server()
