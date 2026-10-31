# TheRealPSV/ha-openwebui-conversation

⭐ 50 · Python · AGPL-3.0 · 推送 2026-10-26 · [GitHub](https://github.com/TheRealPSV/ha-openwebui-conversation) · 个人维护

**Home Assistant 接入 OpenWebUI 的对话代理集成，支持联网搜索**

Home Assistant 自定义集成（经 HACS 安装），将 OpenWebUI 实例接入为对话代理：通过 Base URL 与 API Key 连接已有 OpenWebUI 服务，模型列表自动从 OpenWebUI 工作区同步，可选剥离 Markdown 以适配 HA 展示与 TTS。该代理不能控制家庭设备，仅可用于自动化对话。若 OpenWebUI 配置了 Web Search，可通过自定义句子触发联网搜索并让模型总结结果，搜索触发句需含 {query} 占位符。支持自定义 HTTP 请求头以穿过身份认证代理（如 Cloudflare Access）。代码基于 hass-ollama-conversation 仓库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 Base URL/API Key 连接 OpenWebUI 服务，模型列表自动同步
- 基于句子触发的联网搜索并由模型总结结果
- Additional Headers 支持身份认证代理（如 Cloudflare Access）场景
- Strip Markdown 选项适配 Home Assistant 展示与 TTS

## 适用场景

- 在 Home Assistant 助手中使用 OpenWebUI 后端模型对话
- 通过对话让助手搜索互联网并总结结果
- 在自动化流程中调用 OpenWebUI 对话能力

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L9: The OpenWebUI integration adds a conversation agent powered by [OpenWebUI][openwebui] in Home Assistant.
> L95: Options related to performing a web search with OpenWebUI. The agent will perform a web search through OpenWebUI an

## 星数曲线

```mermaid
xychart-beta
    title "TheRealPSV/ha-openwebui-conversation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-31 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `33b4a303ba89` · [字段定义](../../DATASET.md)*
