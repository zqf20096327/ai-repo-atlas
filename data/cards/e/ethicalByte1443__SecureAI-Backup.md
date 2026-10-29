# ethicalByte1443/SecureAI-Backup

⭐ 18 · Python · 推送 2026-08-22 · [GitHub](https://github.com/ethicalByte1443/SecureAI-Backup) · 个人维护

**企业备份的 AI/ML 数据防泄漏与勒索软件检测平台**

面向企业备份与灾难恢复场景的安全平台：用 Luhn 校验、正则与 TF-IDF+逻辑回归上下文分类器、SentenceTransformers 语义嵌入检测敏感数据（PII、金融数据、云凭证）；用香农熵引擎与 100 棵树的随机森林分类器（5 个结构特征）识别勒索软件高熵文件并自动隔离批次到 quarantine 目录。另含蜜罐诱饵文件与取证告警、AES-256 Fernet 加密、CEF/JSON 格式 SIEM 导出（Splunk/Elastic/QRadar）。以 FastAPI 服务提供，带 Web 仪表盘、Docker 部署与 pytest 测试套件。

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

- 多层 DLP：正则+Luhn+TF-IDF 上下文分类+语义嵌入检测 PII/凭证
- 香农熵引擎+随机森林分类器检测勒索软件并自动隔离批次
- 蜜罐诱饵文件与 canary 触发 CRITICAL 取证告警
- CEF/JSON 格式 SIEM 遥测导出，支持 Splunk/Elastic/QRadar 接入

## 适用场景

- 备份前扫描文件系统，防止敏感数据（PII、密钥）进入备份
- 检测并隔离被勒索软件加密的备份批次
- 通过蜜罐诱饵发现对备份数据的未授权访问
- 将安全事件导出到企业 SIEM 做集中监控

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L23: * **Context Classifier**: TF-IDF N-Gram Vectorizer + Scikit-Learn Logistic Regression (`data/models/context_model.j
> L27: * **Shannon Entropy Engine**: Calculates byte entropy $H = -\sum_{i=1}^{n} p_i \log_2 p_i$ per file (0.0 to 8.0 bit
> L28: * **Random Forest ML Classifier**: 100-estimator Random Forest (`data/models/ransomware_model.joblib`) trained on 5

## 星数曲线

```mermaid
xychart-beta
    title "ethicalByte1443/SecureAI-Backup 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `34ad7532bc3a` · [字段定义](../../DATASET.md)*
