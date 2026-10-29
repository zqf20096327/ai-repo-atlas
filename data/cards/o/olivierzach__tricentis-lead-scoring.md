# olivierzach/tricentis-lead-scoring

⭐ 49 · Python · 推送 2026-09-26 · [GitHub](https://github.com/olivierzach/tricentis-lead-scoring) · 组织维护

**面向营销销售线索的 ML 打分系统：预测转化概率并过滤线索**

Georgia Tech 与 Tricentis 合作的毕业设计仓库：基于 1000+ 营销销售漏斗变量（营销渠道、网站触点、CRM 触点、增强数据）做数据清洗与特征工程，测试逻辑回归、随机森林、Boosted Trees、深度神经网络等模型，最终选定 Boosted Trees（ROC-AUC .86，Precision .22，约为其他模型 5 倍）序列化上线；提供 Flask API 模板响应 POST 请求返回概率得分与接受标记，附 Dockerfile 封装依赖。原始数据受 NDA 限制不可共享。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 折交叉验证与 precision-recall 阈值分析完成多模型选型
- Flask API 模板返回线索转化概率分与接受标记
- 高基数类别编码、旅程路径编码、TF-IDF URL/内容分桶等特征工程
- 处理约 1% 极不平衡数据与删失防泄漏

## 适用场景

- 市场团队用打分结果过滤线索、只把高分线索交给销售
- 基于高分未填表访客做重定向投放
- 分析哪些因素驱动线索转化以优化网站内容

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L15: Goal of this project is to develop a machine learning system that scores leads likelihood to convert based on inter
> L87: Template sets up a simple API to respond to a post request with the model's probabilistic score of sales acceptance

## 星数曲线

```mermaid
xychart-beta
    title "olivierzach/tricentis-lead-scoring 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-29 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `9661423ed203` · [字段定义](../../DATASET.md)*
