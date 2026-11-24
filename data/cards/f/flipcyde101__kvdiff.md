# flipcyde101/kvdiff

⭐ 5 · TypeScript · MIT · 推送 2026-11-22 · [GitHub](https://github.com/flipcyde101/kvdiff) · 个人维护

**定位破坏 LLM 提示缓存的 UTF-8 字节的本地零代码代理**

以本地代理形式部署在编码 Agent 与模型服务之间，逐字节比对请求前缀，定位破坏 KV 提示缓存的确切 UTF-8 字节与 JSONPath 位置，统计浪费成本，并支持 --heal 可选地实时修复前缀（如对 tools 排序）。默认零改动透传全部请求字节与请求头，绑定 127.0.0.1，数据仅存本地 node:sqlite，无遥测。通过 npx 运行，需 Node >=24，无原生扩展。面向使用 Claude Code 等编码 Agent 的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 定位破坏提示缓存的精确 UTF-8 字节偏移与 JSONPath
- 按 6 类断因分类（TOOL_REORDER/VOLATILE_SYSTEM/TTL_EXPIRED 等）
- --heal 可选实时修复前缀，默认零改动透传
- 100% 本地运行，零遥测，本地瀑布式 UI

## 适用场景

- 排查 Claude Code 会话中缓存命中率突然掉零的原因
- 定位 MCP 工具重连导致的前缀失效并自动修复
- 配合本地 llama.cpp/vLLM 调试 KV-cache 前缀复用

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: **Zero-code local proxy that pinpoints the exact UTF-8 byte breaking your LLM prompt cache (Anthropic, OpenAI, Googl
> L81:     Agent["Coding Agent / IDE\n(Claude Code · Codex · Antigravity · Gemini · llama.cpp)"] -->|"HTTP (127.0.0.1:4318


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `7d38aa5d35df` · [字段定义](../../DATASET.md)*
