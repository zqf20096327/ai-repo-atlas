# aliyun/oss-connector-for-ai-ml

⭐ 27 · Python · MIT · 推送 2026-09-20 · [GitHub](https://github.com/aliyun/oss-connector-for-ai-ml) · [官网](https://ossconnector.github.io) · 组织维护 · 中文 README

**连接 PyTorch 等训练/推理框架与阿里云 OSS 的 Python 库**

面向 AI/ML 场景的 Python 库集合，用于对接阿里云 OSS 对象存储。包含两个库：OSS Torch Connector 面向训练场景，支持从 OSS 加载数据集及读写 checkpoint/DCP/safetensors 文件；OSS Model Connector 面向推理场景，从 OSS 加载大模型文件到本地推理框架。核心组件基于 PhotonLibOS 以 C++ 实现，以动态链接库形式打包进 wheel 包，本仓库仅含 Python 代码。提供中文文档站点。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OSS Torch Connector：OSS 数据集加载与 checkpoint/DCP/safetensors 读写
- OSS Model Connector：从 OSS 加载大模型文件到本地推理框架
- 核心基于 PhotonLibOS 的 C++ 实现，以动态链接库随 wheel 分发

## 适用场景

- PyTorch 训练中直接从 OSS 读取数据集、保存/恢复检查点
- 推理服务启动时从 OSS 拉取大模型权重文件
- 国内使用阿里云 OSS 作为训练存储的团队做数据与模型文件管理

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L7: OSS Connector for AI/ML contains some high-performance Python libraries specifically designed for AI and ML scenario
> L11: - OSS Torch Connector is dedicated to AI training scenarios, including loading datasets from OSS and loading/saving
> L13: - OSS Model Connector focuses on AI inference scenarios, loading large model files from OSS into local AI inference

## 星数曲线

```mermaid
xychart-beta
    title "aliyun/oss-connector-for-ai-ml 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-27 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `01eb2db6b4c4` · [字段定义](../../DATASET.md)*
