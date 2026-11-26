# chainstacklabs/web3-ai-trading-agent

⭐ 70 · Python · Apache-2.0 · 推送 2026-11-24 · [GitHub](https://github.com/chainstacklabs/web3-ai-trading-agent) · [官网](https://chainstack.com) · 组织维护

**教程：教开发者本地搭建 Web3 AI 交易代理**

配套 YouTube 视频的实操教程仓库，指导构建在 BASE 链上通过 Uniswap V4 交易 ETH-USDC 的 AI 代理。流程覆盖从手动交易到全自主代理的演进，采用本地优先架构：用 MLX-LM 做 LoRA 微调、PyTorch 训练 GAN 生成合成数据、Gymnasium 做强化学习环境、Ollama 本地推理、Foundry 分叉主网做纸面交易。明确声明不适用于生产环境，仅供学习。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | `idea` | |

## 能力要点

- 本地优先：MLX-LM 微调、Ollama 推理、Foundry 本地分叉主网
- 教师-学生蒸馏流程：QwQ 32B（经 OpenRouter）蒸馏到 Qwen 2.5 3B
- GAN 合成数据 + Gymnasium 强化学习训练交易策略
- Foundry 纸面交易支持在真实市场数据上测试策略

## 适用场景

- 学习 Web3 AI 交易代理的完整技术管线
- 在 BASE/Uniswap V4 上做本地化纸面交易实验
- 实践 LoRA 微调与模型蒸馏的端到端流程

## 场景标签

`金融量化` `教程课程` `微调` · 领域:学习与行业

## 证据(README 行号)

> L1: # Web3 AI trading agent—hands-on walkthrough
> L13: This project builds a Web3 AI trading agent that operates on the ETH-USDC pair on BASE blockchain using Uniswap V4.
> L9: ⚠️ NOT FOR PRODUCTION: This code is for learning purposes only. We assume no responsibility for the code or its usag


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `ebdeeba4421b` · [字段定义](../../DATASET.md)*
