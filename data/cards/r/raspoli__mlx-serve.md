# raspoli/mlx-serve

⭐ 22 · Python · MIT · 推送 2026-10-11 · [GitHub](https://github.com/raspoli/mlx-serve) · 个人维护

**Apple Silicon 本地推理服务器：热切换 MLX 模型并提供 OpenAI 兼容 API**

面向 Apple Silicon Mac（M1+，macOS 13+）的本地推理服务器：以 OpenAI 兼容 API 暴露 MLX 模型，覆盖文本、视觉、嵌入、TTS、STT 与 Laya 决策六类模型，同一时刻仅加载一个模型以适应统一内存；按模型名热切换、子进程隔离、空闲自动卸载（默认 10 分钟，可按请求 keep_alive 覆盖），提供模型管理 API、请求指标观测、YAML 配置与 CLI。设计上可置于 Docker-on-Mac 栈中 LiteLLM 之后，供已有 OpenAI SDK/LiteLLM 客户端直接调用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 六类 MLX 模型（text/vision/embeddings/TTS/STT/decision）经 OpenAI 兼容 API 提供
- 按模型名热切换，同一时刻仅加载一个模型，子进程隔离与自动卸载
- 模型管理 API：预载、强制卸载、删除、从 HuggingFace 拉取
- 请求指标（TTFT/TPS/延迟）、内存监控与 dashboard 端点

## 适用场景

- 在 Mac 上以 OpenAI SDK 直接调用本地 MLX 模型
- 统一内存有限的设备上按需切换加载不同模态模型
- 与 LiteLLM 组合，为 Docker 服务提供 Mac 宿主机上的本地推理后端

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L9: Local inference server for Apple Silicon that hot-swaps MLX models on demand — text, vision, embeddings, TTS, STT, a
> L59: - **OpenAI-compatible API** — drop-in with LiteLLM, any OpenAI SDK, or direct HTTP
> L75: |`text`|`mlx_lm.server` subprocess|`/v1/chat/completions`|`["completion"]`|

## 星数曲线

```mermaid
xychart-beta
    title "raspoli/mlx-serve 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-29"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-29 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `a7b4732a1f29` · [字段定义](../../DATASET.md)*
