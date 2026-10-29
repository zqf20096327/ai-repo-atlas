# moabualruz/claude-code-cli-acp

⭐ 19 · Rust · Apache-2.0 · 推送 2026-09-24 · [GitHub](https://github.com/moabualruz/claude-code-cli-acp) · [官网](https://www.npmjs.com/package/claude-code-cli-acp) · 个人维护

**把 Claude Code CLI 接入 ACP 编辑器（如 Zed）的 Rust 适配器**

用 Rust 实现的 Agent Client Protocol 适配器：通过 PTY 运行真实的交互式 claude CLI，读取 Claude transcript JSONL 作为规范内容来源，向编辑器暴露 JSON-RPC over stdio 的 ACP 服务端。另保留 interactive 直通模式与替代 `claude -p` 的 print 模式，并提供 doctor 命令对照本地帮助、npm 元数据与官方文档做兼容性漂移检查。面向使用 Zed 等 ACP 客户端的开发者，前置要求为已安装认证的 Claude Code 与 Node 18+。 transcripts 以明文存于 ~/.claude，默认日志不含正文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PTY 桥接真实 claude CLI 并读取 transcript JSONL 获取规范内容
- JSON-RPC over stdio 的 ACP 服务端，可被 Zed 等 ACP 客户端启动
- interactive 直通模式与替代 `claude -p` 的 print 模式
- doctor 命令对 claude 版本/文档做兼容性矩阵与漂移检查

## 适用场景

- 在 Zed 等 ACP 兼容编辑器中把 Claude Code 作为 agent 服务端使用
- 以脚本方式调用交互式 Claude 并抽取 transcript 输出
- 检查适配器与快速变化的 Claude Code 之间的兼容性

## 场景标签

 · 领域:开发工具/AI agent 基础设施

## 证据(README 行号)

> L3: ACP adapter for the real interactive Claude Code CLI.
> L5: The adapter runs `claude` through a PTY, reads Claude transcript JSONL for canonical content, and exposes an Agent C

## 星数曲线

```mermaid
xychart-beta
    title "moabualruz/claude-code-cli-acp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `990528b4adbc` · [字段定义](../../DATASET.md)*
