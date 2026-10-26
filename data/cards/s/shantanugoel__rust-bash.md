# shantanugoel/rust-bash

⭐ 33 · Rust · MIT · 推送 2026-04-05 · [GitHub](https://github.com/shantanugoel/rust-bash) · [官网](https://rustbash.dev/) · 个人维护

**面向 AI Agent 的 Rust 沙箱化 bash 解释器，带虚拟文件系统**

用 Rust 实现的沙箱 bash 解释器，供 AI Agent 等场景安全执行脚本：默认在内存虚拟文件系统中运行，不接触宿主文件，无需容器或 VM。支持 80 个内置命令、完整 bash 语法、10 项可配置执行限制（时间/命令数/循环/输出等）以及带 URL 白名单的沙箱 curl。提供 4 种文件系统后端（内存/写时复制覆盖/直通/组合）。以 npm 包、Rust crate、CLI 二进制、C FFI 共享库及 WASM 形式分发，内置 MCP server，可注册自定义命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 虚拟文件系统默认全内存运行，无容器/VM，不访问宿主
- 80 个内置命令 + 40 个解释器内建，覆盖完整 bash 语法
- 10 项可配置执行限制与 curl 网络策略（URL 白名单/方法限制）
- npm/Rust crate/CLI/MCP server/C FFI/WASM 多形态分发

## 适用场景

- 给 LLM Agent 提供 bash 执行工具而不引入容器开销
- 安全运行用户提交的脚本（内存文件系统隔离）
- 在受控文件系统上做确定性 bash 测试
- 通过内置 MCP server 为 Claude Desktop/Cursor/VS Code 提供命令执行

## 场景标签

 · 领域:AI Agent 基础设施/沙箱执行

## 证据(README 行号)

> L3: A sandboxed bash interpreter for AI Agents, built in Rust. Execute bash scripts safely with a virtual filesystem — n
> L18: - **AI tool integration** — framework-agnostic JSON Schema tool definitions for OpenAI, Anthropic, Vercel AI SDK, L
> L219: - **AI agent tools** — give LLMs a bash sandbox without container overhead

## 星数曲线

```mermaid
xychart-beta
    title "shantanugoel/rust-bash 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 31 --> 34
    line [32, 33, 33]
```

2026-10-18 32 → 2026-10-26 33（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `18c7843e6c4e` · [字段定义](../../DATASET.md)*
