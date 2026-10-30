# LilZeeCN/agy-argon-bridge

⭐ 15 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/LilZeeCN/agy-argon-bridge) · 个人维护 · 中文 README

**把 Antigravity CLI 桥接到 Vertex AI 以抵扣 GCP 赠金的本地代理**

本地运行的反向流式桥接服务，将 Google Antigravity CLI (agy) 的 AI Studio 格式请求转换为 Vertex AI 协议，通过 gcloud ADC 鉴权调用 gemini-4-argon 等模型，费用从 Google Cloud 新账号 $300 赠金抵扣。面向希望用赠金在终端编程智能体中使用 Vertex AI 模型的开发者。机制上处理协议转换、URL-Safe Base64 修复、240s 长超时看门狗、SSE 心跳保活与 TCP 半开重试；支持通过 TARGET_MODEL 切换 Vertex AI 全系模型及多账号轮换。安装经 git clone 与 install.sh 脚本完成，注册 macOS launchd 服务监听 127.0.0.1:8050；需 Python 3.10+ 与本地 gcloud CLI。

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

- agy 的 AI Studio 格式到 Vertex AI OAuth/ADC 协议的自动转换
- 240s 深度思考看门狗、20s 间隔 SSE 心跳保活与 TCP 半开自愈重试
- TARGET_MODEL 环境变量切换 Vertex AI 托管模型（argon/flash/pro 系列）
- install.sh 创建隔离 venv 并注册 launchd 常驻服务（127.0.0.1:8050）

## 适用场景

- 利用 Google Cloud $300 赠金在 agy 终端智能体中调用 gemini-4-argon
- 让只支持 AI Studio 格式的客户端接入 Vertex AI 企业级鉴权
- 赠金用尽后通过重新授权快速切换新账号继续使用

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L19: Google 官方推出的 **Antigravity CLI (`agy`)** 是顶级的 Agentic 终端编程智能体，但默认配置下主要调用 `gemini-3.8-flash` 或需配置独立结算的 Google AI Stu
> L28: **`agy-argon-bridge`** 正是为解决上述所有痛点而生的本地企业级反向流式桥接服务：**零侵入、自动转换协议、240s 深度思考防断守护、心跳保活自愈、全自动抵扣 GCP 300$ 赠金！**
> L99: - 安装 `google-genai`、`fastapi`、`uvicorn`、`httpx` 等所需依赖；

## 星数曲线

```mermaid
xychart-beta
    title "LilZeeCN/agy-argon-bridge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b4f0b6f36ae1` · [字段定义](../../DATASET.md)*
