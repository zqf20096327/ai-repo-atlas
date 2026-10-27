# trentster/deerflow-oauth-bridge

⭐ 28 · Python · MIT · 推送 2026-03-08 · [GitHub](https://github.com/trentster/deerflow-oauth-bridge) · 个人维护

**让 DeerFlow 2.0 通过 ChatGPT 订阅 OAuth 调用 OpenAI 模型的本地代理**

运行在本地的轻量代理服务：把 DeerFlow 发出的 Chat Completions 请求翻译为 OpenAI Codex Responses API 格式，用 ChatGPT Plus/Pro 订阅的 OAuth 登录替代 API key，自动处理 token 刷新与流式转换。由 oauth.py（PKCE 流程）、translator.py（双向协议翻译）、server.py（FastAPI 代理）三个模块组成，token 存于本地 ~/.deerflow-bridge/。面向已安装 DeerFlow 2.0 且持有 ChatGPT 订阅的用户，git clone 后运行 setup.sh 完成安装与一次性浏览器登录；列出各 GPT-5 系列模型的支持/不支持状态。

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

- Chat Completions 与 Codex Responses API 的双向协议翻译
- OAuth 登录替代 API key，token 本地存储并自动刷新
- 支持流式/非流式响应、多轮对话与工具调用映射
- 内置 test_bridge.py 预检脚本与 --debug 日志模式

## 适用场景

- 用已有的 ChatGPT Plus/Pro 订阅为 DeerFlow 提供模型，不购买 API credits
- 在 DeerFlow 中把 GPT-5 系列模型配置为可用后端
- 本地调试代理桥接的请求/响应翻译过程

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: DeerFlow OAuth Bridge is a lightweight local proxy that connects DeerFlow 2.0 to OpenAI's models using your existing
> L14: OAuth Bridge (this project)

## 星数曲线

```mermaid
xychart-beta
    title "trentster/deerflow-oauth-bridge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-27 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `0f3508a1f4f2` · [字段定义](../../DATASET.md)*
