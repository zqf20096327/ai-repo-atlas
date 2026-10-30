# pevers/sims-mcp

⭐ 25 · C++ · 推送 2026-01-27 · [GitHub](https://github.com/pevers/sims-mcp) · [官网](http://peterevers.nl/posts/2026/01/sims-mcp/) · 个人维护

**为模拟人生1提供游戏状态读取的 MCP 服务器**

针对 The Sims 1 Legacy 的 Model Context Protocol (MCP) 服务器，通过逆向工程读取游戏内存，向 AI 暴露 get_household_money 与 get_household_persons（含饥饿、精力等动机数值）两个只读函数，用户可让 AI 给出游戏内建议。安装需绕过 DRM（使用 Anadius v1.0.0.158 破解版，仅支持该版本），依赖 Microsoft Visual Studio，用 editbin 关闭 ASLR 后编译 MSVC 项目并注入 DLL。README 标注 WIP，正在扩展向家庭发送动作的功能。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- MCP 函数 get_household_money 读取家庭 Simoleons 余额
- get_household_persons 读取全部家庭成员及 9 项动机数值
- 基于逆向工程注入，需关闭 ASLR 并注入 DLL
- 计划扩展动作发送功能（WIP）

## 适用场景

- 让 AI 根据家庭成员状态给出游戏内建议
- 作为逆向工程 + MCP 的参考实现
- 后续扩展为 LLM 游玩模拟人生的基础设施

## 场景标签

 · 领域:游戏/逆向工程

## 证据(README 行号)

> L5: This is a Model Context Protocol (MCP) server for the game the Sims 1 Legacy. It allows you to retrieve important in
> L15: |`get_household_money`|Get the current household money (Simoleons) from The Sims|

## 星数曲线

```mermaid
xychart-beta
    title "pevers/sims-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-30 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `b11ee24b1820` · [字段定义](../../DATASET.md)*
