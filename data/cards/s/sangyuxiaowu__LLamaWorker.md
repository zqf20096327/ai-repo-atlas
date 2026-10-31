# sangyuxiaowu/LLamaWorker

⭐ 82 · C# · Apache-2.0 · 推送 2026-03-03 · [GitHub](https://github.com/sangyuxiaowu/LLamaWorker) · 个人维护 · 中文 README

**基于 LLamaSharp 的 HTTP API 服务器，提供 OpenAI 兼容接口**

基于 LLamaSharp（llama.cpp 的 .NET 绑定）开发的 HTTP API 服务器：加载本地 GGUF 模型并对外提供 OpenAI 兼容接口，覆盖聊天补全、文本补全、文本嵌入、模型切换等端点。支持多模型配置与切换、流式响应、Function Call、API Key 认证、深度思考参数开关、模型自动释放。提供 CPU/CUDA12/Vulkan 三种后端项目文件，Releases 含 Vulkan 预编译版本与测试 UI，面向希望以 OpenAI API 形式接入本地 LLM 的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 /v1/chat/completions、/v1/embeddings 等 OpenAI 兼容端点
- 支持多模型配置切换、流式响应、Function Call 与 API Key 认证
- 提供 CPU / CUDA 12 / Vulkan 三种后端项目文件与 Vulkan 预编译版本
- 内置测试 UI（wwwroot 静态页）与 Gradio.NET UI 示例

## 适用场景

- 在本地以 OpenAI 兼容 API 的形式运行 GGUF 模型
- 让现有使用 OpenAI SDK 的应用切换到本地模型
- 通过测试 UI 验证模型对话与补全效果

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: LLamaWorker is a HTTP API server developed based on the LLamaSharp project. It provides an OpenAI-compatible API, ma
> L94: - `/v1/chat/completions`: Chat completion requests

## 星数曲线

```mermaid
xychart-beta
    title "sangyuxiaowu/LLamaWorker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 81 --> 83
    line [82, 82]
```

2026-10-18 82 → 2026-10-31 82（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `4547313fa89b` · [字段定义](../../DATASET.md)*
