# SWE-agent/SWE-agent

⭐ 20,614 · Python · MIT · 推送 2026-10-19 · [GitHub](https://github.com/SWE-agent/SWE-agent) · [官网](https://swe-agent.com) · 组织维护

**科研团队的自动修复 GitHub issue 的 LM agent**

SWE-agent 让用户选择的语言模型自主调用工具，修复真实 GitHub 仓库中的 issue，也可用于进攻性网络安全（CTF，EnIGMA 模式）与竞赛编程等自定义任务。配置由单一 yaml 文件管理，面向研究场景设计。由普林斯顿与斯坦福的研究者维护，MIT 许可；README 警告当前开发重心已转向 mini-swe-agent，一般建议新用户改用 mini-SWE-agent，EnIGMA 模式目前需使用 0.7 版本。

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

## 动量与使用信号

- 维护:`active` — 距上次 push 5.4 天,年发版 0,97 位贡献者
- 涨星:近 1 天 **+8**(自 20261016 起算)

## 能力要点

- 接入用户自选 LM（如 GPT-4o、Claude Sonnet 4）自主调用工具修复 GitHub issue
- EnIGMA 模式用于 CTF 进攻性网络安全挑战
- 单一 yaml 文件配置，面向研究可修改设计
- 提供 GitHub Codespaces 浏览器内试运行途径

## 适用场景

- 自动尝试修复仓库中的 GitHub issue
- 在 SWE-bench 上做基准评测
- 解 CTF 网络安全挑战题

## 场景标签

`编码 Agent` `网络安全` · 领域:编码与开发

## 证据(README 行号)

> L20: SWE-agent enables your language model of choice (e.g. GPT-4o or Claude Sonnet 4) to autonomously use tools to
> L28: * ✅ **Made for research**: Simple & hackable by design
> L30: SWE-agent is built and maintained by researchers from Princeton University and Stanford University.

## 星数曲线

```mermaid
xychart-beta
    title "SWE-agent/SWE-agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 20581 --> 20609
    line [20583, 20599, 20607]
```

2026-10-18 20,583 → 2026-10-22 20,607（+24）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `170b5a64d56f` · [字段定义](../../DATASET.md)*
