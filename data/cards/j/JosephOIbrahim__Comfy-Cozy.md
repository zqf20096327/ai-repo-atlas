# JosephOIbrahim/Comfy-Cozy

⭐ 25 · Python · MIT · 推送 2026-07-19 · [GitHub](https://github.com/JosephOIbrahim/Comfy-Cozy) · 个人维护

**ComfyUI 的自然语言副驾驶：对话编辑/运行生图工作流，全部可撤销**

以 MCP 服务器、独立 CLI 和 ComfyUI 原生侧边栏三种形态提供的 ComfyUI 代理：用户用自然语言描述意图，代理负责加载工作流、换模型、调参数、装缺失节点、排队渲染与分析输出；每次编辑均为可撤销的小步变更。提供 133 个 MCP 工具、6 种可切换 LLM 后端（Claude/GPT-4o/Gemini/Ollama/Nemotron/任意 OpenAI 兼容端点），以及不调用 LLM 的确定性参数宏（dreamier/sharper/faster）。另含 workflow.lock 来源固定（模型 SHA-256）、无密钥运行报告与约 30 次运行后的本地风格偏好。前提条件：Python 3.11+、本地运行的 ComfyUI、一个 LLM 后端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 133 个 MCP 工具，支持 6 种可一键切换的 LLM 后端
- 零 LLM 调用的确定性参数宏（dreamier/sharper/faster），即时且可撤销
- workflow.lock 记录模型 SHA-256 与 pack commit，漂移时在 validate 阶段告警
- 三种交付形态：Claude Code/Desktop 内的 MCP 服务器、独立 CLI、ComfyUI 原生侧边栏

## 适用场景

- 用自然语言让代理加载并调整我的 ComfyUI 工作流
- 让代理查找并修复工作流中的缺失节点和弃用节点
- 渲染后用无密钥运行报告定位慢节点和异常
- 在本地 GPU 上以对话方式运行生图流程并随时撤销修改

## 场景标签

`AI 助手` `图像生成` · 领域:对话与助手

## 证据(README 行号)

> L19: > - **134 MCP tools · 6 LLM providers** — Claude, GPT-4o, Gemini, Ollama, NVIDIA Nemotron, or *any* OpenAI-compatib
> L70:     Client["Claude Code /<br/>any MCP client"] --> Cozy["comfy-cozy MCP server<br/>133 tools · validate-first gate 
> L212: comfy-cozy run

## 星数曲线

```mermaid
xychart-beta
    title "JosephOIbrahim/Comfy-Cozy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-30 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `7ab4df2bee41` · [字段定义](../../DATASET.md)*
