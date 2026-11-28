# tDupuis19341/claude-session-rotator

⭐ 66 · C++ · MIT · 推送 2026-11-25 · [GitHub](https://github.com/tDupuis19341/claude-session-rotator) · 个人维护

**为 Claude Code CLI 提供会话轮换与热重载配置的 Windows 封装器**

面向 Windows 10/11 x64 的便携运行时套件，作为 Claude Code CLI 的封装器（wrapper）运行，原 CLI 保持不动；提供预构建二进制包（解压即用，附访问码 2026），无需编译器与外部依赖。核心机制包括 JSON 配置热重载（不重启即生效）、原子 JSON 状态与崩溃回滚、环形缓冲流水线与默认静默的 stderr 遥测；数据本地存储于 ~/.config/ccu/，支持源码 CMake 构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 预构建便携包，无编译器、无外部依赖
- config/settings.json 热重载，修改无需重启
- 原子 JSON 状态引擎，崩溃安全回滚
- 提供 git clone + CMake 源码构建路径

## 适用场景

- 在 Windows 上运行 Claude Code 并通过配置文件轮换会话
- 不想装编译器、直接解压使用 CLI 封装工具
- 需要配置修改即时生效的本地开发工作流

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L18: **Claude Code Unlimited — Claude Code Unlimited — claude-code and llm in one tool** (`claude-session-rotator`) is a
> L54: No. `ccu` is a wrapper — the original CLI stays untouched.

## 星数曲线

```mermaid
xychart-beta
    title "tDupuis19341/claude-session-rotator 星数(近 2 点)"
    x-axis ["2026-11-26", "2026-11-28"]
    y-axis "stars" 65 --> 67
    line [66, 66]
```

2026-11-26 66 → 2026-11-28 66（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `f31940b5542d` · [字段定义](../../DATASET.md)*
