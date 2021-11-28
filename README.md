# Solutions for Collision Avoidance of Warehouse Robots
ABSTRACT  
Mobile robots are widely used in various fields, such as unmanned aerial vehicles (UAV), unmanned ground vehicles (UGV), unmanned underwater vehicles (UUV), and so forth. It is because the single robot is only able to complete relatively simple tasks (while being helpless for complex and large-scale tasks) that a multi-robot system has emerged. The cooperation between multiple robots will not only promote the efficient completion of tasks and enhance the reliability of the system but advances cooperation to complete additional complex tasks. For a multi-robot system, the path planning and control of the robot is the basis for the successful completion of a particular task, which is simultaneously the key technology that needs to be solved. The application of warehousing robots can greatly improve the efficiency of e-commerce warehousing and logistics, as well as alleviating current situations of short supply in the warehousing and logistics industry. This article provides a multi-robot cooperative motion control method to solve the collision avoidance problem while the warehouse robot performs tasks.
Keywords: Robotic, Warehouse Robot, Machine Learning, collision avoidance, pathing planning, MDP.

1.	INTRODUCTION 
With the rapid development of e-commerce, traditional warehousing logistics are unable to adapt to the characteristics of modern logistics which includes a large number of varieties and short cycles. The mobile robot-based automated warehousing logistics technology has studied the method of planning the path of warehousing robots based on a linear time-series logic theory that has already been applied and developed. At present, the warehousing logistics industry has become the second largest application field of robots after the automotive industry. The application of warehouse robots can greatly improve the efficiency of e-commerce warehousing and logistics work, as well as alleviate the current situation of short supply throughout the warehousing and logistics industry. The purpose of robot application is to improve the inventory management and stowage capabilities of e-commerce companies; the core technology to achieve this objective is path planning. Path planning refers to planning a reasonable robot path according to the requirements of the manifest on the basis of the types of current warehousing logistics items and respective storage area; this procedure sets out to improve the operating efficiency of the warehousing robot. 
This article provides a multi-robot cooperative motion control method, which can plan a path that interacts with the environmental information according to the actual storage environment and task requirements. This method will also be able to solve the collision avoidance problem when the robot performs tasks.

2.	TASK DESCRIPTION
As shown in Figure 1, P1 is the starting point, P2 is the end point, the brown squares represent shelves, the blue squares on the shelf represent the target goods, and the blue square in the aisle is the robot. The robot starts from P1, reaches the pick-up location next to the target goods through the aisle, and then proceeds to the end point P2 after picking up the goods.
To study the collision avoidance problem, the number of robots is increased from one to three (as shown in Figure 2). Goods are randomly generated on the shelves, and robots of different colors need to take the goods of the corresponding color from the shelves. In this process, the problem of collision avoidance between robots or between robots and shelves needs to be solved. To solve this problem, two solutions are proposed.   
 
Figure 1
 
Figure 2

3.	METHOD
In this section, three methods are proposed. The advantages and disadvantages of each method are evaluated.

3.1	Pre-planned pathing
The first method is: because the warehouse environment is relatively simple (there are fewer influencing factors), and the shelf position is fixed, the path can be artificially set in advance in the path planning. As used in this article, the way to set the path in advance is to make the robot move vertically to the position with the same y coordinate of the pick-up point, and then move horizontally to the pick-up point. After picking up the goods, the robot will move horizontally and then move vertically until reaching the position, which is one square right of the end point, and will then move to the end point.
To prevent the robot from collision, before the robot moves, the robot will judge whether there are other robots in the desired position. If there is a robot, it will be judged as a collision risk, and the robot will move to the side. If there are robots or shelves on the side and cannot move, they will stay in place and wait.
The advantages of this method include: simpler operation, lower computational complexity, and lower time cost. The disadvantage is that the degree of intelligence is low. As the number of robots increases, they may fall into an infinite loop, where multiple robots may not move and cannot complete tasks.
3.2	Markov decision process (MDP)
Another method is to use the Markov Decision Process to implement path planning. Before introducing this method, we need to know the Markov Decision Process first. The Markov Decision Process (MDP) is a mathematical model of sequential decision, which is used to simulate the randomness strategies and rewards that can be achieved by the agent in an environment where the system state has Markov properties. MDP is constructed based on a set of interactive objects, namely agents and environments, and its elements include state, action, strategy, and reward. In the simulation of MDP, the agent perceives the current system state and implements actions on the environment according to the strategy, thereby changing the state of the environment and getting rewards. The accumulation of rewards over time is called rewards. The theoretical basis of MDP is a Markov chain, thus it is also regarded as a Markov model that considers actions. In terms of application, MDP is used to model reinforcement learning problems in machine learning. By using dynamic programming, random sampling and other methods, MDP can solve agent strategies that maximize returns, and be applied in topics such as automatic control and recommendation systems.
Path planning is a standard MDP problem. We can create a table by value iteration to store the mapping from states (such as the current position of the robot) to action a (control instruction). In this way, if the robot is placed at any position on the map, it can quickly determine its next action, and this action will guide the robot to move to the target point.
The advantage of this method is that it can better plan the robot's path. It can also avoid collisions after the number of robots increases, and there will be no situations in which the robots are stuck with each other and cannot move, which may result in those robots being unable to complete the task. But the disadvantage is that this method has high computational complexity and high time cost (in this map, each robot takes one to two seconds per step).
3.3	Optimization
When the robot is far away, the collision possibility is less. Therefore, the MDP can be used to realize path planning only when the robot is relatively close, that is, when there is a risk of collision. After experimentation and consideration, it is decided that there is a risk of collision within two steps between the robots. As shown in Figure 3, the robot is at the center of the 5 X 5 grid (ie, the black area). If there are other robots in the yellow area, it is judged to be at risk of collision. At this time, the MDP method is used to plan the path of this robot. This method can make the table in the MDP smaller (from 39 X 21 to 5 X 5), greatly reducing the computational complexity and reducing time cost.

4.	CONCLUSION
This article uses python programming in PyCharm to simulate and verify the above method. In the experiment of increasing the number of robots from 1 to 9 (the number in Figure 4 is six), this method can effectively avoid collisions between robots and complete the task. However, in some cases, the behavior of some robots will not be the optimal choice and, occasionally, there may be abnormal robot behaviors. In subsequent experiments, we will continue to optimize this method and explore other methods to better solve the problem of warehouse robot collision.

 
Figure 3


 
Figure 4



REFERENCES
[1]	Yang, Xuxi, and Peng Wei. ”Autonomous on-demand free flight operations in urban air mobility using Monte Carlo tree search.” International Conference on Research in Air Transportation (ICRAT), Barcelona, Spain. 2018.
[2]	Yang, Xuxi, Lisen Deng, and Peng Wei. ”Multi-agent autonomous on demand free flight operations in urban air mobility.” AIAA Aviation 2019 Forum. 2019.
[3]	Bertsekas, D. P. (2012). Dynamic programming and optimal control. Belmont, Mass: Athena Scientific.
[4]	Choset, H., Lynch, K. M., Hutchinson, S. (2005). Principles of robot motion: theory, algoritms, and implementations. Cambridge, MA: Bradford.
