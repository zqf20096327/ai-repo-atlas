# pylab-me/Codex-Shim

⭐ 15 · Rust · Apache-2.0 · 推送 2026-09-08 · [GitHub](https://github.com/pylab-me/Codex-Shim) · [官网](https://github.com/pylab-me/codex-shim/releases/tag/preview-ui-2026-06-10-61) · 个人维护 · 中文 README

**Rust 编写的协议转换层：让 codex-cli 接入 OpenAI 兼容 Chat API**

本地运行的 Responses-to-Chat 转换 shim：Codex CLI 的 /v1/responses 请求被转换为 OpenAI 兼容的 Chat Completions 请求，instructions 映射为 system message、max_output_tokens 映射为 max_tokens；支持小米 MIMO、DeepSeek、LongCat、GLM 等模型。配置采用文件优先（config.yaml/json），提供访问日志与 trace id。明确不支持的 /v1/responses/compact 返回 501。需用 cargo 从源码构建，或下载 GitHub Actions 发布的平台产物；v0.2.x 部分功能依赖私有 crate。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- Responses API 到 Chat Completions 的本地协议转换（/v1/responses 端点）
- 支持小米 MIMO、DeepSeek、LongCat、GLM（README 声明均本地测试）
- 文件优先配置（config.yaml/json）与 API key 环境变量覆盖
- GitHub Actions 发布 Windows/Linux/macOS 平台产物及 SHA256 校验

## 适用场景

- 让 Codex CLI 使用 OpenAI 兼容 API 的模型服务
- 通过本地 shim 将小米 MIMO 等模型接入 codex-cli
- 在不支持 Responses API 的后端上运行 Codex 工作流

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: A tiny Rust Responses-to-Chat shim for Codex CLI to use OpenAI-compatible APIs.
> L9: -> local /v1/responses
> L10: -> OpenAI-compatible Chat Completions

## 星数曲线

```mermaid
xychart-beta
    title "pylab-me/Codex-Shim 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `1d16b5ce5157` · [字段定义](../../DATASET.md)*
