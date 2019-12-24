# best : {'gamma': 0.4, 'learning_rate': 0.05740649534056902, 'max_depth': 5, 'min_child_weight': 6, 'n_estimators': 166, 'subsample': 0.6}
# best param after transform :
# {'gamma': 0.04000000000000001, 'learning_rate': 0.05114812990681138, 'max_depth': 10, 'min_child_weight': 7, 'n_estimators': 316, 'subsample': 0.56}
# rmse of the best xgboost: 6136.126337046346

import matplotlib

# Force matplotlib to not use any Xwindows backend.

matplotlib.use('Agg')
from hyperopt import fmin, tpe, hp, partial
import numpy as np
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error, zero_one_loss
from sklearn.metrics import log_loss
import xgboost as xgb
import pandas as pd
from xgboost import plot_importance
from matplotlib import pyplot as plt
totalcount=10
Devide="edge"
#----------------------------------------------01----------------------------------------------------------
attribute = pd.read_csv(str(totalcount)+"-"+Devide+'-two-data.csv')
label = pd.read_csv(str(totalcount)+"-"+Devide+'-two-label.csv')


label=label['totalLatency']
attribute=attribute.loc[:,~attribute.columns.str.contains('^Unnamed')]


X=attribute
#print(X)

y=label

# ############################################################
# #----------------------------------------------04----------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size = 0.2, random_state=42)
print(X_train.dtypes)

dtrain = xgb.DMatrix(data=X_train,label=y_train,missing=-999.0)
dtest = xgb.DMatrix(data=X_test,label=y_test,missing=-999.0)
DATA=xgb.DMatrix(data=X,label=y,missing=-999.0)
evallist = [(dtest, 'eval'), (dtrain, 'train')]

space = {"max_depth": hp.randint("max_depth", 15),
         "n_estimators": hp.randint("n_estimators", 300),
         'learning_rate': hp.uniform('learning_rate', 1e-3, 5e-1),
         'gamma': hp.randint('gamma', 5),
         "subsample": hp.randint("subsample", 5),
         "min_child_weight": hp.randint("min_child_weight", 6),
         }
#------------------------------------------------------------03------------------------------


def argsDict_tranform(argsDict, isPrint=False):
    argsDict["max_depth"] = argsDict["max_depth"] + 5
    argsDict["gamma"] = argsDict["gamma"] *0.1
    argsDict['n_estimators'] = argsDict['n_estimators'] + 150
    argsDict["learning_rate"] = argsDict["learning_rate"] * 0.02 + 0.05
    argsDict["subsample"] = argsDict["subsample"] * 0.1 + 0.5
    argsDict["min_child_weight"] = argsDict["min_child_weight"] + 1
    if isPrint:
        print(argsDict)
    else:
        pass

    return argsDict
#------------------------------------------------------05----------------
def xgboost_factory(argsDict):
    argsDict = argsDict_tranform(argsDict)

    params = {'nthread': -1,  # 进程数
              'max_depth': argsDict['max_depth'],  # 最大深度
              'n_estimators': argsDict['n_estimators'],  # 树的数量
              'eta': argsDict['learning_rate'],  # 学习率
              'subsample': argsDict['subsample'],  # 采样数
              'min_child_weight': argsDict['min_child_weight'],  # 终点节点最小样本占比的和
              #'objective': 'reg:linear',
              'silent': 0,  # 是否显示
              'gamma': 0,  # 是否后剪枝
              'colsample_bytree': 0.7,  # 样本列采样
              'alpha': 0,  # L1 正则化
              'lambda': 0,  # L2 正则化
              'scale_pos_weight': 0,  # 取值>0时,在数据不平衡时有助于收敛
              'seed': 100,  # 随机种子
              'missing': -999,  # 填充缺失值
              }
    params['eval_metric'] = ['rmse']

    xrf = xgb.train(params, dtrain, params['n_estimators'], evallist, early_stopping_rounds=200)
    joblib.dump(xrf, str(totalcount)+'-only-twoxgboost-'+Devide+'.pkl')
    plot_importance(xrf)
    plt.subplots_adjust(left=0.30, wspace=0.25, hspace=0.25,
                        bottom=0.13, top=0.91)
    plt.savefig(str(totalcount)+"-only-twoxgboost-"+Devide+".png")


    plt.show()
    return get_tranformer_score(xrf)


def get_tranformer_score(tranformer):
    xrf = tranformer
    dpredict = xgb.DMatrix(X_test)
    prediction = xrf.predict(dpredict, ntree_limit=xrf.best_ntree_limit)

    return mean_squared_error(y_test, prediction)

#------------------------------------------06-------------------
algo = partial(tpe.suggest, n_startup_jobs=1)
best = fmin(xgboost_factory, space, algo=algo, max_evals=100, pass_expr_memo_ctrl=None)

#------------------------------------07------------
RMSE = xgboost_factory(best)
print('best :', best)
print('best param after transform :')
argsDict_tranform(best,isPrint=True)
print('rmse of the best xgboost:', np.sqrt(RMSE))
# d= joblib.load('twoxgboost.pkl')
#
# y= d.predict(DATA)
# np.savetxt("Y1.txt", y, fmt="%d", delimiter=",")