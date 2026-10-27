# joeseesun/qiaomu-llm-mcp

⭐ 47 · Python · MIT · 推送 2026-06-19 · [GitHub](https://github.com/joeseesun/qiaomu-llm-mcp) · 个人维护 · 中文 README

**本地 MCP 网关：统一多 LLM Provider 路由、密钥与多模型讨论**

面向同时使用多个 LLM Provider 的开发者，把模型调用接入 MCP 客户端（Codex、Claude Desktop、Cursor 等）：提供单模型调用、多模型对比、流水线、HeavySkill 式多轮讨论（由 Codex 或指定模型主持并渲染报告）、Claude Code CLI 安全调用等 12 类工具。Provider 注册表存于本地 registry.json，密钥默认存 macOS Keychain，MCP 层只暴露密钥状态不返回明文；无云端代理。macOS/Linux + Python 3.10+ 从源码 venv 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 12 个 qllm_* MCP 工具：路由、单/多模型调用、对比、流水线、多模型讨论
- 密钥存 macOS Keychain 或环境变量，工具只返回密钥状态
- HeavySkill 多模型讨论可由 Codex 或指定模型主持，输出 Markdown/HTML 报告
- qllm_claude_code_* 通过 MCP 受控调用本机 Claude Code CLI

## 适用场景

- 在 Codex/Claude 等 MCP 客户端里用同一组工具调用多个 LLM Provider
- 不花 token 先按任务类型选择 Provider/Model
- 让多个模型独立作答后由主控模型主持综合讨论
- 避免把 API Key 写进提示词或配置文件

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: > 把多个 LLM Provider、API Key、模型路由和多模型讨论统一成一个本地 MCP 网关。
> L19: 安装后，MCP 客户端会看到这些工具：
> L30: |`qllm_heavy_discuss`|多视角、多模型讨论，可由模型或 Codex 主持|

## 星数曲线

```mermaid
xychart-beta
    title "joeseesun/qiaomu-llm-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-27"]
    y-axis "stars" 45 --> 48
    line [46, 47, 47]
```

2026-10-18 46 → 2026-10-27 47（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `957c7f73363b` · [字段定义](../../DATASET.md)*
