from concurrent import futures
import grpc
import logging

import Predictor_pb2
import Predictor_pb2_grpc



class PredictorService(Predictor_pb2_grpc.PredictorServiceServicer):
#	oldsides = float(20)
#	oldupdown = float(20)
#	oldaboveunder = float(20)
	
	def predict(self, request, context):
		print (request.sides,request.updown,request.aboveunder)
#		check = CheckAccelerometre(request,2)
#		self.oldsides = request.sides
#		self.oldupdown = request.updown
#		self.oldaboveunder = request.aboveunder
#		print(self.oldsides)
		return Predictor_pb2.AccResponse( sides = request.sides, updown = request.updown, aboveunder = request.aboveunder )
       

#	def CheckAccelerometre(self,request,seuil):
#		if(self.sides == null):
#			return 0
#		if(not (self.sides - seuil <= request.sides <= self.sides + seuil)):
#			return 1
#		if(not (self.updown - seuil <= request.updown <= self.updown + seuil)):
#			return 1
#		if(not (self.aboveunder - seuil <= request.aboveunder <= self.aboveunder + seuil)):
#			return 1
#		return 0
	
	



def server () :

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Predictor_pb2_grpc.add_PredictorServiceServicer_to_server(PredictorService(), server)
    server.add_insecure_port('[::]:9333')
    server.start()
    server.wait_for_termination()

       

if __name__ == '__main__':
    print("start server")
    logging.basicConfig()
    server()
