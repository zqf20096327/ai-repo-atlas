# Parassharmaa/agent-sandbox

⭐ 34 · Rust · MIT · 推送 2026-02-10 · [GitHub](https://github.com/Parassharmaa/agent-sandbox) · 个人维护

**给 AI agent 开发者的 WASM 沙箱执行环境库**

以 WASM 为基础的可嵌入沙箱运行时，供 AI agent 在隔离环境中执行命令与代码：内置 80+ CLI 工具（cat/grep/jq/git 等）、完整 sh/bash shell 解释器、Boa 引擎的 JavaScript 运行时，以及带 SSRF 防护与域名策略的安全 HTTP 网络（默认禁用）。资源限制覆盖 fuel、超时与内存，文件系统带路径穿越防护，AOT 预编译实现 <13ms 冷启动，无需 Docker/VM。提供 Rust crate 与 Node.js（NAPI）两种接入方式，附 macOS/Linux/Windows 预编译二进制。限制：JS 运行时无 Node 内置模块、单线程、shell 不支持进程派生，不适合数据库/GPU/长驻服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 80+ 内置 CLI 工具与完整 sh/bash shell 解释器
- 内置 Boa 引擎 JavaScript 运行时，支持 ES2023+
- SSRF 防护、域名策略与限速的安全 HTTP 网络（默认禁用）
- fuel/超时/内存资源限制与文件系统快照变更跟踪

## 适用场景

- 让文件操作类 agent 在隔离沙箱中执行代码分析、重构与 git 操作
- 安全地评估不受信任的 JavaScript 代码
- 以带防护的 fetch 供 agent 发起安全 API 调用

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: A secure, embeddable, WASM-based sandbox for AI agents. 80+ built-in CLI tools, a full shell interpreter, a JavaScri
> L172: **Best for:** file-manipulation agents (code analysis, refactoring, git ops), sandboxed JS evaluation, safe API ca

## 星数曲线

```mermaid
xychart-beta
    title "Parassharmaa/agent-sandbox 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-28 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `44efd6e58d33` · [字段定义](../../DATASET.md)*
