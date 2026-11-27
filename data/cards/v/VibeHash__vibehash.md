# VibeHash/vibehash

⭐ 3 · Python · MIT · 推送 2026-11-23 · [GitHub](https://github.com/VibeHash/vibehash) · [官网](https://vibehash.org) · 个人维护

**让矿工训练 AI 模型来挖币的 PoUW 加密货币测试网**

一种以有用功为共识的加密货币测试网：矿工不执行哈希运算，而是在中低端硬件上分小块训练 AI 模型（CSV 任务、Qwen3-0.6B/4B 微调、DeepSeek 试点），每块经验证的工作按比例获付 VIBE。系统由 BFT 共识的验证者节点、通过 HTTP 通信的 worker 客户端、钱包和可审计的持久链组成。提供 Windows 安装包、一键安装脚本、PyPI 包、自检命令（selftest）、交互菜单、桌面窗口与多 GPU 多钱包运行方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 按 FLOP 同价支付，无抽签式挖矿
- BFT 共识验证者节点轮值主持、逐块投票
- selftest 自检软件、GPU、真实训练单元、网络、钱包与磁盘
- 支持 Windows 安装包、安装脚本、PyPI 与源码可编辑安装

## 适用场景

- 用旧笔记本或游戏电脑加入测试网挖矿赚取 VIBE
- 在 RunPod 租用 GPU 上跑 worker 参与训练任务
- 在本机一键搭建包含节点与 worker 的完整测试网络

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L3: A proof-of-useful-work cryptocurrency. Instead of hashing, "miners" train AI
> L4: models in small, verifiable chunks sized for mid- and low-end hardware. Every
> L8: This is a **testnet implementation**: validator nodes that take turns leading


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `d18df0b011c2` · [字段定义](../../DATASET.md)*
