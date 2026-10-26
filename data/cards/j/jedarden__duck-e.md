# jedarden/duck-e

⭐ 54 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/jedarden/duck-e) · [官网](https://jedarden.com/projects/ducke/) · 个人维护

**面向橡皮鸭调试的浏览器语音助手，接入 OpenAI Realtime API**

DUCK-E 是一个基于 FastAPI 的浏览器语音助手，用于橡皮鸭式调试：用户口头描述问题，系统通过 WebRTC 将浏览器音频桥接到 OpenAI Realtime API（gpt-realtime-2），由 Whisper-1 转写、Realtime API 生成语音回答。后端提供天气查询（Open-Meteo）、联网搜索、URL 抓取、按用户分类的记忆存储等工具，支持 11 种语音切换、按会话/小时的费用上限与断路器、临时密钥流程与 SSRF 防护。部署需自备具有 Realtime API 访问权限的 OPENAI_API_KEY，提供 Docker Compose 与 pip 两种运行方式。限制：记忆功能在无认证方式的本地开发环境下自动禁用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- WebRTC 全双工语音对话，语音可中途打断，支持按键说话模式
- 服务端工具：天气、web_search、web_fetch（SSRF 防护）、按用户记忆存取
- 费用保护：会话/小时支出上限、断路器、最长会话时长
- 临时密钥流程使真实 API key 不进入浏览器；提供 Prometheus 指标端点

## 适用场景

- 开发者用语音向助手解释代码问题并获得追问与解答
- 调试时让助手联网查资料或抓取指定 URL 内容
- 跨会话记住用户相关事实并用于后续对话

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L3: **DUCK-E** (Digitally Unified Conversational Knowledge Engine) is a browser-based voice assistant for rubber-duck de
> L10: Browser (WebRTC) → WebSocket → FastAPI → OpenAI Realtime API
> L16: 3. Speech is transcribed by OpenAI Whisper-1; the Realtime API handles both understanding and voice response native

## 星数曲线

```mermaid
xychart-beta
    title "jedarden/duck-e 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 53 --> 55
    line [54, 54]
```

2026-10-18 54 → 2026-10-26 54（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `259e82dfde7d` · [字段定义](../../DATASET.md)*
