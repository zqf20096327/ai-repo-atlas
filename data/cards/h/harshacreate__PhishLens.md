# harshacreate/PhishLens

⭐ 3 · Python · MIT · 推送 2026-11-24 · [GitHub](https://github.com/harshacreate/PhishLens) · 个人维护

**检查链接与邮件文本钓鱼迹象并解释原因的 Flask 应用**

PhishLens 检查链接和邮件文本中的钓鱼迹象，对每个评分给出导致该评分的具体迹象说明，支持一次批量检查最多 25 条链接并保存报告。机器学习模型用自建链接训练，另附带外部公共链接集的评估结果；还有针对相似域名的额外检查以发现仿冒链接。普通检查不打开链接，可选的域名查询需用户批准并阻止本地/私有地址。提供 Docker 与源码两种运行方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 检查链接并解释各评分所依据的迹象
- 一次最多检查 25 条链接并保存报告
- 对比四个模型，相似域名额外检查
- 可选域名查询需用户批准并阻止本地/私有地址

## 适用场景

- 批量检查一批可疑链接并生成报告
- 分析邮件文本中的常见警示特征
- 教学/课程项目了解钓鱼检测流程

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L7: PhishLens checks links and email text for signs of phishing. It explains which signs led to each score. It can also 
> L41: Compares four models.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `1fb8e47413d0` · [字段定义](../../DATASET.md)*
