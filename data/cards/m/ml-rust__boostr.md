# ml-rust/boostr

⭐ 20 · Rust · Apache-2.0 · 推送 2026-10-13 · [GitHub](https://github.com/ml-rust/boostr) · 组织维护

**Rust 编写的 ML 框架：同一份代码运行于 CPU/CUDA/WebGPU**

构建在 numr 之上的 Rust 机器学习框架，不引入新张量类型或运行时封装，以扩展 trait 形式为 numr 的 client 附加 ML 操作。提供注意力、训练与推理原语，内置 27 种量化格式，支持 GGUF 模型加载（可 mmap）、分页 KV Cache、多 GPU（NCCL）与分布式推理。通过 Cargo feature flags 启用后端与各类模型（Whisper、Kokoro、VITS 等）。面向想自建 AI/ML 框架或推理服务的开发者，属 ml-rust 组织生态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同一份代码可在 CPU、CUDA、WebGPU 后端运行
- 内置 27 种量化格式与 GGUF 模型加载（mmap）
- 分页 KV Cache、NCCL 多 GPU 与分布式推理特性
- 覆盖语音模型（Whisper/Kokoro/VITS/VoxCPM 等）与音频张量算子

## 适用场景

- 在 Rust 中搭建自定义训练或推理框架
- 跨 CPU/GPU 后端复用同一份 ML 代码
- 加载 GGUF 量化模型做本地推理

## 场景标签

`推理引擎` `模型量化` · 领域:训练与推理

## 证据(README 行号)

> L3:  ML framework in Rust. Write once. Run on any backend.
> L39: boostr extends numr with ML operations and adds no tensor type or runtime wrapper.
> L159: - **boostr**: ML framework (this project)

## 星数曲线

```mermaid
xychart-beta
    title "ml-rust/boostr 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-30 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f8af7c1b95a5` · [字段定义](../../DATASET.md)*
