import grpc

import greeting_service_pb2
import greeting_service_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:8080") as channel:
        stub = greeting_service_pb2_grpc.GreetingServiceStub(channel)

        request = greeting_service_pb2.HelloRequest(name="Ruslan")
        for response in stub.greeting(request):
            print(response)


run()