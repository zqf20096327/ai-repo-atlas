# deflect-ca/baskerville

⭐ 31 · Python · NOASSERTION · 推送 2026-05-28 · [GitHub](https://github.com/deflect-ca/baskerville) · 组织维护

**应用层 DDoS 攻击检测引擎：用 ML 区分正常与异常 Web 流量**

Deflect 生态的分析引擎组件，针对 Layer 7 DDoS 攻击：将进入的 Web 请求按主机与来源 IP 分组为请求集，计算路径深度、唯一查询数、HTML/图片比等特征，再用离线训练的 novelty detector（修改版 Isolation Forest，基于 PySpark ML）预测请求集是否可疑，结果（预测与分数）与特征、模型存入 Postgres。可在线运行即时识别可疑 IP，或离线分析本地日志与 Elasticsearch 日志。依赖 Spark、Kafka、Postgres、Java 8，通过 Kafka/rawlog/es/training 四种管道运行，提供 Docker 开发环境与 Grafana/Prometheus 监控面板。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 请求集→特征向量→novelty detector 预测的正常/可疑判定管道
- 基于 PySpark ML 的修改版 Isolation Forest，训练数据只需小比例异常
- 支持 on-line 即时识别与 off-line 日志分析两种模式
- 提供 Kafka/rawlog/Elasticsearch/training 四种管道与 Grafana 监控面板

## 适用场景

- Web 站点运维中自动识别可疑 IP 与 DDoS 攻击
- 对本地或 Elasticsearch 中的历史访问日志做离线异常分析
- 以预测与分数为依据触发基础设施的响应动作

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L8: websites as they happen and give the infrastructure the time to respond properly. Baskerville is an analytics engine
> L30: *novelty detector*, trained offline on the feature vectors of a set of normal
> L31: request sets, is used to predict whether new request sets are normal or suspicious. The request sets,

## 星数曲线

```mermaid
xychart-beta
    title "deflect-ca/baskerville 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-30 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `4bfb3f329683` · [字段定义](../../DATASET.md)*
