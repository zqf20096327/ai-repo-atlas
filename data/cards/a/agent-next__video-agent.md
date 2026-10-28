# agent-next/video-agent

⭐ 118 · Python · Apache-2.0 · 推送 2026-10-10 · [GitHub](https://github.com/agent-next/video-agent) · [官网](https://open-video.ai) · 组织维护

**本地视频生成运行时：在自己 GPU 上跑 MiniMax H3**

面向开发者的本地视频生成工具，自称'视频模型的 Ollama'：提供 install→pull→run 循环，在本地 NVIDIA GPU 上通过 ComfyUI 后端运行 MiniMax H3 文生视频/图生视频模型，并校验权重完整性。附带 SKILL.md 格式 agent 技能，可被 Claude Code、Cursor 等编码 agent 加载以端到端生成视频；含 prompt 语法、硬约束校验与可选 VLM 评审（未配置时如实 SKIPPED）。v0.1.0 仅支持 H3 单模型，权重受 MiniMax 社区许可（含地域与商用限制）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- install/pull/run 三步在本地 GPU 运行 MiniMax H3，权重校验
- SKILL.md agent 技能，兼容 Claude Code/Cursor/Codex 等宿主
- 可选 OpenAI 兼容 VLM 评审循环，低分镜头自动重生成
- `recommend-quant` 按 VRAM（≥22G/12–22G/9–12G/<9G）选择量化档位

## 适用场景

- 在自己的 GPU 上本地生成短视频而不依赖 SaaS
- 让 Claude Code/Cursor 等 agent 通过技能直接生成视频
- 脚本化批量生成视频（CLI + Python API）

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L6:  Run MiniMax H3 on your own GPU — <code>install · pull · run</code> — plus a drop-in skill
> L14:  Ollama → local LLMs.&nbsp;&nbsp;OpenVideo → local video.
> L143: prompt / skill ──→ open-video CLI ──→ backends/h3 ──→ engines/comfyui ──→ mp4

## 星数曲线

```mermaid
xychart-beta
    title "agent-next/video-agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 117 --> 120
    line [119, 118, 118]
```

2026-10-18 119 → 2026-10-28 118（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `786d652297c7` · [字段定义](../../DATASET.md)*
