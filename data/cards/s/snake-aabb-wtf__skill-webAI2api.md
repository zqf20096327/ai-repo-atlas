# snake-aabb-wtf/skill-webAI2api

⭐ 34 · Python · Unlicense · 推送 2026-07-31 · [GitHub](https://github.com/snake-aabb-wtf/skill-webAI2api) · 个人维护 · 中文 README

**把任意网页 AI 逆向成 OpenAI 兼容 API 的代理生成工具**

用户上传浏览器抓取的 HAR 文件，由 AI 自动分析目标网页 AI 的端点、鉴权与 payload 格式，生成 server.py 与 adapter.py，运行后得到 OpenAI 兼容的本地 API 端点。支持 SSE 流式输出转 OpenAI chunk、HTTP/WebSocket 协议自适应、参数透传与丢弃、PoW 挑战自动求解；工具调用通过 DSML 提示词注入实现而非原生 function calling，依赖目标模型对 XML 指令的理解。提供 GUI 工具续期 Cookie。限制：仅文本不支持多模态，seed/response_format/json_mode 不可用，WebSocket 仅 text frame。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Unlicense |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- HAR 文件自动逆向生成 OpenAI 兼容代理服务器
- DSML 提示词注入实现工具调用，流式下经 StreamSieve 分离标签
- PoW 验证挑战自动求解，支持 DeepSeek 等场景
- Cookie 过期后可通过 GUI 续期，无需重新分析

## 适用场景

- 把已订阅的网页 AI 转成本地 API 供 OpenAI SDK 直接调用
- 接入 Claude Code、Cursor、Continue 等需要 OpenAI 兼容端点的工具
- 私有部署的开源模型免搭前端直接提供 API

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L6: 上传一个 HAR 文件，web2api 自动把任何网页 AI 逆向成 OpenAI 兼容 API。
> L39: |零成本迁移|任何 OpenAI SDK 直接对接，一行不改|

## 星数曲线

```mermaid
xychart-beta
    title "snake-aabb-wtf/skill-webAI2api 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-31 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `a000228b14fc` · [字段定义](../../DATASET.md)*
