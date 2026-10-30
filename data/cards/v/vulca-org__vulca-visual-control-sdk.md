# vulca-org/vulca-visual-control-sdk

⭐ 17 · Python · Apache-2.0 · 推送 2026-09-22 · [GitHub](https://github.com/vulca-org/vulca-visual-control-sdk) · [官网](https://pypi.org/project/vulca/) · 组织维护 · 中文 README

**面向 Claude Code 的图像编辑 SDK：21 个 MCP 工具做分层、重绘与文化评分**

以 Python SDK + 21 个 MCP 工具 + /decompose 等 agent 技能形式提供，运行在 Claude Code 内。功能覆盖：从任意图像抽取 10–20 个语义透明图层、区域重绘（inpaint）与图层编辑合成、L1–L5 五维文化评分（覆盖 13 种传统，可用 YAML 自定义）、分层生成与意图到 brief 的工作流。自身不托管模型，通过 ComfyUI（本地优先，Apple Silicon/MPS 已测试）、Gemini、OpenAI 或 mock 后端驱动。配 CLI，pip 安装，另有 VULCA Workspace 预览（review-first）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 语义图层分解（10–20 层）与区域重绘/图层编辑合成
- L1–L5 五维文化评分，覆盖 13 种传统，支持 YAML 自定义
- 本地优先路径：ComfyUI + Ollama + MPS 端到端测试，无需云端 key
- 21 个 MCP 工具返回结构化 JSON，工具内无隐藏 LLM 规划

## 适用场景

- 让 Claude Code agent 对图像做语义分层与局部重绘
- 按文化传统（如 chinese_xieyi）对作品做多维评分与跨传统对比
- 本地 ComfyUI 环境下生成、编辑与分层生成图像

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L100: Most image SDKs ship a "brain" — a VLM planner that decides what to generate, how to compose, when to stop. Claude
> L106: - **Vulca doesn't host a model** — it drives yours (ComfyUI / Gemini / OpenAI / mock) with structured tooling. No 
> L121: User intent ─▶ Claude Code (planning) ─▶ Vulca MCP tools ─▶ Image artifacts ─┐

## 星数曲线

```mermaid
xychart-beta
    title "vulca-org/vulca-visual-control-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `f7b62f7cbb37` · [字段定义](../../DATASET.md)*
