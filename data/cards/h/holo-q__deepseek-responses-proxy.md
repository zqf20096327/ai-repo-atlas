# holo-q/deepseek-responses-proxy

⭐ 10 · Python · 推送 2026-05-04 · [GitHub](https://github.com/holo-q/deepseek-responses-proxy) · 个人维护

**给 Codex 自定义 provider 补 Responses API 的本地代理**

本地适配器，解决 Codex 0.128.0 自定义 provider 要求 Responses 格式、而上游（如 DeepSeek V4）只提供 OpenAI Chat Completions 格式的不匹配：把 Responses 的 input/instructions/工具 schema 转为 chat messages，并回放 DeepSeek 推理内容、合成 SSE 流式输出。默认指向 DeepSeek V4，上游 URL 与 API key 来源可配置，可指向任意 Chat Completions 上游。安装方式为 Arch AUR 包、uvx 直接运行或源码 checkout，附带 systemd user service。README 自述为 alpha 阶段，宿端 Responses 工具会被丢弃，且尚未声明开源许可证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Responses 与 Chat Completions 双向格式转换，含 DeepSeek reasoning_content 跨工具调用回放
- 非流式上游合成 SSE，兼容流式客户端
- 每个请求输出 JSON 行 trace 到 stderr，事件覆盖转换与上游调用链路
- 支持 Codex 子代理与 apply_patch 自由格式工具的适配

## 适用场景

- 在 Codex CLI 中以 DeepSeek V4 作为自定义 provider 编码
- 让 Codex 子代理跑在同一 DeepSeek provider 上
- 把本地代理指向其他 OpenAI Chat Completions 上游复用同一适配

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: Local adapter for the awkward boundary between current Codex custom providers
> L12: formats. This proxy owns that mismatch in one traceable local process:
> L15: Codex /responses

## 星数曲线

```mermaid
xychart-beta
    title "holo-q/deepseek-responses-proxy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-11-20"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-18 10 → 2026-11-20 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 mid · 依据 README sha `ea1f8564bd29` · [字段定义](../../DATASET.md)*
