# mikelma/craftium

⭐ 215 · C++ · NOASSERTION · 推送 2026-02-17 · [GitHub](https://github.com/mikelma/craftium) · [官网](https://craftium.readthedocs.io/) · 组织维护

**为 AI 研究创建类 Minecraft 3D 单/多智能体环境的框架**

基于 Luanti（原 Minetest）体素引擎 fork 的开源平台，用于创建单智能体与多智能体 3D 环境，实现 Gymnasium 与 PettingZoo API。通过修改引擎源码支持 Python 进程通信、软重置、Lua API 扩展及客户端/服务器同步（适配 LLM/VLM 等慢速 agent）。提供预编译 wheel、Dockerfile 与源码编译三种安装方式，源码编译需先安装 Luanti 的系列系统依赖库。附 ChopTree 等默认环境与 stable-baselines3、Ray rllib、CleanRL 示例。论文被 ICML 2025 接收。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 基于 Luanti（C++）fork，实现 Gymnasium/PettingZoo API
- 支持环境软重置与 Lua 扩展创建 RL 环境
- 客户端/服务器同步机制适配慢速 agent（LLM/VLM）
- 提供程序化生成任务（如多房间地牢环境）

## 适用场景

- 用 PPO 等 RL 算法在 3D 体素环境中训练 agent
- 做元 RL、开放式学习、终身学习等研究实验
- 为 LLM/VLM agent 搭建多智能体 3D 环境

## 场景标签

`多智能体` `强化学习` · 领域:Agent 开发

## 证据(README 行号)

> L11: Craftium is a fully open-source platform for creating fast, rich, and diverse **single and multi-agent** environmen
> L31: - **Modern API 🤖:** Craftium implements the well-known Gymnasium and PettingZoo APIs, opening the door to a vast nu

## 星数曲线

```mermaid
xychart-beta
    title "mikelma/craftium 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 214 --> 216
    line [215, 215]
```

2026-10-18 215 → 2026-10-26 215（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `1f82e53944dd` · [字段定义](../../DATASET.md)*
