# umputun/mpt

⭐ 61 · Go · MIT · 推送 2026-07-25 · [GitHub](https://github.com/umputun/mpt) · [官网](https://mpt.umputun.dev) · 个人维护

**命令行工具：并行向多家 LLM 提问并合并结果**

用 Go 编写的命令行工具，向 OpenAI、Anthropic、Google 及自定义 OpenAI 兼容端点并行发送同一提示，按 provider 标注返回结果；支持 --mix 由指定 provider 合成多方回答、共识模式检测分歧并迭代收敛。可用 glob/Go 风格模式把文件纳入上下文，自动遵循 .gitignore，支持 git diff 集成与 stdin 管道。另可作为 MCP Server 向 MCP 客户端统一暴露多 provider。安装途径包括 go install、homebrew、deb/rpm/apk 包及二进制发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 并行查询 OpenAI/Anthropic/Google/自定义 provider 并合并结果
- --mix 合成模式与共识模式（检测分歧并迭代收敛）
- glob、Go 风格模式与 .gitignore 感知的文件上下文注入，含 git diff 集成
- 可作为 MCP Server 向 MCP 客户端统一暴露多 provider

## 适用场景

- 同一问题并发问多家模型，比对不同回答
- 把代码文件或 git diff 上下文直接交给多模型审查
- 让一个模型综合多个 provider 的回答形成单一结论

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: MPT is a command-line utility that sends prompts to multiple AI language model providers (OpenAI, Anthropic, Google,
> L29: 6. **Acting as an MCP server**: For advanced usage, MPT can run as a Model Context Protocol server, making multiple
> L83: - **MCP Server Mode**: Run as a Model Context Protocol server to make your providers accessible to MCP-compatible c

## 星数曲线

```mermaid
xychart-beta
    title "umputun/mpt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-28 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `33d1a361ef1c` · [字段定义](../../DATASET.md)*
