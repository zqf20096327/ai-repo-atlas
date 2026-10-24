# ggml-org/convert

⭐ 56 · Shell · 推送 2026-10-23 · [GitHub](https://github.com/ggml-org/convert) · [官网](https://huggingface.co/ggml-org) · 组织维护

**自动将模型转换为 GGUF 格式并上传 HF 的流水线**

ggml-org 维护的模型转换自动化流水线：调用 llama.cpp 的转换工具把模型目录中的模型转为 GGUF 格式，并上传到 Hugging Face 组织。需提供具备目标组织写权限的 HF_TOKEN，通过 bash 脚本运行；仅在源模型有更新时才转换，README 始终更新。ggml-org 下所有模型由 GitHub Actions 工作流每周自动转换一次，转换默认使用 llama.cpp master 分支，可通过 --llama-commit 指定提交。给需要批量维护 GGUF 模型发布的开发者与团队使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动批量转换模型为 GGUF 并上传 Hugging Face
- GitHub Actions 工作流每周自动转换 ggml-org 全部模型
- 转换默认使用 llama.cpp master，可用 --llama-commit 固定提交
- 仅在源模型更新时才重新转换

## 适用场景

- 为自己的 HF 组织批量维护 GGUF 格式模型发布
- 定时自动跟进上游模型更新并重新转换
- 指定特定 llama.cpp 版本保证转换一致性

## 场景标签

`模型量化` · 领域:训练与推理

## 证据(README 行号)

> L5: Automated pipeline for converting models to GGUF format and uploading them to HF.
> L37: - The conversion uses the latest `master` of llama.cpp unless `--llama-commit` is set

## 星数曲线

```mermaid
xychart-beta
    title "ggml-org/convert 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24"]
    y-axis "stars" 54 --> 57
    line [55, 56, 56]
```

2026-10-18 55 → 2026-10-24 56（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `9bc283a60a92` · [字段定义](../../DATASET.md)*
