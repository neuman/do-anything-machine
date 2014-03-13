from pybrain.structure import *
from pybrain.datasets import *
from pybrain.supervised.trainers import *


class NeuralNetwork:
	""" Wrapping the PyBrain module into a simple to use tool for the Do-Anything-Machine.

		by Sander Idelson
	"""


	def __init__(self):
		self.inputLayerSize = 1;
		self.inputLayerType = "Linear";
		self.outputLayerSize = 1;
		self.outputLayerType = "Linear";
		self.numberHiddenLayers = 1;
		self.hiddenLayerSizes = [2];
		self.hiddenLayerTypes = ["Sigmoid"]
		self.net = FeedForwardNetwork();


	def size(self, inputLayerSize, hiddenLayerSizes, outputLayerSize):
		self.inputLayerSize = inputLayerSize;
		self.hiddenLayerSizes = hiddenLayerSizes;
		self.numberHiddenLayers = len(self.hiddenLayerSizes);
		self.outputLayerSize = outputLayerSize;

	def type(self, inputLayerType, hiddenLayerTypes, outputLayerType):
		self.inputLayerType = inputLayerType;
		self.outputLayerType = outputLayerType;
		self.hiddenLayerTypes = hiddenLayerTypes;

	def create(self):
		self.connections = [];
		self.hiddenLayer = [];

		if (self.inputLayerType == "Linear"):
			self.inLayer = LinearLayer(self.inputLayerSize);
			self.net.addInputModule(self.inLayer);

		elif(self.inputLayerType == "Sigmoid"):
			self.inLayer = SigmoidLayer(self.inputLayerSize);
			self.net.addInputModule(self.inLayer);

		else:
			print self.inputLayerType, " is not implemented yet."

		if (self.outputLayerType == "Linear"):
			self.outLayer = LinearLayer(self.outputLayerSize);
			self.net.addOutputModule(self.outLayer);
		elif(self.outputLayerType == "Sigmoid"):
			self.outLayer = SigmoidLayer(self.outputLayerSize);
			self.net.addOutputModule(self.outLayer);
		else:
			print self.outputLayerType, " is not implemented yet."

		for i in range(self.numberHiddenLayers):
			if (self.hiddenLayerTypes[i] == "Linear"):
				self.hiddenLayer.append(LinearLayer(self.hiddenLayerSizes[i]));
				self.net.addModule(self.hiddenLayer[i]);

			elif(self.hiddenLayerTypes[i] == "Sigmoid"):
				self.hiddenLayer.append(SigmoidLayer(self.hiddenLayerSizes[i]));
				self.net.addModule(self.hiddenLayer[i]);
			else:
				print self.hiddenLayerTypes[i], " is not implemented yet."
				break;

		for i in range(self.numberHiddenLayers+1):
			if (i == 0):
				c = FullConnection(self.inLayer, self.hiddenLayer[i]);
			elif (i == self.numberHiddenLayers):
				c = FullConnection(self.hiddenLayer[i-1], self.outLayer);
			else:
				c = FullConnection(self.hiddenLayer[i-1],self.hiddenLayer[i]);
			self.net.addConnection(c);

		self.net.sortModules();

	def activate(self, input):
		return self.net.activate(input);


	def supervisedTrainingDataSet(self, input, output):
		self.supervisedDataSet = SupervisedDataSet(self.inputLayerSize, self.outputLayerSize);
		if (len(input) == len(output)):
			for i in range(len(input)):
				self.supervisedDataSet.appendLinked(input[i], output[i]);
		else:
			print "Input and Output are not the same length."
	def supervisedTrainingSetup(self, learningrate=0.01, lrdecay=1.0, momentum=0.0, verbose=False, batchlearning=False, weightdecay=0.0):
		self.trainer = BackpropTrainer(self.net, self.supervisedDataSet, learningrate, lrdecay, momentum, verbose, batchlearning, weightdecay);
	def supervisedTrain(self):
		self.trainer.train()

net = NeuralNetwork();
net.size(2,[3],1);
net.type("Sigmoid",["Sigmoid"],"Sigmoid")
net.create()

input1 = [[0,0],[1,0],[0,1],[1,1]];
output1 = [[1],[2],[3],[4]];

print "old: ", net.activate([1,1])

net.supervisedTrainingDataSet(input1,output1)
net.supervisedTrainingSetup(learningrate=2)
net.supervisedTrain()

print "new: ", net.activate([1,1])