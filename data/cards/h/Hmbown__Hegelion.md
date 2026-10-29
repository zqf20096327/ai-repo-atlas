# Hmbown/Hegelion

⭐ 174 · Python · MIT · 推送 2026-03-15 · [GitHub](https://github.com/Hmbown/Hegelion) · [官网](https://hegelion-web.pages.dev/) · 个人维护

**让 LLM 先自我对立再综合的辩证推理与自动编码 MCP 工具**

Hegelion 是一个 Python 库 + MCP 服务器，向 LLM 编辑器（Claude Desktop/Code、Cursor、VS Code 等）和 Python API 提供两种模式：辩证推理（Thesis→Antithesis→Synthesis 三次独立调用）与 Player-Coach 自动编码（实现者与独立验证教练迭代直至需求核验）。默认 prompt 驱动、无需 API key；可选后端（cli、codex_mcp、auto）支持直接执行与独立教练验证，v0.5.0 移除了 LangGraph 依赖，工具整合为 4 个。MIT 许可，Python 3.10+，pip 安装。

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

- Thesis→Antithesis→Synthesis 三次独立调用的辩证推理
- Player-Coach 循环：教练独立核验需求、不信任实现者自述
- 4 个 MCP 工具（dialectic/autocode/autocode_turn/autocode_session）
- 默认 prompt 驱动无需 API key，可选后端直接执行

## 适用场景

- 在 MCP 编辑器中让模型先自我反驳再做深度分析或写代码
- 自动编码时由独立教练核验需求与测试，避免过早宣布成功
- 在自己的 agent 中用 Python API 生成结构化辩证 prompt

## 场景标签

`Agent 框架` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L7: Hegelion is prompt-driven by default: it generates structured prompts for your editor to execute, no API keys requir
> L9: Use it via MCP in Claude Desktop, Cursor, VS Code, or any MCP-enabled editor, or via the Python API in your own agen
> L71: ### MCP Tools

## 星数曲线

```mermaid
xychart-beta
    title "Hmbown/Hegelion 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 172 --> 175
    line [173, 174, 174]
```

2026-10-18 173 → 2026-10-29 174（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `2a8ba94aa0c1` · [字段定义](../../DATASET.md)*
