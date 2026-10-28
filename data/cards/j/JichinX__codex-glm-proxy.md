# JichinX/codex-glm-proxy

⭐ 21 · Python · MIT · 推送 2026-07-28 · [GitHub](https://github.com/JichinX/codex-glm-proxy) · 个人维护 · 中文 README

**让 Codex CLI 接入智谱 GLM 模型的本地代理**

运行在本地的单文件 Python 代理：接收 OpenAI Codex CLI 发出的 Responses API 请求，转换为 GLM Chat Completions 格式调用智谱 API，再把流式响应与工具调用转回 Responses API 格式。支持多轮对话、OpenAI 模型名到 GLM 模型（glm-4/glm-4-plus/glm-4-flash 等）的自动映射。面向希望用 GLM 替代 OpenAI 后端的中文开发者，需自备 GLM API key，代理默认监听 localhost:18765。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Responses API ↔ Chat Completions 双向格式转换
- 流式响应与工具调用（apply_patch/exec 等）支持
- OpenAI 模型名到 GLM 模型自动映射
- 单 Python 文件，通过 git clone 安装，环境变量配置

## 适用场景

- 用 Codex CLI 配合智谱 GLM 模型做代码生成与修复
- 国内网络与合规要求下使用国产 LLM 编程助手
- 无 OpenAI 账号时本地体验 Codex 编码流程

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L8: Enable **OpenAI Codex CLI** to work with **GLM (智谱 AI)** models by running a local proxy that converts OpenAI Respon
> L173: Codex CLI → Responses API → Proxy → Chat Completions API → GLM

## 星数曲线

```mermaid
xychart-beta
    title "JichinX/codex-glm-proxy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `3395b86c7de6` · [字段定义](../../DATASET.md)*
