# darkautism/llmserver-rs

⭐ 25 · Rust · 推送 2026-09-28 · [GitHub](https://github.com/darkautism/llmserver-rs) · 个人维护

**在 RK3588 NPU 上运行 LLM 的 OpenAI 风格 API 服务器**

用 Rust 编写、运行于 rk3588 芯片 rknpu 硬件上的 API 服务器，提供 OpenAI 兼容端点：/v1/chat/completions 文本对话与 /v1/audio/transcriptions 语音识别。模型以 RKLLM/RKNN 格式从 HuggingFace 仓库或本地目录加载，通过 JSON 配置声明 model_repo/model_name/model_type 等，支持流式输出与 think 模式。提供 microk8s 集群部署模板与 Swagger 在线文档。限制：需 rknpu 驱动 0.9.7 以上及 librkllmrt/librknnrt 运行库，需 cargo 编译构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 兼容端点（chat/completions 与 audio/transcriptions）
- 面向 rk3588/rknpu 硬件运行 RKLLM 格式模型
- JSON 配置支持 HuggingFace 仓库与本地目录模型加载
- 提供 microk8s 集群部署 YAML 模板与 Swagger 文档

## 适用场景

- 在 RK3588 单板机上本地运行 LLM 并以 OpenAI API 形式供应用调用
- 接入 openwebui 等前端使用本地模型对话
- 在 microk8s 集群中部署 LLM 推理服务

## 场景标签

`推理引擎` `语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L3: A Rust-based, OpenAI-style API server for large language models (LLMs) that can run on the Rknpu
> L11: - **OpenAI-style API**: Compatible with OpenAI's API endpoints for easy integration.
> L101: - /v1/chat/completions: Generate chat completions for conversational AI.

## 星数曲线

```mermaid
xychart-beta
    title "darkautism/llmserver-rs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-30 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `98f7b90e476a` · [字段定义](../../DATASET.md)*
