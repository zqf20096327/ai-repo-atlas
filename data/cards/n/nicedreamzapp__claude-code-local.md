# nicedreamzapp/claude-code-local

⭐ 3,539 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/nicedreamzapp/claude-code-local) · [官网](https://nicedreamzapp.github.io/claude-code-local/) · 个人维护

**让 Claude Code 在本地模型上离线续跑的代理服务器**

一个 Python 代理服务器（proxy/server.py），用 Apple MLX（Mac）或 llama.cpp（Linux/Windows）在本地运行开源模型，并以 Anthropic Messages API 格式响应 Claude Code，使无 API key、无云端的本地推理接入 Claude Code 工作流。附带 keepgoing 命令：在触发用量上限后从上次 Claude Code 会话续接到本地或免费云模型；含模型按内存自动选型、doctor 自检脚本、桌面启动器与语音/浏览器/手机等可选 add-on。上游依赖 Claude Code、MLX 及各家模型权重。

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

- MLX 服务器直接以 Anthropic Messages API 格式应答 Claude Code，含流式与工具 JSON 修复
- keepgoing：用量上限后从上次 Claude Code 会话续接到本地或 OpenRouter 免费云模型
- 按 Mac 内存自动选型（8GB 至 96GB+ 分档）并一条命令安装
- turn 间复用 prompt cache，长会话不重复读取上下文

## 适用场景

- Claude Code 用量/积分耗尽时切换到本地模型继续同一会话
- 无网络或注重隐私环境下离线使用 Claude Code 编码
- 在小内存 MacBook 上以小模型跑受限的本地编码会话

## 场景标签

`编码 Agent` `推理引擎` · 领域:编码与开发

## 证据(README 行号)

> L46: **In one sentence:** a small Python server (`proxy/server.py`) runs open AI models on your Mac's chip with Apple's 
> L58: - ⚡ **`proxy/server.py`**: the MLX server. Speaks the Anthropic Messages API with streaming, turns each model's own
> L61: - 🔋 **`bin/keepgoing`** + `bin/keepgoing.py`: finds your last Claude Code conversation in this folder and resumes i

## 星数曲线

```mermaid
xychart-beta
    title "nicedreamzapp/claude-code-local 星数(近 25 点)"
    x-axis ["2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 3362 --> 3555
    line [3378, 3380, 3382, 3388, 3389, 3394, 3398, 3401, 3402, 3378, 3486, 3491, 3494, 3499, 3501, 3510, 3514, 3520, 3522, 3524, 3525, 3528, 3531, 3536, 3539]
```

2026-10-25 3,378 → 2026-11-27 3,539（+161）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `a67edcadce49` · [字段定义](../../DATASET.md)*
