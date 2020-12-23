> Fauvel, K., Lin, T., Masson, V., Fromont, É. and Termier, A., 2020. XCM: An Explainable Convolutional Neural Network for Multivariate Time Series Classification. *arXiv preprint arXiv:2009.04796*.

MTS classifiers are usually grouped into three categories: similarity-based, feature-based and deep learning methods.

Global explainability means that explanations concern the overall behavior of the model across the full dataset, while local explainability informs the user about a particular pre- diction.

**explainable model usually derive ex- planations by examining internal model structures and parameters.**

Gradient- weighted Class Activation Mapping (The method has been shown to provide faithful explanations with regard to the model)

![img](/Users/huangqiming/Desktop/Paper/explainable_neural_network/1*8iyCBSx6i2lRpnKLe5bIrg.png)

Grad-CAM identifies the regions of the input data that are important for predictions in convolutional neural networks using the class- specific gradient information

Grad-CAM can output two types of attribution maps from XCM architecture: one related to observed variables and an- other one related to time Attribution maps are heatmaps of the same size as the input data where some colors indi- cate features that contribute positively to the activation of the target output These attribution maps constitute the explanations provided to support XCM model predictions and are available at sample level.

**Multivariate time series classification**

> [Du *et al.*, 2020] M. Du, N. Liu, and X. Hu. Techniques for Interpretable Machine Learning. *Communications of the ACM*, 2020.

**Two levels of explanations are generally distinguished: global and local**

> [Ancona*etal.*,2018]M.Ancona,E.Ceolini,C.O ̈ztireli, and M. Gross. Towards Better Understanding of Gradient- Based Attribution Methods for Deep Neural Networks. In *Proceedings of the International Conference on Learning Representations*, 2018.

The approaches based on back-propagation are seen as the state-of-the-art explainability methods for deep learn- ing models 

## identified topic and how

give an explanation process of the classification

Train a classification model and extracted the weights layer wise 

Does the neural network really learning what we want ??? Probably not 

Understanding the data 

## supplement

虽然这个GAP不是新的技术，但是在论文《Learning Deep Features for Discriminative Localization 》中，他们发现了GAP的一个作用，能保留空间信息并且定位（localization）?

CNN Visualization: https://poloclub.github.io/cnn-explainer/

我们企图通过不同的手段来解释这些既有的黑盒算法，从而来解释这些黑盒模型的决策依据。比较典型的两种方式是敏感性分析（Sensitivity Analysis）和基于梯度的方法（Gradient-based Methods -> saliency map）

## concepts

Saliency Maps

Gradient- weighted Class Activation Mapping

知识图谱：认知智能

Capsule Network

> four types of explanation mathods:  https://www.youtube.com/watch?v=AFC8yWzypss

​	perturbation-Based: mask each part of the image, and classifiy -> Sensitivity Analysis

​	Function-Based

​	Surrogate-/Sampling-Based, gradient x input -> noisy because of the (local gradient)

​	Structure-Based

​	comput some **relevence value** and sum of a prediction, **deep taylor decomposition** 

​	LRP : <font color=#B22222>Layer-wise Relevance Propagation</font>

Meta-explanation

neuralizing k-means

## thinking

线性回归是一个可解释性的模型，例如我们搜集于房价相关的十个类别的数据，那么当我们线性回归以后，

> 通过我们的学习，CHAS排在第二大的位置，相当于是临河的房子房价越高，不临河的房子房价就比较低

我们就知道，<font color=#B22222>怎么样做可以达到更好的效果</font> 。这是可解释性的第一个验证方式。在CNN里呢？

## path

1. explaiable neural network
2. how to show the explanation of a neural network
3. find some explaiable model (machine learnign, linear regression)
4. try to use linear regression to show the explanation of convolutional neural network(value and positon, change value or position to improve the prediction probability), using Layer-wise Relevance Propagation

