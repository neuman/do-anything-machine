Artificial intelligence sounds awesome doesn’t it?  Machines that can solve problems on their own or answer questions for us would represent an enormous leap forward for all of mankind.  The problem is, artificial intelligence as it exists today is not very flexible.  Today AI’s are trading stocks, beating you at video games, and filtering spam out of your email and a myriad of other tasks; each one specialized for its particular chore.  Therein lies the rub, each AI needs to be custom built by a programmer who specializes in artificial intelligence or machine learning.  In other words, it is currently possible to build machines that learn, but not that can learn how to learn.  If we want machines that can truly solve problems, answer questions on their own, and eventually grow to be sentient minds, we need to overcome that obstacle.  


The "Do Anything Machine" is the first component in the theoretical Sentience Stack, an open source stack of software that when put together can be configured to learn to be a sentient mind.  It's inspired by the way LAMP, a bunch of disparate decoupled components were used together to make it easy to create websites, and that has allowed us to openly and exponentially expanded the internet. I'd like to do that with AI.  There are so many cool robots being made right now, and they deserve to have equally cool brains.  Also, solving the world's problems and all that, hopefully.  This project is obviously ambitious, but might be possible, and that seems like good enough reason to give it a try.  


1. Sentience Stack
1. Do Anything Machine
1. Solves any solvable problem given enough resources
1. Networked Layer
1. Compares notes with other stacks
1. Self Improvement Engine
1. Uses the Do Anything Machine to improve components of the stack itself
1. Problem Recognizer
1. Sorts through data to figure out what needs to be figured out
1. Creativity Jiggler
1. Gets the stack unstuck through randomness and rule breaking
1. Language Learner/User
1. Uses all layers of the stack to learn how to communicate 
Meta-Learning


People seem to be hardwired to learn how to learn from birth, through a process closely related to schematization called inductive transfer.  When a child first learns how to catch a ball, lets say a baseball, it’s difficult.  Often there are a lot of dropped throws and frustration, and the occasional incident of the child getting beaned, being a kid is tough.  But gradually, through a combination of sheer repetition, and exposure, the child learns how to catch the ball, and that first catch is a magical one.  Amazingly, if this child wants to learn how to catch a football, which is a distinctly different skill, the learning process is greatly shortened.  The child can learn how to catch the football faster because the hard part of learning to catch the baseball, was figuring out how to do that learning: learning how to learn to catch a ball.  Because that mechanism was already in place by the time football season rolled around, the child can apply the same pattern to the oblong pigskin and learn to catch it much faster.  


So machines need to be able to learn how to learn (meta-learn), but how can we imbue them with such a fundamentally brainy feature?  Many researchers have attempted to create a universally intelligent machine by duplicating the physical mechanisms of the brain.  This approach may eventually prevail, but for the moment our computational resources are nowhere near vast enough for the task.  Much like an airplane wing only resembles that of a bird, our AI should be inspired by the brain, but built in a manner that fits naturally into the way machines work.  As mentioned before, an individual AI expert may be able to custom make an AI to solve any given problem, so why not just automate that process?  The question becomes, how can an AI that tailors AI’s be built?  
The Do Anything Machine
There are hundreds of existing AI algorithms that are each good and bad at solving specific types of problems.  When a programmer sits down to solve a problem using AI they follow a fairly standard pattern.  


1. Compare the problem to others that have been solved using AI in the past.
2. Pick the one that seems the most similar.  
3. Apply the same algorithm and configuration to the new problem. 
4. Examine the results:
1. If they are good enough, mission accomplished. 
2. If they aren’t good enough, tweak the configuration and try again.
3. If they are really bad, or if the configuration has already been tweaked many times, start again at step 2 with the next most similar.  


This process can only work for problems that actually have solutions, which are referred to as tractable in computer science.  Automating this process implies the necessity for some sort of universal problem-statement-language, a toolkit of interchangeable AI algorithms, a problem-statement-similarity classifier, and a data-store to serve as the memory.  AI algorithm toolkits already exist, and virtually any database could serve as memory, but the universal problem-statement-language and its matching similarity classifier are tricky.  In fact, these two components may be the most significant obstacles to the writing of this theoretical program.  


Any problem that can be modeled can be expressed via programming language.  As such, it seems logical that the universal problem-statement-language be constructed of code itself, specifically as a class that can be subclassed and then fed into the machine.  Essentially expressing a question to a computer in a language it can already process even if it cannot comprehend yet.  


Problem Statement Class
1. Functions
1. Numerical Serializer
1. Converts the model state into a numerical representation
2. Doesn’t really matter how as long as it’s consistent 
3. Must be reversible
1. validation
1. boolean
2. checks to see if possible solutions meet stated criteria 
1. fitness
1. optional but recommended
2. rates possible solutions quality on a scale from 0 to 1
1. randomizer
1. generates a random state of the model
1. sequencer
1. optional but recommended
2. generates the appropriate state from the sequence of all possible states
1. Meta
1. Plain english (or whatever) description of the problem.  


This class is intended to be the interface between the do anything machine and whatever other programs are needed to are needed to accomplish these functions. For example, if we were training a do anything a machine to build a bridge, we would likely use some sort of physics libraries that have built in representation classes of their own as the model, and then write a custom serializer.  In this example, the validation function would likely deserialize a model from do anything machine output, and use the physics libraries to see if the bridge meets some pre-set requirements, like using a finite quantity of materials to build, being able to support a certain load, surviving earthquakes of a certain size, etc.  The fitness function would likely be a simple tally of how many of the sub-tests involved in validation pass (so if it survives earthquakes, but takes tons of materials, that’s a lower score).  


In the early stages of this project, when only the do anything machine exists or is being created, these problem classes would need to be coded by hand.  The hope is however, that eventually a Problem Recognizer can be created that is able to generate these on it’s own.


Operation
Solving a problem you know has a solution is like cracking a combination lock.  A specific series of steps will solve the problem, and can be deduced eventually by trying every possibility, but that would take a long time.  Instead, it makes more sense to use specialized techniques to get right to the answer faster, like listening to the pins as the tumbler turns.  The trick is knowing the right technique for the particular lock, and that is what the do anything machine is designed to learn.  


The first time a problem is posed to the do anything machine, it has no memory, and therefore no context to guide it to an efficient use of resources, so it just tries everything.  The full combination of algorithms and configurations are tried, and their results stored in memory.  The second time, it has context, but not enough to make comparisons, so it does repeats the process of trying every combination.  The third time, it is able to compare the new problem to both previous, and so it attempts to solve the new problem with whichever combination of algorithm and configuration yielded the best solution for the most similar of the previous.  If that combination does not yield a solution, it proceeds to the next best configuration, falling back on brute force dice rolling if all else fails.  Every time a new problem is added, the do anything machine’s context for new problems expands, and thus learning occurs.  
A Slider for the World’s Problems
There’s an adage in engineering:


        Quality, speed, money.  Pick any two.  


The idea being that you can only engineer something high quality and quickly if it’s costly, or high quality and cheaply if you can do it slowly, or quickly and cheaply if it’s ok that it is going to suck.  Unfortunately, the do anything machine is just as bound by this sacred triangle as human engineers are, but we can turn it on it’s head.  Quality is fixed by the problem statement validation function, so that leaves only time and money.  By definition the do anything machine solves any tractable problem given enough resources but specifically, if given enough CPU time.  Cloud computing has recently become very easy to use, and very cheap, so the only limit on CPU time is how much money is available.  More money means a faster solution, more time means a cheaper one.  
The Path To Intelligence
Human children typically don’t develop the ability to inductively reason until about age seven, and that’s with their brains absorbing information and being bombarded by simple problems every day.  Hopefully, it will take less input to get a do anything machine to begin to act intelligently since induction is hardcoded into the basic algorithm.  However, it may still take a huge number of problems for the do anything machine to learn to beat random chance.  


Like a child, a stack will not converge on intelligence without proper nurturing.  The first few problems fed into the machine will have enormous import to the way it understands future problems, and because we’re building a problem-solving-based intelligence, the way it understands all things.  Better start reading those baby books now.  
Networked Layer
We’ve established at this point that the do anything machine can solve any problem given sufficient resources.  We also know that the more problems each machine sees the smarter it gets, and it does that by learning to compare problems.  


So here’s where the real fun starts.  If the machines are networked, they can compare notes with each other to reduce the resources needed by everyone.  


For instance, a machine belonging to a plumber in Montana may have a question it’s having trouble with and so it runs a search and connects to a list of machines that are knowledgeable about the keywords ‘drip system’ ‘garden’ ‘timing’ and ask them if they’ve seen anything like it.  


A machine in Africa answers with some helpful examples, problems it has already solved and how.  One example even includes a whole new algorithm that was generated by using code evolution.  


The plumber’s machine downloads the examples and uses them as a starting point for it’s own exploration, shortening the time to find a solution.  Allowing the do anything machines to connect makes them all smarter faster.  


Self Improvement Engine
Determining the similarity of any two given problems is in itself an extremely difficult problem, one that has many possible approaches and great potential for optimization.  I propose that those optimizations be saved for a later time in favor of some extremely simple to implement approach.  Theoretically, the similarity determiner barely has to work in order for the do anything machine to begin converging on intelligence, and then that’s when the real fun starts.  If the do anything machine can at this point solve any tractable problem, and determining similarity of problems is a problem in of itself, it should be possible to ask the do anything machine “How do we make a better similarity determiner?”.  This process could theoretically be run on any of the components of the program.  


The ability to improve its own components in this manner is a perfect example of how the stack is inspired by but not duplicating nature.  Biological entities gradually improve themselves through evolution, a slow process that uses huge amounts of natural resources for incremental progress across an entire species.  The self improvement engine utilizes different means, but the ends are the same: exponential improvement.  The first fish to walk up onto land secured an enormous advantage that allowed it to reproduce many times more than it’s sea-bound competition.  More offspring means more chances for evolutionary advantage which means better offspring which means even more offspring; an exponential curve.  With the sentience stack improved components means more efficient processing which means better problem solving which means better component improvements.  This process may be tied to the technological singularity, if we’re lucky.  


Creativity Jiggler
When people are trying to solve a problem and find themselves stuck, or bored, they get creative.  For example, a person designing a bridge may have a design based on everything he’s ever seen but simulations show that it doesn’t carry the required load.  The real issue is that every little tweak that makes sense just makes the bridge worse, it seems to be as good as it can possibly be.  At this point, creativity happens.  I won’t pretend to understand the mystical process, but I will wager that it involves mentally exploring all possibilities whether they are logical or not, also known as lateral thinking.  If the bridge designer is creative, they may try out designs that seem completely ridiculous to them until one proves to be the next avenue of exploration.  


The name really says it all about this component.  The jiggler is designed to approximate creativity by breaking the rules.  It’s entire job is to suggest things that do not make sense in the event that the machine gets stuck.  Clearly the quality of the bridge is being measured by the load it bears.  So if you think about the quality of the bridge as a graph, the designer above was stuck at a point on top of a small hill on the graph.  Adjustments in any direction caused the quality to go down that hill, but somewhere, on the other side of one of that valley there is a much bigger hill, with the optimal bridge design sitting on top of it.  The jiggler exists to kick the sentience stack down into the valley to find a hill that’s tall enough.  


Creativity is a mysterious but critical component in any sentient mind because it’s required to think something totally new.  


Problem Recognizer
In the initial phases of this project, only programmers will be able to communicate with the minds that are being created.  While these simplistic interactions are the only way to start, an AI that can only be operated by AI specialists is what we already have.  Because a piece of technology is only as good as what it can do, and that is limited by its interface, the stack needs to be able to communicate with regular people on its own.


No one feeds people broken-down problems to be solved in their everyday lives.  We are constantly absorbing enormous quantities of data and figuring out what things we actually need to figure out all on the fly.  The first step towards making the stack able to operate without a programmer is to enable it to write its own problem classes to feed into the do anything machine. The question as always, is how.  How can a machine be designed that can, when presented with raw data, sieve a problem out of that data? 


I have no idea and I need a good way to say so.  Woops!
Language Learner


In order to really communicate with non-programmers, the stack needs to be able to talk.  Theoretically, learning language is just another problem to be solved, and so the do anything machine should be able to handle it.  In reality however, the problem of learning a language is much more esoteric than the types of problems the do anything machine is optimised for.  For starters, how does one define when language has in fact  been learned?  


As usual, I think the answer lies in human learning.  We gain language through exposure, connection building, and rule acquisition, and so will the stack.  In human terms, I’m talking about grammar school; a series of specifically ordered problems that are solved with relation to a common dataset or vocabulary/grammar.  It may be advantageous to pair the existing stack components with existing ontological databases.  


Language acquisition is one of the most complicated things that sentient beings do, and I’m not sure what the right approach is.  However, this component will be needed for a stack to make the jump from a machine intelligence to sentience because language allows it to asks questions of its own.  Not to mention, grants it the ability to pass a Turing Test.  




Challenge and Conclusion


The most important aspect of implementation is you.  The sentience stack will be open source from day one, allowing anyone to contribute, or attempt alternate approaches as they see fit.  There are many complicated problems that need to be solved in both the framework, many existing algorithms to be standardized and added to the do anything machine’s toolkit and many questions to be answered.  These obstacles may be abundant, but I think they can be overcome by the contributions of the open source community.  

There is always the chance that what is discussed above won’t work, that the machine will never converge on self awareness, or can’t even learn how to learn, after all people have tried to do things like this before.  I believe that a thing cannot be fully understood until it can be recreated, and mankind has never been able to recreate conscious self-awareness, the thing that separates us from so many of the other animals we share this planet with.  The need to understand ourselves is what continues to make the pursuit of artificial sentience worthwhile.  Besides, the worst thing that can happen is that we learn one more way not to do it.  


So many unsolved problems exist in this world that could be eased with the aid of this technology.  From disease and famine to design and fashion, the sentience stack could break down barriers.  It can assist us with creative problems the way a calculator assists us with math problems, handling the issues for which a solution is known to exist and freeing up the user to solve more complicated macro-problems faster and more easily.  


None of this can be done by one person, it is the type of thing that requires many viewpoints and skill sets to create.  If you think it can be done, I challenge you to try, if you don’t I challenge you to prove it.  


________________






   This file is part of The Sentience Stack.

   The Sentience Stack is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   The Sentience Stack is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with The Sentience Stack.  If not, see <http://www.gnu.org/licenses/>.