# x42en/sysplant

⭐ 135 · Nim · GPL-3.0 · 推送 2026-10-19 · [GitHub](https://github.com/x42en/sysplant) · [官网](https://docs.circle-cyber.com/sysplant/) · 个人维护

**Windows syscall hooking 代码生成工具，含 MCP 服务器**

Python 编写的 syscall 检索与桩代码生成工具，聚合 Hell's/Halos's/Tartarus' Gate、FreshyCalls、SysWhispers2/3 及作者提出的 Canterlot's Gate 等迭代器，支持 direct/indirect/random/egg_hunter 四种调用方式，可生成 NIM/C/C++/Rust 代码（Linux 交叉编译）。内置 MCP 服务器，供 Claude Code、Cursor、Windsurf 等 AI 编码助手在对话中直接生成 syscall 代码。供 Linux 上的渗透测试与安全研究人员使用，声明仅限授权系统、教育用途。项目处于 WIP 状态，x86 与 WoW64 支持尚未完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 聚合 7 种 syscall 检索迭代器（含 Canterlot's Gate）与 4 种调用桩方式
- 生成 NIM/C/C++/Rust 代码，支持从 Linux 交叉编译到 Windows
- 内置 MCP 服务器（stdio/SSE/HTTP），接入 AI 编码助手
- 可作为 CLI 工具、Python 模块与 MCP 服务器三种方式使用

## 适用场景

- 红队/渗透测试中生成绕过 AV/EDR 挂钩的 syscall 桩代码
- 学习与比较不同 syscall 检索机制的实现
- 在 Claude Code/Cursor 等 AI 客户端里直接生成 syscall 代码

## 场景标签

 · 领域:网络安全/攻防工具

## 证据(README 行号)

> L17: SysPlant is a python generation tool of the currently known syscall hooking methods. It currently supports followin
> L49: SysPlant ships with a built-in **Model Context Protocol (MCP)** server, allowing AI coding assistants (Claude Code,
> L125: This project is in WIP state...

## 星数曲线

```mermaid
xychart-beta
    title "x42en/sysplant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 134 --> 136
    line [135, 135]
```

2026-10-18 135 → 2026-10-24 135（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `616dc784161d` · [字段定义](../../DATASET.md)*
