# dijiaozhibei-top/baidu-2api

⭐ 14 · Python · AGPL-3.0 · 推送 2026-05-20 · [GitHub](https://github.com/dijiaozhibei-top/baidu-2api) · [官网](https://github.com/dijiaozhibei-top/baidu2api) · 个人维护 · 中文 README

**将百度 chat 对话封装为 OpenAI 兼容 API 的代理服务**

基于 FastAPI 的反向代理服务：从 chat.baidu.com 页面提取 token 与 lid 生成签名，将百度 AI 对话能力封装为 /v1/chat/completions 与 /v1/models 等 OpenAI 兼容接口，支持 SSE 流式输出、reasoning_content 思维链字段、XML/JSON 双模式工具调用与自动回退。暴露 DeepSeek-V4、DeepSeek-R1、ERNIE-4.5 与智能模式四个模型 ID，提供 Web 管理后台管理 API Key 与配置，可选 Bearer 认证。支持源码运行与预编译 Docker 镜像，README 声明接口可能随百度侧变更失效、仅供学习交流。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 完整实现 /v1/chat/completions 与 /v1/models 的 OpenAI 兼容接口
- XML 与 JSON 双模式工具调用，主模式解析失败自动回退
- DeepSeek-R1 推理过程通过 reasoning_content 字段输出
- Web 管理后台可视化配置、API Key 与工具调用模式

## 适用场景

- 让 OpenAI SDK / Claude Code / Cursor 等工具直接调用百度对话模型
- 以 OpenAI 格式统一接入 DeepSeek-V4、ERNIE-4.5 等模型
- 自建带认证与流式输出的对话 API 服务

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: 将 chat.baidu.com 的 AI 对话能力封装为 OpenAI 兼容 API，无需登录即可使用。
> L9: - **OpenAI 兼容** — 完整支持 `/v1/chat/completions` 和 `/v1/models` 接口
> L184: ├── main.py            # FastAPI 服务（OpenAI 格式适配、流式输出）

## 星数曲线

```mermaid
xychart-beta
    title "dijiaozhibei-top/baidu-2api 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `cb58399e4604` · [字段定义](../../DATASET.md)*
