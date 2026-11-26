# 0x471/proof-gated-endpoint

⭐ — · [GitHub]() · 个人维护

**树莓派验证密码学证明后才放行 AI 服务器答案的防权重外泄端点**

在用户与可能被入侵的 AI 服务器之间部署一个树莓派端点：服务器对每个答案附带证明，端点验证后才放行，防止被窃的模型权重藏匿于回答内容中。项目包含软件实现、威胁模型、攻击目录与测量数据；对回复时序、顺序与故意失败等侧信道信号给出实验结果与缓解措施。处于进行中状态，受 ERA Frontier AI Security Residency 支持，声明非生产级安全。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 树莓派端点验证密码学证明后才释放 AI 服务器答案
- 针对时序、顺序、故意失败与 FlashProve 时序等侧信道的攻击目录与测量
- v1 加固版：Rust 实现、沙箱检查器、dm-verity、固定端口
- EZKL 与 FlashProve 两种证明后端的实验对比

## 适用场景

- 研究 AI 服务器侧信道泄露与模型权重外泄的防护
- 验证型推理端点的威胁建模与测量参考
- 复现 zkML（EZKL/FlashProve）证明检查实验

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: A Raspberry Pi checks cryptographic proofs before releasing an AI server's answers. The repository contains its soft
> L15: Work in progress, supported by ERA's Frontier AI Security Residency, October to December 2026. This is not producti


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 mid · 依据 README sha `e4b16a587efa` · [字段定义](../../DATASET.md)*
