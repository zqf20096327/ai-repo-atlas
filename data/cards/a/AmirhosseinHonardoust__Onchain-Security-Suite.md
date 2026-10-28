# AmirhosseinHonardoust/Onchain-Security-Suite

⭐ 25 · Python · MIT · 推送 2025-11-20 · [GitHub](https://github.com/AmirhosseinHonardoust/Onchain-Security-Suite) · 个人维护

**Web3 安全工具套件：静态检测代币合约并 ML 评估部署者风险**

面向分析师与开发者的以太坊/EVM 安全流水线：静态分析 Solidity 代币合约，用正则规则提取 rugpull 相关特征（owner 铸造、费率操纵、黑名单等）并按权重计算 0-100 风险分；聚合部署者全部历史代币，用 RandomForest 分类器输出信任分与风险标签；通过 Etherscan V2 API 自动获取交易与已验证合约源码，另提供两个 Solidity 合约将审计与声誉结果上链存储。限制：训练标签来自简单规则（n_rugpull>=2 判为恶意），未验证合约被跳过，需先运行训练脚本生成模型文件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 正则规则提取 rugpull 特征并按权重求和得 0-100 风险分
- RandomForest（n_estimators=200, balanced）对部署者做风险概率评分
- Etherscan V2 自动拉取交易、合约源码并构建部署者历史
- 两个 Solidity 注册合约支持将审计结果与信任分上链

## 适用场景

- 审计 ERC-20 代币合约是否含 rugpull 结构特征
- 评估某个部署者地址的历史发币风险
- 把代币审计与部署者评分结果上链做透明存证

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L8: - **Machine learning–based reputation scoring** for deployer addresses
> L58:  - Uses a machine learning model to estimate “maliciousness probability”
> L364: * `RandomForestClassifier`

## 星数曲线

```mermaid
xychart-beta
    title "AmirhosseinHonardoust/Onchain-Security-Suite 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `0284993684ec` · [字段定义](../../DATASET.md)*
